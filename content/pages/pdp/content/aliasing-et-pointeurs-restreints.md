Title: Aliasing et pointeurs restreints
Order: 9
Date: 2014-09-27
Slug: aliasing-et-pointeurs-restreints
Authors: Taurre, Lucas-84
Display: true
Licence: CC-BY-NC-SA

Depuis ses débuts, le langage C pose un problème assez gênant aux compilateurs désireux d'optimiser le code, dû à son utilisation massive des pointeurs : le risque d'_aliasing_ (ou « risque de chevauchement »).

Les normes successives ont tenté de l'atténuer à l'aide de la règle de strict _aliasing_ (C89) et des pointeurs restreints (C99) ; deux concepts qui vont retenir notre attention dans ce tutoriel.

[TOC]

# Une histoire d'aliasing
Dans un premier temps, nous allons découvrir cette notion d'_aliasing_ et voir en quoi elle complique le travail du compilateur.

####Rappels

#####La notion d'objet

**C11 (N1570), § 3.15, Terms, definitions, and symbols, al. 1, p. 6.**
> object: region of data storage in the execution environment, the contents of which can represent values.

Le terme d'__objet__, qui sera au centre de nos discussions futures, désigne simplement une zone mémoire pouvant contenir des données.

#####La notion de lvalue

**C11 (N1570), § 6.3.2.1, Lvalues, arrays, and function designators, al. 1, p. 54.**
> An lvalue is an expression that [...] designates an object [...].

Une __lvalue__ est une expression qui désigne un objet (que ce soit pour un accès ou une modification).

```c
int i;
int j;
int *p;
 
/*
 * `p' est une lvalue car elle modifie un objet.
 * `&i' n'est pas une lvalue.
 */
p = &i;
 
/* `i' est une lvalue car elle modifie un objet. */
i = 10;
 
/*
 * `j' est une lvalue car elle modifie un objet.
 * `i' est une lvalue car elle accède à un objet.
 */
j = i;
 
/* `*p' est une lvalue car elle modifie un objet. */
*p = 30;
```

Gardez bien ces deux notions à l'esprit ; nous allons en avoir besoin.

####Présentation de la notion d'aliasing

En programmation, un cas d'__aliasing__ se produit lorsque plusieurs _lvalues_ désignent le même objet ; celles-ci sont alors qualifiées d'__alias__.

| Note                                     |      |
| ---------------------------------------- | ---- |
| Certaines de ces situations dépassent le cadre du présent tutoriel. Pour notre part, nous nous intéresserons uniquement aux alias résultant de l'utilisation de pointeurs, car ce sont ceux qui engendrent les difficultés les plus importantes. |      |

Par exemple, dans le code source ci-dessous, `*p` est un alias de `n`, c'est-à-dire que toute modification de `*p` aura une répercussion sur la valeur de `n` et _vice versa_.

```c
int n;
int *p = &n;
```

Cette définition peut paraître simple, mais elle comporte aussi sa part de subtilités.

```c
int a[2][10];
 
int *p = a[0];
int *q = a[1];
```

On serait ici tenté de dire que les _lvalues_ `*p` et `*q` accèdent au même objet (le tableau `a`), pourtant il n'en est rien. En effet, il ne faut pas perdre de vue que la notion d'objet est étrangère à celle de type. Dès lors, un même objet peut être subdivisé en deux autres, indépendants l'un de l'autre. `*p` et `*q` ne sont donc pas des alias.

De la même manière, dans le code ci-dessous, `*p`, `*q`, `*r` et `*s` ne le sont pas non plus.

```c
char a[4];
 
char *p = a + 0;
char *q = a + 1;
char *r = a + 2;
char *s = a + 3;
```

Cette division fonctionne jusqu'au plus petit objet possible (à savoir un _bit_ dans le cas des champs de _bits_). Ainsi, `a.i` n'est pas un alias de `a.j`.

```c
struct s {
	unsigned int i : 1;
	unsigned int j : 1;
};
 
struct s a;
```

####Problématique d'optimisation du compilateur

Si les relations d'_aliasing_ qui existent entre les différentes _lvalues_ du programme ne sont pas préoccupantes pour le programmeur, cela l'est plus pour le compilateur, qui peut être gêné dans son travail d'optimisation.

#####Problèmes causés par les alias au compilateur

Après avoir vérifié que le code source est syntaxiquement correct, le compilateur entre dans une seconde phase : celle de l'__optimisation de code__. Cette étape consiste simplement en la modification du code dans le but que l'exécution du programme se déroule le plus rapidement possible. Pour cela, il va prendre en compte certains éléments de l'implémentation, comme les différentes instructions dont dispose le processeur. Pour le moment, nous nous concentrerons uniquement sur une des optimisations les plus basiques : la __réorganisation du code__. Un exemple vaudra mieux qu'un long discours.

```c
#include <stdio.h>
 
void
f(void)
{
	const int n = 5;

	printf("%d\n", n);
}
```

Ici, force est de constater que l'instruction de la ligne 6 est inutile, puisque la variable `n` n'est pas modifiée. Aussi le compilateur pourra-t-il, par exemple, remplacer le code d'appel de cette fonction par un simple `printf("%d ", 5)`.

Le problème dans tout cela, c'est que l'aliasing complique cette réorganisation. En effet, dans le code ci-dessous, on peut se dire à première vue que le compilateur pourrait supprimer la ligne 8 et remplacer l'instruction de la ligne 10. Or, si les lvalues `*p` et `n` sont des alias, le résultat attendu est complètement différent (10 en l'occurrence). Par conséquent, compte tenu du risque d'aliasing, le compilateur est obligé de laisser ces instructions telles quelles (ce qui peut, à long terme, ralentir l'exécution du programme).

```c
#include <stdio.h>
 
static int n;
 
void
f(int *p)
{
	n = 5;
	*p = 10;
	printf("%d\n", n);
}
```

#####Analyse d'alias par le compilateur

L'__analyse d'alias__, c'est-à-dire la recherche des situations d'_aliasing_ dans un programme donné, est donc nécessaire pour le compilateur, afin de pouvoir déterminer quels cas peuvent permettre telle ou telle optimisation.

Peu importe le résultat de cette analyse (alias ou pas) : dans les deux cas, une optimisation pourra être effectuée. La seule situation problématique se produit lorsqu'on ne peut pas déterminer, lors de la compilation, les relations d'_aliasing_ qui existent entre deux _lvalues_. Le compilateur est alors obligé de considérer le pire des cas : on parle d'__aliasing pessimiste__.

```c
*p = 4;
*q = 6;
n = *p + *q;
```

Avec uniquement ces informations, le compilateur se retrouve face à trois cas distincts (en supposant que `*p`, `*q` et `n` sont de type `int`) :

* si `*p` et `*q` ne sont pas des alias, alors `n = *p + *q` pourra être remplacé par `n = 10` ;
* si `*p` et `*q` sont des alias, alors `n = *p + *q` pourra être remplacé par `n = 12` ;
* si il est impossible de déterminer les relations d'_aliasing_ qui existent entre `*p` et `*q`, alors le code ne pourra pas être modifié.

Le compilateur se doit donc d'effectuer une analyse d'alias pertinente pour sélectionner une de ces affirmations (et, si possible, une des deux premières). Dans cette optique, beaucoup algorithmes ont été développés. Néanmoins, en pratique, la plupart sont trop lourds pour être intégrés aux compilateurs courants, si bien que ces derniers se contentent généralement d'une analyse superficielle (ce qui peut se révéler pénalisant pour les performances).

# La règle de strict aliasing
Nous avons donc vu en quoi il était important pour le travail d'optimisation du compilateur de connaître les relations d'_aliasing_ qui existent entre les _lvalues_ du programme. Cette préoccupation a été au centre de beaucoup de critiques du langage C à ses débuts, qui lui reprochaient son imprécision dans l'analyse des pointeurs. Aussi la norme aide-t-elle l'analyse d'alias avec un premier concept : la __règle de strict aliasing__.

####Normalisation de la règle de strict aliasing

Nous allons maintenant faire un petit tour d'horizon de la définition et de la normalisation de cette règle en suivant un ordre chronologique (de son inauguration dans la norme C89 à sa précision dans la norme C99).

#####La norme C89

C'est en 1989 que le comité de l'ANSI décida de l'instaurer, dans le but de réduire le nombre de cas d'_aliasing_ pessimistes. Grâce à cela, le compilateur a pu affiner son analyse d'alias en présumant des _lvalues_ comme n'étant pas des alias en fonction de leur type et de celui de l'objet qu'elles désignent.

| Rappel                                   |      |
| ---------------------------------------- | ---- |
| Un objet n'a techniquement pas de type (ce n'est qu'une zone mémoire pouvant contenir des données). Cependant, afin de faciliter l'analyse d'alias, la norme leur en a fixé fictivement un. |      |

Voyons maintenant l'énoncé de la règle.

**C89 (X3J11/88-090), § 3.3, Expressions, al. 6.**
> An object shall have its stored value accessed only by an lvalue that has one of the following types :
>
> * the declared type of the object ;
> * a qualified version of the declared type of the object ;
> * a type that is the signed or unsigned type corresponding to the declared type of the object ;
> * a type that is the signed or unsigned type corresponding to a qualified version of the declared type of the object ;
> * an aggregate or union type that includes one of the aforementioned types among its members (including, recursively, a member of a subaggregate or contained union) ; or
> * a character type.

Un objet ne peut être accédé que par une _lvalue_ qui a un des types suivants :

* un type identique au type déclaré de l'objet ;
* une version qualifiée du type déclaré de l'objet ;
* un type qui est le type signé ou non signé correspondant au type déclaré de l'objet ;
* un type qui est le type signé ou non signé correspondant à une version qualifiée du type déclaré de l'objet ;
* un agrégat ou une union qui inclut un des types mentionnés ci-dessus parmi ses membres (incluant, de manière récursive, les sous-agrégats ou les sous-unions) ;
* un type caractère.

La norme se base sur le __type déclaré__ de l'objet, qui lui est attribué lors de sa définition. Par exemple, dans le code ci-dessous, deux objets sont créés, ayant respectivement comme type déclaré le type `int` et le type `double`.

```c
int n;
double x;
```

#####La norme C99

La norme C99 a peaufiné cette règle en la rapportant, non plus au type déclaré, mais au __type effectif__ de l'objet, une nouvelle notion qui permet de mieux gérer le cas dans lequel l'objet ne dispose pas de de type déclaré. Cela vise essentiellement les objets alloués dynamiquement, puisque ces derniers ne sont pas créés lors d'une définition, mais lors d'un appel à une fonction d'allocation.

**C99 (N1256), § 6.5, Expressions, al. 6, pp. 67-68.**
> The effective type of an object for an access to its stored value is the declared type of the object, if any. If a value is stored into an object having no declared type through an lvalue having a type that is not a character type, then the type of the lvalue becomes the effective type of the object for that access and for subsequent accesses that do not modify the stored value. If a value is copied into an object having no declared type using memcpy or memmove, or is copied as an array of character type, then the effective type of the modified object for that access and for subsequent accesses that do not modify the value is the effective type of the object from which the value is copied, if it has one. For all other accesses to an object having no declared type, the effective type of the object is simply the type of the lvalue used for the access.

Dans le cas où un objet n'a pas de type déclaré, son type effectif est :

* celui de la _lvalue_ le désignant (accès ou modification) ;
* celui de l'objet dont le contenu y a été copié à l'aide de `memcpy` ou `memmove`.

```c
#include <stdlib.h>
 
int *p = malloc(sizeof *p);
 
/*
 * Le type de l'objet désigné par la lvalue `*p' prend le type
 * `int'.
 */
*p = 10;
 
/*
 * Le type de l'objet désigné par la lvalue `*p' prend le type
 * `unsigned int'.
 */
*(unsigned int *)p = 20U;
```

Pour conclure, notons que la norme C11 n'a pas changé l'énoncé de la règle.

#####Illustrations de la règle de strict aliasing

Vous devriez maintenant être au point avec la définition et la normalisation de la règle de strict _aliasing_. Pour illustrer un peu nos propos, nous étudierons tout d'abord quelques exemples et contre-exemples, puis nous verrons quel intérêt le compilateur peut tirer de tout cela.

######Exemples

La question sera de savoir, pour chacune des lignes de code ci-dessous, si l'utilisation de l'alias créé est autorisé.

```c
unsigned int n;
 
/*
 * Correct, car la lvalue `*p' a un type qui est une version
 * qualifiée du type effectif de l'objet.
 */
const unsigned int *p = &n;
 
/*
 * Incorrect, car la lvalue `*q' a un type qui n'est ni une version
 * qualifiée du type déclaré de l'objet, ni le type signé ou non
 * signé correspondant, ni un type caractère.
 */
long int *q = (long int *)&n;
 
/*
 * Correct, car la lvalue `*r' a un type qui est le type signé
 * correspondant à une version qualifiée du type effectif de l'objet.
 */
const int *r = &n;
 
/* Correct, car la lvalue `*s' a un type caractère. */
signed char *s = (signed char *)&n;
```

Mentionnons que toutes ces règles s'appliquent uniquement lors du déférencement, ce qui autorise donc en soi l'affectation (bien que, naturellement, le champ d'action du pointeur soit par la suite réduit puisqu'il sera interdit de le déférencer).

```c
int n;
 
/* Correct : `p' n'est pas déférencé. */
short int *p = (short int *)&n;
 
/* Incorrect : `p' est déférencé. */
*p = 10;
```

######Bénéfices pour le compilateur

Pour le compilateur, le plus intéressant reste la conséquence de cette règle, c'est-à-dire qu'en dehors des accès autorisés mentionnés ci-dessus, deux _lvalues_ ne désigneront jamais un même objet.

Dans cet exemple, la règle de strict _aliasing_ est brisée car `*p` a un type qui n'est ni une version qualifiée du type déclaré de l'objet, ni le type signé ou non signé correspondant, ni un type caractère. Les _lvalues_ `*p` et `n` ne seront donc pas considérées comme des alias lors de la phase d'optimisation (bien qu'en vérité elles le soient). Voilà qui facilite bien l'analyse d'alias !

######Paramétrage du compilateur gcc

Avec le compilateur gcc, la règle de strict _aliasing_ n'est activée par défaut que dans les niveaux d'optimisation. Toutefois, il est possible pour le programmeur de spécifier explicitement si il veut que son code subisse les vérifications associées, à l'aide des options `-fstrict-aliasing` (respect strict de la règle) et `-fno-strict-aliasing` (tolérance de comportements non conformes à la règle).

Si l'utilisation pertinente de l'option `-fno-strict-aliasing` peut vous paraître dangereuse, puisque le code n'est alors plus conforme à la norme, l'histoire retient que de grands noms l'ont soutenu (le noyau Linux pour ne citer que lui).

gcc dispose notamment d'un avertissement permettant de prévenir les situation non conformes à la règle de strict _aliasing_.

> warning: dereferencing type-punned pointer will break strict-aliasing rules

L'option permettant de gérer de tels affichages est `-Wstrict-aliasing[=n]`, avec `n` compris entre 1 et 3 (niveau 3 par défaut). Plus `n` est petit, plus gcc fera de vérifications (par exemple, avec `n = 1` ou `n = 2`, l'avertissement peut se déclencher même si le pointeur n'est pas déférencé). De même, le pourcentage de faux positifs et de faux négatifs dépend du niveau utilisé.

Par exemple, avec gcc 4.4.5, l'avertissement ne se déclare qu'aux niveaux 1 et 2 pour ce code, au niveau de l'instruction d'affectation (ligne 5).

```c
int
main(void)
{
	unsigned int n;
	long int *p = (long int *)&n;

	*p = 10L;
	return 0;
}
```

Si la règle de strict _aliasing_ constitue une aide réelle à l'analyse d'alias des compilateurs, il reste encore le cas des alias de type identique (ou ne différant que par le signe et/ou par le qualificateur, ainsi que celui des types caractères). Il est évident qu'on ne peut pas interdire cette pratique, qui signifierait l'abolition des pointeurs ! Mais c'est à ce moment-là que le programmeur entre en scène avec l'_aliasing_ spécifié, thème qui fera l'objet de notre prochaine sous-partie.

# Les pointeurs restreints
Malgré cette règle, il reste donc encore quelques situations d'_aliasing_ compromettantes. Comme la norme et les compilateurs ne peuvent plus faire d'hypothèses supplémentaires, c'est le programmeur lui-même qui est sollicité.

####Introduction aux pointeurs restreints

L'_aliasing_ spécifié par le développeur est implémenté dans la norme C99 sous la forme de la notion de __pointeur restreint__. L'idée est de permettre la mise en place d'un droit exclusif d'accès sur un objet référencé par un pointeur qualifié de restreint. Ce droit ne peut être transmis qu'à des _lvalues_ dérivées de ce pointeur, c'est-à-dire qui ont obtenu l'adresse de l'objet _via_ celui-ci.

#####Le qualificateur restrict

Pour déclarer un pointeur restreint, la norme C99 a mis à la disposition des programmeurs un nouveau qualificateur : `restrict`. Il est applicable uniquement aux pointeurs sur objet ; il doit donc être placé, lors de la déclaration, après le symbole `*`.

```c
/* `p' est un pointeur restreint sur `int'. */
int * restrict p;
 
/* `q' est un pointeur sur pointeur restreint sur `int'. */
int * restrict *q:
 
/* `r' est un pointeur restreint sur pointeur sur `int'. */
int ** restrict r;
```

#####Définition

Le passage à propos de `restrict` dans la norme C99 peut paraître alambiqué et tordu ; nous vous ferons donc grâce des citations. L'essentiel du fonctionnement des pointeurs restreints peut se résumer dans les deux règles suivantes.

1. il ne peut y avoir qu'un seul pointeur restreint référençant un même objet dans un même bloc ;
2. une _lvalue_ ne peut modifier un objet référencé par un pointeur restreint que si elle est dérivée de ce dernier.

#####Quelques exemples

À ce stade, la définition peut vous paraître encore un peu floue, c'est pourquoi nous vous proposons quelques petits exemples.

```c
#include <stdlib.h>

static char * restrict r, * restrict s;

void
copy(void * restrict dst, void * restrict src, size_t n)
{
	/*
	 * Valide car `p' et `q' ne sont pas des pointeurs
	 * restreints.
	 */
	char *p = dst;
	char *q = src;

	while (n-- != 0) {
		/*
		 * Valide car les lvalues `*p' et `*q' sont
		 * respectivement basées sur les pointeurs restreints
		 * `dst' et `src'.
		 */
		*p++ = *q++;
	}

	/*
	 * Invalide car `r' et `s' sont des pointeurs restreints et
	 * référencent, respectivement, les mêmes objets que `dst' et
	 * `src' dans le bloc de la fonction `copy'.
	 */
	*r = *s;
}

int
main(void)
{
	/*
	 * Valide car `r' et `s' référencent deux objets différents
	 * dans le bloc de la fonction main.
	 */
	r = malloc(10);
	s = malloc(10);

	/*
	 * Valide car `dst' et `src' référencent deux objets
	 * différents dans le bloc de la fonction `copy'.
	 */
	copy(r, s, 10);

	/*
	 * Invalide car `dst' et `src' référencent le même objet dans
	 * le bloc de la fonction `copy'.
	 */
	copy(r, r, 10);

	/*
	 * Invalide car `r' et `s' référencent alors le même objet
	 * dans le bloc de la fonction main.
	 */
	r = s;
	return 0;      
}
```

Bien qu'il soit techniquement possible d'assigner des pointeurs restreints à des pointeurs non restreints, c'est une pratique déconseillée car cela peut compliquer le travail d'optimisation du compilateur.

####Bénéfice des pointeurs restreints

À l'instar de la règle de strict _aliasing_, les pointeurs restreints permettent aux compilateurs d'effectuer des présomptions quant aux relations d'_aliasing_ qui existent entre les pointeurs d'un même bloc. En effet, deux pointeurs restreints sont garantis de ne pas être des alias. Ainsi, c'est toute la phase d'optimisation de code qui en profite, et notamment la réorganisation du code.

#####La vectorisation

De plus, étant donné que le mot-clé `restrict` vise des pointeurs de même type, cela laisse également place à une optimisation plus poussée faisant intervenir les tableaux : la __vectorisation__. Cette dernière pratique consiste à effectuer des opérations sur des petits tableaux de taille fixe plutôt que sur un seul élément à la fois. Cela est possible sur la plupart des processeurs modernes, qui disposent d'instructions spécialisées travaillant sur plusieurs éléments à la fois : les __instructions vectorielles__.

Dans les exemples suivants, nous considérerons un processeur disposant d'instructions vectorielles capables de travailler sur 128 _bits_, c'est-à-dire ici de 16 `char` ou de 4 `int`. Elles seront illustrées par les trois fonctions suivantes :

* `vect_cpy16` : copie un tableau de 16 `char` ;
* `vect_cpy4` : copie un tableau de 4 `int` ;
* `vect_add4` : additionne deux tableaux de 4 `int` et stocke le résultat dans le premier.

#####Exemple (1)

```c
void
memcpy(void * restrict dst, void * restrict src, size_t n)
{
	char *p = dst;
	char *q = src;

	while (n-- != 0)
		*p++ = *q++;
}
```

Dans le code ci-dessus, la règle de strict _aliasing_ est inutile car les _lvalues_ `*p` et `*q` sont toutes deux de type `char`. En revanche, elles sont basées sur un pointeur restreint et sont donc garanties de ne pas être des alias. Le compilateur pourrait donc vectoriser cette boucle, en copiant des tableaux de taille fixe plutôt que des `char` un par un.

```c
void
memcpy(void * restrict dst, void * restrict src, size_t n)
{
	char *p = dst;
	char *q = src;
	size_t i;

	for (i = 0; n - i >= 16; i += 16)
		vect_cpy16(p + i, q + i);

	for (; i < n; ++i)
		p[i] = q[i];
}
```

#####Exemple (2)

```c
void
vect_add(int * restrict res, int * restrict a, int * restrict b, size_t n)
{
	for (size_t i = 0; i < n; ++i)
		res[i] = a[i] + b[i];
}
```

De la même manière, le code ci-dessus opère sur des _lvalues_ basées sur des pointeurs restreints. Ainsi, le compilateur pourrait utiliser des instructions vectorielles afin d'optimiser le code comme suit.

```c
void
vect_add(int * restrict res, int * restrict a, int * restrict b, size_t n)
{
	size_t i;

	for (i = 0; n - i >= 4; i += 4) {
		vect_cpy4(res + i, a + i);
		vect_add4(res + i, b + i);
	}

	for (; i < n; ++i)
		res[i] = a[i] + b[i];
}
```

####Dangers des pointeurs restreints

Malgré tout, il est important de prendre des précautions lors de l'utilisation des pointeurs restreints ; ils ne doivent en effet pas être utilisés à tout-va.

#####Confusion entre appelant et appelé

Si deux pointeurs sont indiqués comme étant restreints mais, qu'en réalité, ils se chevauchent, le résultat est indéterminé et le code produit a de fortes chances d'être incorrect.

```c
#include <string.h>

void
f(void)
{
	int a[8] = { 0, 0, 45, 42, 12, 89, 2, 36 };

	/*
	 * Les deux arguments restreints de `memcpy' se chevauchent,
	 * c'est une situation de comportement indéterminé.
	 */
	memcpy(a, a + 2, 6);
}
```

Or, nous pouvons remarquer que c'est à la fonction appelée de préciser si les arguments doivent être restreints, mais seule la fonction appelante peut contrôler si ces arguments sont conformes (le compilateur ne peut pas faire cette vérification par lui-même).

#####Précautions d'utilisation

On distingue deux grands cas dans lesquels on peut utiliser les pointeurs restreints.

1. Si l'algorithme de la fonction ne fonctionne pas ou n'a aucun sens dans le cas où les paramètres se chevauchent, alors le résultat avec les pointeurs restreints sera toujours incorrect, mais pourra avoir changé. Par exemple, le chevauchement des deux paramètres dans la fonction `fopen` serait complètement absurde.
2. Si le principe de la fonction a un sens dans le cas où les arguments se chevauchent mais que cela est pénalisant pour les optimisations, alors il est préférable de créer deux versions de la fonction (une avec `restrict` et une sans), à la manière des fonctions `memcpy` et `memmove`.

| Attention                                |      |
| ---------------------------------------- | ---- |
| Lors d'un comportement indéterminé, théoriquement, tout peut se passer. Le compilateur a donc tout à fait le droit de produire un code qui arrête brutalement le programme pour éviter de propager une éventuelle erreur. C'est pourquoi il ne faut pas oublier de prévenir l'utilisateur de ces spécifications dans la documentation de la fonction. C'est par exemple le cas pour la fonction `memcpy`. |      |

Au final, on peut représenter tout cela par une sorte de contrat passé entre les deux fonctions. Si il n'est pas respecté par la fonction appelante, alors la fonction appelée se réserve le droit de produire un code incorrect.

####Une optimisation vraiment valable ?

Il ne faut pas oublier que `restrict` est une simple indication et pas une obligation pour le compilateur. Aussi les détracteurs du mot-clé ont-ils souvent souligné le fait que le gain de temps octroyé par l'utilisation des pointeurs restreints n'est pas toujours très important (par exemple, les processeurs qui ne disposent pas d'instructions vectorielles ne jouiront pas de cette optimisation).

Nous pouvons donc légitimement nous demander si l'utilisation des pointeurs restreints est réellement rentable par rapport à l'effort de réflexion associé (qui est loin d'être négligeable). Plusieurs travaux ont conclu que ce n'était pas le cas, et déconseillent donc l'_aliasing_ spécifié.

À vous de vous forger votre propre avis ; n'hésitez pas, dans cette optique, à construire vos propres étalonnages suivant votre utilisation du langage. En tout cas, si vous êtes prêts à fournir un effort supplémentaire pour un bénéfice, si minimal qu'il soit, vous voilà informés !

Ainsi, ce tutoriel touche à sa fin. Nous espérons vous avoir éclairé sur ce difficile sujet d'aliasing et de pointeurs restreints. La norme du langage C est, aujourd'hui encore, une des seules normes de langage de programmation qui prône l'optimisation des compilateurs, le C cherche donc toujours à prouver ses qualités en performances pures.

####Liens externes
#####Alias et optimisation
* (en) [Optimisation de code par le compilateur sur Wikipédia](http://en.wikipedia.org/wiki/Compiler_optimization).  
* (en) [Optimisation de boucles sur Wikipédia](http://en.wikipedia.org/wiki/Loop_optimization).  
* (fr) [Pipeline des instructions sur Wikipédia](http://fr.wikipedia.org/wiki/Instruction_pipeline).  
* (en) [Les processeurs vectoriels sur Wikipédia](http://en.wikipedia.org/wiki/Vector_processor).  
* (en) [Guide de programmation pour la vectorisation des compilateurs C/C++](http://www.drdobbs.com/programming-guidelines-for-vectorizing-c/184401611).

#####Analyse d'alias
* (en) [Analyse d'alias sur Wikipédia](http://en.wikipedia.org/wiki/Alias_analysis).  
* (en) [Exemple d'algorithme effectuant une analyse d'alias performante](http://www.cs.ucla.edu/%7Epalsberg/course/purdue/cs661/F01/papers/das-pldi00.pdf).  
* (en) [L'analyse d'alias de gcc](http://gcc.gnu.org/onlinedocs/gccint/Alias-analysis.html).

#####Règle de strict aliasing
* (en) [Comprendre le strict aliasing](http://cellperformance.beyond3d.com/articles/2006/06/understanding-strict-aliasing.html).  
* (en) [Type-punning et strict aliasing](http://labs.qt.nokia.com/2011/06/10/type-punning-and-strict-aliasing/).  
* (en) [Comprendre le strict aliasing en C/C++](http://dbp-consulting.com/StrictAliasing.pdf).

#####Paramétrage du compilateur
* (en) [Voir les raisons de l'utilisation de -fno-strict-aliasing dans le noyau Linux](https://lkml.org/lkml/2003/2/26/158).  
* (en) [Page de manuel de gcc (recherchez « -fstrict-aliasing »)](http://gcc.gnu.org/onlinedocs/gcc-4.7.1/gcc/Optimize-Options.html#Optimize-Options).

#####Les pointeurs restreints
* (fr) [Le C et ses raisons : les pointeurs restreints](http://blog.huoc.org/pointeurs-restrict.html).  
* (en) [Les pointeurs restreints en C](http://www.lysator.liu.se/c/restrict.html).  
* (en) [Defect Report #294](http://www.open-std.org/jtc1/sc22/wg14/www/docs/dr_294.htm).  
* (en) [Démystification du mot-clé restrict](http://cellperformance.beyond3d.com/articles/2006/05/demystifying-the-restrict-keyword.html).  
* (en) [Pourquoi l'_aliasing_ spécifié est une mauvaise idée](http://www.cs.pitt.edu/%7Emock/papers/clei2004.pdf).