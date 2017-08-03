Title: La règle de la "spirale horaire" (Clockwise/Spiral Rule)
Order: 9
Date: 2014-09-27
Slug: 
Authors: David Anderson, victor
Display: true

Texte initialement posté par email sur comp.lang.c par son auteur, David
Anderson, le 6/5/1994.

[TOC]

----

Il existe une technique connue sous le nom de "règle de la spirale horaire" qui
permet à tout programmeur C de parser toute déclaration C de tête !

Elle consiste à suivre trois étapes simples :

1. En partant du premier élément inconnu, se déplacer en spirale dans le sens
  horaire; lorsqu'on rencontre l'élément suivant, le remplacer par son équivalent
  en langue naturelle :

    `[X]` ou `[]` → Tableau de taille X de… ou Tableau de taille indéfinie de…

    `(type1, type2)` → fonction recevant type1 et type2 retournant…

    `*` → pointeur(s) sur…

2. Répéter l'étape 1. en spirale, dans le sens horaire, jusqu'à ce que tous les
  jetons ont été parcourus.

3. Toujours résoudre les parenthèses en premier !

### Example #1 : Simple déclaration

    :::text
                     ┌───────┐
                     │ ┌─┐   │
                     │ ▲ │   │
                char *str[10];
                 ▲   ▲   │   │
                 │   └───┘   │
                 └───────────┘

La question qu'on se pose :

* Qu'est-ce que `str` ?

    `str` est un…

* On se déplace en spirale horaire commençant par `str` et le premier caractère
  qu'on rencontre est `[`, il s'agit donc d'un tableau, donc…

    `str` est un tableau 10 de…

* Continuons en spirale horaire, et le prochain jeton que nous rencontrons est
  `*`, ce qui signifie que nous avons des pointeurs, donc…

    `str` est un tableau 10 de pointeurs sur…

* Toujours en spirale horaire, nous arrivons en fin de ligne (le `;`) et nous
  en continuant nous arrivons sur le type `char`, donc…

    `str` est un tableau 10 de pointeurs sur char

* Nous avons maintenant "visité" tous les jetons, nous avons donc fini !


### Example #2 : Déclaration d'un pointeur sur fonction

    :::text
                     ┌────────────────────┐
                     │ ┌───┐              │
                     │ │┌─┐│              │
                     │ │▲ ││              │
                char *(*fp)( int, float *);
                 ▲   ▲ ▲  ││              │
                 │   │ └──┘│              │
                 │   └─────┘              │
                 └────────────────────────┘

La question qu'on se pose :

* Qu'est-ce que `fp` ?

    `fp` est un…

* En se déplaçant en spirale horaire, la première chose que l'on voit est `)`;
  ce qui signifie que `fp` est entre parenthèses, nous continuons donc notre
  spirale à l'intérieur de la parenthèse et le prochain caractère rencontré est `*`, donc…

    `fp` est un pointeur sur…

* Nous sommes désormais hors des parenthèses et continuons en spirale horaire,
  nous voyons `(`, il s'agit d'une fonction donc…

    `fp` est un pointeur sur fonction recevant un int et un pointeur sur flottant
    retournant…

* Toujours en spirale, nous voyons `*`, donc…

    `fp` est un pointeur sur fonction recevant un int et un pointeur sur flottant
    retournant un pointeur sur…

* Suivant encore la spirale, nous voyons `;`, mais nous n'avons pas encore
  visité tous les jetons, nous devons continuer et finalement tombons sur char,
  donc…

    `fp` est un pointeur sur fonction recevant un int et un pointeur sur flottant
    retournant un pointeur sur char.


### Exemple #3 : le "Final"

    :::text
                      ┌─────────────────────────────┐
                      │                  ┌───┐      │
                      │  ┌───┐           │┌─┐│      │
                      │  ▲   │           │▲ ││      │
                void (*signal(int, void (*fp)(int)))(int);
                 ▲    ▲      │      ▲    ▲  ││      │
                 │    └──────┘      │    └──┘│      │
                 │                  └────────┘      │
                 └──────────────────────────────────┘

La question que nous nous posons :

* Qu'est-ce `signal` ?

    Remarquez que `signal` est entre parenthèses, nous devons donc les résoudre
    en premier !

* En se déplaçant dans le sens horaire, nous voyons `(`, nous avons donc…

    `signal` est une fonction recevant un int et un…

* Hmmm, nous pouvons appliquer la même règle à `fp`, donc… Qu'est-ce que `fp` ?
  `fp` est aussi entre parenthèses, donc continuons et nous voyons une `*`, donc…

    `fp` est un pointeur sur…

* Continuons en spirale horaire et nous arrivons à `(`, donc…

    `fp` est un pointeur sur une fonction recevant un int et retournant…

* Maintenant continous hors des parenthèses de la fonction et nous obtenons
  `void`, donc…

    `fp` est un pointeur sur une fonction recevant un int et ne retournant
    rien (void)

* Fini avec `fp`, retournons à notre `signal`, nous avons maintenant…

    `signal` est une fonction recevant un int et un pointeur sur une fonction
    recevant un int et ne retournant rien retournant…

* Nous sommes encore dans des parenthèses, donc le prochain caractère rencontré
  est `*`, donc…

    `signal` est une fonction recevant un int et un pointeur sur une fonction
    recevant un int et ne retournant rien retournant un pointeur sur…

* Nous avons maintenant résolu tous les jetons présents dans des parenthèses,
  continuons dans le sens horaire et arrivons à `(`, donc…

    `signal` est une fonction recevant un int et un pointeur sur une fonction
    recevant un int et ne retournant rien retournant un pointeur sur une
    fonction recevant un int et retournant…

* Finalement, nous continuons et la seule chose restante et le mot `void`, et
  donc la définition complète de `signal` est :

    `signal` est une fonction recevant un int et un pointeur sur une fonction
    recevant un int et ne retournant rien retournant un pointeur sur une
    fonction recevant un int et ne retournant rien (void).

La même règle s'applique à `const` et `volatile`. Par exemple :

    const char *chptr;

* Qu'est-ce que `chptr` ?

    `chptr` est un pointeur sur un char constant

Que dites-vous de ça :

    char * const chptr;

* Qu'est-ce que `chptr` ?

    `chptr` est un pointeur constant sur un char

Finalement :

    volatile char * const chptr;

* Qu'est-ce que `chptr` ?

    `chptr` est un pointeur constant sur un char volatile.

Vous pouvez vous entrainer en appliquant cette règle aux exemples du K&R II,
page 122.

----

Copyright © 1993,1994 David Anderson

Traduction © 2013 victor / [progdupeu.pl](http://progdupeu.pl)

Cet article peut être librement distribué à condition que les noms des auteurs
et cette notice soient conservés. Librement traduit sur la base de
[cette reproduction](http://c-faq.com/decl/spiral.anderson.html) du texte
original.
