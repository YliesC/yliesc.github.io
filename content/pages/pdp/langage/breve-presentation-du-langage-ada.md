Title: Brève présentation du langage Ada
Order: 9
Date: 2014-09-27
Tags: ada, tutoriel
Slug: breve-presentation-du-langage-ada
Author: MicroJoe
Display: true

[TOC]

## Pourquoi Ada ?

### Historique (très résumé)

Ada est un langage qui fut créé vers la même époque que le C++ par [le Département de la Défense des États-Unis](https://en.wikipedia.org/wiki/United_States_Department_of_Defense).

Cependant, on remarque aujourd'hui que l'on parle beaucoup plus du langage C++ que d'Ada. En effet, Ada n'a pas réussi à s'imposer face au C++ a l'époque et cela se fait bien ressentir de nos jours ; cependant il n'en reste pas moins un langage intéressant, il est encore utilisé dans certains domaines et possède un développement toujours actif (la dernière spécification validée à cette date se prénommant « Ada 2012 »).

### Caractéristiques

Ada est avant tout un langage de programmation impératif (voire objet, mais je ne l'ai pas encore utilisé de cette façon).

Voici le fameux exemple du « Hello world! » appliqué à ce langage :

```ada
with Ada.Text_IO; use Ada.Text_IO;
procedure Hello is
begin
  Put_Line ("Hello, world!");
end Hello;
```

#### Le typage fort

Le langage Ada est un langage que l'on qualifie de « fortement typé ». Cela veut dire que l'on ne pourra pas faire n'importe quoi avec les types et qu'il faudra expliciter chaque conversion que l'on veut faire : on ne pourra pas convertir implicitement un `float` en `double` par exemple.

**Exemple : les intervalles**

Ada permet l'utilisation d'intervalles (*ranges*) et vous en rencontrerez assez souvent. Ces intervalles permettent de créer de nouveaux types et on aura alors l'assurance qu'une variable de ce type aura une valeur comprise dans cet intervalle.
Par exemple, on peut définir un octet comme un entier dans l'intervalle `(0..255)` ou alors un jour du mois dans l'intervalle `(1..31)` et on est assuré que les variables du type `JourDuMois` auront une valeur comprise dans l'intervalle. Ada fourni des intervalles comme `Natural` qui représente en fait un entier positif (compris entre 0 et la valeur maximale du type `Integer` que l'on peut obtenir par `Integer'Last`).

#### La modularité

Ada permet et encourage l'écriture de modules dans le but de séparer un programme complexe dans plusieurs fichiers. Cela permet d'entreprendre la création de gros programmes sans pour autant s'y perdre.

On notera que pour accèder aux élements d'un module, il faudra par défaut les précéder du nom du module, comme par exemple `Ada.Text_IO.New_Line` (mais on retrouve comme en C++ avec `using namespace` une instruction nommée `use` qui permet de s'affranchir de cette notation, bien que cela reste facultatif). Le chargement des modules utilisés, lui, est obligatoire et se fait à l'aide de l'instruction `with`, ce qui correspond un peu aux `import` du langage Python.

De même qu'en C et C++, on retrouve le principe des fichiers *headers* (extension `.ads`) et des fichiers d'implémentation (extension `.adb`) permettant de séparer la déclaration et l'implémentation. On retrouve donc les mêmes avantages, notamment pouvoir connaitre les principaux types, fonctions et procédures contenus dans un module sans pour autant devoir visualiser l'implémentation.

#### La lisibilité

Beaucoup de programmeurs sont rebutés par la syntaxe du langage qui s'avère assez verbeuse. Néanmoins, Ada privilégie dans ses principes la relecture à la rédaction de programmes ; en effet, on relira beaucoup plus de fois un programme que l'on ne l'écrira. L'utilisation de mots clés complets tels que `loop`, `begin` ou `end` permettent de mieux comprendre le code en un coup d’œil au lieu d'avoir recours aux accolades ouvrantes/fermantes.

Un des exemples de cette lisibilité est la possibilité d'utiliser des noms dans les `end` afin de savoir quel bloc on vient de quitter. Prenons l'exemple suivant :

```ada
procedure Toto is
begin
    -- Plein de code sur plusieurs lignes
end Toto;
```

Même si on ne voit plus de début de la procédure, on sait que l'on quitte Toto à cet endroit précis du code.

Au niveau des conventions de nommage, il faut savoir que l'on est relativement libre : en effet, **la syntaxe du langage n'est pas sensible à la casse**, ainsi, rien ne vous empêche d'écrire le code suivant si on reprend l'exemple ci-dessus :

```ada
PRocedure toTO IS
bEGIN
    -- Plein de code sur plusieurs lignes
end TOTO;
```

Cependant, vous remarquez qu'on a bien perdu en lisibilité par rapport à l'exemple précédent. Il est donc courant d'adopter des conventions au niveau de la syntaxe dont les deux principales recommandations sont :

* Les variables/procédures/fonctions seront au format `Ma_Super_Fonction`.
* Les mots clés seront écrits en minuscules : `declare`, `begin`, `end`, etc.

On remarquera également qu'il est possible d'utiliser les *underscores* pour rendre les nombres plus lisibles dans le code :

```ada
Mon_Entier := 1_000_123 ;
```

On peut également écrire des entiers en utilisant des bases allant de 2 à 16 :

```ada
Mon_Entier := 13#42# ; -- On utilise ici une base 13, nativement
```

Pour en savoir plus, voir ça : <https://en.wikibooks.org/wiki/Ada_Style_Guide/Readability>

#### Bas niveau

Ada permet de faire de la programmation bas niveau, des interruptions à la gestion manuelle de la mémoire avec des pointeurs (comme en C) afin de permettre de l'utiliser dans les systèmes embarqués par exemple. Cependant, typage fort oblige, on ne retrouve pas le moche `void*` du C (pointeur pouvant pointer vers n'importe quel type) et il serait inutile car Ada permet également [la programmation générique](https://en.wikibooks.org/wiki/Ada_Programming/Generics).

## Utilisations

Ada a été développé pour le département militaire des États-Unis et par conséquent ce langage est toujours utilisé dans ce domaine (nous pouvons par exemple citer l'hélicoptère Apache et les systèmes de combat des sous-marins de l'armée américaine ou encore les fusées Ariane 4 et 5). Cependant, on retrouve également ce langage dans le domaine civil et plus particulièrement dans les secteurs dits « critiques » tels que :

 * la finance ;
 * le médical ;
 * les télécommunications ;
 * les transports ;
 * la gestion des centrales nucléaires.

Ce langage a notamment été utilisé pour les systèmes de l'Airbus 380 ou encore le Boeing 787 au niveau de l'aviation. On retrouve aussi Ada dans le ferroviaire, par exemple dans les TGV de la SNCF ou encore… dans le métro de Paris !

Comme vous pouvez le voir, Ada est bel et bien présent autour de nous dans la vie de tous les jours sans que nous nous en rendions forcément compte !

## Manque de popularité

C'est ce qui – je pense – fait le plus d'ombre au langage. Ce problème est en fait dû par un lot de circonstances, parmi lesquelles :

* Les premiers compilateurs Ada coûtaient très cher et étaient à destination de machines puissantes ce qui fait qu'il était très compliqué pour un particulier de pouvoir développer dans ce langage à cause de ces restrictions.
* Ada a été créé pour le domaine militaire à la base. De ce fait, certains programmeurs n'ont pas hésité à boycotter le langage de par sa provenance et de l'utilisation qu'il en était faite (des pacifistes aux « hippies » principalement).
* Le manque de ressources est un réel frein pour encourager des personnes à apprendre ce langage. En effet, les écrits qu'ils soient sur Internet ou sur papier semble dater d'assez longtemps (années 2000 pour la plupart). Cependant, pour motiver les éditeurs à publier de nouveaux livres pour Ada il faudrait une demande importante, mais cette demande est limitée en partie par le manque de ressources ; on tourne un peu en rond.
* Il n'existe pas d'application libre programmée en Ada et ayant connu une popularité suffisante pour motiver les programmeurs à s'essayer à ce langage. De plus le support de Windows a souvent été négligé ce qui a pu rebuter pas mal de potentiels nouveaux utilisateurs du langage.

Comme vous pouvez le constater assez facilement, le fait que le langage ne soit pas l'un des plus populaires lui ternit son image récursivement de ce fait. Par exemple, les portages de bibliothèques populaires vers le langage Ada se font assez rares de par le manque de personnes compétentes pour effectuer et surtout maintenir ce portage.

## Comment programmer en Ada ?

### Trouver des cours

Les ressources concernant Ada sont assez rares par rapport à ce que l'on peut trouver sur les langages C ou C++. Néanmoins, un cours intéressant au format PDF, en français et rédigé pour l'UIT d'Aix-En-Provence [est disponible sur Developpez](http://ada.developpez.com/cours/iut/).
On trouve également d'autres cours mais la plupart son en anglais, comme [le tutoriel Lovelace](http://www.adahome.com/Tutorials/Lovelace/) ou [cet autre tutoriel sur Wikibooks](https://en.wikibooks.org/wiki/Ada_Programming).

### Trouver des outils

GNAT est un compilateur libre (GNU GPL) faisant partie de la fameuse suite GCC. Il permet de compiler des sources Ada en exécutables, cependant si vous êtes un adepte des IDE alors vous pourriez être intéressé par GPS, l'IDE développé par ceux qui maintiennent actuellement Ada.

Comme vous avez pu le remarquer, Ada est souvent également utilisé dans les domaines de l'embarqué. Si vous souhaitez vous aussi tenter l'expérience de l'embarqué avec Ada, sachez qu'il existe un compilateur nommé avr-ada qui permet de compiler du code Ada pour les microcontrôleurs AVR d'ATMEL (incluant donc les cartes Arduino qui sont souvent basées sur ce genre de microcontrôleurs).

## Un petit mot sur SPARK

J'aimerai finir cet article en vous parlant du langage SPARK. C'est un sous-ensemble du langage Ada (cela implique que l'on peut compiler du code SPARK en utilisant un compilateur Ada sans aucun problème mais l'inverse n'est pas vrai).
Il est destiné à être employé dans les systèmes critiques et apporte des sécurités en plus au langage via l'utilisation de commentaires possédants un formatage spécifique. Ceux-ci permettent de, par exemple, dire que la fonction sur laquelle on travaille de devrait jamais toucher aux variables globales.
Cela peut se traduire en SPARK de la façon suivante :

```ada
procedure Increment (X : in out Counter_Type);
--# derives X from X;
```

Cette notation dit que la procédure n'utilisera aucune variable globale et qu'elle n'aura besoin que de la valeur de X en entrée pour assigner X en sortie (ce qui est bel et bien le cas pour réaliser une incrémentation).
Si on veut signaler qu'une procédure utilisera une variable globale pour effectuer certaines opérations, on peut alors le spécifier comme ceci :

```ada
procedure Increment (X : in out Counter_Type);
--# global Count;
```

Et en rajoutant des annotations `derives` pour consolider les vérifications. De cette manière, on peut s'assurer que l'appel à une fonction n’entrainera pas de modifications sur des variables globales qui peuvent être sensibles telles que par exemple la profondeur d'enfoncement des tiges dans un réacteur nucléaire.

De plus, ces vérifications seront effectuées lors de la compilation du programme à l'aide d'une **analyse statique du code** et non pas à l'exécution, ce qui pourrait être dangereux. Ainsi, SPARK permet de sécuriser encore plus le développement d'applications à l'aide d'Ada dans les domaines où les erreurs logicielles peuvent avoir des conséquences dramatiques.

## Conclusion

J’espère que cet article vous aura permis de mieux comprendre les enjeux de l'utilisation d'Ada au sein de notre société dans laquelle l'informatique prend de plus en plus de place. Grâce à Ada et aux concepts sur lesquels ce langage repose tels que le typage fort et la maintenabilité, on peut réaliser des programmes à la fois stables, sûrs et performants prêts à être employés sur le terrain.
N'hésitez pas à parcourir la toile et les livres à propos d'Ada pour en savoir encore plus et pourquoi pas vous lancer dans son apprentissage !

**Sources :**

 * [Ada (Programming language)](https://en.wikipedia.org/wiki/Ada_%28programming_language%29)
 * [Ada Programming](https://en.wikibooks.org/wiki/Ada_Programming)
 * [Information for new Ada95 programmers](http://www.cl.cam.ac.uk/~mgk25/ada.html)
 * [Who's Using Ada?](http://www.seas.gwu.edu/~mfeldman/ada-project-summary.html)
 * [Apprendre à programmer avec Ada](http://www.siteduzero.com/informatique/tutoriels/apprendre-a-programmer-avec-ada)
