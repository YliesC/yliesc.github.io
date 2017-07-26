Title: Le langage C
Order: 9
Date: 2015-06-11
Slug: le-langage-c
Authors: mewtow, paraze, Lucas-84, informaticienzero, Taurre
Licence: CC-BY-NC-SA
Display: true

**Vous souhaitez apprendre à programmer, mais vous ne savez pas comment vous y prendre ? Ou bien vous voulez réviser ?** Alors, permettez-nous de vous souhaiter la bienvenue dans ce cours de programmation en C pour débutants. La programmation est devenue aujourd'hui incontournable, si bien qu’elle est utilisée partout. Tous les logiciels de votre ordinateur ont été programmés. Et ce cours va vous apprendre les bases de la programmation en C pour vous permettre de créer des programmes à votre tour.

Pour pouvoir suivre ce tutoriel, vous n’avez aucun pré-requis ; tout sera détaillé de la manière la plus complète possible.
Nous commencerons par une introduction à la programmation et au C, puis nous avancerons peu à peu dans l'univers de la programmation, tout cela grâce à des cours, des exemples, des exercices d’applications et des travaux pratiques.

[TOC]

# Introduction
Cette première partie sera l'occasion de se familiariser avec les concepts de base de la programmation et du C et de pouvoir commencer à pratiquer en écrivant quelques programmes. Lisez-la bien attentivement, même si vos avez déjà une expérience en programmation, car il est impossible de bien programmer en C si les bases ne sont pas solides.


## Introduction à la programmation
La programmation est un sujet qui fascine énormément. Si vous lisez ce cours, c’est que vous avez décidé de franchir le pas et de découvrir ce que c’est que programmer. Avant de commencer à apprendre quoi que ce soit sur le C et la programmation, il faudrait néanmoins se demander en quoi la programmation consiste. En effet, savez-vous réellement ce que c’est, comment programmer ou encore ce qui caractérise ce fameux langage C ? Ces questions importantes et légitimes méritent des réponses. Ce chapitre va donc faire une introduction au monde de la programmation, et plus particulièrement au langage C.

### Avant-propos
### Esprit et but du tutoriel ###

Ce tutoriel a été écrit dans un seul but : vous enseigner le langage C de la manière la plus complète, la plus rigoureuse et la plus instructive possible. Pour ce faire, le tutoriel combinera beaucoup de théorie, de connaissances importantes, de détails et de recherches en profondeur avec de la pratique par des exemples concrets, des exercices pratiques et des TP. Cette approche va réclamer de votre part des efforts puisque le tutoriel semblera parfois complexe.  

Nous avons choisi cette méthode d’apprentissage, car c’est celle que nous jugeons la plus payante. Elle s’oppose à une plus rapide, qui permet certes d’acquérir des connaissances rapidement, mais qui s’avère bien souvent peu payante sur le long terme, beaucoup de programmeurs débutants étant ainsi perdus lorsqu’ils sont jetés dans la jungle de la programmation à la sortie d’un cours, n’ayant pas acquis de bonnes pratiques et de la rigueur. Nous allons donc essayer de vous enseigner non seulement un langage, mais aussi de bonnes pratiques et de la rigueur.

En résumé, ce tutoriel fera un juste mélange entre théorie, détails et recherches avec de la pratique et des exemples.

### À qui est destiné ce tutoriel ? ###

Le tutoriel a pour but d’être accessible à n’importe qui. Que vous soyez un programmeur expérimenté, un total débutant ou que vous vouliez réviser certaines notions du C, vous êtes le bienvenu dans ce tutoriel. Les explications seront les plus claires possible afin de rendre la lecture accessible à tous.

Cependant, il y a quelques conditions. Même si nous avons conçu le tutoriel pour être clairs, il vous faut plusieurs qualités pour arriver à tenir jusqu’au bout.

* De la **motivation** : ce tutoriel va présenter de nombreuses notions, souvent très théoriques, et qui sembleront parfois complexes. Il vous faut donc être bien motivés pour profiter pleinement de cet apprentissage.	
  * De la **logique** : apprendre la programmation, c’est aussi être logique. Bien sûr, ce tutoriel vous apprendra à mieux l’être, mais il faut néanmoins savoir réfléchir par soi-même et ne pas compter sur les autres (tutoriels ou forums) pour faire le travail à sa place.
* De la **patience** : vous vous apprêtez à apprendre un langage de programmation. Pour arriver à un sentiment de maitrise, il va falloir de la patience pour apprendre, comprendre, s’entrainer, faire des erreurs et les corriger.
* De la **rigueur** : cette qualité, nous allons tenter de vous l’inculquer à travers ce cours. Elle est très importante, car c’est elle qui fera la différence entre un bon et un mauvais programmeur.
* De la **passion** : le plus important pour suivre ce tutoriel, c'est de prendre plaisir à programmer. Amusez-vous en codant, c'est le meilleur moyen de progresser !

Je tiens aussi à préciser qu’un niveau acceptable en anglais est très fortement recommandé. En effet, beaucoup de cours, de forums, de documentations et autres seront en anglais. Tôt ou tard, vous serez confronté à l'anglais, il faut vous y préparer. Si vous êtes encore étudiant, cela ne vous sera que bénéfique ! Si vraiment l’anglais n’est vraiment pas votre fort, vous pouvez utiliser un dictionnaire pour vous aider.

Dernier point qui concerne les mathématiques : contrairement à la croyance populaire, un bon niveau en maths n’est absolument pas nécessaire pour faire de la programmation. Certes, ça peut aider en développant la logique, mais si les mathématiques ne sont pas votre fort, vous pourrez quand même suivre ce cours sans problèmes.

### Allez plus loin ###

Un des concepts fondamentaux de l’apprentissage de notions informatiques sur Internet est le *croisement des sources*. Il permet de voir la programmation sous un angle différent. Par exemple, quelques cours de [Developpez](http://c.developpez.com/cours/?page=lang-c) d’approches différentes sont à votre entière disposition. N’hésitez pas non plus à lire des livres sur le C, notamment le [K&R](http://en.wikipedia.org/wiki/The_C_Programming_Language), écrit par les auteurs du C (une version traduite en français est disponible [aux éditions Dunod](http://www.dunod.com/informatique-multimedia/developpement/cc/ouvrages-denseignement/le-langage-c)). C’est un livre très complet qui pourra vous être utile.

Enfin le plus important : n’hésitez pas à programmer tout seul. Faites des exercices, modifiez les codes du tutoriel, regardez ceux des autres, participez à des projets. C’est la meilleure façon de progresser.

### La programmation, qu’est-ce que c’est ?
La programmation est une branche de l’informatique qui sert à créer des **programmes**. Tout ce que vous possédez sur votre ordinateur sont des programmes : votre navigateur Internet (Internet Explorer, Firefox, Opera, etc.), votre système d’exploitation (Windows, GNU/Linux, etc.) qui est un regroupement de plusieurs programmes appelé **logiciel**, votre lecteur MP3, votre logiciel de discussion instantanée, vos jeux vidéos, etc.

### Les programmes expliqués en long, en large et en travers ###

Un programme est une séquence d’**instructions**, d’ordres, donnés à l’ordinateur afin qu’il exécute des actions. Ces instructions sont généralement assez basiques. On trouve ainsi des instructions d’addition, de multiplication, ou d’autres opérations mathématiques de base, qui font que notre ordinateur est une vraie machine à calculer. D’autres instructions plus complexes peuvent exister, comme des opérations permettant de comparer des valeurs, traiter des caractères, etc.

Créer un programme, c’est tout simplement créer une suite d’instructions de base qui permettra de faire ce que l’on veut. Tous les programmes sont créés ainsi : votre lecteur MP3 donne des instructions à l’ordinateur pour écouter de la musique, le *chat* donne des instructions pour discuter avec d’autres gens sur le réseau, le système d’exploitation donne des instructions pour dire à l’ordinateur comment utiliser le matériel et comment fonctionner, etc.

Petite remarque : on ne peut pas créer d’instructions. Notre ordinateur est conçu, câblé, et peut traiter certaines instructions de bases, précâblées dans ses circuits, sans possibilité d’en inventer d’autres (sauf cas particulier vraiment tordus). Notre ordinateur contient un composant électronique particulier, spécialement conçu pour effectuer ces instructions : il s’agit du **processeur**. Ce qu’il faut retenir, c’est que notre ordinateur contient un circuit, le processeur, qui permet d’effectuer de petits traitements de base qu’on appelle instructions et qui sont la base de tout ce qu’on trouve sur un ordinateur.

Ces instructions sont stockées dans notre ordinateur sous la forme de bits, de petites données qui valent soit 0, soit 1. Ainsi, nos instructions ne sont rien d’autre que des suites de 0 et de 1, stockées dans notre ordinateur, et que notre processeur va interpréter comme étant des ordres à effectuer. Ces suites de zéros et un sont difficilement compréhensibles pour nous humains, et parler à l’ordinateur avec des 0 et des 1 est très dur et très long. Autant vous dire que créer des programmes de cette façon revient à se tirer une balle dans le pied. 

Pour vous donner un exemple, imaginez que vous devez communiquer avec un étranger alors que vous ne connaissez pas sa langue. Communiquer avec un ordinateur reviendrait à devoir lui donner une suite de 0 et de 1 : ça risque de prendre énormément de temps et cela serait difficile. Tout se passe comme si votre processeur parlait un langage particulier, composé de suite de zéro et d’un bien organisé, et qu’il était incapable de parler autre chose. Le langage du processeur s’appelle le **langage machine**. Une question doit vous venir à l'esprit : comment communiquer avec notre processeur sans avoir à apprendre sa langue ?

L’idéal serait de parler à notre processeur en français, en anglais, etc. Mais disons-le clairement : notre technologie n’est pas suffisamment évoluée, et nous avons dû trouver autre chose. La solution retenue a été de créer des langages de programmation plus évolués que le langage du processeur, plus faciles à apprendre, et de fournir le traducteur qui va avec. Ces langages de programmation plus évolués sont des sortes de langages assez simplifiés, assez proches des langages naturels, et dans lesquels on peut écrire nos programmes beaucoup plus simplement qu’en utilisant le langage machine. Grâce à eux, on peut écrire nos programmes sous forme de texte, sans avoir à se débrouiller avec des suites de 0 et de 1 totalement incompréhensibles. Il existe de nombreux langages de programmation, et le C est un de ces langages.

Reste que notre processeur ne comprend pas ces langages évolués ; il ne comprend qu’un seul langage, le sien. Pour utiliser nos langages de programmation, il faut aussi avoir une sorte de traducteur qui fera le lien entre votre langage de programmation et le langage machine du processeur. Ce traducteur va ainsi traduire du texte (écrit dans un langage de programmation évolué) en une suite de zéro et d’un que le processeur peut comprendre. Ainsi vous pourrez commander votre processeur même si vous ne parlez pas sa langue. 

Pour illustrer, ce code écrit en C (que nous apprendrons à connaître) est quand même largement plus facile à comprendre qu’une suite de 0 et de 1.

```c
#include <stdio.h>

int main(void)
{
    printf("Salut !");
    return 0;
}
```
*Imaginez la même chose composée de 0 et de 1, et vous comprendrez tout l'intérêt d'un langage de programmation.*

Il ne reste plus qu’à utiliser un interprète qui va traduire ce texte (un programme écrit dans notre langage de programmation) vers la langue de l’ordinateur (des suites de 0 et de 1) : le **compilateur**. Voici un petit schéma qui résume tout ça :

![Schéma simplifié de la compilation](../../../progdupeupl//galleries/63/b2c79712-d527-4f49-801a-1c770dd2437a.png)

### Le langage C
Malgré tous ces langages de programmation disponibles, nous allons dans ce tutoriel nous concentrer sur un seul langage : le langage C. Avant de parler des caractéristiques de ce langage et des choix qui nous amènent à l’étudier dans ce cours, faisons un peu d’histoire.

### L'histoire du C ###

Le langage C est né au début des années 1970 dans les laboratoires AT&T aux États-Unis. Son concepteur, [Dennis Ritchie](http://fr.wikipedia.org/wiki/Dennis_Ritchie), souhaitait améliorer un langage existant, le B, afin de lui adjoindre des nouveautés. En 1973, le C était pratiquement au point, et il commença à être distribué l’année suivante. Son succès était tel auprès des informaticiens que l'ANSI en 1989, puis l’ISO en 1990 décidèrent de le normaliser, c’est-à-dire d’établir les règles officielles du langage. On parle donc de C89 / C ANSI ou bien C90 / C ISO (au choix). D’autres normes sortirent plus tard, en 1999 (on parle de C99) et en 2011 (on parle de C11).

*Si vous voulez en savoir plus sur l’histoire du C, lisez donc [ce tutoriel](http://c.developpez.com/cours/historique-langage-c/).*

### Pourquoi apprendre le C ? ###

C’est une très bonne question. Après tout, il existe tellement de langages différents, et on peut logiquement se demander pourquoi le C en particulier ? Il y a plusieurs raisons à ça.

* Sa **popularité** : il fait partie des langages de programmation les plus utilisés. Il possède une communauté très importante et de nombreux tutoriels et documentations. Vous aurez donc toujours du monde pour vous aider. De plus, il existe beaucoup de programmes et de bibliothèques développés en et pour le C.	
* Sa **rapidité** : le C est connu pour être un langage très rapide, ce qui en fait un langage de choix pour tout programme où la vitesse est cruciale.
  * Sa **légèreté** : le C est léger, ce qui le rend utile pour les programmes embarqués où la mémoire disponible est faible.
* Sa **portabilité** : cela veut dire qu’un programme développé en C marche théoriquement sur n’importe quelle plateforme. Il faut savoir que le C a été conçu pour la programmation système (drivers, systèmes d'exploitation, matériel embarqué, etc). Or, les plate-formes étant différents, il était difficile à l'époque d'avoir un code générique pouvant marcher sur n'importe quel environnement. La volonté des créateurs du C était donc de faire un langage permettant de produire du code portable.

Ce ne sont que quelques raisons, mais elles sont à mon gout suffisantes pour apprendre ce langage. Bien entendu, le C comporte aussi sa part de défauts. On peut citer la tolérance aux comportements dangereux qui fait que le C demande beaucoup de rigueur pour ne pas tomber dans certains « pièges », un nombre plus restreint de concepts (c’est parfois un désavantage, car on est alors obligé de recoder certains mécanismes qui existent nativement dans d’autres langages), etc. D’ailleurs, si votre but est de développer rapidement des programmes amusants, le C n’est pas du tout adapté pour ça, et je vous encourage à vous tourner vers d’autres langages comme le Python par exemple.

Le C possède aussi une caractéristique qui est à la fois un avantage et un défaut : c’est un langage plutôt de **bas niveau**. Cela veut dire qu’il permet de programmer en étant proche de sa machine, en cherchant à vraiment comprendre ce que l’on fait. C’est à double tranchant : c’est plus difficile et plus long, mais on en apprend beaucoup sur sa machine et on a un grand contrôle de ce que l’on fait. Cette notion de bas niveau est d’ailleurs à opposer aux langages de **haut niveau**, qui permettent de programmer en faisant abstraction d’un certain nombre de choses. Le développement est souvent plus facile et plus rapide, mais en contrepartie on voit moins bien le fonctionnement de la machine. Ces notions de haut et bas niveau sont néanmoins à nuancer, car elles dépendent du langage utilisé et du point de vue du programmeur. 

Je termine cette partie en rajoutant quelque chose. Peut-être avez-vous entendu parler du C++. C’est un langage de programmation qui a été inventé dans les années 1980 par Bjarne Stroustrup, un collègue de Dennis Ritchie, qui souhaitait rajouter des éléments au C. Bien que très ressemblants à l’époque de sa création, ces deux langages sont aujourd’hui très différents (on ne programme pas et on ne réfléchit pas de la même façon en C qu’en C++). Ne croyez pas qu’il y a un langage meilleur que l’autre. Ils sont simplement différents. Si d’ailleurs votre but est d’apprendre le C++, je vous encourage à le faire. Contrairement à ce que l’on pense et dit souvent, il n’y a pas besoin de connaitre le C pour ça. Ce tutoriel ne se concentrera quant à lui que sur ce dernier.

### La norme ###

Comme précisé plus haut, le C est un langage qui possède des règles. Ces règles ont été définies par des informaticiens professionnels et sont toutes regroupées dans ce que l’on appelle **la norme** du langage. Cette norme sert de référence à tous les programmeurs. Chaque fois que l’on a un doute ou que l’on se pose une question, le premier réflexe est de regarder dans la norme ce qui est dit. Bien entendu, la norme n’est pas parfaite et ne répond pas à toutes les questions, et ne précise pas tous les détails. Néanmoins, elle reste la référence du programmeur. 

Cette norme sert aussi de référence pour les compilateurs. En effet, tous les compilateurs respectent cette norme (en règle générale), ce qui fait qu’il n’y aura pas différentes interprétations d’un même code. Cette norme est l’équivalent des règles d’orthographe, de grammaire et de conjugaison de nos interprètes. Imaginez si chacun écrivait ou conjuguait à sa guise tout ce qu'il veut. La norme sert donc à officialiser tout un tas de règles pour que tous les interprètes (et donc les compilateurs) la suivent.

Il existe plusieurs versions de la norme : le C89, le C99 et le C11. Dans ce cours, nous avons décidé de nous servir de la norme C89. En effet, même si c’est la plus ancienne et qu’elle semble restrictive à certains, elle permet néanmoins de développer avec n’importe quel compilateur sans problèmes, contrairement aux normes C99 et C11 que tous les compilateurs ne connaissent pas. De plus, il est très facile de passer aux normes plus récentes ensuite. Voici [le lien](http://flash-gordon.me.uk/ansi.c.txt) vers le brouillon de cette norme. Cela signifie que ce n’est pas la version définitive et officielle de la norme, celle-ci est très chère à obtenir, alors que le brouillon est largement suffisant pour notre niveau et gratuit. Bien entendu, cette norme est en anglais.

*[ANSI]: American National Standard Institute
*[ISO]: International Standard Organisation

### L’algorithmique
L'algorithmique est très liée à la programmation, et elle constitue même une branche à part des mathématiques. Elle consiste à définir et établir des algorithmes.

Un algorithme peut se définir comme étant une suite finie et non-ambiguë d'opérations permettant de résoudre un problème. En clair, il s'agit de calculs qui prennent plusieurs paramètres et fournissent un résultat. Les algorithmes ne sont pas limités à l'informatique, ils existaient même avant son apparition ; prenez les recettes de cuisine par exemple, ou des instructions de montage d'un meuble ou d'un Lego : ce sont des algorithmes.

L'intérêt principal des algorithmes est qu'ils sont très utiles lorsqu'ils sont en relation avec des ordinateurs. En effet, ces derniers peuvent exécuter des milliards d'instructions à la seconde, ce qui les rend bien plus rapides qu'un humain. Illustrons : imaginez que vous deviez trier une liste de 10 nombres dans l'ordre croissant. C'est assez facile et faisable en quelques secondes. Et pour plusieurs milliards de nombres ? C'est impossible pour un humain, alors qu'un ordinateur le fera rapidement.

Ce qu'il faut retenir, c'est qu'un algorithme est une suite d'opérations destinée à résoudre un problème donné. Nous aurons l'occasion d'utiliser quelques algorithmes dans ce cours, mais nous ne nous concentrerons pas dessus. Si vous voulez en savoir plus, lisez le tutoriel sur [l'algorithmique pour l'apprenti programmeur](/tutoriels/62/algorithmique-pour-lapprenti-programmeur/) en même temps que vous apprenez à programmer avec celui-ci.

### Le pseudo-code ###

Pour représenter un algorithme indépendamment de tout langage, on utilise ce qu'on appelle un **pseudo-code**. Il s'agit de la description des étapes de l'algorithme en langage naturel (dans notre cas le français). Voici un exemple de pseudo-code :

```console
Fonction max (x, y)
    
    Si x est supérieur à y
        Retourner x
    Sinon 
        Retourner y

Fin fonction
```

Dans ce cours, il y aura plusieurs exercices dans lesquels un algorithme fourni devra être implémenté (traduit) en C. Si vous voulez vous entrainer davantage tout en suivant ce cours, je vous conseille [France-IOI](http://www.france-ioi.org/) qui permet d'implémenter divers algorithmes en plusieurs langages dont le C. Cela pourra être un excellent complément.

Comme vous avez pu le constater, la programmation est un monde vaste, très vaste, et assez complexe. Comme il existe une multitude de langages de programmation, il faut se concentrer sur un seul d’entre eux à la fois. Dans notre cas, il s’agit du C. Ce langage, et retenez-le bien, est à la fois très puissant et complexe. Souvenez-vous bien qu’il vous faudra faire des efforts pour l’apprendre correctement.

Si vous vous sentez prêts, alors rendez-vous dans le chapitre suivant, qui vous montrera les outils utilisés par un programmeur en C.

## Outils
Maintenant que les présentations sont faites, il est temps de découvrir les outils nécessaires pour programmer en C. Le strict minimum pour programmer se résume en trois points.

* Un **éditeur de texte** : ce logiciel va servir à écrire le code source. En théorie, n’importe quel éditeur de texte suffit, mais le mieux est d’en avoir qui colore le code source, ce qui permet une relecture plus agréable.	
* Un **compilateur** : c’est le logiciel le plus important puisqu’il va nous permettre de transformer le code que l’on écrit en un fichier exécutable compréhensible par le processeur.
* Un ***débugger* / débogueur** (prononcez « débegueur ») : fondamentalement, il n’est pas indispensable, mais ce logiciel est très utile pour chasser les bugs et vérifier le comportement de son programme.

À partir de là, il existe deux moyens de récupérer tous ces logiciels : soit on les prend séparément, et dans ce cas il faut compiler par soi-même, soit on utilise un logiciel qui réunit les trois : un IDE (EDI en français).

Face à la multitude de logiciels différents qui existent, ce chapitre a pour but de vous guider en vous montrant quelques logiciels, que ce soit pour compiler à la main ou avec un IDE.

*[IDE]: Integrated Development Environment
*[EDI]: Environnement de Développement Intégré

### Windows
Bien que de nombreux IDE soient disponibles pour Windows, nous ne parlerons que de deux d’entre eux : Code::Blocks et Visual C++, sans oublier une partie consacrée à la compilation ''via'' l’invite de commande.

### Avec un IDE ###
#### Code::Blocks ####

Code::Blocks est un IDE gratuit et libre (vous pouvez obtenir le code source du logiciel si vous le souhaitez), qui fonctionne avec plusieurs compilateurs différents et qui n’est pas très compliqué à prendre en main. Il n’est cependant disponible qu’en anglais (bien qu’il existe des traductions incomplètes en français) ; néanmoins, avec un dictionnaire et de l’intuition, vous vous en sortirez très bien.

Pour télécharger Code::Blocks, rendez-vous sur [le site officiel](http://www.codeblocks.org/ ), dans la section « *[Downloads]([http://www.codeblocks.org/downloads/)* », puis dans la sous-section « *Download the binary release* ». Cette section vous permettra de télécharger le logiciel ; contrairement à la section « *Download the source code*' » qui sert à télécharger le code source de Code::Blocks.

Il va falloir ensuite télécharger la version du logiciel adaptée à votre système d’exploitation.

* **Windows** : choisissez « `codeblocks-XX.XXmingw-setup.exe` » pour télécharger la version de Code::Blocks pour Windows avec un compilateur intégré. Si vous choisissez la première, vous ne pourrez pas compiler vos programmes ! Je le répète donc encore une fois : choisissez la version avec **mingw** dans le nom. Pour information, MinGW est une adaptation pour Windows du compilateur GCC.
* **Linux** : choisissez la version qui correspond à votre distribution. Attention à ne pas confondre les versions 32 bits et 64 bits.
* **Mac** : téléchargez le fichier proposé.

Une image pour bien comprendre :

![La bonne version à télécharger est entourée de rouge](../../../progdupeupl//galleries/63/3cf4d2c8-811d-48ba-8fb2-dc0d170129fb.png)

Si cependant vous êtes expérimentés et que vous souhaitez installer votre propre compilateur, vous pouvez prendre la première version. Ensuite pour l’installation, laissez-vous guider, elle est très simple. Une fois l’installation terminée, en lançant Code::Blocks, vous devriez obtenir ceci :


![Page principale au lancement de Code::Blocks](../../../progdupeupl//galleries/63/f7e98007-fd02-4436-9dd2-69facaca3938.png)


Cela vous parait compliqué ? Je vais tout vous expliquer dans quelques secondes. Avant, j’aimerais qu’on crée un projet, pour que je puisse vous illustrer tout ça. Pour ce faire, deux possibilités : ou vous cliquez sur « *Create a new project* » dans le menu de démarrage, ou bien vous cliquez sur « *File -> New -> Project* ». Dans tous les cas, vous tombez sur cette fenêtre :

![Fenêtre de choix de création de projet](../../../progdupeupl//galleries/63/11ea2315-c6f6-4c2d-b8df-61df49920891.png)


Choisissez l’icône « *Console application* », entourée en gras sur l’image. Puis double-cliquez dessus ou cliquez sur le bouton « Go » pour créer un projet de type console.

Le premier menu est juste un menu informatif, cliquez sur « *Next* ». La page suivante vous demande quel langage vous voulez utiliser. Sélectionnez « *C* » puis « *Next* ». Vous arrivez ensuite sur cette fenêtre :


![Première fenêtre lors de la création d'un projet](../../../progdupeupl//galleries/63/dfc77369-19a8-49be-841b-c66770fb72d8.png)


Là, il y a plusieurs champs.

* **Project title** : c’est le nom que vous souhaitez donner à votre projet. Un même nom ne peut pas être utilisé plusieurs fois, il faut un nom différent pour chaque projet.	
  * **Folder to create project in** : c’est le répertoire dans lequel le projet sera créé.
* **Project filename** et **resulting filename** : ces champs sont remplis automatiquement par Code::Blocks, on ne s'en préoccupe pas.

Ensuite, dernière fenêtre :


![Deuxième fenêtre lors de la création d'un projet](../../../progdupeupl//galleries/63/73ef3695-4a66-4a20-bc63-3453ff764b37.png)


* **Compiler** : permet de choisir le compilateur que l’on veut utiliser. Ici, comme il n’y a que ce compilateur d’installé, on n’y touche pas.
* **Create "Debug" configuration** : cochez cette case pour avoir un exécutable compilé en mode *Debug*, c’est-à-dire un programme non optimisé qui contiendra toutes les informations nécessaires pour déboguer. L’exécutable ne sera pas portable. 
* **Create "Release configuration'''** : le programme est optimisé, portable et allégé puisqu’il ne possède plus les informations de débogage.

Choisir entre les deux modes importe peu pour l’instant. Il faut simplement que l’un des deux au moins soit coché. Cliquez sur « Finish » pour terminer la création du projet. Maintenant, vous devez avoir une fenêtre comme celle-ci :


![Page principale de Code::Blocks après la création d'un projet](../../../progdupeupl//galleries/63/75e17622-2d3f-4cf0-a7e2-3da2c9f7d964.png)


Je pense que quelques explications ne seraient pas de refus.

1. C’est la **liste des menus**. Certains seront très utilisés, tandis que d’autres presque pas. Retenez que le menu « *File* » est l’un des plus utilisés.
2. Ce sont les **icônes**. Voici les quatre principales :
    * ![Icône Build](../../../progdupeupl//galleries/63/8c0a63e0-b9a3-4d1c-a693-df68cf09ec7d.png) -> c'est l'icône « *Build* », qui sert à compiler le fichier sans le lancer ; le raccourci clavier est **Ctrl + F9**.
    * ![Icône Run](../../../progdupeupl//galleries/63/56e675ac-b2b6-429f-9ae5-7d3d4fe5db5f.png) -> c’est l’icône « *Run* », qui lance le dernier exécutable compilé ; le raccourci clavier est **Ctrl + F10**.
    * ![Icône Build & Run](../../../progdupeupl//galleries/63/e9d9d7ed-c5ca-4eb9-a668-e0b294a9f23c.png) -> c’est l’icône « *Build & Run* », la contraction des deux icônes précédentes : elle compile et exécute ; le raccourci clavier est **F9**.
    * ![Icône Rebuild](../../../progdupeupl//galleries/63/da8d5f16-4f17-4179-ae5c-cd8eb9429aa0.png) -> c’est l’icône « *Rebuild* », qui sert à recompiler tous les fichiers ; par défaut, Code::Blocks ne les recompile pas tous (seuls ceux qui ont été modifiés sont recompilés) ; le raccourci clavier est **Ctrl + F11**.
3. C’est la **zone des projets**. C’est ici que vous pouvez voir tous les fichiers qui composent votre projet. Vous pouvez même avoir plusieurs projets en même temps, mais vous ne pouvez en compiler qu’un à la fois.
4. C’est la **zone principale**, car c’est ici que l’on écrit le code source.
5. C’est la **zone de notification** où apparaissent les erreurs, les messages de compilation, les messages du débogueur, ainsi que les les avertissements.

Vous pouvez voir que Code::Blocks a généré un code par défaut. Nous allons le compiler. Utilisez les icônes ou les raccourcis clavier pour se faire. Il se peut que vous obteniez un message d'erreur comme celui-ci :

```console
"My-program - Release ou Debug" uses an invalid compiler. Skipping...
Nothing to be done.
```

Si cela vous arrive, ne paniquez pas. Il y a deux causes possibles.
​	
* **Vous utilisez Code::Blocks et vous avez téléchargé la version sans compilateur** : dans ce cas, retournez sur le site officiel et prenez la version avec MinGW.
* **Vous avez la bonne version et dans ce cas c’est le chemin vers le compilateur MinGW qui est incorrect** : rendez-vous dans « *Settings -> Compiler&Debugger -> Toolchain executable* », cliquez sur « … », et saisissez le répertoire « *MinGW* » dans votre installation (si vous avez installé Code::Blocks avec MinGW, celui-ci se trouve dans le répertoire de Code::Blocks), puis cliquez sur OK.

Une fois le problème réglé (si problème il y avait), le programme est compilé et un message apparait dans la console :

```console
Hello world!

Process returned 0 (0x0)   execution time : x.xxx s
Press any key to continue.
```

La première ligne correspond à ce qu'affiche le programme. Les deux lignes suivantes sont elles spécifiques à Code::Blocks. La première indique à l'utilisateur si le programme s'est bien déroulé ou s'il y a eu erreur et le temps écoulé depuis le lancement. La seconde demande d'appuyer sur une touche pour continuer. En effet, sans cette dernière ligne, nous n'aurions pas pu voir le programme se lancer qu'il serait déjà terminé. Ce comportement est spécifique à Windows.

#### Visual C++ ####

Visual C++ est un IDE édité par Microsoft et très efficace, car adapté pour Windows. Il possède aussi un débogueur puissant. Bien qu’il ne soit pas libre, Visual C++ est gratuit (dans sa version express) et disponible en de nombreuses langues, dont le français. Il suffit tout simplement d’enregistrer le logiciel pour l’utiliser sans limites de temps ; c’est gratuit et rapide, vous n’avez besoin que d’une adresse mail.

Pour télécharger Visual C++, rendez-vous sur le [site de Microsoft](http://msdn.microsoft.com/fr-fr/express/aa975050.aspx ). Cliquez ensuite sur l’onglet « *Visual C++ 2010 Express* ». Vous arriverez sur la page de téléchargement. Sélectionnez la langue que vous voulez puis cliquez sur « *Télécharger* ».

Le programme d’installation va se charger de tout télécharger et tout installer. À un moment, vous devrez redémarrer. Acceptez, et une fois le redémarrage terminé, l’installation finira tranquillement.

Voici à quoi ressemble Visual C++ 2010 Express :


![Page principale après le lancement de Visual](../../../progdupeupl//galleries/63/5c951ab8-42fb-493b-97e6-34ecb00c1ccb.png)


Comme pour Code::Blocks, j’aimerais vous montrer la création d’un projet avant de vous expliquer l’image. Pour cela, deux possibilités : cliquez sur « *Nouveau projet* » au démarrage, ou bien « *Fichier ->Nouveau -> Projet* ». Vous devriez obtenir cette fenêtre :


![Création de projet page 1](../../../progdupeupl//galleries/63/e4044415-850f-41fe-950a-9877bb32b4ba.png)


Pour créer un projet en console, sélectionnez « *Application console Win32* », et donnez un nom à votre projet dans la case « Nom » en bas de la fenêtre. Une fois ceci fait, vous arrivez sur une fenêtre à propos des paramètres de votre projet. Cliquez sur « *Suivant* » en bas ou « *Paramètres de l’application* » dans la colonne à gauche. Vous devez tomber sur une fenêtre comme celle-ci :


![Création projet page 2](../../../progdupeupl//galleries/63/ffe261a3-4001-4e05-a9c2-24f951caa480.png)


Sélectionnez « *Projet vide* » pour commencer avec un projet vierge, sinon Visual va créé un projet avec des fichiers dont nous ne voulons pas. 

Pour rajouter des fichiers, la manœuvre est très simple : faites un clic droit sur l’onglet « *Fichiers sources* » dans la colonne de gauche, puis allez dans « *Ajouter -> Nouvel élément…* ». Une petite image pour bien comprendre :


![Ajouter un fichier](../../../progdupeupl//galleries/63/0bd2d4b5-023c-4a44-93b4-1f735d9f50c0.png)


Une nouvelle fenêtre apparait alors pour vous demander quel type de fichier il faut ajouter au projet. Cliquez sur « *Fichiers C++ (.cpp)* » (même si ce type de fichier est normalement réservé au C++), et appelez votre fichier `main.c`. Il faut que le fichier se termine par `.c`, sinon Visual ajoutera automatiquement l’extension `.cpp` qui est celle des fichiers C++. Donc faites-y attention ! 

Et si nous examinions un peu les menus de Visual C++ ? Vous devriez normalement avoir une fenêtre comme celle-ci :


![Page principale après la création d'un projet et l'ajout d'un fichier](../../../progdupeupl//galleries/63/235c27b3-975a-4c55-a9c9-71a6668cfa5b.png)


Regardons plus attentivement ces quatre zones.

1. La **barre d’outils** : elle contient tous les menus et les raccourcis (comme la compilation, la génération, etc), certains seront plus utilisés que d’autres.
2. La **zone principale** : c’est ici que l’on écrira le code.
3. L'**explorateur de solutions** : cette zone permet de gérer les fichiers qui composent notre projet. Visual y organise les fichiers en trois types : les fichiers sources, les fichiers ressources et les fichiers d’en-tête (nous verrons tout ça en temps voulu).
4. La **zone de notification** : c’est dans cette zone qu’apparaissent les erreurs, les informations du débogueur, les avertissements et les messages de compilation.

Voici quelques raccourcis claviers pratiques que vous serez souvent amenés à utiliser :

* **F5** : lance l’exécutable en appelant le débogueur ;	
  * **Ctrl + F5** : lance l’exécutable sans appeler le *débugger* ;
  * **F7** : génère une solution (compile) sans lancer le programme ;      
* **Ctrl + Alt + F7** : régénère une solution.

Comme une liste de tous les raccourcis serait trop longue, voici [la liste officielle](http://download.microsoft.com/download/2/9/6/296AAFA4-669A-46FE-9509-93753F7B0F46/VS-KB-Brochure-CPP-A4.pdf) (en anglais). 

Essayons de mettre en pratiques quelques-uns de ces raccourcis en compilant un code minimal. Je vous fournis un code source que nous examinerons dans le chapitre suivant. 

```c
#include <stdio.h>

int main(void)
{
    printf("Hello world!\n");
    return 0;
}
```

Pour le compiler, on doit faire **F7** puis **Ctrl + F5**. Cependant, pour allez plus vite, on peut faire directement **Ctrl + F5**. Si vous utilisez cette combinaison de touches, il se peut que vous tombiez sur une fenêtre semblable à celle-ci :


![Fenêtre d'erreur de recompilation](../../../progdupeupl//galleries/63/fc70851c-2cc9-40f5-afa7-64d477eed97a.png)


Cela signifie qu'il y a eu des modifications dans le code et que la solution n'a pas été régénérée (on a pas recompilé). Dans ce cas, cliquez sur « *Oui* » pour régénérer la solution, ou cliquez sur « *Non* » pour lancer la dernière solution générée (le dernier exécutable compilé).

### Avec l’invite de commande ###

Même si la programmation à l’aide d’un IDE peut être pratique, certains préfèrent néanmoins programmer *à la main*, c’est-à-dire s’occuper eux-mêmes de la compilation. Pour cela, ils utilisent l’invite de commande. Si jamais cette méthode vous tente et que vous avez les compétences nécessaires pour vous servir de l’invite, lisez cette partie.

#### Le compilateur ####

Le plus important dans tout ça est le compilateur. Je vous propose donc de télécharger MinGW, qui est une adaptation pour Windows du compilateur GCC, je vous le rappelle. 

Rendez-vous sur le [site de MinGW](http://www.mingw.org/), puis dans le cadre de gauche dans la section « *[Download](http://sourceforge.net/projects/mingw/files/)* ». Pour se faciliter le travail, on va télécharger l’installateur. Pour cela, cliquez sur le lien en haut de la page « *Looking for the latest version ? Download mingw-get-inst-xxxxxxxx.exe (xxx.x kB)* ».

Exécutez le programme. Arrivés à la partie « *Repository Catalogues* », choisissez « *Use pre-packaged repository catalogues* » si vous voulez utiliser les outils fournis avec l’installateur, ou bien « *Download latest repository catalogues* » si vous voulez que l’installateur télécharge les tout derniers fichiers.

Ceci fait, acceptez la licence (lisez-la si vous en avez le courage), puis sélectionnez le dossier où vous souhaitez que MinGW soit installé. Ensuite, il faut choisir les composants que l’on veut installer. Normalement, seuls « *MinGW Compiler Suite* » et « *C Compiler* » sont cochés. Les autres cases ne nous intéressent pas puisque elles servent à installer des compilateurs pour d'autres langages. Laissez ensuite le programme finir son travail.

Maintenant il reste une dernière étape : configurer la variable d'environnement (PATH). Cette étape va permettre à l'Invite de Commande de comprendre les commandes de compilation de MinGW, sans quoi il serait impossible de compiler un programme.

* Sous Windows XP et antérieur, il faut faire un clic-droit sur « *Poste de travail* » puis choisir « *Propriétés* ». Dans la fenêtre qui s'ouvre, cliquez sur « *Avancés* » puis sur « *Variables d'environnement* ».
* Sous Windows Vista et Seven, il faut faire un clic-droit sur l'icône « *Ordinateur* » dans le menu Démarrer ou bien sur « *Poste de travail* ». Ensuite, cliquez sur « *Paramètres systèmes avancés* ». Dans la nouvelle fenêtre qui s'ouvre, allez dans « *Paramètres systèmes avancés* » et cliquez sur « *Variable d'environnement* ».

Dans la partie *Utilisateur courant*, créez une nouvelle variable et rentrez `%PATH%;C:\MinGW\bin` (le chemin après le point-virgule peut varier en fonction de où vous avez décidés d'installer MinGW, l'important est de bien avoir le répertoire `bin` à la fin).

#### L’éditeur de texte ####

L’éditeur de texte va nous permettre d’écrire notre code source et de l’enregistrer pour que le compilateur fasse son travail. L’idéal est d’avoir un éditeur de texte facile à utiliser et qui colore le code source, ce qui permet une meilleure relecture. Si jamais vous avez déjà un éditeur de texte et que vous l'appréciez, ne changez pas, il marchera très bien lui aussi.

Si cependant vous ne savez pas lequel prendre, je vais vous aider. Personnellement, j’utilise [Notepad++](http://notepad-plus-plus.org/fr/), qui est simple, pratique et efficace. Pour le télécharger, rendez-vous sur la [page de téléchargement](http://notepad-plus-plus.org/fr/download/v5.9.6.2.html), et sélectionnez « *Notepad++ vX.X.X.X Installer* » pour télécharger l’installateur. Pour l'installation je vous laisse faire, elle est facile.

#### Compiler à la main avec l’invite de commande ####

Testons tout ce que l’on vient d’installer en compilant un petit code simple que nous expliquerons dans le chapitre suivant.

```c
#include <stdio.h>

int main(void)
{
    printf("Hello world!\n");
    return 0;
}
```

Copiez-collez ce code dans l’éditeur de texte, puis enregistrez le fichier sous le nom `main.c`. Ensuite, déplacez-vous dans les répertoires à l’aide de l’invite pour arriver dans le répertoire qui contient le fichier source.

```console
C:\Programmation>dir

Répertoire de C:\Programmation

07/12/2011  13:54    <REP>          .
07/12/2011  13:54    <REP>          ..
07/12/2011  13:54             130   main.c

1 fichier(s)              130 octets
2 Rép(s)  172 089 290 752 octets libres
```

Nous allons compiler ce fichier à l’aide d’une commande : `gcc main.c`. Cette commande va transformer le fichier spécifié en exécutable. Si vous regardez le répertoire de nouveau, vous remarquerez d’ailleurs qu'un fichier `.exe` est apparu. C’est le résultat de la compilation. Si vous le lancez, vous verrez le résultat à l'écran :

```console
C:\Programmation>gcc main.c

C:\Programmation>main.exe
Hello world
```

Si vous obtenez une erreur du type *« 'gcc' n'est pas reconnu en tant que commande interne ou externe, un programme exécutable ou un fichiers de commandes »* c'est que vous vous êtes trompés quelque part.

Nous apprendrons dans le chapitre suivant pourquoi le programme affiche un message à l’écran.

Il existe de nombreuses options de compilation pour MinGW que tout un cours entier ne pourrait pas aborder. Si vous souhaitez découvrir ces options, vous pouvez jeter un œil à la [documentation officielle](http://linux.die.net/man/1/gcc). Même si cette page traite de GCC, la très grande majorité des options marchent pour MinGW.

*[MinGW]: Minimalist GNU for Windows
*[GCC]: GNU Compiler Collection

### GNU/Linux - UNIX
Le C étant très lié à UNIX, il existe de nombreux outils disponibles pour ces deux systèmes d’exploitation. Je vais vous en présenter quelques-uns. Afin d’éviter certains problèmes, je vous conseille fortement d’installer le paquet ''build-essential'' avant toute chose sous Debian et ses dérivés (Ubuntu, Kubuntu, etc. en font partis) : ```# aptitude install build-essential```

### Les IDE ###

Sous GNU/Linux et UNIX, il y a évidemment de nombreux IDE disponibles. Si vous souhaitez utiliser un IDE, je vous conseille Code::Blocks. Vérifiez dans vos dépôts s’il est disponible, et si jamais il ne l’est pas, rendez-vous sur [la page de téléchargement du site officiel de Code::Blocks](http://www.codeblocks.org/downloads/26). Une fois que vous l’avez installé, regardez plus haut dans ce tutoriel pour vous familiariser avec lui.

Même si les IDE sont pratiques, beaucoup de programmeurs préfèrent compiler à la main sous ces plateformes. Je vous recommande donc de lire également la partie suivante, même si vous ne pensez pas compiler à la main.

### La compilation en ligne de commande ###

La compilation à la main est prônée par de nombreux programmeurs experts. On dit souvent que ça présente de nombreux avantages. Cependant, pour le programmeur débutant, c’est légèrement différent. En effet, la compilation manuelle présente des avantages et des défauts :

* rapide une fois prise en main et légère ;
* permet d’apprendre plus de choses, voire même d’apprendre plus rapidement certains concepts ;
* on doit cependant tout faire soi-même ;
* parait compliqué et hostile ;
* il faut savoir manipuler le terminal.

Le troisième argument est en orange puisque le fait de tout faire soi-même est très intéressant et est donc un avantage conséquent. Cependant, pour certains cette technique est assez *difficile*. Faire tout soi-même permet au programmeur d’avoir le contrôle absolu sur ce qu’il fait, contrairement à certains IDE qui dissimulent certaines fonctionnalités intéressantes par exemple.

Avant de vous montrer l’utilisation de GCC, le compilateur que nous allons utiliser, il faut d’abord avoir un code source sous la main. Pour créer un code source sans IDE, il faut utiliser un éditeur de texte **et non pas un traitement de texte** ! Un éditeur de texte est un programme qui permet de modifier des fichiers quelconques (tout est fichier, en tout cas sous les GNU/Linux et UNIX, donc avec un éditeur de texte, vous pouvez tout modifier ; cependant, on préfère un éditeur de texte pour programmer, en effet aucune personne saine d’esprit n’irait créer un fichier *.png à la main).

Un traitement de texte comme *LibreOffice Writer* permet non seulement de modifier des fichiers textes, mais offre la possibilité de les mettre en forme, c’est-à-dire mettre en gras du texte, changer la police, ajouter des images, etc.

Il existe des éditeurs de textes graphiques et des éditeurs de textes en console. Voici quelques-uns des plus célèbres et des plus utiles pour un programmeur :

* [Vim](http://www.vim.org/), tutoriel en français : commande ```vimtutor``` ;
  * [Emacs](http://www.gnu.org/s/emacs/), tutoriel en français disponible [ici](http://www.tuteurs.ens.fr/unix/editeurs/emacs.html ) ;
* [jEdit](http://www.jedit.org/), tutoriel en français disponible [ici](http://tousleschats.free.fr/hermes/tuto/index.html) ;
* [Kate](http://kate-editor.org/ ), tutoriel en français disponible [ici](http://www.linuxpedia.fr/doku.php/kate).

jEdit est un très bon éditeur de texte graphique spécialement adapté à la programmation. Vim et Emacs sont des éditeurs de texte extrêmement puissants en pratique, mais assez compliqués, surtout pour un débutant ; ne les laissez pas de côté pour autant, ils ne peuvent que vous être utiles.

Maintenant, créez un fichier **test.c** (que vous pouvez mettre dans un dossier nommé « *prog* » dans votre dossier *home* par exemple) contenant le code suivant :

```c
#include <stdio.h>

int main(void)
{
    printf("Hello world!\n");
    return 0;
}
```

Afin de créer l’exécutable à partir du code source précédent, on fait comme ceci :

```console
gcc test.c
```

Ou bien encore :

```console
gcc *.c   # Le joker * permet de raccourcir la commande.
```

Un exécutable s'est créee : **a.out**, que l'on lance ainsi : 

```console
./a.out
```

Pour modifier le nom de l'exécutable, on utilise l’option **-o** comme ceci : 

```console
gcc test.c -o mon_executable
```

Comme on peut s'en douter, il existe énormément d’options de compilation différentes, si bien qu'on ne peux pas toutes les lister ici. Cependant, [ce tutoriel](http://www.siteduzero.com/tutoriel-3-31992-compilez-sous-gnu-linux.html) ainsi que vers [la documentation officielle](http://www.linux-kheops.com/doc/man/manfr/man-html-0.9/man1/gcc.1.html) sont là pour ça. Bien que ces pages contiennent des éléments avancés du C, elles peuvent servir à n'importe quel moment, d'où l'intérêt de les garder.

Il existe bien entendu d'autres compilateurs comme Comeau C/C++, une liste exhaustive étant impossible à faire.

*[GCC]: GNU Compiler Collection

### Mac OS
### Avec un IDE ###

Plusieurs IDE existent sous Mac OS, par exemple Code::Blocks. Cependant, ce dernier étant assez bogué sur Mac, je vous déconseille fortement de l’utiliser. Nous allons utiliser l’IDE fourni par Apple qui se trouve être le plus complet et le plus puissant : **Xcode**. Il est gratuit, cependant il est en anglais (au même titre que Code::Blocks). Si vous êtes anglophobe, ne vous inquiétez pas, vous pouvez très bien vous en sortir à l'aide de volonté et d'un dictionnaire.

Premièrement, il va falloir télécharger Xcode. Si vous êtes sous Mac OS X Lion, vous n’avez qu’à aller sur le *Mac AppStore* (menu « *Pomme > App Store ...* ») et télécharger Xcode. Si vous êtes sous une version antérieure, il faudra vous rendre sur le site de développeur d’Apple : [Apple Developer Connection](https://developer.apple.com/). Il faudra ensuite vous rendre sur le *Mac Dev Center* puis dans « *Additional download* », vous cliquerez sur « *View all downloads* ». Quand vous aurez la liste, il suffit de chercher la version 3 de Xcode (pour Leopard et Snow Leopard) ou 2 pour les versions encore antérieures (Tiger). Vous pouvez aussi utiliser votre CD d’installation pour installer Xcode (sauf pour Lion). Seule la version 4 de Xcode sera présentée ici.

Une fois le téléchargement terminé, vous aurez un fichier nommé « *Install Xcode.app* », lancez l’application et cliquez sur « *Install* » puis acceptez les conditions d’utilisation. Votre mot de passe administrateur va vous être demandé. L’installation dure un certain temps, allez prendre un café en attendant.


![Installation de xCode](../../../progdupeupl//galleries/63/fc1721f1-caaf-4e7f-8c14-f16357b55dfd.png)


Maintenant que Xcode est installé, vous pouvez supprimer le fichier « *Install Xcode.app* », ça vous libèrera quelques Go d’espace disque. Lancez Xcode maintenant. S’il n’est pas présent dans le dock ou si vous l’en avez supprimé par erreur, vous pourrez toujours retrouver l’application dans le menu */Developer/Applications*.


![Menu principal de xCode](../../../progdupeupl//galleries/63/3d9a98d2-709f-4eed-a5d7-945d9853aab5.png)


Je pense que c’est assez explicite, pas besoin de trop m’attarder là-dessus. Cliquez sur « *Create a new Xcode project* », puis sélectionnez « *Command Line Tool* » dans la partie « *Application* » de « *Mac OS X* » sur la partie gauche puis cliquez sur « *Next* ».


![Première page lors de la création d'un projet avec xCode](../../../progdupeupl//galleries/63/89adcfd5-99fb-484c-9a38-85f4e4711899.png)


Dans le champ « *Product Name* », entrez simplement le nom de votre projet. Dans le champ « *Company Identifier* », vous pouvez mettre votre pseudo par exemple (à moins que vous apparteniez à une entreprise, dans ce cas-là, il faudrait mettre le nom de votre entreprise). Choisissez bien « *C* » dans le champ « *Type* », puis cliquez sur « *Next* ».


![Deuxième page lors de la création d'un projet avec xCode](../../../progdupeupl//galleries/63/84072490-2d26-403c-a391-0e9a6a6b4965.png)


Dans la fenêtre suivante, vous devrez sélectionner le chemin vers lequel vous allez mettre votre projet. Xcode crée un dossier pour votre projet du nom que vous avez entré. Votre projet s’ouvre automatiquement. Vous devriez avoir une fenêtre qui ressemble à ça :


![Page principale après la création d'un projet](../../../progdupeupl//galleries/63/c9ea30bb-a28b-4e17-8da9-b80a46a95712.png)


Une petite présentation s’impose. Je vous ai entouré les 4 parties principales qui consistent l’interface, ainsi que 2 autres en haut de la fenêtre.

La partie en haut à droite, nommée « *View* », sert à afficher ou masquer les parties numérotées (les numéros ont été rajoutés pour bien se repérer). Vous pouvez masquer la partie 4, elle ne nous servira à rien. Il arrivera que la partie 3 ne s’affiche pas, quand vous lancez un programme qui n’affiche rien par exemple, il vous suffira de cliquer sur le bouton numéroté 3 (toujours dans la partie *View*). La partie 1 reste toujours visible en règle générale.

La partie en haut à gauche contient 4 boutons. Le bouton « *Run* » (raccourci : **Cmd + R**) est celui que vous utiliserez le plus souvent, il permet de compiler puis de lancer votre programme. Le bouton « ''Stop'' » permet d’arrêter votre programme à tout moment. Le bouton « *Scheme* » ne nous intéresse pas (il permet de changer quelques options de compilation, de changer de *target*, etc.). Le bouton « *Breakpoints* » sert à activer/désactiver les points d’arrêt. C’est utile si vous utilisez le débogueur.

Dans la partie 1, vous avez 7 onglets tout en haut. Le premier onglet sert à voir l’arborescence de votre projet (fichiers, ressources, etc.). Le 4ème onglet (en forme de point d'exclamation) sert à voir les erreurs et warnings que vous pourrez avoir pendant votre codage. Les autres onglets ne nous intéressent pas. Vous pouvez changer d’onglet en utilisant les raccourcis **Cmd + 1** à **7** en fonction de l’onglet que vous voulez choisir.

La partie 2 est votre éditeur de texte (il affiche aussi les images, etc., je ne vais pas entrer dans les détails). C’est ici que vous allez placer votre code. Si vous avez plusieurs fichiers, sélectionnez le fichier dans la partie 1 et éditez-le dans la partie 2. Vous pouvez ouvrir des onglets (comme sur les navigateurs Internet) en utilisant le raccourci **Cmd + T**. Ce qu’il faut savoir, c’est que pendant que vous tapez votre texte, vous aurez des propositions qui vous seront faites pendant que vous tapez le mot. C'est ce qu’on appelle l’*autocomplétion*. Ça permet d’éviter de taper tout le mot. Pour valider, il suffit d’appuyer sur **Enter** ou **Tab**. Si vous voulez « forcer » l’apparition de l’autocomplétion, vous pouvez appuyer sur la touche **Echap**. Xcode vous montre vos erreurs en *temps réel*, ce qui vous permet de vous rendre compte de vos erreurs de syntaxe tout de suite.

La partie 3 contient la pseudo-console (partie noire de droite) et la zone de débogage (à gauche et la ligne du haut avec les flèches). Ce qui nous intéresse est la partie de droite, c’est là que vous allez exécuter vos programmes ! Pour enlever la partie de débogage, il suffit de cliquer sur le bouton juste à droite du bouton « *Clear* ». Vous pouvez aussi enlever les messages du débogueur (je vous le déconseille) en cliquant sur « *All Output* » et en sélectionnant « *Target Output* ».

La partie 4 ne nous intéresse pas, vous pouvez la masquer comme indiqué plus haut.

Tentons maintenant de compiler notre premier code que voici : 

```c
#include <stdio.h>

int main(void)
{
    printf("Hello world!\n");
    return 0;
}
```

Essayez de compiler ce code. Vous devriez voir s'afficher à l'écran quelque chose comme ceci :

```console
GNU gdb 6.3.50-20050815 (Apple version gdb-1708) (Mon Aug 15 16:03:10 UTC 2011)
Copyright 2004 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "x86_64-apple-darwin". tty /dev/ttys000
sharedlibrary apply-load-rules all [Switching to process 679 thread 0x0]

Hello world! Program ended with exit code: 0
```

Toutes ces lignes ont été ajoutées par le compilateur automatiquement et ne nous intéressent pas vraiment. La dernière ligne affiche cependant le message **Hello world!** ainsi que le résultat de l'exécution.

### En ligne de commande ###

Ça peut vous paraître étrange, mais le plus simple pour installer les outils pour la ligne de commande est d’installer Xcode. Je vous invite donc à installer Xcode comme présenté ci-dessus (et éventuellement les Xcode Tools si vous utilisez une version plus ancienne).

Une fois Xcode installé, allez dans le dossier « */Applications/Utilitaires* » et lancez l’application « *Terminal.app* ». Pour l’éditeur de texte, vous pouvez choisir celui que vous voulez (emacs, vim, nano, etc.). Pour compiler, vous avez le choix : gcc, clang, llvm-gcc. Pour l’utilisation de tout ça, reportez-vous à la partie *GNU/Linux* juste au-dessus.

Ce chapitre vous a fait découvrir quelques-uns des outils utilisés lorsque l’on programme en C, mais il en existe beaucoup d’autres que vous aurez peut-être l’occasion de découvrir un jour. Néanmoins, le choix importe peu puisque le résultat est le même : un fichier en langage machine compréhensible par le processeur (c’est là qu’on dit merci à la norme, parce que sans elle, le comportement varierait en fonction du logiciel utilisé). Quelle que soit votre méthode, je vous encourage à la découvrir en trifouillant un peu. 

Le chapitre suivant va nous faire découvrir le C, et vous pourrez commencer à pratiquer en compilant et en décortiquant un code écrit en langage C.

## Rencontre avec le C
Maintenant que vous êtes parés, il est temps de découvrir le langage C à travers du code. Dans ce chapitre, nous allons nous familiariser avec la programmation en découvrant non seulement des éléments spécifiques au C, mais également des éléments communs à tous les langages de programmation. Lisez attentivement ce chapitre, il vous présentera de nombreux éléments nouveaux et du vocabulaire qui vous est peut-être inconnu.

### Notre cible
Avant de commencer à programmer, il faut aussi définir ce que l’on va programmer, le type de programme que l’on va réaliser. Il existe en effet deux types de programmes : les programmes **graphiques** et les programmes **en console**.

Les programmes graphiques sont les plus courants et les plus connus puisqu’il n’y a pratiquement qu’eux sous Windows ou Mac OS X par exemple. Vous en connaissez énormément, peut-être sans le savoir : le lecteur de musique, le navigateur Internet, le logiciel de discussion instantanée, la suite bureautique, les jeux vidéos, ce sont tous des programmes graphiques, ou programmes GUI. En voici un exemple sous GNU/Linux :

![L'éditeur graphique GIMP est un programme graphique](http://uploads.siteduzero.com/files/392001_393000/392437.png)

Cependant, écrire ce genre de programmes demande beaucoup de connaissances, il faut savoir manier des bibliothèques, connaitre plusieurs notions; bref, savoir programmer. C’est trop compliqué pour nous. Il faut donc se rabattre sur le deuxième type de programme : les programmes en console.

Les programmes console sont les premiers programmes, apparus en même temps que l’écran. Ils étaient très utilisés dans les années 1970 / 1980 (certains d’entre vous se souviennent peut-être de MS-DOS), mais ont fini par être remplacés par une interface graphique avec la sortie de Windows et de Mac OS. Cependant, ils existent toujours, et redeviennent quelque peu populaires avec GNU/Linux.

Voici un exemple de programme en console :

```console
12 - 7 =   5
Right!
9 - 5 =   4
Right!
1 + 5 =   6
Right!
3 + 3 =   6
Right!
5 + 4 =   9
Right!
10 + 9 =   19
Right!
16 - 10 =   6
Right!
9 - 1 =   8
Right!
18 - 10 =   8
Right!
3 + 3 =   6
Right!


Rights 10; Wrongs 0; Score 100%
Total time 16 seconds; 1.6 seconds per problem

Press RETURN to continue...
```

Ce sera le type de programme que nous allons apprendre à créer. Rassurez-vous, quand vous aurez fini le tutoriel, vous aurez les bases pour apprendre à utiliser d’autres bibliothèques, vous pourrez ainsi créer des programmes graphiques. Tout est possible.

*[GUI]: Graphical User Interface

### Analyse du code source
Dans le chapitre précédant, nous avons installé les outils nécessaires à la compilation et nous avons compilé notre premier code source. Il est temps de découvrir plus en détail ce code et de comprendre ce qu'il signifie. 

Je remets ce code ici pour que tout le monde aie le même :

```c
#include <stdio.h>

int main(void)
{
}
```

Copiez-collez ce code pour que vous et moi ayons le même, puis sauvegardez. Même si c’est un minuscule projet, c’est une bonne habitude à prendre qui peut parfois vous épargner des problèmes de fichiers perdus. 

### #include ###

Cette ligne se situe tout en haut du programme.

```c
#include <stdio.h>
```

C'est une **directive de préprocesseur**, facilement reconnaissable car elles commencent toutes par un ```#```. Dans notre cas, elle sert à charger des fichiers qui contiennent du code tout prêt pour réaliser de nombreuses actions (comme afficher un message, récupérer des informations, quitter le programme, lire un fichier, etc). En effet, sans ces fichiers, appelés **fichiers d’en-tête** (en anglais, on parle de *headers*), le C ne sait quasiment rien faire. On dit que c'est un *langage modulaire*. 

L’ensemble de ces fichiers d'en-tête est appelé **bibliothèque** (de l'anglais « *library* »). Le mot « librairie » est plus court, mais il n'est pas correct car il s'agit d'un anglicisme.

Dans notre cas, nous ne chargeons qu'un seul fichier d'en-tête : ```stdio.h```, qui signifie « **St**andar**d i**nput **o**utput », soit « Entrée-sortie standard ». Ce fichier d'en-tête va nous permettre de communiquer avec l'utilisateur en affichant des messages à l'écran et en récupérant des informations.

### int main(void) ###

C’est le cœur du programme :

```c
int main(void)
{
    
}
```

Ce bout de code est appelé **fonction**. Un programme écrit en C n’est composé pratiquement que de fonctions : c’est un bout de code qui sert à donner des instructions à l’ordinateur. Ainsi, on peut créer une fonction *calculer_racine_carree* qui calculera la racine carrée d’un nombre. Vous verrez plus tard dans votre apprentissage qu’un programme C est constitué d’un tas d’autres choses, mais surtout de fonctions.

Notre fonction s’appelle *main* (prononcez « mèïne »). C’est la fonction de base commune à tous les programmes en C, le point d’entrée du programme, son cœur. Le programme commence et finit toujours par elle. Bien sûr, nous n’écrirons pas tout le code dedans, ce serait impossible à entretenir et causeraient trop de problèmes pour de gros projets. Au contraire, elle déléguera le travail, mais on la retrouvera toujours.

Une fonction est délimitée par des accolades (**{** et **}**). Après les accolades il n’y a rien, car pour l’instant nous n’avons que la fonction *main*. À noter que la dernière accolade est suivie d’une ligne vide. Elle ne sert à rien, mais il faut la mettre quand même.

À l’intérieur des parenthèses, il y a le mot « ```void``` ». Ce mot-clé signifie « Je ne veux pas de paramètres ». Il est en effet possible de donner des paramètres à la fonction *main*, mais ce n'est pas de notre niveau.

### Notions de base
Pour l’instant, nous n’avons présenté que le code C minimal. Néanmoins, il existe des notions très importantes et communes à tous les langages de programmation, et nous allons vous les présenter, en les appliquant au C bien entendu. Soyez donc concentré, cette partie est basique, mais importante pour la suite.

### Les mots-clés ###

Les **mots-clés** sont des mots spéciaux, réservés par le compilateur, que l’on ne peut pas utiliser comme on veut. Ils servent à déclarer des variables, concept que l’on découvrira dans le chapitre suivant, à préciser des attributs, et réaliser d’autres actions encore. Le C a réservé 32 mots-clés, que voici :

```c
auto     double   int      struct
break    else     long     switch
case     enum     register typedef
char     extern   return   union
const    float    short    unsigned
continue for      signed   void
default  goto     sizeof   volatile
do       if       static   while
```
> *Norme C89 — A.1.1.2 Keywords*

Nous les verrons tous au fur et à mesure de la progression de ce cours. Certains vous seront plus utiles que d’autres, mais tous ont un rôle.

D’ailleurs, ces mots-clés sont colorés par votre IDE. Cela permet au programmeur de mieux voir, et disons-le, c’est toujours plus joli que du code entièrement en noir. 

### Les opérateurs ###

Les **opérateurs** sont des symboles à la base des expressions (nous verrons plus bas de quoi il s’agit). Ils permettent de faire des opérations comme l’addition, la multiplication, la comparaison de deux valeurs, l’opposé d’une valeur, etc. De même qu’en mathématiques, tous n’ont pas la même priorité : certains passent avant d’autres. 

Les opérateurs en C sont les s