Title: Similarité cosinus et recherche textuelle
Order: 9
Date: 2014-09-27
Slug: similarite-cosinus-et-recherche-textuelle
Author: Graphox
Display: true

De nombreux domaines de recherche sont sollicités par le développement d'Internet, notamment l'évaluation des similarités : similarité entre une requête et des documents (moteur de recherche), entre des artistes (système de recommandation), entre des utilisateurs ou produits (site marchand), entre des images… Tout l'enjeu de ce pan de recherche est donc de départager de manière pertinente le nombre toujours croissant de données qui circulent sur Internet et d'en extraire des informations utiles pour répondre à divers problèmes. L'objectif de cet article est d'amorcer la réflexion en présentant les bases de la similarité cosinus, une méthode principalement utilisée pour l'analyse de texte.

Les exemples en Python qui suivent sont volontairement peu optimisés et n'utilisent pas de bibliothèques spécifiques.

[TOC]

## Une approche du problème : recherche d'artistes similaires

Imaginons un système comme Lastfm qui possède des tags pondérés pour décrire chaque artiste, par exemple « rock : 100, classical : 24… ». Nous héritons de toutes ces informations et notre but est de pouvoir déterminer l'artiste le plus similaire à un autre. L'application proposée ci-dessous est bien entendue limitée puisque pour augmenter nos chances d'obtenir des similarités satisfaisantes, il faudrait déjà se demander si des tags pondérés seuls peuvent décrire correctement un artiste. On admettra que c'est le cas. Pour information, Lastfm utilise également des algorithmes de recherche de *plus proches voisins* pour fournir ses recommandations, en se basant sur les statistiques de sa communauté pour établir des liens de similarité entre les utilisateurs, selon leur tendance d'écoute.

### Le modèle vectoriel

Souvent, dans le domaine de la « similarité », on aime bien représenter graphiquement nos objets et les valeurs dont on dispose. Car en faisant varier ces dernières, on peut espérer trouver un lien entre ces variations chiffrées, leur signification concrète dans le cadre de notre application (la similarité entre les deux objets augmente ou diminue) et une grandeur mathématique visible et mesurable : une distance, un angle, le coefficient d'une droite moyenne, etc. L'avantage d'une telle représentation est que, si jamais on parvient à trouver ce lien, on sait qu'il existe des formules mathématiques facilement applicables pour effectuer toutes sortes de mesures dans un repère. Dans le domaine de la  [recherche d'information](http://fr.wikipedia.org/wiki/Recherche_d'information), on doit ce « [modèle vectoriel](http://fr.wikipedia.org/wiki/Mod%C3%A8le_vectoriel) » à [Gerard Salton](http://fr.wikipedia.org/wiki/Gerard_Salton).


En se basant sur ce modèle, on pourrait matérialiser un artiste par un vecteur dont la dimension serait égale au nombre de tags étudiés et dont chaque attribut correspondrait au poids du tag associé. Si on se limite à un espace à deux dimensions, voici comment on pourrait représenter deux artistes A et B ayant respectivement pour tags (rock : 40, electro : 50) et (rock : 100, electro : 25). Par abus de langage, on appellera aussi A et B les extrémités de ces deux vecteurs.

![](http://progdupeu.pl/media/galleries/64/82544cd5-ae3b-4572-9df3-b9b6eef7deb1.png)

Plus on augmente les différences de poids pour chaque tag et plus la similarité entre les deux artistes baisse. Faites le test : il apparaît que la **distance** entre A et B et l'**angle** formé par les deux vecteurs pourraient être de bons indicateurs de la similarité existant entre les deux objets.

Pour répondre à notre problème, il suffirait donc de représenter chaque artiste dans un repère et de comparer leurs positions relatives. Sur la figure ci-dessous, le vecteur R décrirait un artiste plus similaire à A qu'à C, mais plus similaire à C qu'à B. Cela peut se voir à la fois par la distance entre les différents points et les angles formés par les vecteurs.

![](http://progdupeu.pl/media/galleries/64/f0941e7b-0474-4202-8198-75026307b313.png)

Mais cela est-il toujours vrai ? Quelle méthode choisir ? Avant tout, nous allons implémenter chacune des deux mesures. Bien que cela soit difficilement représentable, on généralisera ce raisonnement à des espaces à plus de deux dimensions.

### La distance euclidienne

Dans un espace à $n$ dimensions, la distance euclidienne $AB$ est définie comme la racine carrée de la somme des différences au carré entre les attributs de même rang des deux vecteurs $A$ et $B$.

$$d(A, B) = \sqrt{\sum\limits_{i=1}^{n}{(A_i - B_i)^2}}$$

Pour obtenir un indice de la similarité existant entre $A$ et $B$, puisque plus la distance est faible, plus la similarité est censée augmenter, on peut prendre l'inverse de la distance euclidienne. Pour éviter d'avoir un dénominateur nul, on ajoute 1 :

$$\mathrm{similarité(A, B)} = \frac{1}{1 + \sqrt{\sum\limits_{i=1}^{n}{(A_i - B_i)^2}}}$$

De ce fait, on a $0 < \mathrm{similarité(A, B)} \le 1$ et plus $\mathrm{similarité(A, B)}$ s'approche de 1, plus la similarité entre les objets représentés par $A$ et $B$ est grande.

#### Implémentation en Python

On a adapté la formule mathématique à notre situation où les vecteurs n'ont pas forcément tous les mêmes tags de base. Pour y remédier, on se place dans un espace comprenant le nombre de dimensions nécessaire pour que chaque tag puisse être représenté (avec `all_keys`) et si l'un des vecteurs ne possède pas d'attribut pour ce tag, alors on lui donne un poids nul par défaut (c'est le rôle des expressions `a.get(k, 0)` et `b.get(k, 0)`).

    :::python
    # coding: utf-8
     
    from math import sqrt
    
    data = {
        'Pink Floyd': {
            'progressive rock': 100,
            'classic rock': 78,
            'psychedelic rock': 70,
            'experimental': 5
        },
        'Alain Souchon': {
            'chanson française': 100,
            'chanson': 34,
            'pop': 33,
            'singer-songwriter': 12
        },
        'Hans Zimmer': {
            'soundtrack': 100,
            'instrumental': 57,
            'classical': 41,
            'composer': 32
        },
        'The Police': {
            'rock': 100,
            'new wave': 66,
            'classic rock': 81,
            'pop': 40
        },
        'Chopin': {
            'classical': 100,
            'piano': 47,
            'romantic': 26,
            'instrumental': 22
        }
    }


    def similarity(a, b):
        all_keys = set(list(a) + list(b))
        diffs = ((a.get(k, 0) - b.get(k, 0)) ** 2 for k in all_keys)
        distance = sqrt(sum(diffs))
        return 1 / (1 + distance)

On peut maintenant calculer les scores de similarité entre tous nos artistes, effectuer un classement descendant et afficher les résultats :

    :::python
    from operator import itemgetter
    
    for artist, tags in data.items():
        scores = {}
        for artist_, tags_ in data.items():
            scores[artist_] = similarity(tags, tags_)
        scores = sorted(scores.items(), key=itemgetter(1), reverse=True)
        print('\nSimilar artists for {}:'.format(artist))
        for artist, score in scores:
            print('\t{} ({:.2})'.format(artist, score))

<p></p>
    :::text
    Similar artists for Pink Floyd:
         Pink Floyd (1.0)
         The Police (0.0057)
         Alain Souchon (0.0054)
         Chopin (0.0054)
         Hans Zimmer (0.0052)
    
    Similar artists for Alain Souchon:
         Alain Souchon (1.0)
         Chopin (0.0062)
         Hans Zimmer (0.0059)
         The Police (0.0055)
         Pink Floyd (0.0054)
    
    Similar artists for Hans Zimmer:
         Hans Zimmer (1.0)
         Chopin (0.0073)
         Alain Souchon (0.0059)
         Pink Floyd (0.0052)
         The Police (0.0051)
    
    Similar artists for Chopin:
         Chopin (1.0)
         Hans Zimmer (0.0073)
         Alain Souchon (0.0062)
         Pink Floyd (0.0054)
         The Police (0.0053)
    
    Similar artists for The Police:
         The Police (1.0)
         Pink Floyd (0.0057)
         Alain Souchon (0.0055)
         Chopin (0.0053)
         Hans Zimmer (0.0051)

Il faut voir la valeur numérique retournée comme un indice, un score qui est destiné à être comparé pour effectuer un classement et non pas comme un pourcentage de ressemblance entre deux objets.

### La similarité cosinus

Si on peut relier la similarité entre deux vecteurs $A$ et $B$ à la mesure de l'angle $\theta$ qu'ils forment, alors on peut l'évaluer en calculant le cosinus de cet angle : c'est ainsi qu'est définie la _similarité cosinus_. Le calcul du cosinus se base sur l'expression du [produit scalaire](https://fr.wikipedia.org/wiki/Produit_scalaire) $A \cdot B = \|A\| \|B\| \cos(\theta)$ et implique qu'aucun des deux vecteurs ne soit nul.

$$\mathrm{similarité(A, B)} = \cos(\theta) = \frac{A \cdot B}{ \|A\| \|B\|} = \frac{ \sum\limits_{i=1}^{n}{A_i \times B_i} }{ \sqrt{\sum\limits_{i=1}^{n}{{A_i}^2}} \times \sqrt{\sum\limits_{i=1}^{n}{{B_i}^2}} }$$

Si nos poids ne peuvent pas être négatifs, alors on a $0 \le \mathrm{similarité(A, B)} \le 1$. Plus la mesure de l'angle est faible, plus son cosinus est élevé : avec cette formule, plus $\mathrm{similarité(A, B)}$ s'approche de 1, plus la similarité entre les objets représentés par les vecteurs $A$ et $B$ est grande.

#### Implémentation en Python

Comme précédemment, on considère que l'absence d'un tag est équivalente à la présence de ce tag avec un poids nul. On peut alors se contenter de calculer le produit scalaire des vecteurs $A$ et $B$ uniquement avec leurs éléments communs (car si au rang $i$ au moins l'un des deux artistes possède un tag de poids 0, on aura $A_i \times B_i = 0$, ce qui peut être ignoré dans la somme).

L'interface de notre programme reste la même et il suffit alors de modifier la fonction qui calcule la similarité entre deux vecteurs. La restriction aux tags communs se fait avec l'expression `… for k in a if k in b`). On suppose que les artistes ont au moins un tag de poids non nul (dénominateur non nul).

    :::python
    from math import sqrt
    
    def similarity(a, b):
        scalar = sum(a[k] * b[k] for k in a if k in b)
        norm_a = sqrt(sum(v ** 2 for v in a.values()))
        norm_b = sqrt(sum(v ** 2 for v in b.values()))
        return scalar / (norm_a * norm_b)

<p></p>

    :::text
    Similar artists for Pink Floyd:
         Pink Floyd (1.0)
         The Police (0.29)
         Alain Souchon (0.0)
         Hans Zimmer (0.0)
         Chopin (0.0)
    
    Similar artists for Alain Souchon:
         Alain Souchon (1.0)
         The Police (0.079)
         Pink Floyd (0.0)
         Hans Zimmer (0.0)
         Chopin (0.0)
    
    Similar artists for Hans Zimmer:
         Hans Zimmer (1.0)
         Chopin (0.37)
         Pink Floyd (0.0)
         Alain Souchon (0.0)
         The Police (0.0)
    
    Similar artists for Chopin:
         Chopin (1.0)
         Hans Zimmer (0.37)
         Pink Floyd (0.0)
         Alain Souchon (0.0)
         The Police (0.0)
    
    Similar artists for The Police:
         The Police (1.0)
         Pink Floyd (0.29)
         Alain Souchon (0.079)
         Hans Zimmer (0.0)
         Chopin (0.0)

### Distances ou angles ?

Quelques observations, que l'on aurait pu prévoir mathématiquement :

- La distance euclidienne, contrairement à la similarité cosinus, donne des résultats peut-être moins en phase avec ce que l'on attend de notre application (Alain Souchon plus proche de Chopin et Hans Zimmer que de The Police, bien qu'il ait avec ce dernier le tag « pop » en commun)

- L'usage seul d'un angle ou d'une distance comme métrique mène à une perte d'information de nature différente. La similarité cosinus mesurant un angle, son point de vue est centré sur l'origine, et si on « étire » les vecteurs, on ne change pas la valeur du cosinus. Mais si on adopte un point de vue plus local et que l'on s'intéresse à la distance entre les deux points, la distance euclidienne varie. Il se passe la même chose lorsque l'on regarde les étoiles : doit-on dire qu'elles sont proches (ou ici « similaires ») si elles apparaissent en effet proches l'une de l'autre depuis la Terre, même si des années-lumière les séparent en réalité ?

![](http://progdupeu.pl/media/galleries/64/420dffce-6ccd-47ca-a315-b9d227c14975.png)

- Avec la distance euclidienne, ce type de phénomène serait géométriquement limité à un cercle (puisque l'on s'intéresse aux distances) mais il y a un autre problème : pourquoi A serait-il plus similaire à C qu'à B sur la figure ci-dessous ?

![](http://progdupeu.pl/media/galleries/64/03bf8a08-3843-4f37-a87c-f607be4aba22.png)

### Les questions à se poser

Pour pouvoir trancher sur la méthode à privilégier, il faut poursuivre ces raisonnements et se demander :

- Ce qui se passerait avec des dizaines et dizaines de dimensions
- Si ces cas problématiques peuvent être négligés lorsque l'on a beaucoup de données à comparer
- Quels sont les cas de divergence les plus extrêmes entre les deux méthodes ? À quoi sont-ils dûs ? Dans ces cas-là, y a-t-il toujours une méthode plus cohérente que l'autre ?
- Quelle méthode donne les résultats les plus cohérents avec ce que l'on attend de **notre application** : certaines méthodes sont parfois appropriées pour certains problèmes et d'autres non, et vice versa
- Quelle méthode donne les résultats les plus cohérents avec **nos données** : combien a-t-on de dimensions ? Les objets sont-ils tous décrits avec la même précision (ou les textes sont-ils de taille homogène) ? Les données sont-elles toutes de qualité ? L'écart type est-il faible ou élevé ? Peut-on se contenter d'une méthode grossière ou faut-il l'affiner ?
- Certaines méthodes ont-elles toujours tendance à favoriser les objets décrits avec beaucoup ou au contraire peu de précision ?
- Les métriques mathématiques ont-elles toujours un sens lorsque l'on néglige certains termes qui, dans notre application, seraient par exemple presque tous nuls ? Dans notre cas, si les produits scalaires sont tous en moyenne très proches de zéro, on peut développer le carré de la distance euclidienne et simplifier le double produit : a-t-on toujours une métrique cohérente ?
- etc.

Pour notre programme, il s'avère que c'est la similarité cosinus qui donne les résultats les plus prévisibles. Encore une fois, il n'y a pas de méthode absolue : on la choisit en fonction de nos objectifs et de nos données. D'ailleurs, on n'a fait qu'appliquer des formules « génériques » à des données brutes (nos tags) sous seul prétexte qu'elles étaient déjà numériques… n'y aurait-il pas eu d'autres façons de construire notre modèle vectoriel ?


## Recherche de documents pertinents

Lorsque l'on entend parler de calcul de similarité en informatique, c'est souvent dans le cadre de données textuelles : comment classer, regrouper des documents ? Comment reconnaître un spam ? Comment, pour une requête, retourner la liste des documents les plus pertinents (dans le cas d'un moteur de recherche par exemple) ? C'est à ce dernier problème que l'on va désormais s'intéresser.

On utilisera un [corpus](http://paste.awesom.eu/2mH&raw) contenant trois extraits et notre but est de déterminer quel document est le plus pertinent pour la requête R.

- un extrait A du _Rouge et du Noir_
- un extrait B des _Misérables_
- un extrait C de _Candide_
- une requête R « Le crime de Julien était un crime, un crime affreux »

Dans le domaine de la [recherche d'information](http://fr.wikipedia.org/wiki/Recherche_d'information), le modèle vectoriel et la similarité cosinus sont très utilisés. Les métriques comme la distance euclidienne le sont aussi, mais il faut alors normaliser les vecteurs de manière à ce que tous les documents soient comparables quelle que soit leur taille, ce qui est parfois fait de manière implicite lorsque l'on calcule des fréquences, par exemple. La similarité cosinus, entre autres, est pour cette raison parfois plus intuitive : elle vérifie que deux documents « pointent » dans la même direction sans souci de leur norme, puisqu'elle est insensible à la multiplication par un scalaire.

Encore faut-il représenter nos documents dans un repère et en dégager des valeurs numériques. Le choix est assez limité. Les dimensions de notre espace vectoriel correspondront à l'ensemble du vocabulaire contenu dans nos différents documents. Ce qui va différer selon les documents, ce sont les fréquences auxquelles apparaissent ces mots.

Dans un premier temps, on pourrait suggérer que le nombre d'occurrences de chaque mot dans le document constitue son « poids ». Puisque l'on ne peut pas représenter facilement un espace à plus de deux dimensions, on va s'intéresser uniquement aux mots « crime » et « julien » :

- Document A : 1 occurrence pour « crime », 1 occurrence pour « julien »
- Document B : 3 occurrences pour « crime », 0 occurrence pour « julien »
- Document C : 0 occurrence pour « crime », 0 occurrence pour « julien »
- Requête R : 3 occurrences pour « crime », 1 occurrence pour « julien »

![](http://progdupeu.pl/media/galleries/64/d6d72588-de69-42ca-bbb4-d72a59a70c0a.png)

Avec la similarité cosinus, le document B serait donc le plus pertinent pour R. Mais dans le cas d'un contenu linguistique, cet indice de similarité est-il réellement pertinent, tout comme le fait de relier proportionnellement le poids d'un terme à son nombre d’occurrences ? Est-ce que l'on peut considérer qu'un document comportant 10 occurrences d'un terme est 10 fois plus pertinent qu'un document n'en comportant qu'une ? Et que faire des mots très courants comme les articles définis ou certains verbes qui risquent, avec leur poids élevé, d'« écraser » les autres mots pourtant plus intéressants lors d'une recherche ?

### Une méthode de pondération : le TF-IDF

Pour palier la plupart de ces défauts, on utilise souvent une méthode nommée [TF-IDF](http://fr.wikipedia.org/wiki/TF-IDF). Partant du constat qu'il était peu judicieux de considérer uniquement la fréquence d'un mot lors du calcul de son poids, le TF-IDF définit le poids d'un terme comme le produit de deux informations :

* La fréquence $\mathrm{tf}(t,d)$ du terme $t$ dans le document $d$ :
  $$\mathrm{tf}(t,d) = \frac{n_{t, d}}{N_d}$$
  où $n_{t, d}$ est le nombre d'occurrences de $t$ dans $d$ et $N_d$ la taille du document $d$ (le nombre de mots).<br /><br />
  Afin que les poids associés aux termes puissent être comparables quelle que soit la longueur des documents (qui est loin d'être toujours un bon critère de pertinence) et que le système ne souffre pas de failles permettant à un site d'augmenter son placement en répétant 1000 fois les mêmes mots-clés (dans le cas d'un moteur de recherche), il est nécessaire de relativiser ce nombre d'occurrences, en introduisant en quelque sorte ce que les anglais appelleraient un _facteur de normalisation_. Ici, on se contente simplement de la définition d'une fréquence en statistique : le nombre d'occurrences sur le nombre d'éléments.

* La fréquence inverse $\mathrm{idf}(t, D)$ du terme $t$ dans tout le corpus $D$ :
  $$\mathrm{idf}(t, D) =  \log \frac{|D|}{|\\{d \in D: t \in d\\}|}$$
  Il s'agit de diviser le nombre total de documents présents dans le corpus $D$ par le nombre de documents contenant le terme $t$, et d'en calculer le logarithme.<br /><br />
  L'idée est simple : cette fréquence inverse que l'on étend à l'ensemble du corpus permet de mesurer le caractère rare ou commun des termes, qui seront alors soit plus discriminants — on cherchera à donner à un mot qui n'apparaît pas souvent un poids élevé de manière à ce que le document qui le contient soit favorisé si on effectue une recherche avec ce mot — ou soit plus anecdotiques (comme c'est le cas des articles définis qui apparaissent dans la majorité si ce n'est la totalité des documents).

Avec ce modèle, le poids $\mathrm{tfidf}(t, d, D)$ d'un terme $t$, qui n'est plus seulement dépendant du document $d$ étudié mais également de l'ensemble du corpus $D$, s'obtient de cette manière :

$$\mathrm{tfidf}(t, d, D) = \mathrm{tf}(t, d) \times \mathrm{idf}(t, D) = \frac{n_{t, d}}{N_d} \times \log \frac{|D|}{|\\{d \in D: t \in d\\}|}$$


### Application

Reprenons nos trois documents A, B et C et notre requête R. Voici les données dont nous avons besoin :

* Document A : 1 occurrence pour « julien », 1 occurrence pour « crime », 138 mots
* Document B : 0 occurrence pour « julien », 3 occurrences pour « crime », 105 mots
* Document C : 0 occurrence pour « julien », 0 occurrence pour « crime », 102 mots
* Requête R : 1 occurrence pour « julien », 3 occurrences pour « crime », 10 mots

On va se limiter aux termes « julien » et « crime » et puisque le document C ne nous intéresse pas (à première vue, il n'a aucune similarité avec notre requête) on ne le représentera pas. Cependant, on le prendra en compte comme élément du corpus à part entière dans les calculs ci-dessous.

#### 1. Calcul des fréquences inverses

* « julien » apparaît dans 1 document sur 3 : $\mathrm{idf}(\mathrm{julien}) = \log \frac{3}{1} = 1.10$
* « crime » apparaît dans 2 documents sur 3 : $\mathrm{idf}(\mathrm{crime}) = \log \frac{3}{2} = 0.405$

#### 2. Calcul des poids TF-IDF pour A

* $\mathrm{tfidf}(\mathrm{julien})_A = \frac{1}{138} \times \mathrm{idf}(\mathrm{julien}) = \frac{1}{138} \times 1.10 = 0.0080$
* $\mathrm{tfidf}(\mathrm{crime})_A = \frac{1}{138} \times \mathrm{idf}(\mathrm{crime}) = \frac{1}{138} \times 0.405 = 0.0029$

On représentera le document A par le vecteur $\vec{OA}(0.0080, 0.0029)$.

#### 3. Calcul des poids TF-IDF pour B

* $\mathrm{tfidf}(\mathrm{julien})_B = \frac{0}{105} \times \mathrm{idf}(\mathrm{julien}) = 0$
* $\mathrm{tfidf}(\mathrm{crime})_B = \frac{3}{105} \times \mathrm{idf}(\mathrm{crime}) = \frac{3}{105} \times 0.405 = 0.012$

On représentera le document B par le vecteur $\vec{OB}(0, 0.012)$.

#### 4. Calcul des poids TF-IDF pour R

* $\mathrm{tfidf}(\mathrm{julien})_R = \frac{1}{10} \times \mathrm{idf}(\mathrm{julien}) = \frac{1}{10} \times 1.10 = 0.11$
* $\mathrm{tfidf}(\mathrm{crime})_R = \frac{3}{10} \times \mathrm{idf}(\mathrm{crime}) = \frac{3}{10} \times 0.405 = 0.12$

La requête R peut donc être représentée par le vecteur $\vec{OR}(0.11, 0.12)$.

Ci-dessous, je me suis permis de multiplier par 10 les proportions des vecteurs $\vec{OA}$ et $\vec{OB}$ pour qu'ils soient plus visibles, mais puisque l'on ne s'intéresse qu'aux angles dans notre raisonnement, cela n'a pas beaucoup d'importance :

![](http://progdupeu.pl/media/galleries/64/77f6f6b5-bb5f-40af-be4c-7a3c759a14c0.png)

Alors que notre première méthode donnait, pour la requête R, un indice de pertinence de 94 % pour le document B et de 89 % pour le document A, notre deuxième méthode avec pondération TF-IDF nous donne un indice de pertinence de 73 % pour le document B et de 88 % pour le document A. Autrement dit, les résultats sont inversés et cette méthode semble plus pertinente.

Cela s'explique par la fréquence inverse de « julien » dans le corpus, qui apparaît seulement dans 1 document sur 3 alors que « crime » apparaît 2 fois sur 3. La proportionnalité qui existait dans notre première méthode est donc brisée et le terme « julien » est avantagé plus que ne l'est le terme « crime » car il est _plus rare_.

__Remarque__ : Jusqu'ici, on s'est limité à deux termes, « crime » et « Julien », afin de représenter plus facilement le problème. En théorie, il faudrait prendre en compte tous les mots de la requête et c'est ce que nous allons implémenter ci-dessous.

### Implémentation en Python

Pour des raisons pratiques, les documents du corpus et les requêtes sont déjà superficiellement traités : retrait de la ponctuation et des accents, et découpage en liste de mots.

    :::python

    corpus = {
        'Le Rouge et le Noir': ['je', 'ne', 'vous', 'demande', 'aucune', 'grace', 'continua', 'julien', 'en', 'affermissant', 'sa', 'voix', 'je', 'ne', 'me', 'fais', 'point', 'illusion', 'la', 'mort', 'attend', 'elle', 'sera', 'juste', 'ai', 'pu', 'attenter', 'aux', 'jours', 'de', 'la', 'femme', 'la', 'plus', 'digne', 'de', 'tous', 'les', 'respects', 'de', 'tous', 'les', 'hommages', 'mme', 'de', 'renal', 'avait', 'ete', 'pour', 'moi', 'comme', 'une', 'mere', 'mon', 'crime', 'est', 'atroce', 'et', 'il', 'fut', 'premedite', 'ai', 'donc', 'merite', 'la', 'mort', 'messieurs', 'les', 'jures', 'quand', 'je', 'serais', 'moins', 'coupable', 'je', 'vois', 'des', 'hommes', 'qui', 'sans', 'arreter', 'ce', 'que', 'ma', 'jeunesse', 'peut', 'meriter', 'de', 'pitie', 'voudront', 'punir', 'en', 'moi', 'et', 'decourager', 'jamais', 'cette', 'classe', 'de', 'jeunes', 'gens', 'qui', 'nes', 'dans', 'un', 'ordre', 'inferieur', 'et', 'en', 'quelque', 'sorte', 'opprimes', 'par', 'la', 'pauvrete', 'ont', 'le', 'bonheur', 'de', 'se', 'procurer', 'une', 'bonne', 'education', 'et', 'audace', 'de', 'se', 'meler', 'ce', 'que', 'orgueil', 'des', 'gens', 'riches', 'appelle', 'la', 'societe'],
        'Les Misérables': ['si', 'la', 'surcharge', 'de', 'la', 'peine', 'etait', 'point', 'effacement', 'du', 'delit', 'et', 'arrivait', 'pas', 'ce', 'resultat', 'de', 'retourner', 'la', 'situation', 'de', 'remplacer', 'la', 'faute', 'du', 'delinquant', 'par', 'la', 'faute', 'de', 'la', 'repression', 'de', 'faire', 'du', 'coupable', 'la', 'victime', 'et', 'du', 'debiteur', 'le', 'creancier', 'et', 'de', 'mettre', 'definitivement', 'le', 'droit', 'du', 'cote', 'de', 'celui', 'la', 'meme', 'qui', 'avait', 'viole', 'si', 'cette', 'peine', 'compliquee', 'des', 'aggravations', 'successives', 'pour', 'les', 'tentatives', 'evasion', 'ne', 'finissait', 'pas', 'par', 'etre', 'une', 'sorte', 'attentat', 'du', 'plus', 'fort', 'sur', 'le', 'plus', 'faible', 'un', 'crime', 'de', 'la', 'societe', 'sur', 'individu', 'un', 'crime', 'qui', 'recommencait', 'tous', 'les', 'jours', 'un', 'crime', 'qui', 'durait', 'dix', 'neuf', 'ans'],
        'Candide': ['ils', 'voguerent', 'quelques', 'lieues', 'entre', 'des', 'bords', 'tantot', 'fleuris', 'tantot', 'arides', 'tantot', 'unis', 'tantot', 'escarpes', 'la', 'riviere', 'elargissait', 'toujours', 'enfin', 'elle', 'se', 'perdait', 'sous', 'une', 'voute', 'de', 'rochers', 'epouvantables', 'qui', 'elevaient', 'jusqu', 'au', 'ciel', 'les', 'deux', 'voyageurs', 'eurent', 'la', 'hardiesse', 'de', 'abandonner', 'aux', 'flots', 'sous', 'cette', 'voute', 'le', 'fleuve', 'resserre', 'en', 'cet', 'endroit', 'les', 'porta', 'avec', 'une', 'rapidite', 'et', 'un', 'bruit', 'horrible', 'au', 'bout', 'de', 'vingt', 'quatre', 'heures', 'ils', 'revirent', 'le', 'jour', 'mais', 'leur', 'canot', 'se', 'fracassa', 'contre', 'les', 'ecueils', 'il', 'fallut', 'se', 'trainer', 'de', 'rocher', 'en', 'rocher', 'pendant', 'une', 'lieue', 'entiere', 'enfin', 'ils', 'decouvrirent', 'un', 'horizon', 'immense', 'borde', 'de', 'montagnes', 'inaccessibles']
    }
    
    queries = {
        'Recherche A': ['crime'],
        'Recherche B': ['le', 'crime', 'affreux', 'de', 'julien'],
        'Recherche C': ['coupable', 'et', 'societe'],
        'Recherche D': ['montagne', 'ciel']
    }

On définit la fonction `vectorize(doc, corpus)` qui nous permettra d'obtenir un vecteur pour le document `doc` en attribuant à chaque terme son poids TF-IDF :

    :::python
    from math import sqrt, log
    
    def tf(term, doc):
        return doc.count(term) / len(doc)
    
    def idf(term, corpus):
        try:
            return log(len(corpus) / sum(1 for doc in corpus if term in doc))
            # le dénominateur équivaut à len([doc for doc in corpus if term in doc])
        except ZeroDivisionError:
            return 0
    
    def vectorize(doc, corpus):
        vector = {}
        for term in doc:
            if term not in vector:
                vector[term] = tf(term, doc) * idf(term, corpus)
        return vector

« Vectorisons » tout de suite les documents de notre corpus et les requêtes :

    :::python
    corpus_v = {}
    for identifier, text in corpus.items():
        corpus_v[identifier] = vectorize(text, corpus.values())
    
    queries_v = {}
    for identifier, text in queries.items():
        queries_v[identifier] = vectorize(text, corpus.values())

On peut valider le modèle TF-IDF en regardant si les termes les plus communs ont bien un poids plus faible que les autres termes plus rares. Pour cela, on affiche par exemple les 10 termes qui ont les poids les plus faibles pour _Les Misérables_ :

    :::python
    from operator import itemgetter
    
    weights = corpus_v['Les Misérables'].items()
    for term, weight in sorted(weights, key=itemgetter(1))[:10]:
        print(term + ' ' + str(weight))

<p></p>

    :::text
    les          0.0
    et           0.0
    la           0.0
    un           0.0
    de           0.0
    le           0.0
    qui          0.0
    une          0.0
    des          0.0
    cette        0.0

Le résultat parle de lui-même : puisque tous les textes possèdent au moins une occurrence de ces mots, on a dans tous les cas $\mathrm{idf} = \log 1 = 0$ et donc $\mathrm{tfidf} = \mathrm{tf} \times 0 = 0$.

Maintenant, on peut calculer la similarité cosinus entre les requêtes et les documents, en reprenant la fonction `similarity(a, b)` définie précédemment et en l'appliquant aux documents vectorisés :

    :::python
    def similarity(a, b):
        scalar = sum(a[k] * b[k] for k in a if k in b)
        norm_a = sqrt(sum(v ** 2 for v in a.values()))
        norm_b = sqrt(sum(v ** 2 for v in b.values()))
        try:
            return scalar / (norm_a * norm_b)
        except ZeroDivisionError:
            return 0
        
    for id_q, vector_q in queries_v.items():
        for id_c, vector_c in corpus_v.items():
            print('Relevance between {} and {}:'.format(id_q, id_c))
            print('{:.2%}'.format(similarity(vector_q, vector_c)))
        print('\n')

On traite le cas où la requête contient un terme absent des documents en lui attribuant un poids de 0 et le cas où la requête ne contiendrait que des mots absents des documents (ou de poids nuls) en retournant une similarité de 0, d'où la gestion des exceptions `ZeroDivisionError` dans le programme.

Voici les résultats retournés. Pour rappel :

* Recherche A : « crime »
* Recherche B : « le crime affreux de Julien »
* Recherche C : « coupable et société »
* Rercheche D : « montagne ciel »

<p></p>

    :::text
    Relevance between Recherche A and Le Rouge et le Noir:
    3.50%
    Relevance between Recherche A and Les Misérables:
    11.20%
    Relevance between Recherche A and Candide:
    0.00%


    Relevance between Recherche B and Le Rouge et le Noir:
    10.11%
    Relevance between Recherche B and Les Misérables:
    3.88%
    Relevance between Recherche B and Candide:
    0.00%


    Relevance between Recherche C and Le Rouge et le Noir:
    4.95%
    Relevance between Recherche C and Les Misérables:
    5.28%
    Relevance between Recherche C and Candide:
    0.00%


    Relevance between Recherche D and Le Rouge et le Noir:
    0.00%
    Relevance between Recherche D and Les Misérables:
    0.00%
    Relevance between Recherche D and Candide:
    9.84%


Cet exemple est bien sûr très basique : en évaluant la similarité entre les documents, on ne prend pas en compte la place des mots dans le texte, la morphologie des phrases ni la présence éventuelle de synonymes ni même de pluriels.

Il existe plusieurs méthodes de pondération, à commencer par des variantes pour le calcul du poids TF-IDF. Par exemple, au lieu de suivre la définition de la fréquence statistique, $\mathrm{tf}(t,d)$ pourrait suivre une échelle logarithmique ou être défini comme le rapport du nombre d'occurrences du terme dans le document sur le nombre maximum d'occurrences d'un même mot dans le document, pour prendre en compte la richesse du vocabulaire utilisé. Autre point intéressant à noter, on utilise souvent une méthode différente pour calculer les poids des termes de la requête et les poids des termes des documents du corpus : en quelque sorte, on construit notre vecteur requête différemment et compte tenu de sa nature (souvent moins d'une dizaine de mots-clés), c'est compréhensible.

Finalement, dans ce domaine, il faut comme toujours se demander si une méthode est bien adaptée à **notre application** et à **nos données** : la réponse n'est pas absolue (cf. *Les questions à se poser*) et les deux exemples traités ci-dessus sont trop limités pour pouvoir conclure quoi que ce soit.
