Title: Les identificateurs en langage C
Order: 9
Date: 2014-09-27
Slug: les-identificateurs-en-langage-c
Author: Taurre
Display: true

Un identificateur peut être défini comme un nom permettant de désigner, de faire référence à une entité du langage. Un exemple d'identificateur bien connu est le nom d'une variable ou d'une fonction. Toutefois, un identificateur est plus qu'un simple nom et c'est ce qui est exposé dans ce cours.

__Remerciements :__

1. Je tiens à remercier Maëlan et Marc Mongenet pour leur relecture attentive de ce cours et leur aide dans son amélioration.


# Première approche
Un identificateur est un nom qui permet de désigner une entité du langage. Oui, mais quelles entités ? La norme C11 en différencie huit types [1] (en comptant les membres de structures/unions/énumérations à part), à savoir les identificateurs :

*    d'objet ;
*    de fonction ;
*    d'étiquette de structure/union/énumération, qui correspond au nom que vous donnez à votre structure/union/énumération ;
*    de membre de structure/union/énumération ;
*    de définition de type (__typedef__) ;
*    d'étiquette, utilisée pour l'instruction de saut __goto__ ;
*    de macro ;
*    de paramètre de macro.

__Note :__

1. En C, un objet est une zone mémoire pouvant contenir des données [2].

Afin d'illustrer cette énumération, voici un code déclarant un identificateur pour chacune des entités présentées ci‐dessus.

```c
#define identificateur_de_macro(identificateur_de_parametre_de_macro)

struct identificateur_d_etiquette_de_structure {
        int identificateur_de_membre_de_structure;
};

typedef int identificateur_de_definition_de_type;

void
identificateur_de_fonction(void)
{
        int identificateur_d_objet;

identificateur_d_etiquette:
        ;
}
```

__Note :__

1. Je ne parlerai pas des identificateurs de macro et de paramètre de macro dans la suite du tutoriel, ces derniers n'existant plus après traitement du code par le préprocesseur.

-----

[1] ISO/IEC JTC1/SC22/WG14, Doc. N1570, avril 2011, p. 35, § 6.2.1, al. 1.  
[2] _Ibid._, p. 6, § 3.15, al. 1.

# Portée, espaces de noms et masquage
Vous avez peut‐être remarqué que j'ai utilisé le terme _déclaration_ dans la présentation, ce n'est pas anodin, il s'agit d'un concept fondamental du langage C permettant la création d'identificateurs.

###La notion de portée###

Une déclaration déclare un identificateur, c'est à dire qu'elle le rend utilisable, visible pour la suite du programme. On dit qu'une déclaration confère une _portée_ à l'identificateur, c'est à dire une portion du programme où il sera utilisable. Il existe quatre types de portée [3] :

* au niveau d'un bloc ;
* au niveau d'un fichier ;
* au niveau d'une fonction ;
* au niveau d'un prototype.

Cependant, je n'aborderai pas la portée au niveau d'un prototype dans la suite de ce cours, étant donné le peu d'intérêt de cette dernière.

####Au niveau d'un bloc####

Une portée au niveau d'un bloc signifie qu'un identificateur est utilisable, visible de sa déclaration jusqu'à la fin du bloc dans lequel il est déclaré.  Ainsi, dans le code suivant :

```c
void
f(void)
{
        int n = 10;
}


void g(void)
{
        n = 20; /* Incorrect */
}
```

L'identificateur _n_ ne peut pas être utilisé dans le bloc de la fonction _g_() car il a une portée limitée au bloc de la fonction _f_().
De même, le code suivant est erroné :

```c
int *p = &a; /* Incorrect */
int a = 10;
```

car au moment de la déclaration de l'identificateur _p_, l'identificateur _a_ n'est pas encore déclaré, il est donc utilisé en dehors de sa portée.

####Au niveau d'un fichier####

Une portée au niveau d'un fichier signifie qu'un identificateur est utilisable, visible de sa déclaration jusqu'à la fin du fichier dans lequel il est déclaré.  Pour obtenir un identificateur ayant une portée au niveau d'un fichier, il est nécessaire de le déclarer en dehors de tout bloc, par exemple comme ceci :

```c
int n;

void
f(void)
{
        n = 10;
}

void
g(void)
{
        n = 20;
}
```

Dans ce code, l'identificateur _n_ a une portée au niveau du fichier et peut par conséquent être aussi bien utilisé dans la fonction _f_() que dans la fonction _g_().

####Au niveau d'une fonction####

Une portée au niveau d'une fonction signifie qu'un identificateur est utilisable, visible dans toute la fonction où il est déclaré et ce, peu importe la position de sa déclaration. Cette portée est propre aux identificateurs d'étiquette, utilisés par l'instruction de saut __goto__.

```c
int
main(void)
{
        int n = 0;

test:
        if (!n) {
                goto dix;
        } else {
                goto fin;
        }
dix:
        n = 10;
        goto test;
fin:
        return 0;
}
```

Comme vous le voyez, les identificateurs _dix_ et _fin_ peuvent être utilisés avant leur déclaration car ils ont une portée au niveau
de la fonction _main_().

###La notion d'espace de noms###

Le concept d'_espace de noms_ n'est pas évident à définir, mais est par contre très facile à comprendre à l'aide d'un exemple. Sachez tout d'abord qu'il existe quatre espaces de noms [4] :

* un dédié aux identificateurs d'étiquettes ;
* un dédié aux identificateurs d'étiquettes de structures/unions/énumérations ;
* un dédié aux identificateurs de membres de structures ou unions ;
* un dédié à tous les autres identificateurs.

__Note :__

1. Avant la normalisation du langage en 1989, les champs de structures ou d'unions ne disposaient pas forcément d'un espace de noms distinct. Cela explique pourquoi certaines structures de la bibliothèque standard préfixent le nom de leur champ (c'est le cas de la structure __tm__ par exemple).

Ensuite, comme convenu, voici un exemple.

```c
int
main(void)
{
        struct test {
                int test;
        };
        struct test test;

        goto test;
test:
        test.test = 10;
        return 0;
}
```

Comme vous le voyez, il y a quatre identificateurs déclarés avec le nom _test_ :

* un identificateur d'étiquette de structure (__struct test__, ligne 4) ;
* un identificateur de membre de structure (__int test__, ligne 5) ;
* un identificateur d'objet (__struct test test__, ligne 8) ;
* un identificateur d'étiquette (__test:__, ligne 11).

Ces quatre identificateurs ont tous une portée au niveau du bloc de la fonction _main_(). Ce code ne pose pourtant aucun problème,
tout simplement parce que ces derniers appartiennent à quatre espaces de noms différents. Tout risque de confusion est évité de par :

* le contexte d'utilisation de l'identificateur (l'instruction __goto__ attend un identificateur d'étiquette) ;
* l'utilisation de mots‐clés (__struct__/__union__/__enum__ pour désigner l'identificateur d'étiquette d'une structure/union/énumération) ;
* l'utilisation d'opérateurs (l'opérateur __.__ ou __‐>__ pour accéder aux membres d'une structure/union) ;
* la syntaxe de la déclaration (par exemple les deux points suivant la déclaration d'un identificateur d'étiquette).

###La notion de masquage###

Une règle importante à retenir est qu'il n'est pas possible de déclarer deux identificateurs de même nom et de même espace de noms dans la même portée [5]. Ainsi, le code suivant est incorrect car il déclare deux identificateurs d'objet _x_ dans le même espace de noms et dans la même portée.

```c
int
main(void)
{
        int x;
        int x; /* Incorrect */

        return 0;
}
```

Maintenant, que se passe-t-il lorsque l'on déclare deux identificateurs de même nom et de même espace de noms, mais dans des portées différentes ? Autrement dit, que se passe‐t‐il dans ce cas ci ?

```c
#include <stdio.h>

int n = 10;

int
main(void)
{
        int n = 20;

        printf("%d\n", n);
        return 0;
}
```

En fait, dans une telle hypothèse, c'est l'identificateur ayant la portée la plus faible qui sera privilégié. On dit qu'il _masque_ celui ou ceux ayant une portée plus élevée [6] (en l'occurrence celui ayant une portée au niveau d'un fichier). Je dis : « celui ou ceux », car les identificateurs déclarés dans un sous‐bloc ont une portée plus faible que ceux déclarés dans le bloc supérieur.

```c
#include <stdio.h>

int n = 10;


int
main(void)
{
        int n = 20;

        if (n == 20) {
                int n = 30;
                printf("%d\n", n);
        }
        return 0;
}
```

Dans cet exemple, il y a trois identificateurs d'objet portant tous les trois le nom _n_ :

* le premier a une portée au niveau du fichier ;
* le second au niveau du bloc de la fonction _main_() ;
* et le troisième au niveau du bloc du __if__.

L'identificateur ayant une portée au niveau du fichier est donc masqué par celui ayant une portée au niveau du bloc de la fonction _main_(), qui est lui‐même masqué par celui ayant une portée au niveau du bloc du __if__. Si l'on exécute ce petit programme, il affichera donc 30.

Notez que le masquage n'opère qu'une fois l'identificateur de portée plus faible déclaré. Ainsi, dans cet exemple :

```c
#include <stddef.h>
#include <stdio.h>

int x;


int
main(void)
{
        size_t x[sizeof x] = { sizeof x };

        printf("%zu %zu\n", x[0], sizeof x);
        return 0;
}
```

L'expression `sizeof x` utilisée pour déterminer la taille du tableau _x_ va être évaluée en utilisant l'identificateur ayant une portée au niveau du fichier, le tableau n'étant pas encore déclaré à ce moment. Toutefois, la seconde expression `sizeof x`, utilisée pour initialiser le premier membre du tableau va, elle, utiliser l'identificateur ayant une portée au niveau du bloc de la fonction _main_() ce dernier étant désormais déclaré.

-----

[3] ISO/IEC JTC1/SC22/WG14, Doc. N1570, avril 2011, p. 35, § 6.2.1, al. 2.  
[4] _Ibid._, p. 37, § 6.2.3, al. 1.  
[5] _Ibid._, p. 35, § 6.2.1, al. 2.  
[6] _Ibid._, p. 36, § 6.2.1, al. 4.

# Liaisons et définitions
Dans le chapitre précédent, nous avons entre autres vu que les identificateurs étaient confinés à une portée et que cette dernière ne pouvait s'étendre au delà d'un fichier. Cependant, si cela s'arrêtait là, il ne serait pas possible d'utiliser des objets ou des fonctions d'autres fichiers. Autrement dit, l'exemple ci‐dessous serait incorrect et il serait nécessaire de n'utiliser qu'un seul fichier source, ce qui serait assez peu commode.

— __autre.c__

```c
int
f(void)
{
        return 1;
}
```

— __main.c__

```c
int f(void);

int
main(void)
{
        f();
        return 0;
}
```

###La notion de liaison###

Heureusement, il existe une solution : la notion de _liaison_. Chaque identificateur peut disposer d'une liaison qui peut être de deux types : externe ou interne [7]. Grâce à cette notion, il est possible de considéré un groupe d'identificateurs comme faisant référence à un même objet ou à une même fonction. En fait, elle permet de préciser que :

* tous les identificateurs avec liaison externe d'un même programme font référence au même objet ou à la même fonction [8] ;
* tous les identificateurs avec liaison interne d'un même fichier font référence au même objet ou à la même fonction [8].

Ainsi, si je reprends l'exemple donné au début de ce chapitre et que l'on considère que tous les identificateurs de fonction _f_() ont une liaison externe, on peut en déduire qu'en fait, ils font tous référence à la même fonction : celle du fichier __autre.c__.

— __autre.c__

```c
int
f(void)
{
        return 1;
}
```

— __main.c__

```c
int f(void);

int
main(void)
{
        f(); /* Retournera 1 */
        return 0;
}
```

La même logique peut être appliquée pour une liaison interne, mis à part que le regroupement se limite à un fichier. En conséquence, dans l'exemple ci‐dessous, si l'on considère tous les identificateurs de fonction _f_() comme ayant une liaison interne, tous ceux situés dans le fichier __main.c__ font référence à la fonction de ce fichier, alors que celui du fichier __autre.c__ fait référence à celle située en son sein.

— __autre.c__

```c
int
f(void)
{
        return 1;
}
```

— __main.c__

```c
int
f(void)
{
        return 2;
}


int
main(void)
{
        f(); /* Retournera 2 */
        return 0;
}
```

###Conditions d'attribution###

Maintenant que vous connaissez la notion de liaison, il reste encore à déterminer dans quelles conditions cette dernière est attribuée à un identificateur. En fait, la présence d'une liaison et son type sont déterminés par la position de la déclaration de l'identificateur ainsi que par l'utilisation des mots‐clés __extern__ et __static__. Concrètement, cela se détermine suivant les règles exposées ci‐dessous.

Un identificateur de fonction ou d'objet ayant une portée au niveau d'un fichier a une liaison externe [9] [10], sauf si sa
déclaration est précédée du mot‐clé __static__, auquel cas il a une liaison interne [11].

```c
int a;         /* Liaison externe */
static int b;  /* Liaison interne */

void f(void);         /* Liaison externe */
static void g(void);  /* Liaison interne */
```

Un identificateur d'objet déclaré à l'intérieur d'un bloc n'a pas de liaison sauf s'il est précédé du mot‐clé __extern__ (voyez la règle suivante) [12].

```c
{
        int a;  /* Pas de liaison */
}
```

Un identificateur d'objet ou de fonction dont la déclaration est précédée du mot‐clé __extern__ a une liaison externe sauf si une déclaration du même identificateur la précède, auquel cas il a la même liaison que ce dernier [13].

__Note :__

1. Dans le cas où une déclaration d'un identificateur de fonction n'est précédée, ni du mot‐clé __static__, ni du mot‐clé __extern__, le mot‐clé __extern__ est implicitement ajouté [14].

Ces règles peuvent paraître quelque peu indigestes, aussi, voici un exemple illustrant chacune de ces dernières.

```c
/*
 * « a » est un identificateur d'objet déclaré en dehors de tout bloc.
 * Il a donc une liaison externe.
 */
int a;

/*
 * « b » est un identificateur d'objet déclaré en dehors de tout bloc.
 * Sa déclaration est précédée du mot‐clé « static ».
 * Il a donc une liaison interne.
 */
static int b;

/*
 * « c » est un identificateur d'objet déclaré en dehors de tout bloc.
 * Sa déclaration est précédée du mot‐clé « extern ».
 * Aucune déclaration du même identificateur ne le précède.
 * Il a donc une liaison externe.
 */
extern int c;

/*
 * « f » est un identificateur de fonction.
 * Sa déclaration n'est pas précédée du mot‐clé « extern » ou « static ».
 * Dès lors, il faut faire comme si elle était précédée du mot‐clé « extern ».
 * Aucune déclaration du même identificateur ne le précède.
 * Il a donc une liaison externe.
 */
void f(void);

/*
 * « g » est un identificateur de fonction.
 * Sa déclaration est précédée du mot‐clé « static ».
 * Il a donc une liaison interne.
 */
static void g(void);

/*
 * « h » est un identificateur de fonction.
 * Sa déclaration est précédée du mot‐clé « extern ».
 * Aucune déclaration du même identificateur ne le précède.
 * Il a donc une liaison externe.
 */
extern void h(void);


int
main(void)
{
        /*
         * « a » est un identificateur d'objet déclaré à l'intérieur d'un bloc.
         * Sa déclaration est précédée du mot‐clé « extern ».
         * Il existe déjà une autre déclaration de celui‐ci avec liaison externe.
         * Il a donc une liaison externe.
         */
        extern int a;

        /*
         * « b » est un identificateur d'objet déclaré à l'intérieur d'un bloc.
         * Sa déclaration est précédée du mot‐clé « extern ».
         * Il existe déjà une autre déclaration de celui‐ci avec liaison interne.
         * Il a donc une liaison interne.
         */
        extern int b;

        /*
         * « c » est un identificateur d'objet déclaré à l'intérieur d'un bloc.
         * Sa déclaration n'est pas précédé du mot‐clé « extern ».
         * Il n'a donc pas de liaison.
         */
        int c;

        /*
         * « d » est un identificateur d'objet déclaré à l'intérieur d'un bloc.
         * Sa déclaration est précédée du mot‐clé « extern ».
         * Aucune déclaration du même identificateur ne le précède.
         * Il a donc une liaison externe.
         */
        extern int d;

        /*
         * « g » est un identificateur de fonction.
         * Sa déclaration n'est pas précédée du mot‐clé « extern ».
         * Dès lors, il faut faire comme si elle était précédée du mot‐clé « extern ».
         * Il existe déjà une autre déclaration de celui‐ci avec liaison interne.
         * Il a donc une liaison interne.
         */
        void g(void);

        return 0;
}
```

__Note :__ 

1. Le mot‐clé __static__ ne peut être utilisé, pour modifier la liaison d'un identificateur, qu'en dehors de tout bloc et ce, aussi bien pour les identificateurs d'objet que les identificateurs de fonction [15] [16].

###La notion de définition###

Je vous ai dit que la notion de liaison permettait de grouper des identificateurs et de les considérer comme faisant référence au même objet ou à la même fonction. Je vous ai également dit que tous les identificateurs avec liaison _externe_ d'un _même programme_ font référence au même objet ou à la même fonction et que tous les identificateurs avec liaison _interne_ d'un _même fichier_ font référence au même objet ou à la même fonction. Cependant, il y a un corollaire qui découle de ces deux règles : il ne peut exister qu'_un seul objet_ ou qu'_une seule fonction_ qui puisse être référencé par le groupe d'identificateurs.

Au fond, c'est assez logique. Prenez l'exemple ci‐dessous, l'identificateur de fonction _f_ déclaré dans le bloc de la fonction _main_() a une liaison interne. Cependant, laquelle des deux fonctions désigne‐t‐il ? La première ? La deuxième ? Les deux ?

```c
static int
f(void)
{
        return 1;
}

static int
f(void)
{
        return 2;
}


int
main(void)
{
        static int f(void);

        f();
        return 0;
}
```

Il est impossible de le dire, il faudrait qu'il n'existe qu'une seule fonction ou, dit plus formellement, qu'il n'y ait qu'une seule _définition_ de la fonction _f_(). Qu'est‐ce qu'une définition ? C'est ce que nous allons voir tout de suite.

####Les identificateurs de fonction####

Une définition d'un identificateur de fonction est une déclaration qui comporte le corps de la fonction [17]. Autrement dit, dans le code ci‐dessous, le premier élément est une déclaration de l'identificateur de fonction _f_ alors que le deuxième est une définition de l'identificateur de fonction _f_ (car il comporte le corps de celle-ci) .

```c
/* Déclaration */
int f(void);	

/* Définition */
int
f(void)
{
        return 1;
}
```

####Les identificateurs d'objet####

Une définition d'un identificateur d'objet est une déclaration qui alloue l'objet qu'il référence [17]. Vous voilà bien peu avancé...  Heureusement, il y a une règle simple et absolue pour différencier une déclaration et une définition d'un identificateur d'objet : une déclaration d'un identificateur d'objet, en dehors de tout bloc, comportant une initialisation est une définition [18]. Dans tous les autres cas, il s'agit d'une déclaration.

```c
int a;          /* Déclaration */
static int b;   /* Déclaration */
extern int c;   /* Déclaration */
int d = 10;     /* Définition */
```

Cependant, il y a une (petite) subtilité : les déclarations d'identificateurs d'objet, en dehors de tout bloc, à l'exception de celles précédées du mot‐clé __extern__, sont appelées des _définitions potentielles_. Et, dans le cas où un fichier comprend une ou plusieurs définitions potentielles d'un identificateur d'objet mais aucune définition de cet identificateur, une définition est implicitement incluse au début du fichier avec un initialiseur valant zéro [19].

Rassurez-vous, nous allons revoir cela en douceur. Avant toute chose, il est nécessaire de bien différencier une déclaration, une définition potentielle et une définition d'un identificateur d'objet. Pour ce faire, voici un exemple simple.

```c
/*
 * Cette déclaration ne comporte pas d'initialisation.
 * Elle n'est pas précédée du mot‐clé « extern ».
 * Il s'agit donc d'une définition potentielle.
 */
int n;

/*
 * Cette déclaration comporte une initialisation.
 * Il s'agit donc d'une définition.
 */
extern int n = 10;

/*
 * Cette déclaration ne comporte pas d'initialisation.
 * Elle n'est pas précédée du mot‐clé « extern ».
 * Il s'agit donc d'une définition potentielle.
 */
static int n;

/*
 * Cette déclaration ne comporte pas d'initialisation.
 * Elle est précédée du mot‐clé « extern ».
 * Il s'agit donc d'une déclaration.
 */
extern int n;
```

Ensuite, reprenons cette règle pas à pas à l'aide du code ci‐dessous.

```c
int n;

int
main(void)
{
        return n;
}
```

Comme vous le voyez, nous avons un fichier comprenant une définition potentielle de l'identificateur d'objet _n_, mais aucune
définition de cet identificateur. Ce que dit l'obscure règle que je vous ai présentée auparavant, c'est que dans le cas où un fichier comprend une ou plusieurs définitions potentielles d'un identificateur mais aucune définition de cet identificateur (ce qui est le cas de notre fichier), une définition est implicitement inclue au début de ce fichier avec un initialiseur valant zéro. Autrement dit, appliquée à notre exemple, cela donne ceci :

```c
/* Définition implicite */
int n = 0;
int n;

int
main(void)
{
        return n;
}
```

####Formalisation de l'interdiction####

Maintenant que nous avons vu la notion de définition, il m'est possible de formaliser ce que je vous ai dit au début de la présentation de cette notion : il ne peut exister qu'un seul objet ou qu'une seule fonction qui puisse être référencée par un groupe d'identificateur. Ou, dit de manière plus formelle :

* il ne peut y avoir qu'une seule définition d'un même identificateur avec liaison externe dans tout le programme [20] ;
* il ne peut y avoir qu'une seule définition d'un même identificateur avec liaison interne dans un même fichier [21] ;

__Note :__

1. Certains compilateurs (gcc pour ne citer que lui) sont par défaut capables de gérer certains cas de définitions multiples. Sachez cependant qu'il s'agit d'une extension non standard. Dans le cas de gcc, il est possible de désactiver cette extension en utilisant l'option __‐fno‐common__.

Le code ci‐dessous est donc incorrect car il comporte plus d'une définition avec liaison interne de l'identificateur _n_.

```c
static int n = 10;
static int n = 20;


int
main(void)
{
        return n;
}
```

De même, le code qui suit est faux car il existe plus d'une définition avec liaison externe de l'identificateur _n_ dans tout le programme (n'oubliez pas la définition implicite !).

— __autre.c__

```c
int n = 10;
```

— __main.c__

```c
int n;

int
main(void)
{
        return n;
}
```

Notez enfin que si un identificateur apparaît dans un fichier avec à la fois une liaison externe et interne, le résultat est indéterminé [22].

— __autre.c__

```c
int
f(void)
{
        return 1;
}
```

— __main.c__

```c
int f(void);

static int
f(void)
{
        return 2;
}


int
main(void)
{
        f();
        return 0;
}
```

Dans cet exemple, l'identificateur _f_() du fichier __main.c__ a à la fois une liaison externe et interne. Il est donc impossible de dire à quelle fonction il fait référence.

###En Bref###

Que retenir de ce chapitre si ce n'est qu'il est affreusement théorique et complexe ? En fait, il est possible d'en déduire une méthode générale afin de partager des variables ou des fonctions entre plusieurs fichiers source.

Étant donné que les fichiers d'en‐têtes sont très souvent inclus dans plusieurs fichiers (pensez à ceux de la bibliothèque standard par exemple), ces derniers ne doivent contenir que des déclarations. En effet, si ce n'est pas le cas, vous allez vous retrouver avec des définitions multiples (explicites ou implicites) et, dès lors, rencontrer des erreurs lors de la compilation.

Les fichiers source, quant à eux, recueillent donc les définitions. Ainsi, lorsque vous souhaitez utiliser une ou plusieurs variables ou fonctions définies dans un autre fichier, vous incluez le ou les fichiers d'en‐tête comprenant leur déclarations dans les fichiers source où vous souhaitez les utiliser. Cette méthode a l'avantage d'éviter d'avoir à réécrire toutes les déclarations dans chaque fichier.

L'exemple ci‐dessous illustre ce qui vient d'être exposé.

— __autre.h__

```c
#ifndef AUTRE_H
#define AUTRE_H

extern int n;           /* Déclaration */
extern void setn(int);  /* Déclaration */

#endif /* !AUTRE_H */
```

— __autre.c__

```c
/* Inclusion des déclarations */
#include "autre.h"	

/* Définition potentielle */
int n;

/* Définition */
void
setn(int a)
{
        n = a;
}
```

— __main.c__

```c
/* Inclusion des déclarations */
#include <stdio.h>

#include "autre.h"

int
main(void)
{
        printf("%d\n", n); /* 0 */
        setn(99);
        printf("%d\n", n); /* 99 */
        return 0;
}
```

-----

[7] ISO/IEC JTC1/SC22/WG14, Doc. N1570, avril 2011, p. 36, § 6.2.2, al. 1.  
[8] _Ibid._, p. 36, § 6.2.2, al. 2.  
[9] _Ibid._, p. 37, § 6.2.2, al. 5.  
[10] _Ibid._, p. 37, § 6.2.2, al. 5.  
[11] _Ibid._, p. 36, § 6.2.2, al. 3.  
[12] _Ibid._, p. 37, § 6.2.2, al. 6.  
[13] _Ibid._, p. 37, § 6.2.2, al. 4.  
[14] _Ibid._, p. 37, § 6.2.2, al. 5.  
[15] _Ibid._, p. 38, § 6.2.4, al. 3.  
[16] _Ibid._, p. 110, § 6.7.1, al. 7.  
[17] _Ibid._, p. 108, § 6.7, al. 5.  
[18] _Ibid._, p. 158, § 6.9.2, al. 1.  
[19] _Ibid._, p. 158, § 6.9.2, al. 2.  
[20] _Ibid._, p. 155, § 6.9, al. 5.  
[21] _Ibid._, p. 155, § 6.9, al. 3.  
[22] _Ibid._, p. 37, § 6.2.2, al. 7.

# Les noms
Nous allons à présent terminer notre tour d'horizon des identificateurs avec un sujet plus léger et plus simple : le nom des identificateurs.

###Caractères utilisables###

Un nom est composé d'une suite de lettres et de chiffres. Oui, mais quelles lettres et quels chiffres ? La liste exhaustive nous est donnée par la norme [23].

```text
a b c d e f g h i j k l m n o p q r s t u v w x y z
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
0 1 2 3 4 5 6 7 8 9 _
```

Sachez qu'un nom ne peut pas commencer par un chiffre, il doit obligatoirement débuter par une lettre ou par un _underscore_ [24].

###Noms réservés par le langage###

Nous savons désormais de quels caractères peuvent être composés nos noms.  Cependant, tous les noms ne sont pas utilisables. En
effet, certains sont réservés par le langage C lui‐même et ne sont donc pas disponibles [25].

```c
auto            if              unsigned
break           inline          void
case            int             volatile
char            long            while
const           register        _Alignas
continue        restrict        _Alignof
default         return          _Atomic
do              short           _Bool
double          signed          _Complex
else            sizeof          _Generic
enum            static          _Imaginary
extern          struct          _Noreturn
float           switch          _Static_assert
for             typedef         _Thread_local
goto            union
```

Il est à noter que certaines implémentations réservent aussi les mots __asm__ et __fortran__. Il est donc également préférable de les éviter.

###Noms réservés par la bibliothèque standard###

À côté des noms réservés par le langage lui‐même, il y a ceux réservés par la bibliothèque standard. En fait, tous les noms de fonctions (par exemple _printf_()) ou de variables (par exemple _errno_) utilisés par celle‐ci sont à éviter, même si vous n'incluez pas l'en‐tête les utilisant.  Renseignez‐vous sur les différents en‐têtes pour obtenir les noms qu'ils emploient.

En plus de cela, la bibliothèque standard réserve certains types de noms dans des portées particulières. Ainsi, sont interdits :

* les noms commençant par un _underscore_ et une lettre majuscule ou commençant par deux _underscores_ et ce, peu importe leur portée [26] ;
* les noms commençant par un _underscore_ et ayant une portée au niveau d'un fichier [26].

Afin de bien cerner cette interdiction, voici un petit code d'exemple.

```c
/* Interdit */
#define _HELLO

/* Interdit */
#define __HELLO

/* Interdit */
#define __hello 

/* Interdit car il a une portée au niveau d'un fichier */
#define _hello

/* Interdit pour les même motifs */
struct _structure {
        /* Permis car il s'agit d'un membre de structure */
        int _membre; 
};


int
main(void)
{
        /* Permis car il a une portée au niveau d'un bloc */
        int _variable;

        /* Interdit car « auto » est un mot-clé réservé du langage */
        int auto; 

        return 0;
}
```

Remarquez enfin que dans le cas de l'en‐tête __<errno.h\>__, les noms de macro commençant par un « E » et un chiffre ou une lettre
majuscule ne doivent pas non plus être employés [27] de même pour l'en‐tête __<signal.h\>__ et les noms de macro commençant par « SIG » ou « SIG\_ » et une lettre majuscule [28].

-----

[23] ISO/IEC JTC1/SC22/WG14, Doc. N1570, avril 2011, p. 59, § 6.4.2.1, al. 1.  
[24] _Ibid._, p. 59, § 6.4.2.1, al. 2.  
[25] _Ibid._, p. 58, § 6.4.1, al. 1.  
[26] _Ibid._, p. 182, § 7.1.3, al. 1.  
[27] _Ibid._, p. 205, § 7.5, al. 4.  
[28] _Ibid._, p. 265, § 7.14, al. 4.

Voilà qui termine mon exposé sur les identificateurs. J'espère que vous y voyez désormais plus clair et que vous jonglez avec les portées et les liaisons.