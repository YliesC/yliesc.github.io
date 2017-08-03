Title: Mise en cache intelligente avec Django
Order: 9
Date: 2014-09-27
Slug: mise-en-cache-intelligente-avec-django
Author: Microjoe
Display: true

Vous êtes en train de construire votre site internet avec Python et Django, tout va pour le mieux du monde ; mais plus votre site grossit et plus des fonctionnalités gourmandes apparaissent, effectuant de plus en plus de requêtes SQL même si vous les optimisez afin d’éviter la casse.

Que faire quand on a optimisé la génération de ses pages mais que le rendu est encore lent ? Utiliser la mise en cache !

[TOC]

# Présentation
La mise en cache est une technique courante qui consiste à **stocker pendant un temps défini un résultat qui provient d’une opération lourde**. Lors de la demande d’accès à ce résultat, on retourne la valeur que l’on a gardé en mémoire au lieu de relancer l’opération lourde, il en résulte un gain de réactivité (très) important.

### Les différentes implémentation du cache

Django nous propose nativement un système de cache assez poussé. Celui-ci vous permet d’utiliser différentes plateformes afin de se souvenir des valeurs que vous voulez réutiliser, dont notamment :

 * Solutions très rapides : via la RAM
    * [memcached](http://memcached.org/), la référence en la matière qui va stocker directement dans la mémoire vive les valeurs afin de garantir un temps d’accès optimal ; de plus, l’architecture distribuée de memcached permet d’utiliser des machines distantes afin de répartir la mise en cache, tout est géré automatiquement.
    * Si vous n’êtes pas en mesure d’installer, de configurer et d’utiliser memcached (par exemple si vous n’avez pas les droits root sur le serveur) mais que vous voulez tout de même avoir un stockage en RAM pour un accès plus rapide, [Django possède un *backend* prévu à cet effet](https://docs.djangoproject.com/en/dev/topics/cache/#local-memory-caching).
 * Solutions un peu moins rapides : via le disque
    * [Dans une base de données](https://docs.djangoproject.com/en/dev/topics/cache/#database-caching) ;
    * [Dans des fichiers temporaires](https://docs.djangoproject.com/en/dev/topics/cache/#filesystem-caching).
 * Autres solutions :
    * [Un cache qui ne cache rien](https://docs.djangoproject.com/en/dev/topics/cache/#dummy-caching-for-development) (à utiliser sur des versions de développement par exemple) ;
    * [Un cache personnalisé](https://docs.djangoproject.com/en/dev/topics/cache/#using-a-custom-cache-backend).

C’est à vous de faire le choix concernant le *backend* que vous voulez utiliser en fonction de vos besoins, mais sachez qu’il est possible d’utiliser plusieurs *backends* sur un même site ! Par exemple, les éléments peu nombreux et utilisés très souvent pourront être stockés dans la mémoire vive alors que les éléments plus volumineux, nombreux et moins souvent accédés pourront se trouver sur le disque (sauf si vous avez à votre disposition 256 Go de RAM).

### Différents niveaux de mise en cache

De plus, Django nous permet différent seuils de granularité :

 * **Une mise en cache globale du site :** chaque page sera cachée pendant un certain temps.
 * **Une mise en cache par vue :** seulement certaines vues seront cachées par l’utilisation d’un décorateur Python.
 * **Une mise en cache au niveau des *templates* :** c’est la méthode la plus fine, qui permet de cacher uniquement certains bouts dans certains modèles HTML.

C’est en se basant sur cette dernière technique que nous allons réaliser une mise en cache intelligente.

# Exemple : système de notifications
### Situation initiale

Prenons un cas concret : vous êtes en train de réaliser une application pour votre site qui s‘occupe de gérer l’envoi de messages entre les membres de votre site. Vous avez intégrer la notification de nouveaux messages via une icône présente sur tout le reste de votre site.

```django
<div class="message-box-icon">
    Vous avez {{ get_new_messages_count user }} nouveaux messages.
</div>
```

Cependant, **la requête pour récupérer le nombre de nouveaux messages est lourde et prend 3 secondes**. Sachant que cette requête est effectuée sur chaque page puisque vous vous servez le l’icône pour afficher le nombre de nouveaux messages, **toutes les pages de votre site mettent 3 secondes de plus à charger à cause de cette requête**.

Heureusement, comme on l’a vu précédemment, Django nous propose un système de mise en cache au niveau des *templates* HTML. Et si nous utilisions cet outil afin d’accélérer la génération de nos pages ?

### Mise en place du cache

Rendons nous dans notre *template* où le code gourmand est appelé, et mettons ce résultat en cache :

```django
{% load cache %}

<div class="message-box-icon">
    {# On cache le bloc suivant sous le nom de 'messages-count' pendant 120 secondes #}
    {% cache 120 message-count %}
        Vous avez {{ get_new_messages_count user }} nouveaux messages.
    {% endcache %}
</div>
```

Après avoir configuré correctement le système de cache (n’utilisez pas le cache qui ne cache pas sinon ça risque de ne pas fonctionner), on remarque que la première génération de page prend toujours 3 secondes mais que **les autres pages sont rendues quasiment instantanément** !

Cependant il y a un problème. En effet, si vous vous connectez sous le nom d’un autre utilisateur, alors vous aller voir le bloc qui a été caché pour le premier utilisateur à avoir entrainé la mise en cache. Ainsi il se peut très bien que vous ayez une notification de nouveau message alors que c’est en fait le nombre de messages pour le premier utilisateur qui avait été mis en cache !

### Indépendance du cache

Django nous permet de palier à ce problème : il nous suffit de trouver un élément unique qui diffère et de le passer à la balise de mise en cache pour que celle-ci stocke les différentes valeurs en fonction de cet élément unique. Dans le cadre de nos utilisateurs, on peut dire que le pseudonyme est un bon élément unique :

```django
{% load cache %}

<div class="message-box-icon">
    {# On cache le bloc suivant sous le nom de 'messages-count' pendant 120 secondes #}
    {% cache 120 message-count user.username %}
        Vous avez {{ get_new_messages_count user }} nouveaux messages.
    {% endcache %}
</div>
```

Ainsi, chaque utilisateur aura sa propre mise en cache de son nombre de nouveaux messages. Ouf !

# Mise à jour intelligente du cache
### Persistance indésirable

Il nous reste cependant un dernier petit problème à régler :

Considérons que je viens de recevoir un nouveau message ; la valeur mise en cache m’indique bien que j’ai un nouveau message puisque c’est la première page que je génère, tout fonctionne comme prévu.

Je lis mon message et éventuellement répond à son auteur avant de continuer paisiblement ma navigation sur le site. Cependant, je remarque que le nombre de nouveaux messages reste bloqué à 1 ! En effet, la valeur a été mise en cache pendant un certain temps (120 secondes dans notre exemple précédent) et ne sera pas actualisée avant que ces 120 secondes se soient écoulées !

Cet effet est gênant pour tous les utilisateurs de votre site, mais comment faire pour éviter ce cas de figures tout en gardant les bénéfices de la mise en cache ?

### Péremption automatique

Afin de solliciter un appel frais à la fonction de génération de notifications, il nous faudrait invalider le contenu qui a été précédemment mis en cache. Pour cela, nous allons devoir utiliser l’accès « bas niveau » au cache de Django.

Le cache fonctionne comme un dictionnaire avec un système de clés/valeurs ; pour supprimer un élément il nous faut donc retrouver sa clé. Les clés utilisées au niveau du cache sont assez bizarres, considérons le bloc suivant :

```
{% cache 120 message-count user.username %}
    ...
{% endcache %}
```

La clé associée sera la suivante :

```text
template.cache.message-count.f71dbe52628a3f83a77ab494817525c6
```

On y retrouve le nom du bloc ainsi qu’un hash MD5 créé à partir des arguments passés au bloc. Pour retrouver facilement cette clé, on peut utiliser la fonction `make_template_fragment_key` apparue dans la version 1.6 de Django :

```python
>>> from django.core.cache.utils import make_template_fragment_key
>>> make_template_fragment_key('messages-count', ['toto'])
'template.cache.message-count.f71dbe52628a3f83a77ab494817525c6'
```

Il nous reste maintenant à supprimer cette clé du cache lors des actions qui pourraient potentiellement mettre à jour ce cache. Par exemple, si l’on reprend notre cas, on aimerai bien que le cache soit mis à jour lors de la consultation du nouveau message :

```python
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

def view_message(request):

    # Si on consulte un message qui n’était pas lu jusqu’à présent,
    # on peut considérer qu’il est lu et donc mettre à jour l’icône
    # du nombre de messages non-lus.
    if not message_read(msg):
        cache.delete(make_template_fragment_key('message-count', request.user.username))

    # Rendu du template, etc.
```

Il vous reste à mettre en place cette demande explicite de suppression de contenu mis en cache à chaque endroit où ce contenu aurait pu en effet être modifié. Ainsi, les utilisateurs sont toujours prévenus en temps et en heure et en plus si aucun changement n’a été détecté la valeur peut directement être lue dans le cache !

Vous êtes désormais en mesure d’utiliser la mise en cache de Django sur votre site internet sans y retrouver les effets néfastes : la mise à jour différée des données.

Sources :

 * [La documentation officielle de Django 1.6](https://docs.djangoproject.com/en/1.6/topics/cache/) ;
 * [Mon expérience personnelle lors de la mise en place d’un système de cache pour Progdupeupl](http://progdupeu.pl/forums/sujet/407/utilisation-de-cache-pour-un-rendu-beaucoup-plus-rapide).
