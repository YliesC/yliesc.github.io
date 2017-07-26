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

*Pour les curieux, il existe [un cours sur le fonctionnement d’un ordinateur](http://www.siteduzero.com/tutoriel-3-509203-fonctionnement-d-un-ordinateur-depuis-zero.html) expliqué depuis zéro.*

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

Les opérateurs en C sont les suivants :

```c
[  ]  (  )  .  ->
++  --  &  *  +  -  ~  !  sizeof
/  %  <<  >>  <  >  <=  >=  ==  !=  ^  |  &&  ||
?  :
=  *=  /=  %=  +=  -=  <<=  >>=  &=  ^=  |=
, 
```
> *Norme C89 — A.1.1.6 Operators*
> *Vous noterez que ```sizeof``` est à la fois un mot-clé et un opérateur.*

Les opérateurs peuvent être classés en C en sept catégories :

* les opérateurs arithmétiques ;
  * les opérateurs d’affectation ;
  * les opérateurs logiques ;
  * les opérateurs de comparaison ;
  * l’opérateur conditionnel ;
* les opérateurs bit-à-bit ;
* et quelques opérateurs inclassables.

Nous examinerons toutes ces catégories au fur et à mesure que nous progresserons dans le tutoriel. Comme pour les mots-clés, vous en utiliserez certaines plus que d’autres, mais toutes ont leur utilité.

### Expressions et instructions ###

La différence entre les deux notions est un peu subtile et conduit parfois à des confusions. Une **expression** est évaluée et produit un résultat. Les lignes de code suivantes sont toutes des expressions.

```c
"Hello world!"
2 + 3
10 > 2
```

Généralement, une expression ne peut être écrite seule, sans contexte autour. Cela correspondrait en français à énoncer un sujet sans le verbe qui va derrière.

Une instruction, quant à elle, est un ordre qui permet d’exécuter telle ou telle action. Pour vous aider, chaque instruction peut se traduire par une phrase verbale en français.

```c
printf("Hello world!");   /* Affiche « Hello world! ». */
x = 2;    /* Affecte la valeur 2 à x. */
```

Toutes les instructions se terminent par un point-virgule (nous apprendrons au fur et à mesure les quelques-unes qui n’en requièrent pas). 

La frontière entre instruction et expression est assez floue puisqu’une instruction peut être constituée de nombreuses expressions. Le code ci-dessous est un exemple d’une instruction qui est aussi une expression.

```c
x = 2 + 3;
```

On donne en effet un ordre à l’ordinateur (« Affecte la valeur 2 + 3 à x »), mais c’est aussi une expression qui produit la valeur 5 comme résultat. Vous verrez qu’en C, la majorité des lignes de code sont des instructions-expressions. C’est ce qui s’appelle la **programmation impérative**. C’est le choix des concepteurs du langage, mais ce n’est pas la seule possibilité (il en existe d’autres, mais ça ne nous concerne pas en tant qu’utilisateurs du C).

### Les blocs d’instructions ###

Un **bloc d’instructions** est formé d’une suite d’instructions délimitée par des accolades, et tout ce qu’il y a entre les accolades est par conséquent à l’intérieur d’un bloc d’instructions. La fonction ```main``` est par exemple suivie d’un bloc d’instructions composé de deux instructions.

### Les séparateurs ###

Lorsque l’on écrit, on met des espaces entre les mots pour rendre le tout plus clair. Pour la programmation, c’est pareil. On insère des espaces et des retours à la ligne dans un code source pour le rendre plus clair et plus lisible. Par exemple, les deux codes ci-dessous sont identiques pour le compilateur, mais le second est plus lisible pour le programmeur que le premier.

```c
int x=0,y,rep;

int x = 0, y, rep;
```

Ce dernier point m’amène donc à l’indentation.

### L’indentation ###

L’**indentation** est vraiment quelque chose de très important. Elle consiste en l’ajout de tabulations ou d’espaces dans un code source. Un code bien indenté est un code clair et agréable à lire. Le style d’indentation définit comment les programmeurs se débrouillent afin de faire ressortir du code.

Parce qu’un code vaut 1000 mots :

```c
#include<stdio.h>
int main(void)
{ printf("Hey !\n");
  printf("Bien ?");
  return 0;}
```

En comparaison avec :

```c
#include <stdio.h>

int main(void)
{
    printf("Hey !\n");
    printf("Bien ?");

    return 0;
}
```

Il existe de [nombreux styles d'intendation](http://en.wikipedia.org/wiki/Indent_style) différents. C'est à vous de choisir celui que vous préférez, et surtout de vous y tenir. Ce cours utilisera quant à lui le style Allman (ou style ANSI).

Il faut aussi que vous sachiez qu’il existe une *règle* concernant le nombre de colonnes (de caractères entre autres) à ne pas dépasser par ligne. C’est une très ancienne règle, qui limite le nombre de caractères par ligne à 80. Vous n’êtes pas obligé de la suivre, loin de là. Mais sachez que certains l’affectionnent encore, et ne soyez pas surpris si certains codes suivent cette règle. Dans ce tutoriel, ce ne sera pas le cas.

### Les commentaires ###

Il est souvent nécessaire de **commenter son code source** pour décrire des passages un peu moins lisibles ou tout simplement pour offrir quelques compléments d’information au lecteur du code. Un commentaire est ignoré par le compilateur : il disparait et n’est pas présent dans l’exécutable. Il ne sert qu’au programmeur et aux lecteurs du code.

Un commentaire en C est écrit entre les signes ```/*``` et ```*/``` :

```c
/* Ceci est un commentaire */
```

Il peut très bien prendre plusieurs lignes :

```c
/* Ceci est un commentaire qui
   prend plusieurs lignes. */
```

Le plus dur quand on utilise les commentaires, c’est de trouver un juste milieu : trop de commentaires tue le commentaire, et bien souvent la grande majorité des commentaires sont inutiles. À l’inverse, pas assez de commentaires peuvent rendre la relecture du code plus difficile, surtout pour du code compliqué. 

Pour trouver ce juste milieu, il faut savoir plusieurs choses. Premièrement, pas besoin de commenter chaque ligne : si certaines instructions sont évidentes, les commenter sera superflu. Deuxièmement, essayer de faire des blocs de commentaires donnant une explication générale plutôt que de commenter chaque ligne une à une. Les commentaires doivent servir à décrire quelque chose de flou, ne vous sentez donc pas poussés à en mettre partout.

L’idée de base est que **les commentaires doivent aider le lecteur et éviter de redire ce que le code dit**.

Voilà à quoi ressemblerait notre code (excessivement) commenté : 

```c
/* Directive de préprocesseur qui permet de charger des fonctions utiles */
#include <stdio.h>

/* La fonction principale */
int main(void)
{
    /* Et des instructions */
    printf("Hello world!\n");
    return 0;
}

/* Fin du code, le programme s’achève ici */
```

Bien sûr, en pratique, ces commentaires sont inutiles.

En outre, vous pouvez rencontrer un autre style de commentaires, dit "commentaire de style C++" , qui provient du langage C++. Ce type de commentaire, noté `//` n'est autorisé en C que depuis le C99, je vous conseille donc de ne pas les utiliser en C et de les remplacer par les bon vieux `/*...*/`. Ces commentaires C++ commentent tout ce qui est situé entre eux et la fin de la ligne. Je les mentionne uniquement parce que vous risquez d'en voir parfois dans les codes des autres programmeurs.

Voilà, vous avez enfin fait la connaissance du C à travers du code. Certes, nous n’avons vu qu’un petit code et avons seulement survolé les différents éléments, mais il n’empêche que cela représente certainement beaucoup de nouveautés pour vous. Relisez donc à tête reposée si nécessaire.

## Les variables
Programmer, c’est avant tout donner des ordres à notre ordinateur. Ces ordres vont permettre à notre ordinateur de faire ce qu’on veut. Notre ordinateur peut manipuler un peu de tout : du texte, de la vidéo, des nombres, etc. Les ordres qu’on va donner à notre ordinateur vont ainsi lui permettre de manipuler de l’information sous différentes formes, plus ou moins variées. À ce stade du tutoriel, on sait que ces ordres, ces instructions sont effectués par notre processeur. Mais on ne sait rien sur la façon dont notre ordinateur fait pour maintenir ces informations, ni sur comment les utiliser dans notre langage C. De même, on ne sait pas comment donner des ordres à notre ordinateur, pour qu’il fasse ce qu’on lui demande. 

Ce chapitre va pallier ce problème : il vous expliquera comment manipuler les types de données les plus simples disponibles en langage C. Ceux-ci ne sont autre que des nombres et des lettres. Ils sont manipulables grâce à ce qu’on appelle des **variables**, qui sont l’objet de ce chapitre. Après ce chapitre, vous saurez notamment comment manipuler des nombres et des lettres en langage C. Vous pourrez ainsi profiter de votre ordinateur comme s’il s’agissait d'une grosse calculette, bien plus rapide et puissante. Néanmoins, rassurez-vous ; le niveau en maths de ce chapitre sera très très faible : si vous savez compter, vous pourrez comprendre le chapitre facilement ! 

Cela peut paraitre simple, et pas très intéressant. Mais il faut bien commencer par les bases, comme la manipulation de données simples : manipuler du texte ou de la vidéo est complexe, et nécessite en plus de savoir comment manipuler des nombres. Eh oui ! Comme vous allez le voir, tout est nombre pour notre ordinateur, même le texte et même la vidéo. 

### Qu’est-ce qu’une variable ?
Pour comprendre ce qu’est une variable, et comment manipuler celles-ci, il faut commencer par comprendre comment notre ordinateur fait pour stocker ces informations de base. 

Notre ordinateur a été conçu pour être assez polyvalent : il peut en théorie stocker tout type d’informations. Pour ce faire, celui-ci utilise une ruse particulièrement simple : il stocke ses informations en les découpant en petites unités d’information qu’on appelle des **bits**. Ces bits sont donc des unités très simples qui ne peuvent prendre que deux valeurs : 0 ou 1. 

Pour stocker des informations plus complexes, il suffit de prendre plusieurs de ces bits et de les regrouper les uns à côté des autres. En faisant ainsi, on peut créer des suites de 0 et de 1 qui peuvent s’interpréter comme des nombres. On peut ainsi représenter des nombres positifs, des nombres négatifs, des nombres à virgule, etc. Tout ce que peut faire notre ordinateur, c’est manipuler ces suites de bits, ces nombres. En somme, notre ordinateur n’est qu’une grosse calculatrice.

Mais alors comment notre ordinateur fait pour stocker du texte, de la vidéo, etc. s’il ne sait traiter que des nombres ? Eh bien il faut savoir que les informations plus complexes, comme de la vidéo, du texte, etc. sont toutes stockées dans notre ordinateur sous la forme de nombres. En utilisant plusieurs de ces bits, on peut ainsi représenter n’importe quoi : du texte, des nombres, de la vidéo, etc. Je suppose qu’il sera difficile de me croire, mais sachez tout de même que toute information qu’on trouve dans notre ordinateur est représentée avec seulement des 0 et des 1 !

### Mémoire ###

Ces bits sont stockés dans un composant électronique particulier, présent das notre ordinateur : la **mémoire**. Son rôle : stocker tous les bits qui permettent de représenter nos informations.

Enfin, je dis « **la** mémoire », mais en fait il y en a plusieurs. Tout comme un humain possède plusieurs mémoires (mémoire à court terme, mémoire à long terme, etc.) qui lui servent à mémoriser plein d’informations, l’ordinateur se sert aussi de plusieurs mémoires pour stocker tout un tas de données de différentes tailles.

Mais pourquoi plusieurs mémoires et pas une seule ? Le fait est que si l’on souhaitait utiliser une seule grosse mémoire dans notre ordinateur, celle-ci serait donc fatalement très lente : il est impossible de créer des mémoires qui soient à la fois rapides et qui puissent contenir beaucoup de données. On ne peut donc utiliser une seule grosse mémoire capable de stocker toutes les données dont on a besoin. Ce problème s’est posé dès les débuts de l’informatique. Les inventeurs des premiers ordinateurs modernes furent rapidement confrontés à ce problème. Pour ceux qui ne me croient pas, regardez un peu cette citation des années 1940, provenant d’un rapport de recherche portant sur un des premiers ordinateurs existant au monde :

>Idéalement, nous désirerions une mémoire d’une capacité indéfiniment large telle que n’importe quelle donnée soit immédiatement accessible. Nous sommes forcés de reconnaître la possibilité de la construction d’une hiérarchie de mémoire, chacune ayant une capacité plus importante que la précédente, mais accessible moins rapidement.
> *Burks, Goldstine, et Von Neumann*

Comme on le voit, cette citation (traduite de l’anglais) montre le problème, mais évoque aussi la solution adoptée face à ce problème. Pour résoudre ce problème, il suffit de **segmenter la mémoire de l’ordinateur en plusieurs sous-mémoires, de taille et de vitesse différentes qu’on utilise suivant les besoins**. On aura donc des mémoires pouvant contenir peu de données dans lesquelles on pourra lire et écrire rapidement et des mémoires plus importantes, mais plus lentes. Cette solution a été la première solution inventée pour résoudre ce problème et est encore massivement utilisée à l’heure actuelle : on n’a pas encore fait mieux !

Nous avons dit que l’ordinateur utilisait plusieurs mémoires. Et il faut savoir que trois de ces mémoires sont importantes, et doivent être connues de tout programmeur. Je vous présente donc : 

* les registres  ;
* la RAM ;
* le disque dur

Alors évidemment, ce ne sont pas les seules : on pourrait aussi citer la mémoire cache et d’autres encore, mais cela n’a rien à faire dans un tutoriel sur le C. Et puis il y a déjà des cours à ce sujet sur le Site du Zéro, citons par exemple *[Fonctionnement d'un ordinateur depuis zéro](http://www.siteduzero.com/tutoriel-3-509203-fonctionnement-d-un-ordinateur-depuis-zero.html)*.

Les **registres** sont des mémoires intégrées dans notre processeur. Elles sont très rapides, mais ne peuvent contenir que des données très simples : on peut difficilement mettre plus qu’un nombre dedans. Leur utilité est de stocker des données temporaires afin d’y accéder plus rapidement.

La **mémoire RAM** est une mémoire un peu plus grosse, et plus lente que les registres. Elle peut contenir pas mal de données, et on l’utilise généralement pour stocker le programme qu’on vient de lancer, ainsi que les données qu’il va manipuler. 

Cette mémoire a tout de même un léger défaut : elle perd son contenu quand on coupe le courant. Autant dire qu’on doit trouver une autre mémoire pour stocker notre système d’exploitation, nos programmes, etc. : c’est le rôle du **disque dur**, une mémoire très grosse, mais très lente.

En C, la mémoire la plus utilisée est la mémoire vive. Et donc, pour bien comprendre comment programmer en C, il faudra comprendre comment interagir avec cette mémoire RAM. Plus loin dans ce cours, nous verrons également comment manipuler des fichiers sur le disque dur. Mais pour ce qui est des registres, c’est autre chose : le C cache presque totalement la gestion de ceux-ci, qui est réalisée presque entièrement par le compilateur. Impossible de les manipuler directement ! 

### La RAM ###

Hé, une minute : si je stocke une donnée dans ma mémoire, comment je fais pour la récupérer ? Eh bien dans ce cas-là, vous n’avez pas trop le choix : vous devez savoir où se trouve votre donnée dans la mémoire de l’ordinateur. Généralement, cette donnée se trouvera en mémoire RAM. On peut bien sûr copier notre donnée dans un registre, ou sur le disque dur, mais passons. Et pour retrouver notre donnée en RAM, rien de plus simple. 

#### Bytes et octets ####

Dans notre RAM, les bits sont regroupés en « paquets » contenant une quantité fixe de bits : des « **cases mémoires** », aussi appelées *bytes*.

Généralement, nos mémoires utilisent des bytes de 8 bits. Autrefois, certaines mémoires avaient des bytes de 6 ou 5 bits, parfois plus. Mais maintenant, la situation s’est un peu normalisée et la grande majorité des mémoires utilisent des bytes de 8 bits. Un groupe de 8 bits s’appelle un **octet**.  

Avec un octet, on peut stocker 256 informations différentes. Par exemple, on peut stocker 256 nombres différents. On peut stocker les lettres de l’alphabet, ainsi que les symboles alphanumériques. On peut aussi stocker tous les nombres de 0 à 255, ou de -128 à 127, tout dépend de comment on s’y prend.

Pour stocker plus d’informations (par exemple les nombres de -1024 à 1023), on peut utiliser plusieurs octets, et répartir nos informations dedans. Nos données peuvent prendre un ou plusieurs octets qui se suivent en mémoire, sans que cela pose problème : nos mémoires et nos processeurs sont conçus pour gérer ce genre de situations facilement. En effet, nos processeurs peuvent parfaitement aller lire 1, 2, 3, 4, etc. octets consécutifs d’un seul coup sans problème, et les manipuler en une seule fois.

#### Adresse mémoire ####

Chacun de ces octets se voit attribuer un nombre unique, **l’adresse**, qui va permettre de la sélectionner et de l’identifier celle-ci parmi toutes les autres. Il faut imaginer la mémoire RAM de l’ordinateur comme une immense armoire, qui contiendrait beaucoup de tiroirs (les cases mémoires) pouvant chacun contenir un octet. Chaque tiroir se voit attribuer un numéro pour le reconnaitre parmi tous les autres. On pourra ainsi dire : je veux le contenu du tiroir numéro 27 ! Pour la mémoire c’est pareil. Chaque case mémoire a un numéro : son adresse.

| Adresse | Contenu mémoire |
| ------- | --------------- |
| 0       | 11101010        |
| 1       | 01111111        |
| 2       | 00000000        |
| 3       | 01010101        |
| 4       | 10101010        |
| 5       | 00000000        |

En fait, on peut comparer une adresse à un numéro de téléphone (ou à une adresse d’appartement) : chacun de vos correspondants a un numéro de téléphone et vous savez que pour appeler telle personne, vous devez composer tel numéro. Les adresses mémoires fonctionnent exactement de la même façon !


![Exemple : on demande à notre mémoire de sélectionner la case mémoire d’adresse 1002 et on récupère son contenu (ici, 17).](http://uploads.siteduzero.com/files/379001_380000/379202.png)


### Références ###

Pour retrouver votre donnée dans la RAM, on doit donc simplement préciser son adresse. Ce principe peut se généraliser aux autres mémoires : on doit fournir ce qu’on appelle une **référence**, qui permet d’identifier la localisation de notre donnée dans la mémoire : dans quel registre elle est (l’« adresse » du registre est alors ce qu’on appelle un nom de registre), à quel endroit sur le disque dur, etc. Ainsi, toute donnée est identifiée dans notre ordinateur par une référence, qui permet d’accéder à notre donnée plus ou moins directement. Notre adresse n’est donc qu’un cas particulier de référence, cette notion étant plus générale.

Manipuler nos données se fait alors *via* des références, plus ou moins compliquées, qui peuvent permettre de calculer l’adresse de notre donnée, et déterminer si elle est dans un registre, la RAM, le disque dur, etc.

### Variables ###

Le seul problème, c’est que manipuler explicitement des références est un vrai calvaire. Si vous ne me croyez pas, essayez de programmer en assembleur, le seul langage dans lequel on doit manipuler des références explicitement. C'est une horreur. Mais rassurez-vous : on a moyen de se passer de ce genre de choses. Pour ce faire, on peut décider de camoufler ces références plus ou moins efficacement. Pour cela, on peut décider de remplacer ces références par autre chose. 

Dans nos langages de programmation, et notamment dans le langage C, on remplace des références par des variables. Cette variable correspondra à une portion de mémoire, appelée **objet**, à laquelle on donnera un nom. Ce nom permettra d’identifier notre variable, tout comme une référence permet d’identifier une portion de mémoire parmi toutes les autres. On va ainsi pouvoir nommer les données qu’on manipule, chacun de ces noms étant remplacés par le compilateur en référence vers un registre ou vers une adresse mémoire.

### Déclarer une variable
Entrons maintenant dans le vif du sujet en apprenant à déclarer nos variables. Pour bien commencer, il faut savoir qu’une variable est constituée de deux éléments obligatoires.

* Un **identificateur** : c’est en gros le « nom » de la variable. 
* Un **type**.         

Le type d’une variable permet d’indiquer ce que l’on veut stocker : un nombre entier, un nombre à virgule (on dit aussi un **flottant**), un caractère, etc. Pour préciser le type d’une variable, on doit utiliser un mot-clé, spécifique au type que l’on souhaite donner à notre variable. 

Une fois qu’on a décidé le nom de notre variable, ainsi que son type, on peut la créer (on dit aussi la déclarer) comme ceci : 

```console
type identificateur;
```

En clair, il suffit de placer un mot-clé indiquant le type de la variable, et de placer le nom qu'on lui a choisi immédiatement après. Faites bien attention au point-virgule à la fin !

### Les types ###

Comme dit précédemment, un type permet d’indiquer au compilateur quel type de données on veut stocker. Ce type va permettre de préciser :

* toutes les valeurs que peut prendre la variable ;
* et les opérations qu’on peut effectuer dessus, histoire de ne pas additionner une lettre avec un nombre à virgule.

Définir le type d’une variable permet donc de préciser son contenu potentiel et ce qu’on peut faire avec. Le langage C fournit 8 types de base : 

| Type              | Sert à stocker            |
| ----------------- | ------------------------- |
| ```char```        | un caractère ou un entier |
| ```short```       | un entier                 |
| ```int```         | un entier                 |
| ```long```        | un entier                 |
| ```float```       | un flottant               |
| ```double```      | un flottant               |
| ```long double``` | un flottant               |

Les types ```short```, ```int``` et ```long``` servent tous à stocker des nombres entiers qui peuvent prendre des valeurs positives, négatives, ou nulles. On dit qu’il s’agit de types signés. Pour ces trois types, il existe un type équivalent non signé. Un type entier non signé est un type entier qui n’accepte que des valeurs positives ou nulles : il ne peut pas stocker de valeurs négatives. Pour déclarer des variables d’un type non signé, il vous suffit de faire précéder le nom du type entier du mot-clé ```unsigned```.

Le ```char``` peut lui aussi servir à stocker des nombres. Il sert surtout au stockage de caractères, mais ces derniers étant stockés dans l'ordinateur sous forme de nombres, il est possible de stocker des nombres dans un ```char```. Le seul problème, c’est que ce ```char``` peut très bien être signé sur certains compilateurs et pas sur d’autres. Suivant le compilateur utilisé, le ```char``` sera soit signé par défaut, soit il sera non signé. Pour éviter les ennuis en utilisant un ```char``` comme un nombre, vous pouvez les déclarer explicitement non signés : ```unsigned char``` ou signés : ```signed char```.

#### Capacité d’un type ####

Tous les types stockant des nombres (tous sauf le type ```char```) ont des bornes, c’est-à-dire une limite aux nombres qu’ils peuvent stocker. Il faut dire que le nombre de *bytes* occupé par une variable d’un certain type est limité, et est généralement fixé définitivement pour toutes les variables de ce type par le compilateur. En conséquence, on ne peut pas mettre tous les nombres possibles dans une variable de type ```int```, ```float```, ou ```double```. On aura forcément une valeur minimale et une valeur maximale : certains nombres seront trop grands ou trop petits pour rentrer dans une variable d’un certain type. Ces bornes (que vous pouvez trouver au paragraphe 2.2.4.2 de la norme) sont les suivantes :

| Type                 | Minimum        | Maximum        |
| -------------------- | -------------- | -------------- |
| ```signed char```    | -127           | 127            |
| ```unsigned char```  | 0              | 255            |
| ```short```          | -32 767        | 32 767         |
| ```unsigned short``` | 0              | 65 535         |
| ```int```            | -32 767        | 32 767         |
| ```unsigned int```   | 0              | 65 535         |
| ```long```           | -2 147 483 647 | 2 147 483 647  |
| ```unsigned long```  | 0              | 4 294 967 295  |
| ```float```          | $-1 × 10^{37}$ | $+1 × 10^{37}$ |
| ```double```         | $-1 × 10^{37}$ | $+1 × 10^{37}$ |
| ```long double```    | $-1 × 10^{37}$ | $+1 × 10^{37}$ |

Si l'on regarde bien le tableau, on remarque que certains types ont des bornes identiques. En vérité, les valeurs présentées ci-dessus sont les *minima* garantis par la norme et il est fort probable qu’en réalité, vous puissiez stocker des valeurs plus élevées que celles-ci (le type ```int``` s'apparente souvent à un ```long```, par exemple). Cependant, dans une optique de portabilité, vous devez considérer ces valeurs comme les *minima* et les *maxima* de ces types, peu importe la capacité réelle de ces derniers sur votre machine.

Information : le type ```unsigned int``` équivaut à un ```unsigned```, ne soyez pas surpris si plus tard en lisant les codes d'autrui vous ne trouveriez seulement ce mot-clé.

#### Taille d’un type ####

Peut-être vous êtes vous demandés pourquoi existe t-il autant de types différents. La réponse est toute simple : la taille des mémoires était très limitée à l’époque où le langage C a été créé. En effet, le [PDP-11](http://cm.bell-labs.com/cm/cs/who/dmr/kd14.jpg) sur lequel le C a été conçu ne possédait que 24 Ko de mémoire (pour comparaison une calculatrice TI-Nspire possède 100 Mo de mémoire, soit environ 4000 fois plus). Il fallait donc l’économiser au maximum en choisissant le type le plus petit possible. Cette taille dépend des machines, mais de manière générale vous pouvez retenir les deux suites d’inégalités suivantes : ```char``` ≤ ```short``` ≤ ```int``` ≤ ```long``` et ```float``` ≤ ```double``` ≤ ```long double```.

Aujourd’hui ce n’est plus un problème, il n’est pas nécessaire de se casser la tête sur quel type choisir (excepté si vous voulez programmer pour de petits appareils où la mémoire est plus petite). En pratique, on utilisera surtout ```char``` pour les caractères, ```int``` pour les entiers et ```double``` pour les flottants. Les autres types ne servent pas à grand-chose.

### Les identificateurs ###

Maintenant que l’on a vu les types, parlons des identificateurs. Comme dit précédemment, un identificateur est un nom donné à une variable pour la différencier de toutes les autres. Et ce nom, c’est au programmeur de le choisir. Cependant, il y a quelques limitations à ce choix. 

* On ne peut utiliser que les 26 lettres de l’alphabet latin (majuscules ou minuscules) : pas d’accents, pas de ponctuation ni d’espaces. Le caractère *underscore* (« _ ») et les chiffres sont cependant acceptés.      
* Un identificateur ne peut pas commencer par un chiffre.
* Les mots-clés ne peuvent pas servir à identifier une variable ; on ne peut donc pas utiliser ces mots : 
    * ```auto```
      * ```break```
    * ```case```
    * ```char```
      * ```const```
      * ```continue```
      * ```default```
    * ```do```
      * ```double```
    * ```else```
      * ```enum```
      * ```extern```
    * ```float```
    * ```for```
    * ```goto```
    * ```if```
    * ```int```
    * ```long```
    * ```register```
    * ```return```
    * ```short```
    * ```signed```
      * ```sizeof```
    * ```static```
      * ```struct```
      * ```switch```
      * ```typedef```
      * ```union```
    * ```unsigned```
    * ```void```
      * ```volatile```
    * ```while``` 
* Pour simplifier, on peut parfaitement considérer que deux variables ne peuvent avoir le même identificateur (le même nom). Il y a parfois quelques exceptions, mais cela n’est pas pour tout de suite.        
* Les identificateurs peuvent être aussi longs que l’on désire, toutefois le compilateur ne tiendra compte que des 32 premiers caractères.

Voici quelques exemples pour bien comprendre : 

| Identificateur correct    | Identificateur incorrect | Raison                         |
| ------------------------- | ------------------------ | ------------------------------ |
| variable                  | Nom de variable          | Espaces interdits              |
| nombre_de_vie             | 1nombre_de_vie           | Commence par un chiffre        |
| test                      | test!                    | Caractère « ! » interdit       |
| un_dernier_pour_la_route1 | ```continue```           | Mot-clé réservé par le langage |

À noter que le C fait la différence entre les majuscules et les minuscules (on dit qu’**il respecte la casse**). Ainsi les trois identificateurs suivants sont différents.

```c
variable
Variable
VaRiAbLe
```

### D’autres mots-clés ###

En plus des mots-clés qui servent à indiquer le type de notre variable, on peut utiliser d’autres mots-clés lors de la déclaration de nos variables. Le but : donner un peu plus d’informations sur nos variables. On peut ainsi préciser que l’on veut que nos variables soient constantes et non modifiables, ou d’autres choses encore. On ne va pas voir tous les mots-clés existants, et pour cause : il nous manque quelques informations pour vous expliquer le rôle de certains. Nous allons seulement parler des mots-clés ```const```, ```volatile``` et ```register```.

Comme vous l’avez surement deviné, ces mots-clés se placent avant le type et le nom de la variable, lors de la déclaration.

#### const ####

Le premier que je vais vous montrer est ```const```. Ce mot-clé signifie « constant » en français. Il sert donc à déclarer une variable comme étant constante, c’est-à-dire qu’on ne pourra pas modifier sa valeur au cours du programme. Sa valeur restera donc inchangée durant toute l’exécution du programme. À quoi ça sert ? C’est utile pour stocker une variable qui ne changera jamais, comme la constante $\pi$ qui vaudra toujours 3,14159265 ou $e$ qui vaudra toujours 2,718281828. 

Une recommandation qui est souvent faite est de déclarer comme étant ```const``` tout ce qui est possible. Cela permet d’éviter pas mal d’erreurs et aide à éclaircir le code. Par convention, une variable constante est souvent écrite en majuscule. Voir une variable constante en minuscule peut paraître étrange pour certains. De plus, **il est extrêmement horripilant de voir des variables non constantes en majuscules** !

#### register ####

Vient ensuite ```register```. Celui-ci permet de dire au compilateur que l’on veut que notre variable soit stockée de préférence dans un registre du processeur, au lieu de devoir être placée en mémoire RAM. C’est en effet le compilateur qui décide quelle variable stocker dans les registres, durant combien de temps, et à quel moment. On dit qu’ils se chargent d’allouer les registres. ```register``` permettait autrefois d’indiquer au compilateur que la variable désignée ```register``` était à placer (ou à copier) dans les registres dès que possible. 

L’utilité de ```register``` est très simple : un registre est au bas mot plus de 100 à 200 fois plus rapide que la mémoire RAM de notre ordinateur. Ainsi, placer (ou copier) une variable dans les registres permet d’accéder à celle-ci bien plus rapidement que si on devait la lire ou l’écrire depuis la mémoire RAM. Idéalement, on voudrait donc mettre toutes nos variables dans ces registres. Mais le problème, c’est que notre processeur ne possède que peu de registres. Il n’est ainsi pas rare d’avoir à se débrouiller avec seulement 4 à 8 registres. Autant dire qu’il faut alors réfléchir consciencieusement aux variables à placer dedans : il faut mettre de préférence des variables auxquelles on va accéder souvent (et ne pas hésiter à déplacer des variables entre registres et mémoire si besoin est). ```register``` permettait de préciser quelles étaient les variables à mettre en priorité dans les registres, histoire d’orienter le choix du compilateur. Cela permettait alors de rendre nos programmes plus rapides.

Mais c’était il y a longtemps : de nos jours, ```register``` ne sert plus à rien (ou presque). La raison est très simple : les compilateurs actuels disposent d’algorithmes mathématiques qui permettent de gérer les registres de façon quasi optimale. En tout cas, nos compilateurs se débrouillent nettement mieux que les programmeurs pour décider quel registre utiliser et quelles données placer dedans. Ils n’ont donc plus besoin d’aide, et ```register``` est souvent ignoré ou sous-utilisé par ces compilateurs. En clair : ```register``` est une antiquité, qui ne doit plus être utilisé, et ne sert strictement à rien. Après, libre à vous de tenter de l’utiliser, mais au moins, vous savez d’avance que c’est inutile.

#### volatile ####

Le dernier est moins connu, car moins utilisé : il s’agit de ```volatile```. C’est un peu l’inverse de ```register```. Une variable marquée ```volatile``` ne peut pas être copiée ou placée dans les registres du processeur.

```volatile``` sert dans certains cas bien particuliers, que vous ne rencontrerez surement jamais. Il arrive qu’une variable soit modifiée par autre chose que le programme dans lequel on a déclaré cette variable. Par exemple, certaines variables peuvent être modifiées par des périphériques, comme la souris, le clavier, etc. Ou encore, on peut avoir à manipuler des variables accessibles par plusieurs programmes, qui peuvent être mises à jour à n’importe quel moment. Ces modifications de la variable se feront alors en mémoire RAM : il est en effet impossible pour un périphérique ou un programme d’aller modifier le contenu d’un registre déjà attribué à un autre programme.

Si on stocke notre variable dans un registre, les mises à jour effectuées en mémoire RAM ne seront pas répercutées sur la copie de la variable stockée dans les registres. Le programme qui aura stocké cette variable dans ses registres continuera donc de manipuler une variable périmée, non mise à jour. Cela peut donner lieu à des bugs relativement bizarres ou catastrophiques.

Pour éviter toute catastrophe, ces variables spéciales doivent donc être marquées ```volatile```, histoire de ne pas pouvoir être placées dans les registres du processeur, et lues ou écrites en mémoire RAM.

Je tiens à préciser que ```volatile``` n’est toutefois utile que pour certaines variables, potentiellement accessibles par autre chose que le programme qui l’a déclaré (un autre programme, un périphérique, etc.), et qui peuvent être modifiées n’importe quand. Ce genre de cas est très rare, et n’arrive que quand on doit travailler avec du matériel très spécial, ou qu’on veut créer des programmes très compliqués, qui manipulent directement le matériel, comme des pilotes de périphériques des systèmes d’exploitation, etc. Autant être franc, vous n’aurez certainement jamais à utiliser ```volatile``` dans un programme, tellement ce genre de cas est rare et particulier. Mais un peu de culture générale ne fait jamais de mal, et peut être utile au cas où. 

### Déclaration et initialisation ###

Maintenant que nous savons toutes les bases, entrainons-nous à déclarer quelques variables :

```c
double taille;
volatile unsigned int age;
char caractere;
short petite_valeur;
```

On peut aussi déclarer plusieurs variables **de même type** sur une même ligne, en séparant leurs noms par une virgule : 

```c
int age, taille, nombre;
```

Je vous conseille d’utiliser les deux méthodes de déclaration que vous venez de voir (multiligne et monoligne) simultanément, comme ceci :

```c
int annee, mois, jour;
int age, taille;
int x, y, z;
```

J’ai regroupé les déclarations de variables selon les « rapports » qu’ils ont entre eux.

Je vous présente du code, des explications, encore du code puis encore des explications. Mais durant tout ce temps, vous avez peut-être essayé de compiler ces codes. Êtes-vous surpris de voir qu’il ne se passe rien ? Les plus malins d’entre vous auront peut-être compris qu’il ne se passe rien en apparence. Je dis bien en apparence car, en réalité, l’ordinateur fait parfaitement son travail : il va réserver des cases mémoire pour nos variables. Votre ordinateur fait donc tout ce que vous lui demandez de faire : déclarer des variables, et non modifier leurs valeurs et encore moins les afficher !

Alors OK, notre case mémoire est réservée pour notre variable, mais quelle est la valeur qu’il y a dedans (quel est l’objet dans le tiroir) ? Eh bien en fait, c’est indéterminé. Il peut y avoir n’importe quelle valeur (n’importe quel objet dans le tiroir).

#### Initialisation ####

Mais heureusement, on peut donner une valeur à une variable dès sa déclaration. On dit aussi qu’on **initialise** notre variable. Ainsi on est sûr que la case mémoire ne contient pas n’importe quoi. 

Pour initialiser une variable, on procède ainsi si c’est une variable destinée à contenir une valeur numérique :

```console
type identificateur = valeur;
```

Ou comme ceci si c’est un caractère :

```console
char identificateur = 'lettre';
```

Voici quelques exemples de déclarations de variables :

```c
volatile unsigned int age = 25;
short petite_valeur = 1;
const long abc = 3141596;
char caractere = 'h';
```

Petite note sur ```const``` : il faut donner une valeur à la variable dès la déclaration puisque l’on ne pourra plus la modifier après !

*Petite précision : la norme C89 réclame que l’on sépare les déclarations du reste du code : on ne peut pas déclarer une variable où l’on veut. Si l’on veut vraiment suivre la norme, on déclare d’abord toutes les variables en début de bloc (c’est-à-dire après une accolade ouvrante) et ensuite vient le reste des instructions.*

#### Initialisation des nombres flottants ####

Je tiens à retenir votre attention sur la manière d’initialiser les variables flottantes (soit donc de type ```float``` ou ```double```). En fait, ces variables sont faites pour contenir des nombres à virgule. À l’initialisation, il ne faut donc pas se contenter de donner sa valeur, il faut aussi mettre la « virgule ». Sauf que l’on ne met pas une virgule : on met un point.

```c
const double pi = 3.14;
```

Cela vient du fait que le C est une invention américaine, et que les anglophones utilisent le point à la place de la virgule, on met un point là où nous autres francophones mettons une virgule. 

Et vous devez impérativement mettre ce point, même si vous voulez stocker un nombre entier dans un ```float``` ou un ```double```.  Par exemple, vous ne devez pas écrire ```double a = 5;``` mais ```double a = 5.;``` (certains préfère ```double a = 5.0;```, cela revient au même). Si vous ne le faites pas, vous risquez d’avoir quelques problèmes.

Voici un petit tableau récapitulatif afin de bien comprendre :

| Type              | Initialisation  |
| ----------------- | --------------- |
| ```char```        | 0 ou ```'\0'``` |
| ```short```       | 0               |
| ```int```         | 0               |
| ```long```        | 0               |
| ```float```       | 0.              |
| ```double```      | 0.              |
| ```long double``` | 0.              |

### Affectation ###

Nous savons donc déclarer (créer) nos variables, et les initialiser (leur donner une valeur à la création). Il ne nous reste plus qu’à voir la dernière manipulation possible : **l’affectation**. Cette affectation permet de modifier la valeur contenue dans une variable, pour la remplacer par une autre valeur.

Il va de soi que cette affectation n’est possible que pour les variables qui ne sont déclarées avec ```const``` : par définition, de telles variables sont en effet constantes et ne peuvent voir leur contenu changer. Cela interdit toute affectation pour ces variables déclarées constantes. 

Pour faire une affectation, il suffit d’opérer ainsi :

```console
identificateur = nouvelle_valeur;
```

On voit que la syntaxe est similaire à celle d’une déclaration avec initialisation : la seule différence, c’est qu’on n’a pas à préciser le type. Ce type est en effet fixé une fois pour toutes lors de la déclaration de notre variable : pas besoin de le préciser lors d’une affectation. Si je veux changer la valeur de mes variables, je procède tout simplement comme suit.

```c
age = 30;
taille = 177.5;
petite_valeur = 2;
```

Il n’y a aucune limite, voyez par exemple :

```c
petite_valeur = 2;
petite_valeur = 4;
petite_valeur = 8;
petite_valeur = 16;
petite_valeur = 8;
petite_valeur = 4;
petite_valeur = 2;
```

À chaque affectation, la variable va prendre une nouvelle valeur. Par contre, ne mettez pas le type quand vous voulez changer la valeur, sinon vous aurez le droit à une belle erreur du type « *redefinition of 'nom_de_votre_variable'* » car vous aurez créé deux variables avec le même identificateur !

Le code suivant est donc incorrect : 

```c
int age = 15;
int age = 20;
```

Si vous exécutez tous ces codes, vous verrez qu’ils n’affichent toujours rien. Mais pourquoi ? Tout simplement parce qu’on n'a pas demandé à notre ordinateur d'afficher quoique ce soit. Et ce n'est pas pour tout de suite : on apprendra comment faire pour afficher quelque chose sur la console au chapitre suivant. Quoiqu'il en soit, ne soyez pas pressés et prenez bien le temps d’assimiler toutes les notions présentées dans ce chapitre.

### Utiliser des variables
Nous savons désormais déclarer, affecter et initialiser une variable, mais que diriez-vous d’apprendre à réaliser des opérations dessus ? Il est en effet possible de réaliser des calculs sur nos variables, comme les additionner, les diviser voire même des opérations plus complexes. C’est le but de cette sous-partie. Nous allons donc enfin transformer notre ordinateur en grosse calculette programmable ! Cette partie est importante, donc même si vous détestez les mathématiques, vous devez la lire.

### Calculs de base ###

Le langage C fournit 5 opérations de base sur nos variables.
​     
* L'addition **+**.       
* La soustraction **-**.       
* La multiplication *****.       
* La division **/**.        
* Le modulo **%** (le reste d’une division euclidienne).

Le langage C fournit aussi d’autres fonctions mathématiques préprogrammées, mais qu’on ne peut pas encore utiliser à ce stade. Nous devrons donc reporter à plus tard l’utilisation de fonctions mathématiques plus complexes. Si jamais vous devez utiliser une fonction mathématique plus complexe, il faudra la programmer, pour le moment. 

Commençons par détailler ces 5 opérations de base.

#### Addition, soustraction et multiplication ####

C’est tout simple : pour faire notre calcul, il suffit d’assigner le résultat du calcul à une variable : 

```c
int somme, difference, produit;

somme = 2 + 3;   /* 5 */
difference = 8 - 12;   /* -4 */
produit = 6 * 7;   /* 42 */
```

On pourrait multiplier les exemples à l’infini, je pense néanmoins que vous avez compris le concept. 

#### Division ####

La division en informatique est différente de celle en mathématiques. Si je vous dis $\frac{15}{4}$, vous en déduisez que le quotient est 3,75. Pourtant, le résultat de celle-ci est 3 en langage C.

```c
int division = 15 / 4;
```

Suite à la lecture du chapitre suivant, vous pourrez vérifier cette affirmation en affichant la valeur de cette opération, mais vous n’en êtes pas encore là, et je vous défends de vous y rendre avant la fin de ce chapitre.

Pour l’ordinateur, le résultat de ```15 / 4``` est bien ```3```. Pourquoi ? Parce qu’on lui a demandé de faire une division d’entiers (appelée **division euclidienne**), donc il répond par des entiers. Si l’on veut afficher le résultat complet (à nos yeux), il faut l’indiquer à l’ordinateur. Comment faire ? Essayez de trouver la solution tout seul.

Un indice ? Pensez aux flottants.

La solution :

```c
double division = 15. / 4.;   /* même si pour nous, c’est la même chose que 15 / 4 */
```

Même si pour nous c’est intuitif, pour l’ordinateur il faut bien préciser si ce sont des entiers ou des flottants.

#### Modulo ####

Le modulo est un peu le complément de la division puisqu’il permet de connaitre le reste d’une division euclidienne. C’est une opération de base aux yeux de l’ordinateur, même si elle est assez peu connue. Un petit code pour la route :

```c
int modulo = 11 % 4;
```

Ici, le résultat de cette instruction est 3, car $11 = 2 \times 4 + 3$. Le modulo est la réponse au problème de la division d’entiers.

#### Opérations entre variables ####

Le principe est tout simple : au lieu d’opérer sur des nombres, on opère sur des variables. Ainsi on peut faire les mêmes opérations sur des variables : 

```c
var = var1 + var2;
d = c / b * a;
```

On peut ainsi rajouter autant de variables que l’on veut, et même mélanger avec des nombres :

```c
d = c / b * a - s + 7 % 2
```

Cependant, il faut faire attention à la priorité des opérateurs : comme en mathématiques, certains opérateurs passent avant d’autres : ```* / %``` ont une priorité supérieure à ```+ -```.

Dans ce code : 

```c
x = nombre + y * 4;
```

C’est ```y * 4``` qui sera exécuté d’abord, puis on ajoutera ```nombre``` au résultat. Faites donc attention, sous peine d’avoir de mauvaises surprises. Dans le doute, mettez des parenthèses.

### Les raccourcis ###

Comment vous y prendriez-vous pour multiplier une variable par trois ? La solution « naïve » serait de faire :

```c
variable = variable * 3;
```

Cependant, c’est long, fatigant, et peut vite devenir fastidieux si l'on fait beaucoup d’opérations de ce genre. On a donc inventé des techniques permettant de raccourcir notre code : les **raccourcis**. Ces raccourcis fonctionnent pour toutes les opérations arithmétiques de base. Ainsi, pour faire la même opération que le code précédent, on peut raccourcir ainsi :

```c
variable *= 3;
```

Ce code concis marche exactement comme le précédent. Et le principe est valable pour toutes les opérations, pour n’importe quelle valeur :

```c
variable += 2;
variable -= 9;
variable /= 8;
variable %= 4;
```

Cependant, il existe encore deux autres raccourcis très fréquemment utilisés. 

#### Incrémentation et décrémentation ####

Ce sont deux opérations qui, respectivement, ajoute ou enlève 1 à une variable. On pourrait utiliser les raccourcis vus juste avant : 

```c
variable += 1;
variable -= 1;
```

Cependant, on a inventé de nouveaux raccourcis pour ces deux opérations, car elles sont très utilisées (vous comprendrez vite pourquoi dans les prochains chapitres). Ces deux raccourcis sont les suivants : 

```c
variable++;
```

Pour l’**incrémentation** (on ajoute 1) et :

```c
variable--;
```

pour la **décrémentation** (on enlève 1). Ces deux lignes sont parfaitement équivalentes aux deux premières. Elles permettent simplement de raccourcir le code. Ce que je viens de vous montrer s’appelle l’[in/dé]crémentation **postfixée**. En effet, il est aussi possible de faire une [in/dé]crémentation **pré-fixée** : le signe est alors avant la variable et non après : 

```c
++variable;
--variable;
```

Il y a une subtile différence entre les deux formes. Une [in/dé]crémentation pré-fixée change la valeur de l’expression avant d'envoyer la valeur, alors qu’une [in/dé]crémentation post-fixée renvoie la valeur et la modifie ensuite. Petit exemple pour bien comprendre : si j'ai une variable a qui vaut 5, ```++a``` incrémentera immédiatement la variable a, qui vaudra alors 6. 

```c
int a = 5 ;
int b = ++a ; /* ici, b vaudra 6 */
```

Par contre, ```a++``` attendra avant d'incrémenter la variable : celle-ci sera incrémentée après la prochaine "utilisation". 

```c
int a = 5 ;
int b = a++ ; /* ici, b vaudra 5, et a sera mit à 6 une fois que 
               la valeur de a++ est recopiée dans b */
```

Fondamentalement, utiliser l’une ou l’autre des deux formes ne change pas grand chose, sauf dans quelques cas particuliers. Dans la plupart des cas, les programmeurs utilisent la forme postfixée (```i++```) en permanence. Il n'y a pas vraiment de raisons valables pour faire cela à l'heure actuelle, mais cette pratique est monnaie courante. Aussi, ne soyez pas étonné de voir des codes utilisant la forme post-fixée alors qu'une forme préfixée aurait été plus adéquate.

### Les conversions de type ###

La conversion de type est une opération qui consiste à changer le type d’une variable en un autre. Je peux ainsi convertir une variable de type ```float``` en type ```int```, par exemple. Il existe deux types de conversions : les **conversions explicites** et les **conversions implicites**.

#### Les conversions explicites ####

Ce sont des conversions voulues et demandées par le programmeur. Elles se déclarent en suivant ce modèle :

```console
(<Type>) <Expression>
```

Voici par exemple un code où l’on demande explicitement la conversion d’un ```double``` en ```int```.

```c
int a;
const double pi = 3.14;

a = (int) pi;
```

La valeur de ```pi``` reste inchangée, elle vaudra toujours 3.14 dans la suite du programme. Par contre, ```a``` vaut maintenant 3, puisque le flottant a été converti en entier. Expliciter une conversion peut nous servir quand on veut forcer le résultat d’une opération par exemple. Imaginons que nous voulons faire une division, mais que les deux opérandes soient de type ```int```.

```c
int a, b;
double c;

a = 5;
b = 9;

c = a / b;
```

Vu qu’on fait une division euclidienne, le résultat sera tronqué. Si on veut avoir un résultat avec la partie décimale, il suffit de faire une conversion explicite d’un des deux opérandes en ```double``` :

```c
c = (double) a / b;
/* ou */
c = a / (double) b;
```

#### Les conversions implicites ####

Ce sont des conversions que fait le compilateur tout seul, sans que l’on ait demandé quoi que ce soit. En général, ça ne gêne pas le programmeur, mais ça peut parfois être problématique si la conversion n’était pas voulue. Par exemple, si l’on reprend le code précédent, il y aura toujours une conversion.

```c
int a;
const double pi = 3.14;

/* Il y a conversion implicite de double en int, mais rien 
n’est précisé, c’est le compilateur qui fait ça de lui-même. */
a = pi;
```

Cependant, les conversions amènent parfois à des pertes d’information si l’on n’y prend pas garde.

#### Perte d’information ####

Une perte d’information survient quand on convertit le type d’une variable en un autre type plus petit et que celui-ci ne peut pas contenir la valeur reçue. Si, par exemple, je convertis un ```double``` de 100 chiffres en un ```short```, il y a perte d’information, car le type ```short``` ne peut pas contenir 100 chiffres. La règle à retenir est la suivante :

> Si on convertit un type T vers un type S plus petit, il y a perte d’information.
> *-- Règle des conversions*

Les conversions, et surtout les conversions implicites qui peuvent être vicieuses, doivent être manipulées avec précaution, au risque de tomber sur des valeurs fausses en cas de perte d’information. Nous découvrirons d’ici quelques chapitres comment connaitre la taille d’un type T pour éviter ces pertes d’information.

Voilà, c’est la fin de ce chapitre. On a déjà vu beaucoup de choses, n’hésitez pas à potasser pour bien assimiler tout ça. Les variables sont vraiment la base de la programmation, il faut bien les comprendre.

Rendez-vous au prochain chapitre qui sera très intéressant : vous pourrez par exemple demander l’âge de l’utilisateur pour ensuite l’afficher !

## Manipulations basiques des entrées/sorties
Durant l’exécution d’un programme, le processeur, qui est le cerveau de l’ordinateur, a besoin de communiquer avec le reste du matériel. Il doit en effet recevoir des informations pour réaliser des actions et il doit aussi en transmettre. Ces échanges d’informations sont les **entrées** et les **sorties** (ou *input / output* pour les anglophones), souvent abrégée E/S (ou I/O par les anglophones).

Les entrées permettent de recevoir une donnée en provenance de certains périphériques. Les données fournies par ces entrées peuvent être une information envoyée par le disque dur, la carte réseau, le clavier, la souris, un CD, un écran tactile, bref par n’importe quel périphérique.Par exemple, notre clavier va transmettre des informations sur les touches appuyées (par exemple **1** et **8**) au processeur ou à la mémoire : notre clavier est donc une entrée.

À l’inverse, les sorties vont transmettre des données vers ces périphériques. On pourrait citer l'exemple de l'écran : notre ordinateur lui envoie des informations pour qu'elles soient affichées.

Dans ce chapitre, nous allons apprendre différentes fonctions fournies par le langage C, qui vont nous permettre de recevoir ou d'envoyer des informations sur nos sorties et d'en recevoir sur nos entrées. Vous saurez ainsi comment demander à un utilisateur de rentrer une information au clavier, et comment afficher quelque chose sur la console.

### Les sorties
Intéressons-nous dans un premier temps aux sorties. Afin d’afficher un caractère ou même un texte (on préfère le terme de « chaîne de caractères ») à l’écran, il faut utiliser **des fonctions**. Depuis votre premier code, vous en utilisez une : la fonction *main*. Une fonction, en simplifiant un peu, est un morceau de code exécutant des instructions. Des instructions qui permettent d’effectuer des opérations (avec par exemple des fonctions mathématiques) sur des variables ou encore d’écrire du texte à l’écran par exemple.

Nous allons voir trois fonctions d’affichage de données dans ce chapitre, je nomme fièrement :

* *printf* pour écrire une chaîne de caractères *formatée* ;	
  * *puts* pour écrire une chaîne de caractères toute simple ;
* *putchar* pour écrire un caractère.

### printf — Écrire une chaîne de caractères de manière formatée ###

La fonction *printf* affiche donc une chaîne de caractères (c'est à dire du texte) à l’écran. On l'utilise comme ceci :

```c
printf("Votre texte...");
```
Cette fonction permet non seulement d'afficher des chaînes de caractères simples, mais également la valeur d'une variable passée en paramètre. Pour ce faire, il suffit d'utiliser un **indicateur de conversion** : il s'agit du caractère spécial ```%``` suivi d'une lettre qui varie en fonction du type de la variable. Voici les indicateurs de conversions de la norme C89 :

| Type                 | Indicateurs de conversions |
| -------------------- | -------------------------- |
| ```char```           | ```%c```                   |
| ```int```            | ```%d```                   |
| ```long```           | ```%ld```                  |
| ```short```          | ```%hd```                  |
| ```float```          | ```%f```                   |
| ```double```         | ```%f```                   |
| ```long double```    | ```%Lf```                  |
| ```unsigned int```   | ```%u```                   |
| ```unsigned short``` | ```%hu```                  |
| ```unsigned long```  | ```%lu```                  |

Après avoir inscrit un indicateur de conversion dans la chaîne de caractère (entre les guillemets), il faut indiquer de quelle variable il faut afficher la valeur. Il suffit de rajouter une virgule après les ces derniers, suivis du nom de la variable, comme ceci : 

``` console
printf("%[lettre]", variable_a_afficher);
```

Essayez donc d’afficher la valeur de la variable pi :

``` c
/* Cette variable est constante (utilisation de « const »)
car la valeur de pi ne change jamais */
const double pi = 3.1415926536; 
printf("pi = %f", pi);
```
```console
pi = 3.1415926536
```

C’est tout simple. Vous pouvez répéter ces opérations autant que fois que vous le voulez, il suffit de rajouter le symbole ``` %[lettre]```  à chaque fois que vous souhaitez afficher la valeur d’une variable. Il n’y a aucune limite, voyez par exemple :

```c
double flottant = 19.75;
int nombre = 10, nombre_2 = 0;
char lettre = 'a';

nombre_2 = nombre * 3;

printf("nombre = %d, nombre_2 = %d, flottant = %f, lettre = %c", nombre, nombre_2, flottant, lettre);
```

Amusez-vous à créer des variables et à en afficher la valeur pour voir si vous avez bien compris. Attention cependant, vous devez préciser la variable dont il faut afficher la valeur, sinon vous pouvez aller des valeurs fantaisistes au plantage du programme !

#### Le scoop du jour ####

Devinez quoi, vous pouvez effectuer toutes sortes d’opérations à l’intérieur même de *printf* , comme des calculs par exemple. Quelques codes pour bien comprendre :

``` c
printf("%d | ", 1 + 2 * 3); /* Affiche « 7 » */

printf("%d | ", (1 + 2) * 3); /* Affiche « 9 » */

printf("%f | ", -1. + 2. * 4. / 3.); /* Affiche « 1.666667 » */

printf("%c", 'x'); /* Affiche « x » */
```
```console
7 | 9 | 1.666667 | x
```

Faites bien attention à mettre le « . », dans le cas contraire, le résultat serait faussé. Nous pouvons faire sensiblement la même chose avec des variables :

``` c
int x = 42, y = 21;

printf("%d", x * y / 2);

```
```console
441
```

#### Tabulations et compagnie ####

Afin d’afficher une tabulation ou encore un retour à la ligne, on utilise un **caractère d'échappement**.

```c
printf("La valeur de la variable\n\tx est : %f\n\ty = %d", x, y);
```
```console
La valeur de la variable
        x est : 42.424340
        y = 1
```

```'\n'``` et ```'\t'``` font partie de ces caractères. Voici un petit tableau qui en liste quelques-uns parmi les plus utilisés :

| Caractère d’échappement | Signification          |
| ----------------------- | ---------------------- |
| ```'\n'```              | Retour à la ligne      |
| ```'\t'```              | Tabulation horizontale |
| ```'\r'```              | Retour chariot         |
| ```'\f'```              | Saut de page           |
| ```'\''```              | Affiche une apostrophe |
| ```'\"'```              | Affiche un guillemet   |
| ```'\\'```              | Affiche un antislash   |
| ```'%%'```              | Affiche un %           |

#### Précision ####

Si vous avez été attentifs, vous avez dû remarquer que lorsqu'on affiche un flottant il y a un certain nombre de zéros qui suivent, et ce peu importe s'ils sont utiles ou non. Heureusement, les programmeurs de la fonction *printf*  ont pensé à tout. Afin de supprimer certains zéros inutiles, vous pouvez préciser la **précision de l’affichage**. Une précision, sous la forme d’un point ('.') suivi par un nombre, indique donc le nombre de chiffres qu’il y aura derrière la virgule.

``` c
double x = 42.42734;

printf("%.2f", x);
```
```console
42.43
```

On remarque dans cet exemple un arrondi au centième. Il correspond au nombre indiqué lors de la précision de l'affichage. La variable n'a pas été modifiée, l'arrondi n'intervient que pour l'affichage. 

Pour finir, voici la chaîne de format (simplifiée) qu’utilise la fonction *printf*  :

```console
% [.précision] indicateur de conversion
```

#### Sur plusieurs lignes ####

Plutôt qu'appeler plusieurs fois la fonction *printf* pour écrire du texte, on peut ne l'appeler qu'une fois et écrire plusieurs lignes. Pour cela, on utilise le signe ```\``` à chaque fin de ligne. Exemple :

```c
#include <stdio.h>

int main(void)
{
	printf("Texte ecrit sur plusieurs \
		   lignes dans le code source \
		   et egalement dans la console.");

    return 0;
}
```
```console
Texte écrit sur plusieurs                  lignes dans le code source
   et également dans la console.
```

L'inconvénient est que le texte affiché dans la console n'est pas parfaitement alignés. Il existe heureusement une autre possibilité : on peut écrire plusieurs phrases entre guillemets sans problème :

```c
#include <stdio.h>

int main(void)
{
	printf("Texte ecrit sur plusieurs "
		   "lignes dans le code source "
		   "mais sur une seule dans la console.");

    return 0;
}
```
```console
Texte écrit sur plusieurs lignes dans le code source mais sur une seule dans la console.
```

Ce qu'il faut retenir de ces deux méthodes, c'est que l'on est pas obligé d'appeler systématiquement *printf* pour afficher de nouvelles phrases, mais qu'au contraire il est possible d'en afficher plusieurs en n'utilisant qu'une fois la fonction.

### puts — Écrire une chaîne de caractères ###

L’utilisation de la fonction *puts* est plus simple puisque elle ne se contente d'afficher que des chaînes de caractères simples.

```c
puts("Salut les zeros !");
```

Cette fonction n’a pas de chaîne de format à évaluer comme *printf*, elle est donc plus simple à utiliser ainsi que (très légèrement) plus rapide à l’exécution. Ainsi, le code suivant ne fonctionnera pas :

```c
int var = 0;

puts("%d", var);
```

Je tiens à préciser que *puts* ajoute automatiquement une fin de ligne à la fin de la chaîne de caractères que vous souhaitez afficher.

### putchar — Écrire un caractère ###

La fonction *putchar* affiche tout simplement un caractère.

```c
putchar('c');
```

On peut également afficher une variable de type ```char``` avec cette fonction.

```c
char caractere = 'Z';

putchar(caractere);
```

### Interagir avec l'utilisateur
Maintenant que nous savons déclarer, utiliser et même afficher des variables, nous sommes fin prêts pour interagir avec l’utilisateur. En effet, jusqu’à maintenant, on s’est contentés d’afficher des informations. Nous allons voir comment en récupérer grâce à la fonction *scanf*, dont l'utilisation est assez semblable à *printf*.

```console
scanf("%[lettre]", &variable_dans_laquelle_on_va_mettre_notre_valeur);
```

Souvenez-vous de la brève explication sur la mémoire au début du chapitre précédent. Celle-ci, je vous le rappelle, fonctionne comme une armoire avec des tiroirs (les adresses mémoires) et des objets dans ces tiroirs (nos variables). La fonction *scanf* a besoin de connaitre l’emplacement en mémoire de nos variables afin de les modifier. Afin d’effectuer cette opération, on utilise le symbole ```&```. Ce concept de transmission d’adresses mémoires est un petit peu difficile à comprendre au début, ne vous inquiétez pas ; vous aurez l’occasion de bien revoir tout cela en profondeur dans le chapitre des pointeurs.

Vous pouvez tester ce programme : 

```c
int age;

puts("Donnez votre age :");
/* Si vous oubliez le &, le programme plantera quand vous le lancerez, 
car vous tenterez d’accéder à une adresse mémoire inexistante ! */
scanf("%d", &age);
printf("Vous avez %d an(s) !\n", age);
```
```console
Donnez votre age :
15
Vous avez 15 an(s) !
```

Ici, *scanf* attend patiemment que l’utilisateur saisisse un nombre au clavier afin de modifier la valeur contenue à l’adresse de *age* : on dit que c'est une **fonction bloquante**, puisqu'elle suspend l'exécution du programme tant que l'utilisateur n'a rien rentré. Ensuite, *printf* affiche bien ce qui est voulu.

Les indicateurs de conversions sont peu différents de ceux de *printf* :

| Type                 | Affichage | Exemple                                  |
| -------------------- | --------- | ---------------------------------------- |
| ```char```           | ```%c```  | ```char lettre;  scanf("%c", &lettre);``` |
| ```int```            | ```%d```  | ```int age;  scanf("%d", &age);```       |
| ```long```           | ```%ld``` | ```long age;  scanf("%ld", &age);```     |
| ```short```          | ```%hd``` | ```short age;  scanf("%hd", &age);```    |
| ```float```          | ```%f```  | ```float taille;  scanf("%f", &taille);``` |
| ```double```         | ```%lf``` | ```double taille;  scanf("%lf", &taille);``` |
| ```long double```    | ```%Lf``` | ```long double taille;  scanf("%Lf", &taille);``` |
| ```unsigned int```   | ```%u```  | ```unsigned int age;  scanf("%u", &age);``` |
| ```unsigned short``` | ```%hu``` | ```unsigned short age  scanf("%u", &age);``` |
| ```unsigned long```  | ```%lu``` | ```unsigned long age;  scanf("%u", &age);``` |

Vous pouvez utiliser cette fonction de différentes manières, vous pouvez lire plusieurs entrées en même temps, par exemple :

```c
int x, y;

scanf("%d %d", &x, &y);
printf("x = %d | y = %d\n", x, y);
```

L’utilisateur a deux possibilités, soit d’insérer un espace, soit d’insérer un retour à la ligne :

```console
14
6
x = 14 | y = 6

/* OU ENCORE */

14 6
x = 14 | y = 6
```

La fonction *scanf* est en apparence simple, oui, je dis bien en apparence, car son utilisation peut devenir très complexe en sécurisant les entrées de l’utilisateur, par exemple. Cependant, à votre niveau, vous ne pouvez pas encore gérer le cas où l’utilisateur entre du texte à la place d’un nombre ; si cela arrive, votre programme aura de très fortes chances de planter. Ce n’est pas très grave, vous saurez en temps voulu comment gérer de manière avancée les entrées de l’utilisateur.

### Exercice
Vous êtes prêts pour un exercice ? Essayez de coder une minicalculatrice qui :

* Dit bonjour ;
  * Demande deux nombres entiers à l’utilisateur ;
  * Les additionne, soustrait, multiplie et les divise (avec un arrondi au millième) ;
* Dit au revoir.

Voici ce que ça pourrait donner :

```console
Bonjour !

Veuillez saisir le premier nombre : 4
Veuillez saisir le deuxième nombre : 7

Calculs :

        4 + 7 = 11
        4 - 7 = -3
        4 * 7 = 28
        4 / 7 = 0.571

Au revoir !
```

Essayez vraiment de réaliser ce petit programme sans aide, sans regarder le code de correction. Si besoin est, elle est [ici](http://paste.awesom.eu/informaticienzero/odf&ln).

Vous y êtes arrivé sans problème ? Bravo ! Dans le cas contraire, ne vous inquiétiez pas, ce n'est pas grave. Relisez bien tous les points qui ne vous semblent pas clairs et ça devrait aller mieux.

Maintenant, vous êtes capable de communiquer avec l’utilisateur. Cependant, nos actions sont encore un peu limitées. Nous verrons dans les prochains chapitres comment mieux réagir à ce que l’utilisateur communique.

## Les conditions
Jusque-là, vous ne savez qu'écrire du texte, manipuler des nombres et interagir un tout petit peu avec l'utilisateur.

En gros, pour le moment, un programme est quelque chose de sacrément stupide : il ne permet que d'exécuter des instructions dans l'ordre. Pour le moment, on ne sait faire que cela : faire des calculs simples dans un certain ordre. Notre ordinateur ne sert pas à grand chose de plus qu'une vulgaire calculette qu'on peut acheter n'importe où. Mine de rien, il serait sympathique de pouvoir faire plus de choses. Mais rassurez-vous : on peut faire mieux ! Les langages de programmation actuels fournissent des moyens permettant à notre programme de faire des choses plus évoluées et de pouvoir plus ou moins s'adapter aux circonstances au lieu de réagir machinalement. Pour rendre notre ordinateur "plus intelligent", on peut par exemple souhaiter que celui-ci n'exécute une suite d'instructions que si une certaine condition est remplie. Ou faire mieux : on peut demander à notre ordinateur de répéter une suite d'instructions tant qu'une condition bien définie est respectée.

Pour ce faire, diverses **structures de contrôle** de ce type ont donc été inventées. Voici les plus utilisées et les plus courantes : ce sont celles qui reviennent de façon récurrente dans un grand nombre de langages de programmation actuels. On peut bien sûr en inventer d’autres, en spécialisant certaines structures de contrôle à des cas un peu plus particuliers ou en en inventant des plus évoluées. 

| Nom de la structure de contrôle | Ce qu'elle fait                          |
| ------------------------------- | ---------------------------------------- |
| ***If...Then***                 | exécute une suite d'instructions si une condition est respectée. |
| ***If...Then...Else***          | exécute une suite d'instructions si une condition est respectée ou exécute une autre suite d'instructions si elle ne l'est pas. |
| ***Switch***                    | exécute une suite d'instructions différente suivant la valeur testée. |
| ***While...Do***                | répète une suite d'instructions tant qu'une condition est respectée. |
| ***Do...While***                | répète une suite d'instructions tant qu'une condition est respectée. La différence, c'est que la boucle ***Do...While*** exécute au moins une fois cette suite d'instructions. |
| ***For***                       | répète un nombre fixé de fois une suite d'instructions. |

Concevoir un programme (dans certains langages de programmation), c'est simplement créer une suite d'instructions, et utiliser ces fameuses structures de contrôle pour l'organiser.

Ces structures de contrôle permettent donc de modifier le comportement du programme suivant la valeur de différentes conditions. Ainsi, si une condition est vraie, alors le programme se comportera d'une telle façon, si elle est fausse, le programme fera telle ou telle chose, etc. Notre ordinateur a donc besoin de deux choses pour exécuter ces structures de contrôle :

 * des instructions pour évaluer ces conditions ;
 * et des instructions qui vont faire reprendre notre processeur au bon endroit, en fonction du résultat de notre condition.

Les première sont ce qu'on appelle des instructions de test. Les secondes sont ce qu'on appelle des instructions de branchement conditionnelles.

Dans ce chapitre, on va voir comment utiliser les structures de contrôles les plus basiques disponibles en C, à savoir les trois premières structures de contrôle mentionnées dans le tableau du dessus. Nous allons aussi voir comment faire tester si une condition est vraie ou fausse à notre ordinateur.

### Conditions et booléens
Il va de soit qu'avant de pouvoir utiliser des structures de contrôle, on doit pouvoir exprimer, écrire des conditions. Pour cela, le langage C fournit de quoi écrire quelques conditions de base. Divers opérateurs existent en C : ceux-ci permettent d'effectuer des comparaisons entre deux nombres. Ces opérateurs peuvent s'appliquer sur deux nombres écrits en dur dans le code, ou deux variables qui stockent un nombre. Ces opérateurs vont donc effectuer des comparaisons entre deux nombres, et vérifier si la comparaison est vraie ou fausse. Par exemple, ces opérateurs permettront de vérifier si une variable est supérieure à une autre, si deux variables sont égales, etc.

### Comparaisons ###

L'écriture d'expression avec des opérateurs est similaire aux écritures mathématiques que vous voyez en cours : l'opérateur est entre les deux variables à comparer. On a donc une variable à gauche de l'opérateur, et une à droite. 

Pour donner un exemple, on va prendre l'opérateur de supériorité : l'opérateur >. Avec cet opérateur, on pourra écrire des expressions du style : ```a > b``` , qui vérifiera si la variable a est strictement supérieure à la variable b.

Mais cet opérateur n'est pas le seul. Voici un tableau réunissant ses collègues :

| Symbole en langage C | Signification                            |
| -------------------- | ---------------------------------------- |
| ```==```             | Est-ce que les deux variables testées sont égales ? |
| ```!=```             | Est-ce que les deux variables testées sont différentes ? |
| ```<```              | Est-ce que la variable à gauche est strictement inférieure à celle de droite ? |
| ```<=```             | Est-ce que la variable à gauche est inférieure ou égale à celle de droite ? |
| ```>```              | Est-ce que la variable à gauche est strictement supérieure à celle de droite ? |
| ```>=```             | Est-ce que la variable à gauche est supérieure ou égale à celle de droite ? |

Ces opérateurs ne semblent pas très folichons : avec, on ne peut faire que quelques tests de conditions basiques sur des nombres. Mais pour un ordinateur, tout est nombre, et on peut donc se débrouiller avec ces opérateurs pour exprimer toutes les conditions que l'on veut : il suffira des les combiner entre eux, avec les bonnes valeurs à comparer. Vous verrez quand on passera à la pratique, cela sera plus clair.

Dans les faits, le processeur de notre ordinateur possède souvent des instructions pour effectuer ces comparaisons. Vous pouvez parfaitement considérer que ces comparaisons peuvent être calculées directement par le processeur.

### Les booléens ###

Comme je l'ai dit, ces opérateurs vont avoir un résultat : vrai si la condition est vérifiée, et faux si la condition est fausse. Mais notre ordinateur ne connait pas vrai ou faux : il ne connait que des suites de bits, des nombres ! Et on est alors obligé de coder, de représenter les valeurs "vrai" ou "faux" avec des nombres. 

Certains langages fournissent pour cela un type bien séparé pour stocker le résultat des opérations de comparaisons. La représentation des valeurs "vrai" et "faux" est ainsi gérée par le compilateur, et on peut travailler dans notre code en utilisant à la place des valeurs True (vrai en anglais) ou False (faux). Mais dans les premières versions du langage C, ce type spécial n'existe pas ! Il a donc fallu ruser et trouver une solution pour représenter les valeurs "vrai" et "faux". Pour cela, on a utilisé la méthode la plus simple : on utilise directement des nombres pour représenter ces deux valeurs. Ainsi, la valeur Faux est représentée par un nombre entier, tout comme la valeur Vrai. Le langage C impose que :

* Faux soit représenté par un zéro ;
* et que Vrai soit représenté par tout entier différent de zéro.

Et nos opérations de comparaisons suivent cette règle pour représenter leur résultat. Ainsi, une opération de comparaison va renvoyer 0 si elle est fausse et renverra 1 si elle est vraie. Les opérateurs de comparaisons vérifient l'existence d'une certaine relation entre les valeurs qui lui sont associées (opérandes). Le résultat de cette vérification est égal à l'une de ces deux valeurs : 0, si la condition est logiquement fausse et 1 si en revanche elle est vraie.

#### Exemple ####

Vous ne me croyez pas ? Alors, vérifions quels sont les résultats renvoyés par diverses comparaisons. Par exemple, essayons avec le code suivant :

```c
int main(void)
{
    printf("10 == 20 renvoie %d\n", 10 == 20);
    printf("10 != 20 renvoie %d\n", 10 != 20);
    printf("10 < 20 renvoie %d\n", 10 < 20);
    printf("10 > 20 renvoie %d\n", 10 > 20);

    return 0;
}
```

Le résultat :

```console
10 == 20 renvoie 0
10 != 20 renvoie 1
10 < 20 renvoie 1
10 > 20 renvoie 0
```

Le résultat confirme bien ce que je vous ai dit ci-dessus : les résultats de ces conditions sont soit 0 si la comparaison effectuée est fausse, soit 1 si elle est vraie.

### Les opérateurs logiques
Toutes ces comparaisons sont un peu faibles seules : il y a des choses qui ne sont pas possibles en utilisant une seule de ces comparaisons. 

Par exemple, on ne peut pas vérifier si un nombre est dans un intervalle en une seule comparaison. Supposons que pour une raison quelconque, je veuille vérifier que le contenu d'une variable de type ```int``` est compris entre 0 et 1000, 0 et 1000 non inclus. Je ne peux pas vérifier cela avec une seule comparaison (ou alors il faut vraiment ruser). On peut vérifier que notre entier est inférieur à 1000 OU qu'il est supérieur à zéro, mais pas les deux en même temps. Il nous faudrait donc trouver un moyen de combiner plusieurs comparaisons entre elles pour résoudre ce problème. Eh bien rassurez-vous : le langage C fournit de quoi combiner plusieurs résultats de comparaisons, plusieurs booléens. Il fournit pour cela ce qu'on appelle des **opérateurs booléens**, aussi appelés des **opérateurs logiques**.

### Les opérateurs logiques de base ###

Il existe trois opérateurs logiques. L'opérateur ET, l'opérateur OU, et l'opérateur NON. Les opérateurs ET et OU vont permettre de combiner deux booléens. L'opérateur NON ne servira par contre pas à cela, comme vous allez le voir. Voyons plus en détail ces trois opérateurs.

#### L'opérateur ET ####

L'opérateur ET va manipuler deux booléens. Il va renvoyer "vrai" si les deux booléens sont vrais, et renverra faux sinon.

| Premier booléen | Second booléen | Résultat |
| --------------- | -------------- | -------- |
| Faux            | Faux           | Faux     |
| Faux            | Vrai           | Faux     |
| Vrai            | Faux           | Faux     |
| Vrai            | Vrai           | Vrai     |

Il permet par exemple de vérifier que deux comparaisons sont vraies en même temps : il suffit d'appliquer un opérateur ET sur les booléens renvoyés par les deux comparaisons pour que notre opérateur ET nous dise si les deux comparaisons sont vraies en même temps. Cet opérateur s'écrit &&. Il s'intercalera entre les deux comparaisons ou booléens à combiner. Par exemple, reprenons l'exemple vu plus haut, avec l'intervalle. Si je veux combiner les comparaisons ```a > 0``` et ```a < 1000```, je devrais écrire ces deux comparaisons entièrement, et placer l'opérateur ET entre les deux. Ce qui fait que l'expression finale sera ```a > 0 && a < 1000```.

#### L'opérateur OU ####

L'opérateur OU fonctionne exactement comme l'opérateur ET : il prend deux booléens et les combines pour former un résultat. La différence c'est que l'opérateur OU ne vérifie pas que les deux booléens vrais en même temps. À la place, il va vérifier si un seul des booléens qu'il manipule est vrai. Si c'est le cas, il renverra "vrai". Dans les autres cas, il renverra "Faux".

| Premier booléen | Second booléen | Résultat |
| --------------- | -------------- | -------- |
| Faux            | Faux           | Faux     |
| Faux            | Vrai           | Vrai     |
| Vrai            | Faux           | Vrai     |
| Vrai            | Vrai           | Vrai     |

Cet opérateur s'écrit ||. Il s'intercalera entre les deux booléens ou les deux comparaisons à combiner. Pour donner un exemple, supposons que je veuille savoir si un nombre est divisible par 3 ou par 5, ou les deux. Pour cela, je vais devoir utiliser deux comparaisons : une qui vérifie si notre nombre est divisible par 3, et une autre qui vérifie s’il est divisible par 5. Ces conditions sont ```a % 3 == 0``` pour le test de divisibilité par 3, et ```a % 5 == 0``` pour le test de divisibilité par 5. Il reste juste à combiner les deux tests avec l'opérateur ||, ce qui donne : ```( a % 3 == 0 ) || ( a % 5 == 0 )```. Vous remarquerez que j'ai placé des parenthèses pour plus de lisibilité.

#### L'opérateur NON ####

Cet opérateur est un peu spécial : il va manipuler un seul booléen, contrairement à ses confrères ET et OU. Son rôle est d'inverser ce dernier.

| Booléen | Résultat |
| ------- | -------- |
| Faux    | Vrai     |
| Vrai    | Faux     |

Cet opérateur se note ! . Son utilité ? Simplifier certaines expressions. Par exemple, si je veux vérifier qu'un nombre n'est pas dans l'intervalle $] 0 , 1000 [$, on peut utiliser l'opérateur NON intelligemment. Je sais vérifier qu'un nombre est dans cet intervalle : il me suffit d'écrire l'expression ```a > 0 && a < 1000```, vu plus haut. Pour rappel, cette expression permet de vérifier qu'un nombre est dans cet intervalle. Pour vérifier la condition inverse, à savoir "le nombre a n'est pas dans cet intervalle", il suffit d'appliquer l'opérateur NON à cette expression. On obtient alors l'expression ```! ( a > 0 && a < 1000 )```.

Vous remarquerez que pour cet exemple, on peut se passer de l'opérateur NON en récrivant une expression plus légère, à savoir ```a <= 0 || a >= 1000```. C'est ainsi, on peut simplifier les expressions écrites avec des opérateurs logiques pour diminuer le nombre d'opérateurs utilisés. Cela sert pour simplifier l'écriture des calculs, ou gagner marginalement en performances lors des calculs des expressions utilisant ces opérateurs. Pour la culture générale, ces techniques de simplification servent aussi dans divers domaines de l’informatique, et même en électronique. Pour les curieux, il existe un tutoriel sur le sujet sur le Site du Zéro, accessible via ce lien : [l'algèbre de Boole](http://www.siteduzero.com/tutoriel-3-342264-l-algebre-de-boole.html).

### Évaluation en court-circuit ###

Dans les opérateurs logiques && et ||, on exécute obligatoirement la première comparaison avant la seconde. C'est toujours le cas : la norme du C impose de tester d'abord la première comparaison, puis d'effectuer la seconde. Ce n'est pas le cas dans d'autres langages, mais passons.

Ce genre de détail permet à nos opérateurs && et || d'avoir un comportement assez intéressant, qui peut être utile dans certains cas pour éviter des calculs inutiles. Pour l'illustrer, je vais reprendre l'exemple utilisé plus haut : on veut vérifier qu'un entier est compris entre 0 et 1000 (0 et 1000 ne comptent pas, ne sont pas inclus dans l'intervalle voulu). On utilise pour cela l'expression logique ```a > 0 && a < 1000```. Et c'est là que les choses deviennent intéressantes. Supposons que a soit inférieur ou égal à zéro. Dans ce cas, on saura dès la première comparaison que notre entier n'est pas dans l'intervalle. On n'a pas besoin d'effectuer la seconde. Eh bien rassurez-vous : le langage C nous dit si jamais la première comparaison d'un && ou d'un || suffit à donner le bon résultat, la seconde comparaison n'est pas calculée. 

Par exemple, pour l'opérateur &&, on sait d'avance que si la première comparaison est fausse, la seconde n'est pas à calculer. En effet, l'opérateur ET ne renvoie vrai que si les deux comparaisons sont vraies. Si une seule d'entre elles renvoie faux, on pas besoin de calculer l'autre. Et vu que la première comparaison, celle de gauche, est celle effectuée ne premier, on est certain que si celle-ci renvoie faux, la seconde n'est pas calculée.

Pour l'opérateur ||, c'est différent : la seconde comparaison n'est pas calculée quand la première comparaison est vraie. En effet, l'opérateur || renvoie vrai dès qu'une seule des deux comparaisons testées est vraie. Donc, si la première est vraie, pas besoin de calculer la seconde.

Ce genre de propriétés des opérateurs && et || peut-être utilisée efficacement pour éviter de faire certains calculs. Il suffit de choisir intelligemment quelle comparaison mettre à gauche de l'opérateur, suivant la situation.

### Encore mieux ! ###

Bien sûr, on peut aussi mélanger ces opérateurs pour créer des conditions encore plus complexes. Voici un exemple d'une expression logique plutôt complexe (et inutile, je l'ai créé uniquement pour l'exemple) :

```c
int nb_1 = 3, nb_2 = 64, nb_3 = 12, nb_4 = 8, nb_5 = -5, nb_6 = 42;

int boolean = ((nb_1 < nb_2 && nb_2 > 32) ||
               (nb_3 < nb_4 + nb_2 || nb_5 == 0)) &&
               (nb_6 > nb_4);

printf("La valeur logique est egale a : %d\n", boolean);
```

Ici, la variable *boolean* est égale à 1, la condition est vrai. Comme vous le voyez, j'ai inséré des retours à la ligne pour la clarté du code. 

#### Parenthèses ####

En regardant le code écrit plus haut, vous avez surement remarqué la présence de plusieurs parenthèses : celles-ci enlèvent toute ambigüité dans les expressions créées avec des opérateurs logiques. Et oui, en mathématiques on doit utiliser des parenthèses dans nos équations; et bien c'est pareil avec des expressions utilisant des opérateurs logiques. Par exemple, le code suivant :

```c
printf( "%d\n", (a && b) || (c && d) );
```

Est différent de :

```c
printf( "%d\n", a && (b || c) && d );
```

Pour être sûr d'avoir le résultat souhaité, ajoutez des parenthèses.

### La structure if
Vous savez désormais manipuler les booléens, cela est certes très amusant, mais l'intérêt de la chose limité est assez limité pour le moment. Ils nous permettent de savoir si une ou plusieurs conditions sont respectées, mais reste à trouver un moyen pour exécuter un bloc d'instruction suivant le résultat de ces conditions. C'est le rôle de l'instruction ```if``` et de ses consœurs.

### L'instruction if ###

L'instruction ```if``` sert à exécuter un bloc d'instructions si une expression logique ou une condition est vérifiée ou passe à la suite du programme si ce n'est pas le cas. 

![](http://uploads.siteduzero.com/files/391001_392000/391452.png)

L'instruction ```if``` ressemble à ceci :

```c
if(/* Expression logique */)
{
    /* Une ou plusieurs instructions */
}
```

Si la condition testée par le ```if``` n'est pas vérifiée, le bloc d'instruction est zappé et le programme recommence immédiatement à la suite du bloc d'instruction délimité par l'instruction ```if```. 

Si vous n'avez qu'une seule instruction à réaliser, vous avez la possibilité de ne pas mettre d'accolades.

```c
if(/* Expression logique */)
    /* Une seule instruction */
```

Cependant, je vous conseille de mettre les accolades systématiquement afin de rendre vos codes plus clairs et de ne pas vous poser de problèmes si vous décidez de rajouter des instructions par la suite en oubliant d'ajouter des accolades. Bien sûr, ce n'est qu'un avis personnel, vous êtes libre de faire ce que vous voulez.

#### Exemple numéro 1 ####

Faisons un test :

```c
int nombre_1 = 10, nombre_2 = 20;

if(nombre_1 < nombre_2)
{
    printf("%d est inferieur a %d\n", nombre_1, nombre_2);
}
```

La sortie de ce code est évidemment :

```console
10 est inférieur à 20
```

L'instruction ```if``` évalue l'expression logique ```nombre_1 < nombre_2```, conclue qu'elle est valide, et exécute le bloc d'instruction.

#### Exemple numéro 2 ####

Maintenant, on va regarder ce qui se passe quand la condition testée dans notre ```if``` n'est pas valide. 

Essayez le code suivant :

```c
int nombre_1 = 10, nombre_2 = 20;

if(nombre_1 > nombre_2)
{
    printf("%d est superieur a %d\n\n", nombre_1, nombre_2);
}
```

Aucune surprise, puisque *nombre_1* est inférieur à *nombre_2*. La condition est fausse et le bloc d'instruction du ```if``` n'est pas exécuté.

### L'instruction else ###

Avec notre instruction ```if```, on sait exécuter un bloc d'instruction quand une condition est remplie. Mais c'est tout. Si l'on veut exécuter un bloc d'instruction alternatif dans le cas où la condition ne serait pas remplie, on doit rajouter une autre instruction ```if``` à la suite. 

```c
if (a > 5)
{
    /* du code */
}

if (a <= 5)
{
    /* code alternatif */
}
```

Le seul problème, c'est qu'on doit rajouter un ```if``` et évaluer une nouvelle condition. Ce n'est pas très efficace et assez long à taper. Pour limiter les dégâts, le C fournit une autre instruction : l'instruction ```else```, qui signifie "sinon". Celle-ci se place immédiatement après le bloc d'instruction d'un ```if```. Elle permet d’exécuter un bloc d'instruction alternatif si la condition testée dans le ```if``` n'est pas remplie. Sa syntaxe est la suivante :

```c
if(/*Expression logique*/)
{
    /*Une ou plusieurs instructions*/
}

else
{
    /*Une ou plusieurs instructions*/
}
```

Et elle doit être comprise comme ceci :

![](http://uploads.siteduzero.com/files/391001_392000/391455.png)

L'instruction ```else``` ne possède aucune parenthèse, pensez-y lorsque vous programmez.

#### Exemple ####

Passons maintenant à la pratique : les exemples, il n'y a que cela de vrai. Supposons que je veuille créer un programme très simple, auquel on fourni une heure, et qui indique si il fait nuit ou jour à cette heure-ci. On suppose qu'il fait jour de 9 heures à 20 heures, et qu'il fait nuit sinon. J'obtiendrais ce résultat :

```c
int main(void)
{
    int heure;
    scanf("%d", &heure);

    if(heure > 8 && heure < 20)
    {
        printf("Il fait jour.\n");
    }
    else
    {
        printf("Il fait nuit.\n");
    }

    return 0;
}
```

### If / else if ###

Nos instructions ```if``` et ```else``` sont très utiles. Et lorsqu'on les utilise, il arrive parfois que l'on imbrique plusieurs instructions ```if``` ou ```else``` les unes dans les autres. Ainsi, de tels codes sont possibles :

```c
if (condition)
{
    /* du code */
}

else
{
    /* plusieurs instructions */

    if (autre condition)
    {
        /* du code */
    }
}
```

Ces codes sont assez longs à écrire, et de telles imbrications sont assez difficiles à lire quand beaucoup de ```if``` et de ```else``` sont imbriqués. Pour éviter ces inconvénients, on a inventé une instruction qui permet de simplifier l'écriture de certaines de ces imbrications. Il s'agit de l'instruction ```else if```. Les imbrications simplifiables avec un ```else if``` sont celles qui s'écrivent comme ceci : 

```c
if(/*Expression logique*/)
{
    /*Une ou plusieurs instructions*/
}

else 
{
    if(/*Expression logique*/)
    {
        /*Une ou plusieurs instructions*/
    }
}
```

Faites bien attention : le bloc d'instruction du ```else``` doit contenir un ```if```, éventuellement avec un ```else```, mais rien d'autre. Celles-ci peuvent alors être simplifiées comme suit :

```c
if(/*Expression logique*/)
{
    /*Une ou plusieurs instructions*/
}

else if(/*Expression logique*/)
{
    /*Une ou plusieurs instructions*/
}
```

Tout se passe comme si on avait enlevé les accolades du ```else```. De cette description, on peut facilement déduire qu'une instruction ```else if``` suit toujours un ```if``` ou un autre ```else if```.  Notre instruction ```else if``` va s’exécuter si le bloc d'instruction placé juste au-dessus de lui ne s’exécute pas. Si c'est le cas, il testera sa condition, et s'exécutera si celle-si est valide.

Petite remarque : si on place une instruction ```if``` suivie de plusieurs ```else if``` (le tout éventuellement terminé par un ```else``` final), un seul bloc d'instruction sera exécuté : celui pour lequel la condition testée est vraie. Notre ordinateur va ainsi tester les conditions du ```if``` et des différents ```else if```, jusqu'à tomber sur la bonne, et exécuter le bloc d'instruction qui correspond. Voyez par exemple :

```c
int main(void)
{
    int heure = 11;

    if(heure >= 7 && heure <= 12)
    {
        printf("On est le matin !\n");
    }
    else if(heure >= 9 && heure <= 12)
    {
        printf("Le petit dejeune, c'est fini !\n");
    }
    else if(heure < 7 || heure > 12)
    {
        printf("On est soit l'aprem', soit le soir, soit la nuit.\n");
    }

    return 0;
}
```
```console
11
On est le matin !
```

#### Un petit exercice pour bien comprendre ####

Imaginez que vous ayez un score de jeu vidéo sous la main :

* Si le score est inférieur à 2000, afficher *« C'est la catastrophe »*.
* Si le score est supérieur ou égal à 2000 et que le score est inférieur à 5000, afficher *« Tu peux mieux faire »*.
* Si le score est supérieur ou égal à 5000 et que le score est inférieur à 9000, afficher *« Tu es sur la bonne voie »*.
* Sinon, afficher *« Tu es le meilleur ! »*.

À vous de codez ça. Si vous n'y arrivez pas, ce n'est pas grave, relisez simplement ce chapitre autant de fois que nécessaire. Voici la correction, regardez seulement après avoir essayé de faire l'exercice :

```c
int main(void)
{
    int score;

    printf("Quel est le score du joueur : ");
    scanf("%d", &score);

    if(score < 2000)
    {
        printf("C'est la catastrophe\n");
    }

    else if(score >= 2000 && score < 5000)
    {
        printf("Tu peux mieux faire \n");
    }

    else if(score >= 5000 && score < 9000)
    {
        printf("Tu es sur la bonne voie\n");
    }

    else
    {
        printf("Tu es le meilleur !\n");
    }

    return 0;
}
```

### L'instruction switch
L'instruction ```switch``` permet de comparer successivement une variable à une ou plusieurs valeurs (ou comparants). Si la variable concorde avec telle ou telle valeur, on exécute la ou les instructions qui suivent. Cette instruction se présente sous la forme suivante :

```c
switch(/* variable */)
{
    case /* comparant_1 */ :
        /* Instructions */
        break;

    case /* comparant_2 */ :
        /* Instructions */
        break;

    /* Etc... */

    default: /* Si aucune comparaison n'est juste */
        /* Instruction(s) à exécuter dans ce cas */
        break;
}
```

Ce qu'il faut retenir, c'est que ```switch``` compare une variable à une liste de comparants. Chaque comparant est défini à l'aide d'un ```case```. Si la comparaison est vraie, alors le ```switch``` exécute toutes les instructions jusqu'au prochain ```break``` (ce mot-clef permet de mettre fin à une itération, nous verrons cela plus en détail dans le prochain chapitre). Si aucune comparaison n'est bonne, alors ce sont les instructions associées au ```default``` qui seront exécutées. Voici un exemple dans lequel on compare la variable *note* à 0, 1, 2, 3, 4 et 5 :

```c
int main(void)
{
    int note;

    printf("Quelle note as-tu obtenu : ");
    scanf("%d", &note);

    switch(note)
    {
        /* si note == 0 */
        case 0:
            puts("No comment.");
            break;

        /* si note == 1 */
        case 1:
            puts("Cela te fait 4/20, c'est accablant.");
            break;

        /* si note == 2 */   
        case 2:
            puts("On se rapproche de la moyenne, mais ce n'est pas encore ca.");
            break;

        /* si note == 3 */
        case 3:
            puts("Tu passes.");
            break;

        /* si note == 4*/
        case 4:
            puts("Bon travail, continue ainsi !");
            break;

        /* si note == 5 */
        case 5:
            puts("Excellent !");
            break;

        /* si note est différente de 0, 1, 2, 3, 4 et 5 */
        default:
            puts("Euh... tu possedes une note improbable.");
            puts("Vivement le prochain chapitre qui permettra de demander a l'utilisateur de refaire son choix !");
            break;
    }

    return 0;
}
```

Comme dit précédemment, si la condition est vraie, le ```switch``` exécute toutes les instructions jusqu'au prochain ```break```. Cela permet de faire des combinaisons comme celle-ci : 

```c
int main(void)
{
    int note;

    printf("Quelle note as-tu obtenu : ");
    scanf("%d", &note);

    switch(note)
    {
        /* si la note est comprise entre 0 et 4 inclus */
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
            printf("Tu n'as pas la moyenne.\n");
            break;

        /* si au contraire la note est égale ou supérieure à 5 */

        case 5:
        case 6:
        case 7:
        case 8:
        case 9:
        case 10:
            printf("Tu as la moyenne.\n");
            break;

        default:
            printf("Erreur : note impossible\n");
            break;
    }

    return 0;
}
```

### L'opérateur ternaire
L'opérateur ternaire, qui est une autre façon de faire un test de condition, tient son nom du fait qu'il est le seul à avoir trois opérandes. En effet, il se compose comme suit :

```console
(condition) ? instruction si vrai : instruction si faux
```

Les parenthèses ne sont pas obligatoires. Ce qu'il y a à retenir, c'est qu'il se comporte comme un ```if / else```, tout en étant plus condensé et plus rapide à écrire. Voyez par vous-mêmes :

```c
#include <stdio.h>

int main(void)
{
    int heure;

    scanf("%d", &heure);

    (heure > 8 && heure < 20) ? printf("Il fait jour.") : printf("Il fait nuit.");

    return 0;
}
```

Il est également possible de l'écrire sur plusieurs lignes, même si cette pratique est moins courante :

```c
(heure > 8 && heure < 20) ?
    printf("Il fait jour.")
    : printf("Il fait nuit.");
```

Les ternaires peuvent sembler inutiles, surtout que s'ils sont mal employés ils rendent un programme moins lisible. Cependant, l'exercice suivant va vous prouvez que quand on les emploie bien, ce sont de bons alliés.

### Exercice ###

Pour bien comprendre cette nouvelle notion, nous allons faire un petit exercice. Imaginez qu'on veuille faire un mini jeu vidéo dans lequel on affiche le nombre de coups du joueur. Seulement voilà, vous êtes maniaques du français et vous ne supportez pas qu'il y ait un ```'s'``` en trop ou en moins. Essayez de coder un programme dans lequel on demande à l'utilisateur le nombre de coups puis on affiche le résultat.

Fini ? Voici la correction :

```c
#include <stdio.h>

int main(void)
{
    int nb_coups;

    printf("Donnez le nombre de coups : ");
    scanf("%d", &nb_coups);

    printf("\nVous gagnez en %d coup%c", nb_coups, nb_coups > 1 ? 's' : ' ');
    return 0;
}
```

Ce programme utilise les ternaires pour condenser l'expression et aller plus vite dans l'écriture du code. Sans les ternaires il aurait fallu faire quelque chose comme :

```c
#include <stdio.h>

int main(void)
{
    int nb_coups;

    printf("Donnez le nombre de coups : ");
    scanf("%d", &nb_coups);

    printf("\nVous gagnez en %d coup", nb_coups);

    if (nb_coups > 1)
        putchar('s');
    else
        putchar(' ');

    return 0;
}
```

Ce chapitre a été important, il vous a permis de comprendre les conditions en C : les booléens,  ```if```, ```else```, ```else if```, le ```switch``` et les ternaires. Il vous a aussi appris les opérateurs de comparaisons et les opérateurs logiques qui vous seront très utiles dans le prochain chapitre donc si vous n'avez pas très bien compris ou que vous n'avez pas tout retenu, je vous conseille de relire ce chapitre.

Le chapitre suivant traitera des boucles, un moyen simple de refaire une action plusieurs fois.

## Les boucles
Ce chapitre est la suite du précédent puisque nous allons aborder ici les **boucles**. Une boucle est un moyen de répéter des instructions selon une condition. Ces structures, dîtes **itératives**, que nous allons voir dans ce chapitre sont les suivantes :

| Nom de la structure de contrôle | Ce qu'elle fait                          |
| ------------------------------- | ---------------------------------------- |
| Boucle ***While...Do***         | répète une suite d'instructions tant qu'une condition est respectée. |
| Boucle ***Do...While***         | répète une suite d'instructions tant qu'une condition est respectée. La différence, c'est que la boucle ***Do...While*** exécute au moins une fois cette suite d'instructions. |
| Boucle ***For***                | répète un nombre fixé de fois une suite d'instructions. |

### La boucle while
La première des boucles que nous allons étudier est la boucle ```while``` (qui signifie "tant que"). Celle-ci permet de répéter un bloc d'instruction tant qu'une condition est remplie.


![](http://uploads.siteduzero.com/files/391001_392000/391427.png)


### Syntaxe ###

La syntaxe de notre boucle ```while``` est assez simple, comme vous pouvez en juger :

```c
while (/* expression booleenne */)
{
    /* bloc d'instruction à répéter */ 
}
```

#### Exemple ####

Je vous propose un petit exemple complètement inutile qui va illustrer tout ça :

```c
int i = 0;

while (i < 5)
{
    printf("La variable i vaut %d\n", i);
    i++;
}
```

Dans cet exemple, on utilise une variable nommée *i*, mais on aurait très bien pu l’appeler *compteur*. Cependant, les programmeurs sont faignants, c'est pourquoi ils appellent généralement leurs variables *i* lorsqu'elles sont couplées avec les boucles (cela s'apparente presque à une convention de nommage). Mais pourquoi *i* en particulier ? Nous verrons cela quelques chapitres plus loin. En attendant, voici ce que ce code affiche à l'écran :

```console
La variable i vaut 0
La variable i vaut 1
La variable i vaut 2
La variable i vaut 3
La variable i vaut 4
```

Le fonctionnement est simple à comprendre : 

* Au tout départ, notre variable *i* vaut 0. Étant donné que 0 est bien inférieur à 5, la condition est vraie, donc on rentre dans la boucle.
* On affiche la valeur de *i*.
* On incrémente *i*, qui vaut maintenant 1.
* On recommence la boucle.

Ces étapes vont ainsi se répéter pour 1, 2, 3 et 4. Quand la variable *i* vaudra 5, la condition sera fausse, et le ```while``` ne sera alors pas exécuté. 

### Boucles infinies ###

Le point vital dans les boucles, c'est **qu'elles puissent se terminer** : si elles n'ont pas de quoi s'arrêter, elles s'exécuteront à l'infini ! Soyez donc très vigilants ! Par exemple, observez le code suivant :

```c
unsigned int i = 0;

/* Ce qui équivaut à while(1) <--> Toujours vrai */
while(i >= 0)
{
    printf("La variable i vaut %d\n", i);
}
```

Affiche dans la console sans jamais s'arrêter :

```console
La variable i vaut 0
La variable i vaut 0
La variable i vaut 0
...
```

Le code continuera jusqu'à ce que l'utilisateur arrête le programme. C'est ce qu'on appelle une **boucle infinie**. Les boucles infinies peuvent être utiles s'il y a une condition d'arrêt (une touche sur laquelle on appuie, un numéro à rentrer, etc) ; c'est d'ailleurs sur ce principe que fonctionnent de nombreux programmes comme les jeux vidéos : tant que l'utilisateur ne demande pas de quitter, on reste dans la boucle qui contient toutes les instructions du jeu.

### Exercice ###

Pour bien faire rentrer ce qu'on a vu plus haut, rien ne vaut un petit exercice. On va vous demander de créer un morceau de code qui vérifie si un nombre est premier, et affiche le résultat à l'écran. Ce nombre, ce sera une variable nommée *number*, qui aura été déclarée précédemment dans notre code, mais vous pouvez aussi la saisir au clavier avec un scanf. Bref, peu importe.

Nous allons vous donner quelques détails. Tout d'abord, on sait qu'un nombre x n'est pas divisible par un nombre y si ```x % y``` est différent de zéro. Ensuite, vous allez devoir utiliser une boucle ```while```, et quelques structures de contrôles annexes. Et enfin, pour rappel, un nombre premier est divisible uniquement par 1 et par lui-même. Et maintenant, à vos claviers ! 

Ça y est, vous avez fini ? Alors votre code doit sûrement ressembler à quelque chose dans le genre : 

[secret]{
```c
#include <stdio.h>

int main(void)
{
    int nombre, i = 2;

    puts("nombre = ");
    scanf("%d", &nombre);

    while ((i < nombre) && (nombre % i != 0))
    {
        ++i;
    }

    if (i == nombre)
    {
        puts("nombre est premier");
    }

    else
    {
        puts("nombre n'est pas premier");
    }

    return 0;
}
```
}

Les plus malins qui ont un bon niveau en mathématique savent déjà qu'il y a moyen de faire mieux que ce code naïf. On peut en effet utiliser de nombreux théorèmes et diverses astuces pour savoir si un nombre est premier. La correction présentée au-dessus va en effet prendre beaucoup de temps à vérifier qu'un nombre est premier et fait beaucoup de calculs inutiles. Par exemple, on n'est pas obligé de vérifier si le nombre* est divisible par des nombres supérieurs à sa racine carrée.

### La boucle do-while
La deuxième boucle que nous allons voir est similaire à la première : il s'agit de la boucle ```do while```. 

### Fonctionnement ###

Notre boucle ```do while``` fonctionne comme la boucle ```while```, à un petit détail prêt : une boucle ```do while``` s'exécutera toujours au moins une fois, alors qu'une boucle ```while``` peut ne pas s'exécuter.


![](http://uploads.siteduzero.com/files/391001_392000/391425.png)


### Syntaxe ###

En terme d'écriture, la première différence avec ```while``` est qu'ici le test de la condition se fait à la fin de la boucle et non au début. La deuxième chose notable est la présence d'un point-virgule tout à la fin. Il est obligatoire de le mettre, sinon la compilation échouera. 

#### Exemple ####

Voici le même code que pour la boucle ```while```, mais écrit avec une boucle ```do while``` :

```c
int i = 0;

do
{
    printf("La variable i vaut %d\n", i);
    ++i;

} while (i < 5);
```

Cet exemple affiche la même chose que le code utilisé comme exemple pour la boucle ```while``` :

```console
La variable i vaut 0
La variable i vaut 1
La variable i vaut 2
La variable i vaut 3
La variable i vaut 4
```

#### Autre exemple ####

Comme je l'ai dit plus haut, notre boucle ```do while``` s'éxecute au moins une fois. Pour vous le prouver, voici un exemple :

```c
int main(void)
{    
    do
    {
        puts("Boucle do-while");
    } while (0);

    return 0;
}
```

Et ce code affiche pourtant ceci à l'écran :

```console
Boucle do-while
```

Pourquoi ? Vous vous souvenez du chapitre précédant on nous avions vu les booléens ? On avait dit que 0 signifiait faux. Ainsi, le ```while``` ne s'exécute pas puisque la condition est fausse, alors que le ```do while``` s'exécute puisqu’il affiche bien *« Boucle do-while »*, alors que la condition est là encore fausse. Ce code prouve bien qu'une boucle ```do while``` s'exécute toujours au moins une fois.

### La boucle for
La troisième et dernière boucle que nous allons voir est la boucle ```for```. Celle-ci permet de répéter une suite d'instruction un certain nombre de fois, ce nombre de fois étant fixé par un ou plusieurs compteurs.

### Fonctionnement ###

Une boucle ```for``` se décompose en trois parties. 

* L'**initialisation** du compteur : on prépare le compteur en l'initialisant à la valeur que l'on veut (le plus souvent c'est 0).
* La **condition** : comme pour les deux autres boucles, il faut une condition. Tant qu'elle est vraie, la boucle s'exécute ; elle se stoppe dès qu'elle devient fausse.
* La **modification** du compteur : cette étape modifie le compteur. Même s'il s'agit le plus souvent d'une incrémentation, on peut utiliser toutes les opérations que l'on veut.

Petit détail : l'initialisation se fait une seule fois, avant de rentrer dans la boucle, et non à chaque tour de boucle. Par contre, la modification du compteur et le test de la condition ont lieu à chaque tour de boucle.

Une boucle ```for``` peut être vue comme une sorte de spécialisation d'une boucle ```while```. En fait, une boucle ```for``` est strictement équivalente à ce code :

```console
Initialisation du compteur ;

while ( condition ou expression booléenne )
{
    Instructions de la boucle ;

    Modification du compteur ;
}
```

#### Syntaxe ####

La syntaxe de cette boucle est assez différente des deux autres, mais elle n'en est pas moins utile. Pour utiliser une telle boucle, on doit procéder comme ceci :

```console
for (initialisation du compteur ; condition ; modification du compteur)
{
    Instructions;
}
```

Attention à bien déclarer le compteur avant la boucle, en C89 il est interdit d'écrire quelque chose comme `for(int i =0; i <9; i++)`. Vous pourrez le faire à partir du C99.

#### Exemple ####

Je pense qu'un exemple vous aidera à bien saisir tout ça :

```c
int variable;

for (variable = 0 ; variable < 10 ; variable++)
{
     printf("variable vaut %d\n", variable);
}
```

Ce code affichera en sortie :

```console
variable vaut 0
variable vaut 1
variable vaut 2
variable vaut 3
variable vaut 4
variable vaut 5
variable vaut 6
variable vaut 7
variable vaut 8
variable vaut 9
```

Amusez-vous à changer l'initialisation, la condition ou la modification du compteur pour voir les changements. Il est essentiel de bien comprendre cette boucle qui est moins évidente que les deux autres, cependant très utilisée ; nous verrons mieux son intérêt et son utilité quand nous avancerons dans le cours.

#### Exercice ####

Nous allons nous entraîner avec quelque chose de vraiment basique. Nous allons calculer la somme de tous les nombres compris entre 1 et N. En clair, si je vous donne un nombre N, vous allez devoir calculer $1 + 2 + 3 + ... + (N-2) + (N-1) + N$ . Bien sûr, vous allez devoir utiliser une boucle.

A vos claviers ! Si c'est fini, voici la correction : 

[secret]{
```c
#include <stdio.h>

int main (void)
{
    const unsigned int n = 250;
    unsigned int somme = 0;
    unsigned int i;

    for (i = 1; i <= n; ++i)
    {
        somme += i;
    }

    printf ("%d\n", somme);
    return 0;
}
```
}

Comme quoi, rien de bien compliqué. Une petit remarque cependant : ceux qui s’intéressent un peu aux mathématiques ont surement résolu cet exercice sans boucle. En effet, il faut savoir que cette somme peut se calculer plus facilement : elle vaut exactement $\frac {N \times (N+1)} {2}$.

### Utilisation avancée ###

Les boucles ```for``` ne vous ont pas encore livré tous leurs secrets. Comme quoi, on en apprend toujours plus sur le C, même quand on pense déjà bien le connaître.

#### Plusieurs compteurs ####

Le nombre de compteurs ou de conditions n'est pas limité, comme le prouve le code suivant.

```c
for (i = 0, j = 2 ; i < 10 && j < 12; i++, j += 2)
```

Ici, on définit deux compteurs *i* et *j* initialisés respectivement à 0 et 2. On exécute le contenu de la boucle tant que *i* est inférieur à 10 et que *j* est inférieur à 12, et on augmente *i* de 1 et *j* de 2 à chaque tour de boucle. Le code est encore assez lisible, cependant la modération est de mise, un trop grand nombre de paramètres rendant le ```for``` illisible.

#### Boucles imbriquées ####

Petite précision : il est possible d'**imbriquer** les boucles. Cela consiste simplement à mettre une ou plusieurs boucles dans une autre, comme ceci : 

```c
for (i = 0 ; i < 1000 ; ++i)
{
    for (j = i ; j < 1000 ; ++j)
    {
          /*  code  */
    }
}
```

Et cela marche aussi avec des boucles ```while```, ```do while```, etc. On peut ainsi imbriquer une boucle ```while``` dans une boucle ```do while```, imbriquer une boucle ```while``` dans une boucle ```for```, et j'en passe.

Cela peut servir. Pour donner un exemple, imaginons que je veuille savoir quelles sont les additions de deux nombres entiers dont la somme vaut 1000. En clair, je veux savoir quelles sont les valeurs possibles de a et de b tels que a + b = 1000. Pour cela, je peux résoudre le problème de manière naïve et utiliser deux boucles imbriquées pour tester toutes les possibilités.

```c
for (i = 0 ; i <= 1000 ; ++i)
{
    for (j = i ; j <= 1000 ; ++j)
    {
        if (i+j == 1000) 
        {
            printf ("%d + %d = 1000 \n", i, j);
        }
    }
}
```

### Branchements inconditionnels
Dans ce chapitre, ainsi que dans le chapitre précédent, on a vu comment modifier l’exécution de notre programme en fonction de certaines conditions. Ainsi, notre programme peut faire autre chose que mécaniquement passer à l'instruction suivante et peut recommencer son exécution à un autre endroit, suivant qu'une condition soit réalisée ou pas. Pour ce faire, on utilise des structures de contrôles. Au niveau de notre processeur, ces structures de contrôle sont fabriquées avec ce qu'on appelle des instructions de branchement conditionnelles : ce sont des instructions qui vont faire reprendre notre programme à un autre endroit si une condition est vraie, et qui ne font rien sinon. Ceux qui veulent savoir comment on utilise ces branchements pour fabriquer ces structures de contrôles peuvent aller lire le début de ce tutoriel (les trois premières sous-parties) : [Structures de contrôle en assembleur](http://www.siteduzero.com/tutoriel-3-563628-un-peu-de-programmation.html).

Mais la plupart du temps, notre ordinateur supporte aussi des instructions de branchement inconditionnels. Ces instructions vont faire reprendre l’exécution de notre programme à un endroit bien précis, quelle que soit la situation. Celles-ci n'agissent pas suivant ce que leur dit une condition, mais vont toujours faire reprendre notre programme à un endroit bien précis. Alors certes, il s'agit d'instructions de notre processeur, qui sont souvent inaccessibles en C. Mais le langage C fournit quelques fonctionnalités qui fonctionnent exactement comme des branchements inconditionnels. Ils sont souvent utilisés de concert avec nos structures de contrôle, pour les améliorer, ou pour qu'elles fassent ce qu'il faut. 

Il existe ainsi trois grands branchements inconditionnels en C :
​	
* celui qui permet de passer au tour de boucle suivant, sans finir celui en cours : ```continue``` ;
  * celui qui permet (entre autres) de quitter la boucle en cours : ```break``` ;
* celui qui permet de sauter carrément dans un autre morceau de code ```goto```.

Voyons un peu plus en détail ces branchements inconditionnels.

### break ###

Nous avons déjà étudié le rôle de ```break``` au sein de l'instruction ```switch``` : il permettait simplement de quitter notre ```switch``` pour reprendre immédiatement après. Eh bien, sachez qu'on peut aussi l'utiliser avec des boucles. Son but ? Permettre de quitter une boucle (ou un ```switch```, comme on l'a déjà vu), pour reprendre immédiatement après. 

#### Boucle ou structure de contrôle simple ####

Pour illustrer ça, prenons un algorithme tout simple :

```console
Pour (i = 0 ; i < 10 ; i++)
{
     Si i == 5
        Quitter la boucle;

     Sinon afficher i;
}
```

Notre but est de quitter si jamais la variable *i* atteint la valeur 5. Alors pour vous entrainer, essayez de coder vous-même la boucle sans regarder la solution.

[secret]{
```c
int i;

for (i = 0 ; i < 10 ; i++)
{
    if (i == 5)
        break;

    printf("i = %d\n", i);
}
```

Et voici le résultat à l'exécution :

```console
i = 0
i = 1
i = 2
i = 3
i = 4
```

L'exécution de la boucle a bien été arrêtée par ```break```. 
}

#### Structures de contrôle imbriquées ####

Il est important de préciser que ```break``` ne permet de sortir que d'une seule boucle (ou d'une seule structure de contrôle de type ```if```, ```else if```, etc.). Ainsi, dans le cas de boucles imbriquées, on reviendra à la précédente.

```c
#include <stdio.h>

int main(void)
{
    int i;

    for (i = 0; i < 10; i++)
    {
        printf("[for] i = %d\n", i);

        while (i < 5)
        {
            if (i == 4)
                break;

            printf("[while] i = %d\n", i);
            i++;
        }
    }

    return 0;
}
```
```console
[for] i = 0
[while] i = 0
[while] i = 1
[while] i = 2
[while] i = 3
[for] i = 5
[for] i = 6
[for] i = 7
[for] i = 8
[for] i = 9
```

Dans ce code, il y a une boucle ```for``` qui contient une boucle ```while```. Au départ, *i* vaut 0, et ainsi la condition est vraie et on rentre dans la boucle. On affiche la variable, et dès que *i* vaut 4, on quitte la boucle. Comme la condition du ```while``` est fausse, on ne rentre plus dedans, mais la boucle ```for``` continue de s'exécuter, et affiche les cinq valeurs suivantes de *i*. 

### continue ###

Le deuxième mot-clef est ```continue```. Son rôle est d'arrêter l'itération en cours et de passer à la suivante. En gros, on peut dire que ```continue``` permet de terminer le tour de boucle en cours, et fait reprendre immédiatement au tour de boucle suivant. Prenons le même code algorithme que précédemment : 

```console
Pour (i = 0 ; i < 10 ; i++)
{
     Si i == 5
        continue;

     Sinon afficher i;
}
```

Qui est capable me dire ce que le code une fois traduit en C affichera ? 

[secret]{
```console
i = 0
i = 1
i = 2
i = 3
i = 4
i = 6
i = 7
i = 8
i = 9
```
}

On remarque que quand *i* a été mis à 5, la condition ```if (i == 5)``` est devenue vraie et ```continue``` a zappé l'itération en cours.

### goto ####

Le troisième et dernier mot-clef que je souhaite vous présenter est ```goto```. Ce mot-clef sert à sauter vers une autre partie du code. Il permet de reprendre l’exécution du programme à l'endroit qu'on veut. 

Pour préciser l'endroit où l'on veut reprendre notre programme, le langage C fournit ce qu'on appelle des **labels**. Ces labels permettent de nommer une ligne de code, une instruction particulière, en lui donnant un nom. Pour identifier la ligne de code à laquelle on souhaite faire reprendre notre programme, il suffit ainsi d'ajouter un label à notre ligne de code, en rajoutant le nom du label suivi d'un caractère : devant notre instruction. Pour reprendre l’exécution du programme à une ligne de code bien précise, il suffit d'utiliser le mot-clé ```goto```, suivi du nom du label de la ligne de code correspondante.

#### Exemple ####

Voici un algorithme tout simple :

```console
Pour (i = 0 ; i < 10 ; i++)
{
     Si i == 5
        Sautez à l'étiquette Erreur;

     Sinon afficher i;
}

Erreur:
     Afficher que i vaut 5
```

Dans notre exemple, le label n'est autre que *erreur*. Ce label est défini plus bas dans le code : il est attaché à notre instruction qui affichera à l'écran que la variable vaut 5. Essayez de transposer cet algorithme en C.

[secret]{
```c
int i;

for (i = 0 ; i < 10 ; i++)
{
     if (i == 5)
         goto Erreur;

     printf("i = %d\n", i);
}

Erreur:
     puts("\ni vaut 5");
```

Et voici le résultat à l'exécution :

```console
i = 0
i = 1
i = 2
i = 3
i = 4

i vaut 5
```
}

On voit bien que quand *i* atteint la valeur 5, le programme saute au label *Erreur* et affiche bien *i vaut 5*. Le label est ici après ```goto```, mais peut très bien se trouver avant.

#### Goto Statement Considered Harmful ####

Il me faut cependant vous prévenir : de nos jours, il est tout de même assez rare qu'on utilise des ```goto```, et certains langages de programmation ne permettent même pas de l'utiliser !

Pourquoi ? Eh bien en fait, il faut savoir qu'autrefois, ```goto``` était assez relativement utilisé par les programmeurs. Quand je dis autrefois, c'était avant les années 1960-1970. Nul doute que vous n'étiez pas encore nés à cette époque. À cette époque, on n'utilisait pas vraiment de structures de contrôles, et les programmeurs créaient des programmes en utilisant pas mal de ```goto``` pour compenser. Mais cet usage du ```goto``` a fini par être de plus en plus critiqué au fil du temps.

Première attaque contre le ```goto``` : en 1966, deux mathématiciens, Böhm et Jacopini, prouvèrent que l'on pouvait se passer totalement de ```goto``` en utilisant des structures de contrôle. La déchéance de ```goto``` était en marche. 

Dans notre exemple vu plus haut, ```goto``` est effectivement superflu et peux facilement être remplacé par autre chose.

```c
int i;

/* code plus court et plus lisible */
for (i = 0 ; i < 10 ; i++)
{
     if (i == 5)
     {
         puts("i vaut 5");
         break;
     }

     printf("i = %d\n", i);
}
```

Mais certains programmeurs continuèrent d'utiliser du ```goto```, en disant que c'était plus facile de programmer ainsi. Alors vint le coup de grâce final ! En mars 1968, un informaticien du nom d'*Edsger Dijkstra* écrivit un article qui fit sensation. Cet article portait le nom suivant : *Goto Statement Considered Harmful*. Dans cet article, Dijkstra porta de nombreuses critiques sur le ```goto```, et préconisait de remplacer celui-ci par une utilisation judicieuse des structures de contrôles qu'on vient de voir dans ce chapitre et dans le chapitre précédent. Cet article lança un véritable débat dans les milieux académiques ainsi que parmi les programmeurs. Au final : ```goto``` perdit la bataille, l'usage des structures de contrôle usuelles se répandit dans le monde comme une trainée de poudre.

Le principal reproche qui est fait à ce pauvre ```goto``` est qu'il a tendance à rendre le code illisible. En comparaison, un code dans lequel on trouve des structures de contrôle est beaucoup plus compréhensible par un humain. C'est pour ce genre de raisons que l'usage de ```goto``` en C est très fortement déconseillé, en particulier pour les débutants.

Je vous parle de ```goto``` par souci d'exhaustivité, mais sachez qu'il est aujourd'hui rarement utilisé. L'un des très rares cas dans lesquels ce mot-clef prend son intérêt, c'est la gestion des erreurs. Cependant, nous ne verrons pas ce cas dans ce tutoriel. En attendant de découvrir comment bien utiliser ```goto```, je vous recommande de ne pas l'utiliser.

### Exercices
On ne le répète jamais assez, **pratiquez** ! Voici donc quelques exercices permettant de s'entraîner et de s'améliorer.

### Calcul du PGCD de deux nombres ###

Commençons par une curiosité mathématique très prisée en programmation. Nous allons programmer un des premiers algorithmes qui aie été inventé à l'époque de l'Antiquité. On pourrait croire qu'il est tout de même assez récent et date des débuts de l'informatique. Mais ce n'est pas le cas : il a été inventé par Euclide, mathématicien de la Grèce antique, qui est considéré comme le créateur de la géométrie. 

#### Énoncé ####

Mais cet algorithme n'est pas vraiment un algorithme géométrique. Cet algorithme effectue un traitement simple : il calcule le PGCD de deux nombres. Pour rappel, le PGCD de deux nombres a et b, n'est rien d'autre que le plus grand nombre qui peut diviser à la fois a et b.

Cet algorithme est très simple. On suppose que *a* est supérieur à *b*. On commence par affecter la valeur de *b* à *a*, ensuite, puis on attribue la valeur de *r* à *b* (le reste). Ensuite on calcule *r* de la division euclidienne (d'entiers) de *a* par *b* ; et on recommence toutes ces étapes jusqu'à ce que le reste soit nul. On a alors trouvé le résultat : c'est le *b* qui a été obtenu à la fin de ce processus.

Avec cette explication, vous avez tout ce qu'il vous faut : à vos claviers !

#### Correction ####

Cette correction est disponible [ici](http://paste.awesom.eu/informaticienzero/1hK&ln).

### Une overdose de lapins ###

C'est mignon un lapin, vous ne trouvez pas ? Si vous avez répondu oui, alors vous allez être ravi par cet exercice.

#### Énoncé ####

Au 13ème siècle, un mathématicien italien du nom de *Leonardo Fibonacci* posa un petit problème dans un de ses livres, qui mettait en scène des lapins. Ce petit problème mis en avant une suite de nombre particulière, nommée la [suite de Fibonnaci](http://fr.wikipedia.org/wiki/Suite_de_Fibonacci), nommée du nom de son inventeur. Il fit les hypothèses suivantes.
​	
* Le premier mois, on place un couple de deux lapins dans l'enclos.
  * Les lapins se reproduisent tous les deux mois.
  * Dès qu'il le peut, tout couple de lapins capable d'avoir des enfants donne naissance à deux lapereaux, et donc à un nouveau couple.
* Et enfin, pour éviter tout problème avec la SPA, les lapins ne meurent jamais.

Le problème est le suivant : combien il y a-t-il de couples (de paires) de lapins dans l'enclos au n-ième mois ? Le but de cet exercice est de coder un petit programme qui fasse le calcul automatiquement, et qui affiche le résultat sur la console.

#### Indice ####

[secret]{
Le fait est que ce problème est assez simple à résoudre en remarquant un petit truc. Si on dispose de x couples de lapins au mois N, celui donnera naissance à un nouveau couple deux mois plus tard. Deux mois plus tard, on se retrouvera donc avec x nouveaux couples de lapins, venant de la reproduction des couples d'il y a deux mois, auquel il faut ajouter les lapins qui étaient déjà là le mois d'avant. Autrement dit, si je note le nombre de lapins au n-ième mois $Fn$, on a : $F_n+2 = F_n+1 + F_n$. Ce qui peut aussi s'écrire $F_n = F_n-1 + F_n-2$.

Ensuite, au mois numéro 1, on a un seul couple de lapins. $F_1 = 1$. En enfin, au mois numéro 0, on a 0 lapins : l'expérience n'a pas encore commencée : $F_0 = 0$. En sachant ça, vous pouvez aisément coder le programme demandé.
}

#### Correction ####

Et voilà, notre petit problème avec les lapins est [résolu](http://paste.awesom.eu/informaticienzero/vRe&ln). Sympathique, non ? 

### Des pieds et des mains pour convertir mille miles ###

Si vous avez déjà voyagé en Grande-Bretagne ou aux États-unis, vous savez que les unités de mesure utilisées dans ces pays sont différentes des nôtres. Au lieu de notre cher système métrique, dont les stars sont les centimètres, mètres et kilomètres, nos amis outre-manche et outre-atlantique utilisent le système impérial, avec ses pouces, pieds et *miles*, voire lieues et *furlongs* ! Et pour empirer les choses, la conversion n'est pas toujours simple à effectuer de tête ... Aussi, la lecture d'un ouvrage tel que *Le Seigneur des Anneaux*, dans lequel toutes les distances sont exprimées en unités impériales, peut se révéler pénible.

#### Votre mission ####

Grâce au langage C, nous allons aujourd'hui résoudre tous ces problèmes ! Votre mission, si vous l'acceptez, sera en effet d'écrire un programme affichant un tableau de conversion entre miles et kilomètres. Le programme ne demande rien à l'utilisateur, mais doit afficher quelque chose comme ceci :

```console
Km    Miles
5     8
10    16
15    24
20    32
25    40
30    48
```

Autrement dit, le programme compte les kilomètres de 5 en 5 jusqu'à 30, et affiche à chaque fois la valeur correspondante en *miles*. Un *mile* vaut exactement 1.609 344 km, cependant, nous allons utiliser une valeur approchée : nous prendrons huit-cinquièmes de kilomètre (soit 1.6km). Autrement dit, $1$ km $= \frac{8}{5}$ miles.

Bon courage et bonne chance !

#### Un indice ? ####

[secret]{
Ne lisez cette section que si vous avez déjà cherché par vous-mêmes, mais que malgré vos efforts, vous êtes dans une impasse.

Que doit faire notre programme ? Tout d'abord, nous devons afficher la première ligne, qui dit « Km - Miles ». Ceci ne comporte pas de difficulté. Ensuite, nous devons compter jusqu'à 30 de 5 en 5, et afficher la conversion en miles à chaque fois. Pour compter, il nous faudra utiliser une variable, qui prendra les valeurs successives du kilométrage. Nous compterons tant que la variable n'aura pas atteint 30 ; à chaque étape, nous afficherons la conversion et ajouterons 5.
}

#### Correction ! ####

Si vous avez lu l'indice, vous devriez normalement y arriver en reprenant les chapitres appropriés du cours. Voici un [exemple de code possible](http://paste.awesom.eu/informaticienzero/Jfh&ln).

Pour aller plus loin, vous pouvez vous amuser à faire la conversion inverse (miles vers km) ou à faire un affichage plus joli. Si vous vous sentez d'attaque, vous pouvez même demander les bornes et le pas à l'utilisateur. Pour parfaire le tout, vous pouvez même intégrer plusieurs unités différentes et demander à l'utilisateur laquelle il souhaite convertir !

### Puissances de trois ###

Passons à un exercice un peu plus difficile, du domaine des mathématiques. Essayez de le faire même si vous n'aimez pas les mathématiques. 

#### Consignes ####

Vous devez vérifier si un nombre est une puissance de trois, et afficher le résultat. De plus, si c'est le cas, vous devez afficher l'exposant qui va avec. Le nombre en question est stocké dans une variable de type ```int```. Celle-ci a été déclarée avant dans votre code, et peut venir d'une entrée, ou être stockée quelque part, bref. 

À vos marques... Prêts ? Codez ! 

#### Un indice ? ####

Comment savoir si un nombre est une puissance de trois ? Si vous êtes perdu dans cet exercice pas si facile, lisez les lignes suivantes.

[secret]{
Pour savoir si un nombre est une puissance de trois, vous pouvez utiliser le modulo. Attention cependant : si le reste vaut 0, le nombre n'est pas forcément une puissance de trois. Un dernier indice ? Si le nombre est bien une puissance, le reste est forcément non-nul.
}

#### Correction ! ####

Ça y est ? Terminé ? Vous pensez avoir tout bon ? Alors voici [la correction](http://paste.awesom.eu/informaticienzero/hfh&ln). Comme quoi, ce n'était pas bien compliqué !
}

### La disparition : le retour ###

Connaissez-vous le roman *La Disparition* ? Il s'agit d'un roman français de Georges Perec, publié en 1969. Sa particularité est qu'il ne contient *pas une seule fois* la lettre « e ». On appelle ce genre de textes privés d'une lettre des *lipogrammes*. Celui-ci est une prouesse littéraire, car la lettre « e » est la plus fréquente de la langue française : elle représente une lettre sur six en moyenne ! Le roman faisant environ 300 pages, il a sûrement fallu déployer des trésors d'inventivité pour éviter tous les mots contenant un « e ».

Si vous essayez de composer un tel texte, vous allez vite vous rendre compte que vous glissez souvent des « e » dans vos phrases sans même vous en apercevoir. Nous avons besoin d'un vérificateur qui nous sermonnera chaque fois que nous écrirons un « e ». C'est là que le langage C entre en scène !

#### Votre mission ####

Écrivez un programme qui demande à l'utilisateur de taper une phrase, puis qui affiche le nombre de « e » qu'il y a dans celle-ci. Une phrase se termine toujours par un point « . », un point d'exclamation « ! » ou un point d'interrogation « ? ». Pour effectuer cet exercice, il sera indispensable de lire la phrase caractère par caractère.

Exemple :

```console
Entrez une phrase :
>>> Bonjour, comment allez-vous ?

Attention, 2 'E' ont été repérés dans votre phase !
```

Pour améliorer votre programme, vous pourriez demander à l'utilisateur de quelle lettre il souhaite se passer, plutôt que de toujours compter les « e ».

Notez qu'il existe un logiciel, infiniment plus évolué, qui fait ce genre de travail : **grep**. Cet utilitaire permet en fait de retrouver certaines expressions (lettres, mots ou autres) dans un fichier et de les afficher. Il peut également compter le nombre de fois qu'une expression apparaît dans un fichier. Quoi qu'il en soit, à vous de jouer !

#### Un indice ? ####

Avez-vous vraiment bien cherché ? Pourquoi ne pas aller faire un tour, puis revenir pour tenter de coder avec les idées fraîches ? Non, vraiment, vous voulez de l'aide ?

[secret]{
La première chose à faire est d'afficher un message de bienvenue, afin que l'utilisateur sache quel est votre programme. Ensuite, Il vous faudra lire les caractères tapés, un par un, *jusqu'à ce qu*'un point (normal, d'exclamation ou d'interrogation) soit rencontré. Dans l'intervalle, il faudra compter chaque « e » qui apparaîtra. Enfin, il faudra afficher le nombre de « e » qui ont été comptés, si présents.
}

#### Correction ####

Là encore, il ne s'agit que [d'une solution](http://paste.awesom.eu/informaticienzero/eNY&ln) parmi tant d'autres. Aviez-vous pensé à gérer les « E » majuscules ? Si vous n'êtes pas arrivé à coder cet exercice, encore une fois, essayez de le refaire en cachant la solution. Persévérez jusqu'à ce que vous y arriviez tout seul.

Les boucles sont assez faciles à comprendre, la seule chose dont il faut se souvenir étant de faire attention de bien avoir une condition de sortie pour ne pas tomber dans une boucle infinie. 

Le prochain chapitre montrera comment gagner du temps et de se faciliter la tache en découpant habilement son code.

## Les fonctions
Nous avons découvert beaucoup de nouveautés dans les chapitres précédents. Nos programmes commencent à grossir, même s'ils restent encore modestes. C'est pourquoi il est important d'apprendre à découper son programme en **fonctions**.

### A quoi ca sert ?
Les fonctions ne sortent pas de nulle part : si on les a inventées, c'est qu'elles peuvent servir à quelque chose. Reste à comprendre pourquoi. Car les fonctions sont des inventions qui répondent à des besoins bien précis : grandement faciliter la vie du programmeur !

Lorsque vous créez un programme, le résultat sera une grosse suite d'instructions placées les unes à la suite des autres. Et parmi cette gigantesque suite d'instructions, il y a souvent des "sous-suites", des paquets d'instructions, des morceaux de code qui reviennent régulièrement et qui sont présents en plusieurs exemplaires dans le programme final. Ces sous-suites servent pratiquement toujours à exécuter une tâche bien précise et ont presque toujours une signification importante pour le programmeur. Par exemple, il va exister une de ces sous-suites qui va servir à calculer un résultat bien précis, communiquer avec un périphérique, ou autre chose encore.

### Sans fonctions ###

Sans utiliser de fonctions, ces suites d'instructions sont présentes en plusieurs exemplaires dans le programme. Le programmeur doit donc recopier à chaque fois ces suites d'instructions, ce qui ne lui facilite pas la tâche. Et dans certains programmes, devoir recopier plusieurs fois la séquence d'instruction qui permet d'agir sur un périphérique ou de faire une action spéciale est franchement barbant ! 

De plus, ces suites d'instructions sont présentes plusieurs fois dans le programme final, exécuté par l'ordinateur. Et elles prennent de la place inutilement ! Mine de rien, à chaque fois qu'on recopie une de ces suites d'instructions récurrentes, on réinvente la roue. On perd ainsi beaucoup de temps à faire du copier-coller où à réécrire ce qui a déjà été fait. Les informaticiens ont donc inventé un moyen qui permet à ces suites d'instructions d'être présentes une seule fois dans le programme et d'être réutilisables au besoin. On a donc inventé les **fonctions**.

### Avec les fonctions ###

La technique du sous-programme consiste à n'écrire qu'un seul exemplaire de ces suites d'instructions, et lui donner un nom. Au lieu de recopier cet exemplaire à chaque fois qu'on veut le réutiliser, il suffira tout simplement de placer son nom à la place. On appellera cette suite d'instruction une **fonction**.

Cet exemplaire sera écrit en dehors du programme principal, le fameux main que l'on utilise depuis le début. On peut remarquer que la fonction main est déjà une fonction, qui regroupe tout le programme.

Les fonctions, qui sont des bouts de code réutilisables au besoin, présentent ainsi de gros avantages.

* Elles sont **réutilisables**. Plus besoin de recopier bêtement du code plusieurs fois de suite ! Avec une fonction, il suffit d'écrire une seule fois la fonction et ensuite de l'appeler autant de fois que l'on veut.
* Elles sont plus facilement **maintenables** : si votre fonction est inadaptée, il suffit d'en changer le code. C'est beaucoup plus rapide que de modifier plusieurs exemplaires d'une même suite d'instruction, surtout s'ils sont disséminés n'importe comment dans tout le programme.
* Elles permettent de **mieux s'organiser** : en divisant le code en fonctions, on peut ainsi séparer les différentes opérations et mieux s'y retrouver lors de la relecture du code. C'est quand même plus agréable de lire un code bien aéré qu'une gigantesque suite d'instructions de 2000 lignes dans laquelle tout est mélangé n'importe comment.

Bref, les fonctions n'ont que des avantages. Reste à savoir comment faire pour créer notre fonction, ce que nous allons voir dès la sous-partie suivante.

### Déclarer une fonction
Une fonction n'est donc qu'un vulgaire bloc de code, un morceau de programme. Mais ce morceau de programme a tout de même quelques caractéristiques. 

Par exemple, imaginons que je veuille créer une fonction qui calcule une opération mathématique complexe. On va prendre le logarithme d'un nombre, par exemple (si vous ne savez pas ce que c'est, ce n'est pas important). Notre fonction va donc devoir manipuler un nombre, celui dont on veut calculer le logarithme. De même, elle va fournir un résultat, le logarithme du nombre. Avec cet exemple, on voit qu'une fonction doit être définie par trois éléments. 

Elle a parfois besoin de **paramètres** : ce sont toutes les informations que l'on donne à la fonction pour qu'elle puisse travailler. Ces informations vont donner des données que notre fonction va devoir manipuler afin d'obtenir un résultat. Dans notre exemple, le nombre dont on veut calculer le logarithme est un paramètre de la fonction.

Elle contient aussi du **code** : ce code va dire ce que va faire la fonction. C'est tout ce qui compose l'intérieur d'une fonction, une fonction sans code, une fonction vide entre autres est une fonction inutile.

Et enfin, notre fonction peut renvoyer un **résultat**. Ce n'est pas obligatoire d'en renvoyer un, mais la majorité des fonctions renvoient un résultat.

### Déclarer une fonction ###

Maintenant que vous avez vu la partie "théorique", regardons comment tout cela s'applique en C. On vient de voir qu'une fonction est constituée de plusieurs éléments. Tous ces éléments seront donc indiqués dans notre fonction, à des endroits différents. Mais commençons par le commencement : nous allons d'abord apprendre à déclarer une fonction : cela consiste à indiquer à notre langage qu'on veut créer une fonction. Une fois celle-ci déclarée, il ne restera plus qu'à dire ce qu'elle fait, en écrivant son code et en spécifiant le résultat.

Pour déclarer une fonction, nous allons devoir donner quelques informations sur notre fonction, et notamment sur ses arguments et sur son résultat. Ces fameuses informations sont :

* le **type de retour** : il s'agit du type du résultat de la fonction. Après tout, notre fonction pourrait aussi bien renvoyer un nombre entier, qu'un flottant ou un caractère, aussi préciser le type du résultat est obligatoire.
* le **nom de la fonction** : c'est vous qui le choisissez. Les règles sont les mêmes que pour les variables.
* les **paramètres** : les paramètres sont ce avec quoi la fonction va travailler. Vous pouvez en mettre autant que vous voulez.

Pour déclarer une fonction, il va falloir préciser ces trois détails. Voici comment procéder pour préciser ces trois paramètres et ainsi déclarer une fonction :

```console
type identificateur (paramètres)
{
     /* corps de la fonction */
}
```

À l'intérieur de notre fonction (dans ce qui est nommé le corps de la fonction dans l'exemple du dessus), on va y placer le code de notre fonction. Pour illustrer ce concept, prenons un exemple tout banal :

```c
int ma_fonction(int parametre)
{
    /* Instructions */
}
```

J'ai ici défini une fonction appelée *ma_fonction*. Elle prend un ```int``` comme paramètre, et a pour résultat un ```int```.

#### void ####

Il se peut que l'on est besoin de coder une fonction qui ne retourne aucun résultat. C'est un cas courant en C. Ce genre de fonction est appelé **procédure**. Pour écrire une procédure, il faut indiquer à la fonction en question qu'elle ne doit rien retourner. Pour ce faire, il existe un "type de retour" spécial : ```void```. Ce type signifie "vide", et sert à indiquer que la fonction n'a pas de résultat.

Ce mot-clef sert aussi à indiquer qu'une fonction ne prend aucun paramètre. C'est assez rare, mais cela arrive. Dans ce cas, il suffit de définir la fonction en mettant ```void``` dans la liste des paramètres.

####Paramètres ####

Un paramètre sert à fournir des informations à la fonction lors de son exécution. La fonction *printf* par exemple récupère ce qu'elle doit afficher dans la console à l'aide de paramètres. Vous pouvez envoyer autant de paramètres à une fonction que vous voulez, il suffit de les séparer à l'aide d'une virgule. Cependant, ils doivent avoir des noms différents, tout comme les variables. Il est aussi possible de ne pas mettre d'arguments dans notre fonction, comme indiqué plus haut.

#### Exemples ####

Pour vous faire bien saisir toutes ces notions, entrainez vous à déclarer des fonctions. Essayez de déclarer une fonction :

* retournant un ```double``` et prenant un ```char``` et un ```int``` en argument ;
* retournant un ```unsigned short``` et ne prenant aucun paramètre ;
* retournant un ```float``` et prenant un ```int```, un ```long``` et un ```double``` en paramètres ;
* retournant un ```int``` et prenant un ```int``` constant et un ```unsigned long``` en paramètre ;
* ne retournant rien et ne prenant aucun paramètre ;

Je pense qu'avec tous ces exemples vous commencez à bien saisir comment déclarer une fonction.

### Le corps d'une fonction ###

Intéressons-nous maintenant au corps de la fonction, le code qu'il y a à l'intérieur. Comme pour la fonction *main*, le code est à l'intérieur des accolades. Et ce code, c'est nous qui allons l'écrire. Alors que doit-on écrire ? En bref, ce que vous voulez que la fonction fasse.

#### return ####

À ce stade, vous savez comment déclarer une fonction sans problème. Il vous manque juste une dernière information : comment faire pour préciser quel est le résultat de la fonction ? Comment lui dire : *« Le résultat que tu dois renvoyer, c'est ça »* ? Pour cela, on doit utiliser le mot-clef ```return```. Une fois que vous avez une variable qui contient le résultat que vous voulez, il suffit  d'écrire ```return```, suivi du nom de la variable, le tout suivi d'un point-virgule. À ce moment-là, la fonction s’arrêtera et renverra son résultat immédiatement. Cela signifie que tout le code qui est écrit après le ```return``` ne sera pas exécuté : notre fonction a déjà son résultat de disponible, pourquoi faire quoi que ce soit de plus ?

Petite remarque : un ```return``` peut parfaitement renvoyer une valeur qui est une constante. Pour donner un exemple, on va prendre une fonction assez simple, qu'on nommera *valueSign*. Notre fonction va prendre un argument de type ```int``` en entrée et va renvoyer :

* 0 si cet argument est nul ;	
  * 1 si celui-ci est positif ;
* et -1 si celui-ci est négatif.

Une version naïve de cette fonction s'écrirait comme ceci :

```c
int valueSign (int a)
{
    if ( a > 0 )
    {
        return 1 ;
    }

    else if ( a < 0 )
    {
        return -1 ;
    }

    else
    {
        return 0 ;
    }
}
```

#### Variables locales ####

Autre détail, qui concerne les variables que vous déclarez à l'intérieur du corps d'une fonction. Autant vous prévenir tout de suite : n'essayez pas d’accéder à une variable qui est déclarée dans une fonction en dehors de celle-ci. Si vous faites cela, vous allez au-devant de graves ennuis.

En effet, sauf cas exceptionnels, il faut savoir que ces variables ne sont accessibles que dans notre fonction, et pas de l'extérieur. C'est ainsi : les variables déclarées à l'intérieur de la fonction sont des données temporaires qui lui permettent de faire ce qu'on lui demande. Ces données sont des données internes à notre fonction, qu'elle seule doit manipuler et qui ne doivent généralement pas être accessibles à d’autres programmes ou d'autres fonctions. Si ce n'est pas le cas, c'est que cette variable doit être passée en paramètre ou qu'elle doit être renvoyée en tant que résultat. 

En fait, vous pouvez considérer que dans la majorité des cas, ces variables déclarées dans une fonction sont créées quand on commence l’exécution de la fonction, et qu'elles sont enlevées de la mémoire une fois que la fonction renvoie son résultat. Si je dis la majorité des cas, c'est qu'il y a une exception. Mais laissons cela de côté pour le moment : le temps de parler des variables statiques n'est pas encore arrivé.

### Exemple ###

Prenons un exemple tout bête. Vous voulez faire une fonction qui renvoie le carré d'un nombre passé en paramètre. Commençons déjà par traduire notre fonction en pseudo-code :

```console
Entrée : nombre

Carré :
       Multiplier nombre par lui-même
       Retourner nombre
```

Maintenant, exerçons-nous en codant cet algorithme. Je vous encourage à le faire avant de regarder la solution, cela vous fera progresser. Sinon, celle-ci ce trouve [ici](http://paste.awesom.eu/informaticienzero/1j4&ln).

Maintenant que vous avez saisi le principe, nous allons apprendre à utiliser nos fonctions, car pour l'instant elles ne font rien.

### Utiliser une fonction
Nous avons déjà utilisé quelques fonctions, notamment *printf* et *scanf*. Pour les utiliser, il suffit de taper le nom de la fonction suivi des paramètres entre parenthèses. Eh bien, pour nos fonctions c'est exactement la même chose. Prenons pour illustration la fonction *carre* vue dans la partie précédente. Voici le programme complet :

```c
#include <stdio.h>

int carre(int nombre)
{
    return nombre * nombre;
}

int main(void)
{
    int nombre, nombre_au_carre;

    puts("Entrez un nombre : ");
    scanf("%d", &nombre);
 
    nombre_au_carre = carre(nombre);

    printf("Voici le carre de %d : %d\n", nombre, nombre_au_carre);
    return 0;
}
```

On demande à l'utilisateur de rentrer un nombre entier. Une fois ceci fait, on appelle la fonction avec cette ligne :

```c
nombre_au_carre = carre(nombre);
```

On dit que *nombre* est un argument de la fonction *carre*. Paramètres et arguments sont très liés ; la différence entre les deux est que les premiers apparaissent lors que la définition de la fonction alors que les seconds apparaissent lors de son l'appel. On demande ensuite à attribuer à la variable *nombre_au_carre* la valeur retournée par la fonction *carre*. Ainsi, si *nombre* vaut 4, on appelle la fonction, et celle-ci retournera alors 16 (car $4^2 = 16$).

Un petit code commenté ?

```c
#include <stdio.h>

/* d) le nombre passé en paramètre en c) est récupéré */

int carre(int nombre)
{
    /* e) on fait le calcul et on renvoie la valeur */
    return nombre * nombre ;
}

int main(void)
{
    /* a) on déclare nos variables */
    int nombre, nombre_au_carre;

    puts("Entrez un nombre : ");
    /* b) on récupère la valeur de nombre */
    scanf("%d", &nombre);
 
    /* c) on appelle la fonction carre */
    nombre_au_carre = carre(nombre);
    /* f) nombre_au_carre vaut maintenant la valeur retournée par la fonction carre */
    
    /* g) on affiche le résultat */
    printf("Voici le carre de %d : %d\n", nombre, nombre_au_carre);
    return 0;
}
```

Ça va, vous suivez ? C'est simple : lors de l'appel de la fonction, on lui donne des arguments et le programme s'occupe du reste. C'est lui qui fera les calculs et qui renverra la valeur à afficher.

Sachez qu'il est possible d'optimiser notre code en se passant de cette variable intermédiaire qui stocke le résultat. En effet, on peut très bien appeler la fonction directement dans le *printf*, comme ceci :

```
#include <stdio.h>

int carre(int nombre)
{
    return nombre * nombre;
}

int main(void)
{
    int nombre;

    puts("Entrez un nombre :");
    scanf("%d", &nombre);

    printf("Voici le carre de %d : %d\n", nombre, carre(nombre));
    return 0;
}
```

Ce code revient au même que le précédant, car le deuxième paramètre de *printf* sera la valeur retournée par la fonction. Autrement dit, c'est un nombre dans les deux cas, et affichera bien la même chose à l'écran :

```console
Entrez un nombre :
10
Voici le carré de 10 : 100
```

La fonction *main* appelle la fonction *printf*, qui elle-même appelle la fonction *carre*. C'est une imbrication de fonctions. Ainsi, une fonction peut en appeler une autre ; c'est ainsi que tout programme écrit en C fonctionne. Entrainez-vous à appeler des fonctions en utilisant toutes les fonctions que nous avons vues au cours de ce chapitre. Nous verrons d'autres exercices en fin de chapitre.

### Appel de fonctions ###

Il faut aussi préciser une chose importante sur les arguments : si on passe une variable en argument d'une fonction, la variable en elle-même ne sera pas modifiée. La fonction utilisera à la place une copie de la variable ! C'est très important, et c'est source de comportements bizarres si on ne fait pas attention. Retenez bien : **les arguments d'une fonction sont copiés et c'est cette copie qui est manipulée par notre fonction**. Considérons l'exemple suivant.

```c
#include <stdio.h>

void fonction(int nombre)
{
    ++nombre;
    printf("Variable nombre dans la fonction : %d\n", nombre);
}

int main(void)
{
    int nombre = 5;

    fonction(nombre);
    printf("Variable nombre dans le main : %d\n", nombre);

    return 0;
}
```
```console
Variable nombre dans la fonction : 6
Variable nombre dans le main : 5
```

Vous avez vu ? La fonction manipule bien une copie de la variable, car lorsque l'on revient dans la fonction *main*, la valeur de la variable est toujours la même : l'original n'a pas été modifié. Nous verrons néanmoins dans quelques chapitres comment modifier l'original dans la fonction et non une copie.

On peut légitimement se demander pourquoi un tel comportement. La raison est assez complexe, mais je peux au moins vous dire que la raison est fortement liée au matériel de notre ordinateur. La façon dont les fonctions sont exécutées au niveau de notre ordinateur impose que ces arguments soient copiés. Pour le moment, ce n'est pas de votre niveau, mais vous aurez surement la réponse plus tard.
​		

### Les prototypes
Avez-vous remarqué qu'à chaque fois je mets ma fonction avant la fonction *main* ? En effet, mettre la fonction après le *main* provoquera un comportement indéterminé. La compilation pourrait très bien marcher comme elle pourrait planter. En effet, lorsque la fonction est placée avant, le compilateur connait ses paramètres et sa valeur de retour. Du coup, quand on appelle la fonction, le compilateur vérifie que les arguments qu'on lui donne sont bons. Si au contraire la fonction est après, le compilateur ne connait pas la fonction. Du coup, il lui fixe arbitrairement des caractéristiques : la fonction retourne un ```int``` et prend un nombre indéterminé de paramètres. Et quand on tente d'appeler la fonction, la compilation plante, car les arguments ne correspondent pas aux yeux du compilateur.

Heureusement, il existe une sorte de mode d'emploi qui permet d'indiquer toutes les caractéristiques d'une fonction au compilateur. Avec cette indication, on peut placer la fonction où on veut dans le code. Et ce mode d'emploi a un nom : un **prototype**. Un prototype se déclare quasiment comme une fonction :

```console
type nom_de_la_fonction(arguments);
```

Voilà à quoi ressemble un prototype. Placez-le simplement tout en haut de votre fichier et c'est bon ! votre fonction est utilisable partout dans le code. Essayez donc d'appliquer ça à la fonction *carre* :

```c
#include <stdio.h>

int carre(int nombre);

int main(void)
{
    int nombre, nombre_au_carre;

    puts("Entrez un nombre :");
    scanf("%d", &nombre);
 
    nombre_au_carre = carre(nombre);
    printf("Voici le carre de %d : %d\n", nombre, nombre_au_carre);

    return 0;
}

int carre(int nombre)
{
    nombre *= nombre;
    return nombre;
}
```

Ce code marche parfaitement, vous pouvez tester si vous voulez. La seule chose à retenir c'est le point-virgule après le prototype. Il est obligatoire, sinon la compilation plantera.

Si vous mettez toutes vos fonctions avant le main, les prototypes peuvent sembler inutiles, mais je vous encourage à les utiliser. Dès que vous aurez des projets conséquents, vous serez obligés de les déclarer.

Avant de conclure sur cette partie, je tiens à préciser quelque chose : dans les paramètres du prototype, seuls les types sont vraiment nécessaires, les identificateurs sont facultatifs. Ainsi le prototype précédant peut s'écrire :

```c
int carre(int);
```

Cependant, cette astuce ne marche que pour les prototypes, n'allez pas le faire pour une fonction (je vous laisse chercher pourquoi).

### Exercices
Comme le dit le vieil adage : "C'est en forgeant qu'on devient forgeron". C'est donc en vous entrainant que vous devenez petit à petit des programmeurs C. Dans cette partie, je vais vous proposer des algorithmes de fonctions, ce sera à vous de les traduire en C. Je mets la solution au cas où vous auriez vraiment du mal, mais je vous encourage à le faire avant de regarder la solution. C'est comme ça que vous progresserez le plus.

### Afficher un rectangle ###

Le premier exercice que je vous propose est d'afficher un rectangle. C'est très simple vous allez voir. Voici l'algorithme que je vous propose : 

```console
Entrée : longueur, largeur 

Afficher
    Déclarer deux variables i (longueur) et j (largeur);

    Pour (i = 0 ; i < longueur ; i++)
    {
        Pour (j = 0; j < largeur ; j++)
        {
            Afficher le symbole '*'
        }

        Sauter une ligne
    }
```

Le code devra afficher ceci dans la console : 

```console
Donnez la longueur :
5
Donnez la largeur :
3

***
***
***
***
***
```

#### Correction ####

```c
#include <stdio.h>

/* Prototype avec const qui permet de voir que l'on ne modifie pas la variable */
void rectangle(const int longueur, const int largeur);

int main(void)
{
    int longueur, largeur;

    puts("Donnez la longueur : ");
    scanf("%d", &longueur);

    puts("Donnez la largeur : ");
    scanf("%d", &largeur);

    puts(" ");

    rectangle(longueur, largeur);
    return 0;
}

void rectangle(const int longueur, const int largeur)
{
    int i, j;

    for (i = 0; i < longueur; i++)
    {
        for (j = 0; j < largeur; j++)
        {
            putchar('*');
        }

        puts(" ");
    }
}
```

Essayez aussi d'afficher le rectangle dans l'autre sens si vous voulez, cela vous servira d'entrainement.

### Afficher un triangle ###

Cette fonction est similaire à la précédente, mais pas tout à fait identique, sauf que cette fois on veut afficher un triangle. Rassurez-vous, l'exercice est plus simple qu'il n'y parait. Pour bien faire cet exercice, on va utiliser d'abord le pseudo-code pour écrire notre algorithme. En voici un tout simple que je vous propose :

```console
Entrée : nombre_de_lignes

Afficher
    Déclarer deux variables i (nombre de lignes) et j (nombre de colonnes);

    Pour (i = 0 ; i < nombre_de_lignes ; i++)
    {
        Pour (j = 0; j <= i ; j++)
        {
            Afficher le symbole '*'
        }

        Sauter une ligne
    }
```

Ce code, une fois traduit, devrait afficher la sortie suivante dans la console :

```console
Donnez un nombre :
5

*
**
***
****
*****
```

Bien entendu, la taille du triangle variera en fonction du nombre que l'on donne.

#### Correction ####

```c
#include <stdio.h>

void triangle(const int nombre);

int main(void)
{
    int nombre;

    puts("Donnez un nombre : ");
    scanf("%d", &nombre);

    puts(" ");
    triangle(nombre);

    return 0;
}

void triangle(const int nombre)
{
    int i, j;

    for (i = 0; i < nombre; i++)
    {
        for (j = 0; j <= i; j++)
        {
            putchar('*');
        }

        puts(" ");
    }
}
```

### Coupure ###

Imaginez le scénario suivant. Vous êtes un agent dans une banque et aujourd'hui vous recevez votre client. Celui-ci vous demande de lui livrer une somme avec la coupure qu'il vous a indiquée. Par exemple, il vous dit qu'il souhaite récupérer 300 000 € uniquement en billets de 500€ et de 200€. Dans ce cas vous lui donnerez le plus de billets de 500€ possible puis vous continuerez avec des billets de 200€.

Ici, la coupure sera la suivante :

* Des billets de 100€.
* Des billets de 50€.
* Des billets de 20€.
* Des billets de 10€.
  * Des pièces de 2€.
* Des pièces de 1€.

Votre client vous indique la somme qu'il souhaite et vous la lui fournissez en tenant compte de la coupure spécifique.

```console
Quelle somme voulez-vous ? 285
2 billet(s) de 100.
1 billet(s) de 50.
1 billet(s) de 20.
1 billet(s) de 10.
2 pièce(s) de 2.
1 pièce(s) de 1.
```

Exemple de prototype pour la fonction :

```c
void coupure (const int somme);
```

Et exemple de pseudo-code :

```console
Entrée : somme

Afficher
    Déclarer deux variables n (nombre de billet) = somme et tmp (variable temporaire) = somme;
      
    Si n /= 100 > 0
    {
        Afficher "n billet(s) de 100."
    }

    tmp -= n * 100;
    n = tmp / 50;

    Si (tmp / 50) > 0
    {
        Afficher "n billet(s) de 50."
    }

    tmp -= n * 50;
    n = tmp / 20;

    Si (tmp / 20) > 0
    {
        Afficher "n billet(s) de 20."
    }

    tmp -= n * 20;
    n = tmp / 10;

    Si (tmp / 10) > 0
    {
        Afficher "n billet(s) de 10."
    }

    tmp -= n * 10;
    n = tmp / 2;

    Si (tmp / 2) > 0
    {
        Afficher "n piece(s) de 2."
    }

    Si ((tmp -= n * 2) > 0)
    {
        Afficher "tmp piece(s) de 1."
    }
```

#### Correction ####

```c
#include <stdio.h>

void coupure(const int somme)
{
    int n = somme, tmp = somme;

    if((n /= 100) > 0)
    {
        printf("%d billet(s) de 100.\n", n);
    }

    tmp -= n * 100;
    n = tmp / 50;
    if((tmp / 50) > 0)
    {
        printf("%d billet(s) de 50.\n", n);
    }

    tmp -= n * 50;
    n = tmp / 20;
    if((tmp / 20) > 0)
    {
        printf("%d billet(s) de 20.\n", n);
    }

    tmp -= n * 20;
    n = tmp / 10;
    if((tmp / 10) > 0)
    {
        printf("%d billet(s) de 10.\n", n);
    }

    tmp -= n * 10;
    n = tmp / 2;
    if((tmp / 2) > 0)
    {
        printf("%d billet(s) de 2.\n", n);
    }

    if((tmp -= n * 2) > 0)
    {
        printf("%d piece(s) de 1.\n", tmp);
    }
}

int main(void)
{
    int somme;

    scanf("%d", &somme);
    coupure(somme);

    return 0;
}
```

Afin de bien s'entrainer, essayez donc de créer quelques fonctions en variant les paramètres. Nous aurons bientôt un chapitre entier dédié aux exercices, qui vous fera manipuler toutes les notions que nous avons vues jusque-là. En attendant, le prochain chapitre parlera de comment découper un projet.

## Découper son projet
Ce chapitre est la suite directe du précédent : nous allons voir comment découper nos projets en plusieurs fichiers. En effet, même si l'on découpe bien son projet en fonctions, ce dernier est difficile à relire si tout est contenu dans le même fichier. Ce chapitre a donc pour but de vous apprendre à découper vos projets efficacement.

### Portée et masquage
### La notion de portée ###

Avant de voir comment diviser nos programmes en plusieurs fichiers, il est nécessaire de vous présenter une notion importante, celle de **portée**. La portée d'une variable ou d'une fonction est la partie du programme où cette dernière est utilisable. Il existe plusieurs types de portées, cependant nous n'en verrons que deux :

* au niveau d'un bloc ;
* au niveau d'un fichier.

#### Au niveau d'un bloc ####

Une portée au niveau d'un bloc signifie qu'une variable n'est utilisable, visible que de sa déclaration jusqu'à la fin du bloc dans lequel elle est déclarée. Illustration :

```c
#include <stdio.h>

int main(void)
{
    {
        int nombre = 3;
        printf("%d\n", nombre);
    }

/* Incorrect ! */
    printf("%d\n", nombre);
    return 0;
}
```

Dans ce code, la variable *nombre* est déclarée dans un sous-bloc. Sa portée est donc limitée à ce dernier et elle ne peut pas être utilisée en dehors.

#### Au niveau d'un fichier ####

Une portée au niveau d'un fichier signifie qu'une variable n'est utilisable, visible, que de sa déclaration jusqu'à la fin du fichier dans lequel elle est déclarée. Pour obtenir une variable ayant une portée au niveau d'un fichier, il est nécessaire de la déclarer en dehors de tout bloc, par exemple comme ceci :

```c
#include <stdio.h>

int nombre = 3;

int triple(void)
{
    return nombre * 3;
}

int main(void)
{
    nombre = triple();
    printf("%d\n", nombre);
    return 0;
}
```

Dans ce code, la variable *nombre* a une portée au niveau du fichier et peut par conséquent être aussi bien utilisée dans la fonction *triple* que dans la fonction *main*.

### La notion de masquage ###

En voyant les deux types de portées, vous vous êtes peut-être posé la question suivante : que se passe-t-il s'il existe plusieurs variables et/ou plusieurs fonctions de même nom ? Eh bien, cela dépend de la portée de ces dernières : si elles ont la même portée comme dans l'exemple ci-dessous, alors le compilateur sera incapable de déterminer à quelle variable ou à quelle fonction le nom fait référence et, dès lors, retournera une erreur.

```
int main(void)
{
    int nombre = 10;
    int nombre = 20;
    return 0;
}
```

En revanche, si elles ont des portées différentes, alors celle ayant la portée la plus faible sera privilégiée, on dit qu'elle **masque** celle(s) de portée plus élevée. Autrement dit, dans l'exemple qui suit, c'est la variable du bloc de la fonction *main* qui sera affichée.

```c
#include <stdio.h>

int nombre = 10;

int main(void)
{
    int nombre = 20;

    printf("%d\n", nombre);
    return 0;
}
```

Notez que je dis « celle(s) de portée plus élevée » car les variables déclarées dans un sous-bloc ont une portée plus faible que celle déclarée dans le bloc supérieure. Ainsi le code ci-dessous est parfaitement valide et affichera 30.

```c
#include <stdio.h>

int nombre = 10;

int main(void)
{
    int nombre = 20;

    if (nombre == 20)
    {
        int nombre = 30;
        printf("%d\n", nombre);
    }

    return 0;
}
```

### Diviser pour mieux régner
### Création d'un nouveau fichier source ###

Bien, maintenant que nous avons vu la notion de portée, voyons comment diviser notre projet en plusieurs fichiers. Voici la marche à suivre pour crée un nouveau fichier *.c*, appelé **fichier source**.

#### Pour Code::Blocks ####

Pour ajouter des fichiers au projet, il faut faire *File -> New -> File...*. De là, vous allez tomber sur une fenêtre comme celle-ci : 

![Première fenêtre dans l'étape de création d'un fichier source](http://uploads.siteduzero.com/files/382001_383000/382649.png)

Pour ajouter un fichier source, cliquez sur *C/C++ source*. Si vous êtes sous Windows, vous pouvez passer la première fenêtre sans problème, celle-ci indiquant simplement que vous vous apprêtez à créer un fichier. Vous arrivez ensuite sur une fenêtre où l'on vous demandera plusieurs renseignements (cf. ci-dessous). 

![](http://uploads.siteduzero.com/files/382001_383000/382650.png)

La première case demande où sera situé le fichier. Cliquez sur les trois-points pour ouvrir une fenêtre. Par défaut, celle-ci s'ouvre sur le dossier contenant votre projet. Sinon, déplacez-vous pour atteindre le dossier de votre projet. Donnez ensuite un nom au fichier (appelons-le **autre.c**). Laissez de côté le deuxième cadre, il sera rempli automatiquement. Enfin, cochez toutes les cases du bas (*Debug* et *Release*), puis cliquez sur *Finish*.

#### Pour Visual Studio ####

Pour Visual Studio 2010 la manipulation est simple. Faites un clic droit sur votre projet, puis *Ajouter -> Nouvel élément* (ou bien **Ctrl** + **Maj** + **A**). Vous tombez sur cette fenêtre :

![](http://uploads.siteduzero.com/files/402001_403000/402304.png)

Pour ajouter un fichier source, il suffit de cliquer sur *Fichier C++ (.cpp)*, de donner un nom au fichier (pour l'exemple, **autre.c**) **en précisant bien l'extension .c** (sinon votre fichier sera considéré comme un fichier C++ et votre projet sera donc compilé par le compilateur C++) et de cliquer sur *Ajouter*.

#### Pour Xcode ####

Sous Xcode, afin d'ajouter un fichier à votre projet, appuyez sur **command** + **N**, vous devriez voir ceci :

![](http://uploads.siteduzero.com/files/382001_383000/382653.png)

Sélectionnez *C File* et appuyez sur *Next*. On vous demande alors le nom de votre fichier (nommez-le **autre.c**), dans quel dossier vous souhaitez l'enregistrer et dans quel projet l'ajouter. Une fois ces champs remplis, appuyez sur *Create*. Lorsque vous revenez dans votre projet, vous remarquerez, qu'en dessous de **main.c**, il y a votre nouveau fichier.

#### Compilation manuelle ####

Si jamais vous compilez en ligne de commande, il vous suffit de créer un nouveau fichier *.c* et de le rajouter lors de la compilation.

Pour la suite de ce chapitre, je vais considérer que vous avez donc deux fichiers source. Dans mon cas, il s'agira de **main.c** et de **autre.c**. Continuons donc notre découvertes des portées.

### Les fonctions ###

Dans le chapitre précédent, nous avions, entre autres, créé une fonction *triple* que nous avons placée dans le même fichier que la fonction *main*. Essayons à présent de les répartir dans deux fichiers distincts, par exemple comme ceci :

```c
/* Fichier autre.c */

int triple(int nombre)
{
    return nombre * 3;
}
```
```c
/* Fichier main.c */

int main(void)
{
    int nombre = triple(3);
    return 0;
}
```

Si vous testez ce code, vous aurez droit à un bel avertissement de votre compilateur du type *« implicit declaration of function 'triple' »*. Quel est le problème ? Le problème est que la fonction *triple* n'est pas déclarée dans le fichier **main.c** et que le compilateur ne la connaît donc pas lorsqu'il compile le fichier. Pour corriger cette situation, nous devons déclarer la fonction en signalant au compilateur que cette dernière se situe dans un autre fichier. Pour ce faire, nous allons inclure le prototype de la fonction *triple* dans le fichier **main.c** en le précédant du mot-clé ```extern```, qui signifie que la fonction est externe au fichier.

```c
/* Fichier autre.c */

int triple(int nombre)
{
    return nombre * 3;
}
```
```c
/* Fichier main.c */

extern int triple(int nombre);

int main(void)
{
    int nombre = triple(3);
    return 0;
}
```

En terme technique, on dit que la fonction *triple* est **définie** dans le fichier **autre.c** (car c'est là que se situe le corps de la fonction) et qu'elle est **déclarée** dans le fichier **main.c**. Sachez qu'une fonction ne peut être définie qu'**une seule fois**.

Pour information, notez que le mot-clé ```extern``` est facultatif devant un prototype (il est implicitement inséré par le compilateur). Je vous conseille cependant de l'utiliser, dans un soucis de clarté et de symétrie avec les déclarations de variables.

### Les variables ###

La même méthode peut être appliquée aux variables, mais uniquement à celle ayant une **portée au niveau d'un fichier**. Également, à l'inverse des fonctions, il est plus difficile de distinguer une définition d'une déclaration de variable (elles n'ont pas de corps comme les fonctions). La règle pour les différencier est qu'une déclaration sera précédée du mot-clé ```extern``` alors que la définition non. C'est à vous de voir dans quel fichier vous souhaitez définir la variable, mais elle ne peut être définie qu'**une seule fois**. Enfin, sachez que seule la définition peut comporter une initialisation. Ainsi, cet exemple est tout à fait valide :

```c
/* Fichier autre.c */

int nombre = 10;	/* une définition */
extern int autre;	/* une déclaration */
```
```c
/* Fichier main.c */
extern int nombre;	/* une déclaration */
int autre = 10;		/* une définition */
```

Alors que celui-ci, non :

```c
/* Fichier autre.c */

int nombre = 10;	/* il existe une autre définition */
extern int autre = 10;	/* une déclaration ne peut pas comprendre une initialisation */
```
```c
/* Fichier main.c */

int nombre = 20;	/* il existe une autre définition */
int autre = 10;		/* une définition */
```

### On m'aurait donc menti ? ###

Je vous ai dit plus haut qu'il n'était possible de définir une variable ou une fonction qu'une seule fois, en fait ce n'est pas tout à fait vrai. Il est possible de rendre une variable (ayant une portée au niveau d'un fichier) ou une fonction locale à un fichier en précédant sa définition du mot-clé ```static```. De cette manière, la variable ou la fonction est interne au fichier où elle est définie et n'entre pas en conflit avec les autres variables ou fonctions locales à d'autres fichiers. La contrepartie est que la variable ou la fonction ne peut être utilisée que dans le fichier où elle est définie (c'est assez logique). Ainsi, l'exemple suivant est tout à fait correct et affichera 20.

```c
/* Fichier autre.c */
static int nombre = 10;
```
```c
/* Fichier main.c */
#include <stdio.h>

static int nombre = 20;

int main(void)
{
    printf("%d\n", nombre);
    return 0;
}
```

### Les fichiers d'en-têtes
Pour terminer ce chapitre, il ne nous reste plus qu'à voir les fichiers d'en-têtes. Jusqu'à présent, lorsque vous voulez utiliser une fonction ou une variable définie dans un autre fichier, vous insérez sa déclaration dans le fichier ciblé. Seulement voilà, si vous utilisez dix fichiers et que vous décidez un jour d'ajouter ou de supprimer une fonction ou une variable ou encore de modifier une déclaration, vous vous retrouvez Gros-Jean comme devant et vous êtes bon pour modifier les dix fichiers ... ce qui n'est pas très pratique.

Pour résoudre ce problème, on utilise des fichiers d'en-têtes (d'extension *.h*). Ces derniers contiennent conventionnellement des déclarations de fonctions et de variables et sont inclus *via* la directive ```#include```, dans les fichiers qui utilisent les fonctions et variables en question.

La création d'un fichier d'en-tête fonctionne de la même manière que celle d'un fichier source. Les utilisateurs d'un environnement de développement intégré devront simplement penser à sélectionner *Header File* (*Fichier d'en-tête* en français) au lieu de *Source File*.

La structure d'un fichier d'en-tête est généralement de la forme :

```c
#ifndef CONSTANTE_H
#define CONSTANTE_H

/* les déclarations */

#endif
```

Les directives du préprocesseur sont là pour éviter les inclusions multiples : vous devez les utiliser pour chacun de vos fichiers d'en-têtes. Vous pouvez remplacer CONSTANTE par ce que vous voulez, le plus simple et le plus fréquent étant le nom de votre fichier, par exemple AUTRE_H si votre fichier se nomme **autre.h**. Voici un exemple d'utilisation de fichier d'en-tête :

```c
/* Fichier d'en-tête autre.h */

#ifndef AUTRE_H
#define AUTRE_H

extern int triple(int nombre);

#endif
```
```c
/* Fichier source autre.c */

#include "autre.h"

int triple(int nombre)
{
    return nombre * 3;
}
```
```c
/*Fichier source main.c */

#include "autre.h"

int main(void)
{
    int nombre = triple(3);
    return 0;
}
```

Plusieurs remarques à propos de ce code :

* dans la directive d'inclusion, les fichiers d'en-têtes sont entre guillemets et non entre crochets comme les fichiers d'en-têtes de la bibliothèque standard ;
* les fichiers sources et d'en-têtes correspondants portent le même nom ;
* je vous conseille d'inclure le fichier d'en-tête dans le fichier source correspondant (dans mon cas **autre.h** dans **autre.c**) afin d'éviter des problèmes de portée ;
* si vous compilez à la main, il vous suffit de spécifier les fichiers sources, les fichiers d'en-têtes seront automatiquement inclus.

Nous avons conclu ce chapitre en parlant des fichiers d'en-tête. Nous avons vu de nouvelles directives de préprocesseur. Il est temps de vous les expliquer. Nous apprendrons à connaitre et à maitriser le préprocesseur dans le chapitre suivant.

## Le préprocesseur
On l'a déjà rencontré, on l'a déjà utilisé, mais on ne s'est jamais vraiment intéressé à son fonctionnement ni aux possibilités qu'il nous offre. Je parle bien sûr du **préprocesseur**. Ce chapitre va vous faire découvrir que le préprocesseur est bien plus puissant que la simple utilisation dont on en a fait jusqu'à maintenant.

### Le fonctionnement du préprocesseur
### Qu'est-ce que le préprocesseur ? ###

Comme dit en introduction, nous avons déjà rencontré le préprocesseur, sans jamais vraiment s'intéresser à lui. Le préprocesseur est un programme qui réalise des traitements sur le code source avant que ce dernier ne soit réellement compilé. On peut considérer que le préprocesseur a trois rôles (même si c'est quelque peu restrictif).

* Réaliser des **inclusions** : c'est un cas commun que nous avons déjà vu dès le premier code. Le préprocesseur inclut tout le contenu d'un fichier d'en-tête dans un autre fichier, soit d'en-tête soit source.

* Définir des **macros** : une macro est un substitut à un morceau de code, qui peut éventuellement prendre des paramètres. Il suffit de définir la macro et de l'utiliser dans le code. Après le passage du préprocesseur, tous les appels à cette macro seront remplacés par le code associé. Si vous êtes habitués au monde de la bureautique et des traitements de texte, vous devez certainement savoir ce que c'est exactement. Nous étudierons les macros dans la deuxième partie.

* Permettre la **compilation conditionnelle** : le préprocesseur permet également de définir le code à compiler. Cela permet d'écrire du code pour plusieurs plate-formes ou systèmes d'exploitation dans le même fichier source. On peut par exemple imaginer du code spécifique à Linux et à Windows ; dans ce cas, il suffira de préciser lors de l'écriture du code quelle partie du code doit être compilée et le préprocesseur supprimera l'autre. Nous étudierons des exemples dans la troisième partie.

### Exemple d'utilisation avec les inclusions ###

Nous avons vu dès le début du cours comment inclure des fichiers d'en-tête avec la directive ```#include```, mais sans jamais expliquer ce qu'elle faisait. Son but est très simple : inclure le contenu d'un fichier dans un autre fichier. Ainsi, si jamais l'on se retrouve avec deux fichiers comme ceux-ci avant la compilation :

```c
/* Fichier d'en-tête fichier.h */

#ifndef FICHIER_H
#define FICHIER_H

extern int glob_var;

extern void Func1(int);
extern long Func2(double, char);

#endif
```
```c
/* Fichier source fichier.c */

#include "fichier.h"

void Func1(int arg)
{
    /* du code */
}

long Func2(double arg, char c)
{
    /* du code */
}
```

On ne se retrouve qu'avec un seul fichier à l'arrivée :

```c
/* Fichier source fichier.c */

extern int glob_var;

extern void Func1(int arg);
extern long Func2(double arg, char c);

void Func1(int arg)
{
    /* du code */
}

long Func2(double arg, char c)
{
    /* du code */
}
```

On peut voir que le contenu de **fichier.h** (une variable globale et deux prototypes) a été inclus dans **fichier.c** et toutes les directives de préprocesseur ont disparu. C'est ce qui se passe chaque fois que l'on inclut un fichier d'en-tête. 

D'ailleurs, si vous utilisez *gcc*, vous pouvez compiler avec l'option *-E* pour voir le code source **après** le passage du préprocesseur. Pour ceux qui utilisent Code::Blocks comme IDE, il est possible de faire pareil : allez dans *Project -> Build Options -> Other Options* et ajouter *-save-temps -masm=intel*. Cette option sauvegardera tous les fichiers générés par la compilation. Le code après le passage du préprocesseur est contenu dans les fichiers **.i**.

Mais comme nous l'avons dit, le préprocesseur ne se limite pas à des inclusions. Examinons sans plus tarder ses possibilités.

### Une directive : #define
Comme nous l'avons dit dans la partie précédente, le préprocesseur permet la définition de macros, c'est à dire des substituts à des morceaux de code. Pour créer une macro, il faut trois éléments.

* ```#define``` : cette directive va nous permettre de définir une macro.
* Le **nom de la macro** : par convention, celui-ci est écrit en majuscules. On peut choisir le nom que l'on veut, à condition de respecter les mêmes règles que pour les variables.
* La **définition** : c'est le code que l'on souhaite substituer.

Nous verrons qu'il est également possible de rajouter des paramètres à nos macros.

### Des macros simples ###
#### Une définition simple ####

Prenons un exemple très simple : je définis une macro qui substitue l'identificateur *TAILLE* à la valeur 100. 

```c
/* Dans le cas d'une définition simple comme celle-ci, on parle souvent de constante de préprocesseur. */

#define TAILLE 100
```

Ce code signifie que chaque fois que l'on appellera *TAILLE* dans le code, le préprocesseur remplacera la macro (*TAILLE*) par sa définition (100). Voici un code illustrant le principe.

```c
#include <stdio.h>
#define TAILLE 100

int main(void)
{
    int variable = 5;

    /* On multiplie par TAILLE */
    variable *= TAILLE;
    printf("Variable vaut : %d\n", variable);

    /* On additionne TAILLE */
    variable += TAILLE;
    printf("Variable vaut : %d\n", variable);

    return 0;
}
```

Ce code sera remplacé, après le passage du préprocesseur, par celui ci-dessous.

```c
int main(void)
{
    int variable = 5;

    variable *= 100;
    printf("Variable vaut : %d\n", variable);

    variable += 100;
    printf("Variable vaut : %d\n", variable);

    return 0;
}
```

Je n'ai pas inclus le contenu de ```<stdio.h>``` car celui-ci est trop long et trop compliqué pour le moment. Néanmoins, l'exemple permet d'illustrer le principe des macros et surtout leur avantage : il suffit de changer la définition de la macro pour que le reste du code s'adapte. Illustrons : on veut changer 100 par 200. Le seul problème est qu'on utilise beaucoup cette valeur, disons 50 fois dans le code. Sans macro, il faudrait changer toutes les valeurs une par une, donc faire 50 modifications. Avec une macro, il suffit de changer la définition et tout le code s'adapte ensuite.

#### Macros dans d'autres macros ####

On peut même faire encore mieux : on peut utiliser une macro dans une autre macro. Imaginez que vous souhaitiez calculer le nombre de pixels d'une fenêtre. Vous avez trois macros : la largeur, la hauteur et le total. Il est possible d'appeler les macros LARGEUR et HAUTEUR directement dans la macro TOTAL et ainsi obtenir le nombre de pixels. 

```c
#define HAUTEUR 1440
#define LARGEUR 700
#define TOTAL (HAUTEUR * LARGEUR)

printf("Total = %d pixels\n", TOTAL);
```

Si j'explicite les étapes, j'obtiens les codes suivants.

```c
printf("Total = %d pixels\n", (HAUTEUR * LARGEUR));
```
```c
printf("Total = %d pixels\n", (1440 * 700));
```

On obtient bien au final le nombre total de pixels. L'avantage ? Non seulement on s'évite des modifications en cas de changement, mais ça va également plus vite à écrire que HAUTEUR * LARGEUR. Les parenthèses ne sont pas obligatoires, mais elles sont fortement recommandées et nous verrons pourquoi par la suite.

Ce qu'il faut retenir c'est qu'il est possible d'utiliser des macros dans d'autres macros, mais également qu'il est possible de faire des opérations (tous les signes mathématiques sont utilisables, c'est à dire +, -, *, / et %).

Allez, exercice ! Faites-moi une macro qui additionne le résultat de deux autres macros. La première macro multiplie un nombre choisi (disons 100) par trois et la deuxième le divise par deux. La correction est sur [past.awesom.eu](http://paste.awesom.eu/informaticienzero/cdx&ln).

#### D'autres définitions ####

Jusqu'à maintenant, on s'est contenté de macros qui n'ont pour définition que des valeurs numériques. Fort heureusement, il est possible d'avoir d'autres définitions. Nous venons de voir qu'il était possible qu'une définition soit composée d'une ou plusieurs macros, mais ce n'est pas tout. Elle peut également être composée de caractères voire même de fonctions, de boucles et de conditions. Illustrons cela.

```c
#define HELLO  puts("Hello world!")
```

Je défini la macro HELLO comme étant un substitut du code ```puts("Hello world!")```. Vous noterez que je ne mets pas de point-virgule à la fin de la définition. La plupart des programmeurs font ça par convention. Dans ce cas, il ne faut pas oublier de le rajouter lorsqu'on utilise la macro.

```
#define HELLO  puts("Hello world!")

int main(void)
{
    HELLO;
    return 0;
}
```

### Avec paramètre(s) ###

Pour l'instant, nous ne faisons que manipuler des macros déjà fixées. Or il serait bien de pouvoir faire comme pour les fonctions, c'est à dire transmettre des paramètres à la macro. C'est possible et c'est même la principale utilisation des macros : agir sur des paramètres. Pour déclarer une macro avec des paramètres, c'est très simple, on rajoute des parenthèses, comme pour les fonctions, en séparant les paramètres par des virgules.

```c
#define MACRO(paramètres) définition
```

Illustrons ce nouveau concept avec un exemple ludique : nous allons écrire deux macros : RAD qui convertira un angle en radian et DGR qui fera l'inverse. Pour ceux qui ne connaissent pas, un radian vaut approximativement 57.29 degrés. Pour passer de l'un à l'autre, on fait ceci :

* Conversion de $x$ degrés en radians : $\frac{\pi \times x}{180}$
* Conversion de $x$ radians en degrés : $\frac{180 \times x}{\pi}$

Voici un exemple d'exécution de ce code.

```console
Donnez un angle en degrés :
57.29
57.290 degrés = 1.000 radians

Donnez un angle en radians :
3.1415
3.142 radians = 180.024 degrés
```

Je vous laisse coder cet exemple. Aidez-vous de la correction [ici](http://paste.awesom.eu/informaticienzero/lt9&ln) si vous avez vraiment du mal. 

Appliquons encore ce concept avec un deuxième exercice : créons la macro MIN qui renvoie le minimum entre deux nombres (exercice bateau classique je l'accorde, dont la correction se trouve [ici](http://paste.awesom.eu/informaticienzero/Pmb&ln)). Quelque chose a dû vous frapper dans les corrections : pourquoi écrire ```(x)``` et pas simplement ```x``` ?

#### Les inconvénients ####

Évidemment, les macros avec des paramètres présentent des dangers. Le plus gênant est qu'il faut parfois *surparenthèser* pour éviter toute ambigüité. En effet, si l'on n’y prend pas garde, on peut avoir des surprises dues à la priorité des opérateurs. Prenons l'exemple d'une macro MUL.

```c
#define MUL(a, b)  (a * b)
```

Tel quel, le code peut réserver des surprises. Si en effet j'appelle la macro comme ceci :

```c
MUL(2+3, 4+5)
```

J'obtiens comme résultat 19 (la macro sera remplacée par ```2 + 3 * 4 + 5```) et non 45, le résultat attendu. Pour garantir la bonne marche de la macro, je dois rajouter des parenthèses.

```c
#define MUL(a, b)  ((a) * (b))
```

Dans ce cas, j'obtiens bien le résultat souhaité, c'est-à-dire 45 (```(2 + 3) * (4 + 5)```). Je vous conseille de rajouter des parenthèses en cas de doute pour lever toute ambigüité.

Je tiens à terminer cette sous-partie en vous mettant en garde par rapport à un autre danger appelé **effet de bord**. Un effet de bord est un effet indésirable. Il apparait souvent dans les macros où un paramètre est réutilisé plusieurs fois.

```c
#define CARRE(a) ((a) * (a))
```

Un appel tel que le suivant :

```c
CARRE(a++)
```

entrainera le code suivant :

```c
((a++) * (a++))
```

On remarque que l'opérateur ```++``` est appliqué deux fois, ce qui rendra le code faux. Faites donc attention quand vous déclarez des macros que celles-ci n'entrainent pas des effets de bord indésirables.

### Sur plusieurs lignes ###

Si jamais notre macro est un peu longue, plutôt que de la définir sur une seule ligne, il est possible de le faire sur plusieurs. On utilise pour cela le symbole ```\```chaque fois que l'on veut aller à la ligne.

```c
#define MACRO  puts("Hello world!"); \
    putchar('a'); \
    printf("%d", 2 + 3)

int main(void)
{
   MACRO;
   return 0;
}
```

Après le passage du préprocesseur, le fichier source ressemblera à celui ci-dessous.

```c
int main(void)
{ 
    puts("Hello world!");
    putchar('a');
    printf("%d", 2 + 3);

    return 0;
}
```

Cependant, les macros sur plusieurs lignes présentent également un inconvénient : on peut avoir des problèmes d'interprétation, comme le prouve l'exemple suivant.

```c
#include <stdio.h>

#define SWAP(a, b, tmp)\
    (tmp) = (a);\
    (a) = (b);\
    (b) = (tmp);

int
main(void)
{
    int a[3]={1,2,3};
    int b[3]={2,4,6};
    int tmp;
    int itr;

    for (itr=0; itr<3; ++itr)
        SWAP(a[itr], b[itr], tmp);

    for (itr=0; itr<3; ++itr)
        printf("%d %d\n",a[itr],b[itr]);

    return 0;
}
```

Contrairement à ce qui est souhaité, seule la première instruction de la macro fera partie du corps de la boucle, les trois autres seront situés en dehors de celui-ci. En effet, le remplacement produira en vérité le code suivant (notez l'instruction vide à la fin qui résulte de l'ajout d'un point-virgule à la fin de l'appel à la macro _SWAP_) :

```c
for (itr=0; itr<3; ++itr)
    (tmp) = (a);
(a) = (b);
(b) = (tmp);
;
```

Une solution simple à ce problème consiste à utiliser une boucle ```do { } while```. De cette manière, le corps de la macro ne constitue plus qu'une seule instruction _avec le point-virgule suivant l'appel à la macro_, celui-ci étant nécessaire pour terminer une instruction ```do {} while``` (ce qui, finalement, permet d'uniformiser les appels de macro et les appels de fonctions)

```c
#include <stdio.h>

#define SWAP(a, b, tmp)\
do {\
    (tmp) = (a);\
    (a) = (b);\
    (b) = (tmp);\
} while (0)

int
main(void)
{
    int a[3]={1,2,3};
    int b[3]={2,4,6};
    int tmp;
    int itr;

    for (itr=0; itr<3; ++itr)
        SWAP(a[itr], b[itr], tmp);

    for (itr=0; itr<3; ++itr)
        printf("%d %d\n",a[itr],b[itr]);

    return 0;
}
```

### Des macros sans définition ###

Comme l'indique le titre, il est possible de créer des macros sans les définir, ce qui fait qu'on créé un substitut à un code inexistant. Exemple :

```c
#define MACRO
```

Ici, MACRO est une macro qui n'a aucune définition, aucun code associé. Pourtant, cette technique est souvent utilisée. Nous allons voir comment dans la partie suivante.

### Des directives de condition
### Les directives #if, #elif, #else et #endif ###

Ces quatre directives de préprocesseur font partie de ce que l'on appelle des **directives de condition** qui permet d'exécuter ou non du code en fonction de la validité d'une condition (si la condition est vraie, le code est exécuté sinon il est ignoré). Les trois premières correspondent à ```if```, ```else if``` et ```else``` ; la dernière est obligatoire et conclue toute condition.

Voici un exemple très banal dans lequel on teste si une macro est négative, nulle ou positive.

```c
#include <stdio.h>

#define A   2

#if (A) < 0
#define B puts("A < 0")
#elif (A) > 0
#define B puts("A > 0")
#else
#define B puts("A == 0")
#endif

int main(void)
{
    B;
    return 0;
}
```

### defined ###

Cette directive, associée à celles ci-dessus, permet de tester l'existence ou la non-existence d'une constante. Le principe est simple : si la constante à tester est déjà définie, on exécute le code associé, sinon il est supprimé. Cette technique est utilisé pour produire des programmes portables. En effet, chaque système et chaque compilateur définissent une constante qui lui est propre. On a donc une constante pour Windows, une pour Mac, une pour Linux, mais également des constantes pour gcc, Visual Studio, MinGW, etc. En testant si une constante existe on peut déterminer sur quelle plate-forme et avec quel compilateur on compile et adapter le code en conséquence. Il est cependant important de noter que **ces constantes ne sont pas standards**. Autrement dit, elles peuvent varier selon plusieurs paramètres. Renseignez-vous bien lorsque vous voudrez les utiliser.

Voici un exemple de code qui teste si l'on est sous Windows 32 ou 64 bits ou bien sous Linux ou MacOS pour inclure un fichier d'en-tête spécifique au système d'exploitation cible (celui-ci étant le même pour Linux et MasOS).

```c
/* si on est sous Mac ou Linux */
#if defined __APPLE__ || defined linux
#include <unistd.h>

/* ou bien si on est sous Windows 32 bits ou 64 bits */
#elif defined __WIN32__ || defined __WIN64__
#include <windows.h>

#endif
```

Bien entendu, les autres opérateurs de conditions sont eux aussi utilisables.

### Les directives #ifdef et #ifndef ###

La première directive signifie « si la constante est définie », la deuxième étant son contraire, « si la constante n'est pas définie ». Elles sont en quelque sorte des "raccourcis" de ```defined```. En effet, si vous n'avez qu'une seule constante à tester, il est plus rapide d'utiliser ces deux directives que ```defined```. Illustrations avec un code basique dans lequel on ne teste que pour Windows et Linux.

```c
#ifdef __WIN32__  /* à la place de #if defined __WIN32__ */
#include <windows.h>
#endif

#ifdef linux  /* à la place de #elif defined linux */
#include <unistd.h>
#endif
```

#### Sécurisation d'un fichier d'en-tête ####

L'avantage de cette technique est que l'on peut sécuriser les fichiers d'en-tête. En effet, lorsque l'on créé un fichier d'en-tête, il faut toujours faire attention aux **inclusions infinies**. Cela peut arriver quand un fichier d'en-tête 1 inclut un fichier d'en-tête 2 qui lui-même inclut 1. Le préprocesseur rentre dans une sorte de boucle infinie qui fait au final planter la compilation. Pour éviter ces cas, je vous avais fourni un code à mettre obligatoirement à chaque création de fichier d'en-tête. Il est maintenant temps d'expliquer exactement son fonctionnement. Je vous remets le code en dessous ; sauriez-vous l'expliquer sans regarder la réponse ?

```c
#ifndef FICHIER_H
#define FICHIER_H

#endif
```

* ```#ifndef FICHIER_H``` : si la constante associée au fichier n'a jamais été défini, le préprocesseur rentre dans la condition et poursuit l'exécution du code. 
* ```#define FICHIER_H``` : on définit la constante du fichier. La prochaine fois, la condition sera fausse et le fichier ne sera pas inclus.  
* ```#endif``` : termine la condition.

Ce code est simple, mais il permet d'éviter des inclusions infinies et donc des problèmes. Je vous conseille donc très fortement de l'utiliser chaque fois que vous créez un fichier d'en-tête.

### Constantes pré-définies
### Macros standards ###

La norme prévoit que quatre constantes de préprocesseur sont définies (cf norme C89 - 3.8.8 Predefined macro names). Ces quatre macros sont ```__LINE__``` (le numéro de la ligne actuelle), ```__FILE__``` (le nom de fichier courant), ```__DATE__``` (la date de compilation du fichier, sous la forme Mois / Jour / Année) et ```__TIME__``` (l'heure de la compilation, sous la forme hh:mm:ss). Les trois premieres sont des chaines de caractères, la dernière un entier. 

Je vous invite à tester le code ci-dessous chez vous.

```c
#include <stdio.h>

int main(void)
{
    puts(__FILE__);
    puts(__DATE__);
    puts(__TIME__);
    printf("%d\n", __LINE__);

    return 0;
}
```

### Détecter le compilateur et le système ###

Je tiens à conclure cette partie en vous offrant une liste de quelques constantes courantes. Bien entendu, cette liste n'est pas exhaustive, mais elle contient la plupart des constantes servant à définir le système d'exploitation et / ou le compilateur. Je le répète encore une fois : ces constantes ne sont pas standards et peuvent donc varier.

#### Systèmes d'exploitation ####

* **Windows** : ```_WIN32``` (32 bits) ou ```_WIN64``` (64 bits)
* **GNU/Linux** : ```Linux``` ou ```__linux__```
* **Apple** : ```__APPLE__``` ou ```__MACH__```
* **FreeBSD** : ```__FreeBSD__```
* **NetBSD** : ```__NetBSD__```
* **Solaris** : ```sun``` ou ```__SVR4```

Une liste plus complète des systèmes d'exploitation est disponible [ici](http://sourceforge.net/p/predef/wiki/OperatingSystems/).

#### Compilateurs ####

* **Visual C++** : ```_MSC_VER```
* **GCC** : versions : ```__GNUC__```, ```__GNUC_MINOR__``` ou ```__GNUC_PATCHLEVEL__```
* **Borland** : ```__TURBOC__``` ou ```__BORLANDC__```
* **MinGW** : ```__MINGW32__```
* **Cygwin** : ```__CYGWIN__``` ou ```__CYGWIN32__```

Une liste plus compète des compilateurs est disponible [ici](http://sourceforge.net/p/predef/wiki/Compilers/).

Il existe encore beaucoup d'autres constantes prédéfinies, comme pour connaitre la version du compilateur ou le nom de la fonction courante par exemple. Je ne les mets pas ici car elles sont très nombreuses, mais vous en connaissez l'existence, si jamais il y a besoin un jour.

Le préprocesseur est une notion assez simple à comprendre et particulièrement puissante quand on le connait. Cependant, malgré ses nombreux avantages, il possède également des défauts, notamment celui de rendre la correction d'un code erroné plus difficile. Enfin, je tiens à préciser que nous n'avons pas tout appris sur le préprocesseur. Si jamais vous voulez approfondir vos connaissances, je vous invite à lire [le tutoriel de Pouet_forever](http://progdupeu.pl/tutoriels/84/le-preprocesseur/).

Le chapitre suivant nous permettra de découvrir l'en-tête standard ```<math.h>```, ce qui vous permettra de voir l'intérêt des fichiers d'en-tête, d'améliorer vos connaissances sur le C et les mathématiques et de pratiquer un peu. Que de bonnes choses !

## L'en-tête <math.h>
Dans les chapitres précédents, on a vu comment bien organiser notre code avec de fonctions. On a aussi vu comment regrouper ces fonctions de façon cohérente dans des fichiers séparés, en utilisant des fichiers d’en-tête. Cela nous mène directement au concept de bibliothèque. Ce sont des fichiers dans lesquelles on va regrouper des fonctions, qu'on pourra réutiliser au besoin.

Ces bibliothèques peuvent contenir toute sorte de fonctions : fonctions mathématiques, fonctions de gestion de la mémoire, etc. Le langage C normalise quelques bibliothèques de base, qui seront disponibles avec n"importe quel compilateur sous n'importe quel système d'exploitation (à condition de ne pas utiliser un environnement trop exotique). On peut notamment citer la bibliothèque ```<math.h>```, qui rassemble quelques fonctions mathématiques. Dans ce chapitre, nous allons découvrir ce que cette bibliothèque a dans le ventre !

NB : il se peut que vous n'ayez pas le niveau mathématique pour tout comprendre. Dans ce cas, lisez quand même le chapitre, même si vous ne comprenez pas tout.

### Les bibliothèques
### Les bibliothèques en informatique ###

Je tiens à attirer votre attention sur le fait que la bibliothèque mathématique du langage C est une bibliothèque un peu *spéciale*. Celle-ci se comporte comme une bibliothèque tierce, soit une bibliothèque qui se rajoute par-dessus la bibliothèque standard. Les bibliothèques peuvent être présentés sous forme de code source ou de fichiers binaires à lier à vos programmes. 

Dans les grandes lignes, il existe deux grand types de bibliothèques : les bibliothèques statiques, et les bibliothèques dynamiques. Avec une bibliothèque statique, le code de la bibliothèque est inclus dans l'exécutable lors de la compilation. Ce dernier est donc plus important, il prend plus de place. Une bibliothèque dynamique est un fichier utilisé par un exécutable, mais n'en faisant pas partie. Ce fichier contient des fonctions qui pourront être appelées pendant l'exécution d'un programme, sans que celles-ci soient incluses dans son exécutable. Il faut dans ce cas fournir la bibliothèque avec le programme.

Les systèmes d'exploitations récents sont pratiquement tous multitâche : ils permettent d’exécuter plusieurs programmes "en même temps". Il arrive donc que certains programmes utilisent les mêmes bibliothèques en même temps. Avec des bibliothèques dynamiques, il est possible de ne charger celles-ci qu'une seule fois en mémoire et de laisser tous les programmes en utiliser la même copie. On parle alors de **bibliothèques partagées**.

Ces bibliothèques sont donc des fichiers binaires, qui possèdent généralement les extensions suivantes :

* Bibliothèques statiques :
    * `.a` :  sous UNIX et GNU/Linux (pour **A**rchive) ;	
    * `.lib` : sous Microsoft Windows (**LIB**rary).
* Bibliothèques dynamiques :
    * `.so` : sous UNIX et GNU/Linux (**S**hared **O**bject) ;
    * `.dylib` : sous Mac OS X (**Dy**namic **Lib**rary) ;
    * `.dll` : sous Microsoft Windows (**D**ynamically **L**inkable **L**ibraries).

Notre fameuse bibliothèque mathématique se nomme **libm** et est une bibliothèque statique. Celle-ci ne se lie au programme que sous les systèmes de type UNIX et GNU/Linux (Windows le fait automatiquement).

### Lier une bibliothèque ###

À savoir, il est courant de voir sur la toile la traduction anglaise du verbe lier : *link*. Certains parlent même de "*linkage* d'une bibliothèque", et utilisent l'expression "J'ai *linké* la bibliothèque mathématique". En bon francophiles, nous allons utiliser le terme *lier* par la suite.

Afin de lier une bibliothèque sous GCC et MinGW, on procède ainsi :

```console
-l<bibliothèque>
```

Si vous compilez en ligne de commande, cela donnera dans notre cas :

```console
gcc main.c -lm    # m comme mathématiques
```

Pour lier une bibliothèque, il faut d'abord mettre les fichiers au bon endroit. S'il s'agit d'une bibliothèque statique, il faut la mettre dans le bon dossier. Nous avons alors deux choix. Le premier, c'est de mettre tous les fichiers dans le dossier du compilateur.

* Avec **Code::Blocks**, il faut la mettre dans le dossier `lib` situé dans le répertoire du compilateur.	
  * Avec **Visual C++**, il faut la mettre dans le dossier `C:\Program Files (x86)\Microsoft Visual Studio xx.x\VC\lib`.
  * Avec **xCode**, il faut la mettre dans le dossier ```<Racine Disque>/Bibliothèque/Frameworks```.
* Pour ceux qui compilent **à la main**, il suffit d'ajouter les fichiers dans le dossier `lib` du compilateur.

Ça semble logique, mais c'est assez embêtant : on se retrouve avec des dossiers remplis de bibliothèques dont on ne sait plus d'où elles viennent, désinstaller un logiciel demande de sauvegarder toutes les bibliothèques installées, etc. Bref, pas très pratique. Pour pallier à ces problèmes, il y a une deuxième solution : on crée un dossier indépendant, dans lequel on crée un sous-dossier par bibliothèque. Cela permet de bien organiser ses fichiers, d'être indépendants des logiciels utilisés et est plus facile à entretenir. Le choix de la méthode est votre.

Si au contraire il s'agit d'une bibliothèque dynamique, c'est tout simple, celle-ci doit être mise dans le répertoire du projet. 

Ensuite, il faut modifier les propriétés du projet pour qu'il lie bien la bibliothèque au projet. La méthode varie selon que vous êtes avec :

* **Code::Blocks** : Ouvrez ou créez un projet puis allez dans *Project -> Build options -> Linker settings -> Other linker options*, insérez ensuite tout le texte nécessaire dans la zone de texte.	
* **Visual Studio** : Il suffit de rajouter la ligne suivante chaque fois que vous voulez lier une bibliothèque, en remplaçant *non_de_la_lib* par le nom de la bibliothèque à linker.

```c
#pragma comment (lib, "nom_de_la_lib.lib")
```

Il est également possible de l'ajouter comme élément du projet.

### Découvrir <math.h>
Nous allons maintenant étudier la bibliothèque mathématiques du langage C afin que vous sachiez quoi faire par la suite dans le TP. Le fichier d'en-tête de cette bibliothèque se nomme ```<math.h>``` contient un certain nombre de déclarations de fonctions mathématiques ainsi qu'une macro. Vous le savez, tout comme ```<stdio.h>``` ou ```<stdlib.h>```, on inclue le fichier d'en-tête mathématiques de cette manière :

```c
#include <math.h>
```

La norme C89 précise que la bibliothèque mathématique est composée d'une macro et de 22 fonctions. Cependant, je vous présenterai seulement les fonctions les plus connues et les plus utiles.

### Une macro utile ###

Pour commencer, nous allons rapidement parler de la macro *HUGE_VAL*, qui représente la valeur de type ```double``` la plus élevée que l'ordinateur peut gérer. Cette valeur dépend de la machine de l'utilisateur. Cette macro est principalement utilisée lors des retours de fonctions afin de savoir si ces dernières se sont bien exécutées.

### Sinus, cosinus et tangente ###

Les premières fonctions disponibles dans cette bibliothèque sont les fonctions trigonométriques *sinus*, *cosinus*, et *tangente*. Cela doit vous rappeler quelque chose que vous avez vu dans vos cours de mathématiques. Les prototypes de ces trois fonctions sont les suivants :
​	
* ```double sin(double x);```	
* ```double cos(double x);```
* ```double tan(double x);```

Ces fonctions prennent un nombre réel en radians et retournent un résultat appartenant à l'intervalle $[-1 ; +1]$

Voici un exemple d'utilisation.

```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    double x, y, z;

    x = sin(0.028);
    y = cos(0.028);
    z = tan(0.028);

    printf("x = %.10f\ny = %.10f\nz = %.10f", x, y, z);
    return 0;
}
```
```console
x = 0.0279963415
y = 0.9996080256
z = 0.0280073196
```

Comme vous pouvez le voir, j'ai indiqué à la fonction *printf* la précision, c'est-à-dire le nombre de chiffres après la virgule que je souhaite afficher.

### Mesurer un angle ###

Si les fonctions sinus, cosinus et tangente sont disponibles, c'est aussi le cas de leurs fonctions réciproques, à savoir arc-sinus, arc-cosinus et arc-tangente :

* ```double asin(double x);```	
  * ```double acos(double x);```
* ```double atan(double x);```

Ces fonctions attendent un paramètre appartenant à $ [-1 ; +1]$ et retournent un résultat appartenant à $\left[ frac{-\pi}{2} ; frac{+\pi}{2} \right]$. 

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double x, y, z;

    x = asin(0.0279963415);
    y = acos(0.9996080256);
    z = atan(0.0280073196);

    printf("x = %f\ny = %f\nz = %f\n", x, y, z);
    return 0;
}
```
```console
x = 0.028000
y = 0.028000
z = 0.028000
```

### Logarithmes ###
Commençons par les fonctions concernant les logarithmes. Je nomme *log* et *log10* :

* ```double log(double x);```	
* ```double log10(double x);```

Comme la plupart des fonctions de la bibliothèque mathématique, elles  prennent comme argument un ```double``` et renvoient un ```double<```. La fonction *log* renvoie le logarithme népérien du nombre passé en paramètre, alors que *log10* renvoie le logarithme en base 10. Bien entendu, le paramètre doit appartenir  à $] 0 ; +\infty [$ ; la fonction retourne alors un résultat appartenant à $\mathbb{R}$.

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double x, y, z;

    x = log(4242);
    y = log10(4242);
    z = log10(1000000);

    printf("x = %f\ny = %f\nz = %f\n", x, y, z);
    return 0;
}
```
```console
x = 8.352790
y = 3.627571
z = 6.000000
```

### Exponentielle ###

Passons à la fonction *exp*, qui prend un nombre réel et renvoie un résultat appartenant à $] 0 ; +\infty [$. Simple précaution : cette fonction ayant une croissance très rapide, attention si vous manipuler de grands nombres à ne pas dépasser la capacité maximale d'un ```double```.

```c
double exp(double x);
```

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double x = exp(3);
    printf("x = %f\n", x);
    return 0;
}
```
```console
x = 20.085537
```

### Puissances ###

Étudions maintenant la fonction *pow*.

```c
double pow(double x, double y);
```

Elle élève le nombre *x* à la puissance *y* ($x^y$). Cette fonction est très lourde et lente à l’exécution, je vous recommande donc de ne pas l'utiliser pour les calculs de faibles puissances. Mais, pourquoi cette fonction est-elle si lente ? La raison est simple : elle est très puissante, puisque elle gère les nombres et les exposant négatifs, ce qui n'est pas une mince affaire. 

Cependant, il existe quelques cas que *pow* est incapable de gérer.

* Il n'est pas possible de lui fournir un nombre négatif et un exposant fractionnaire sans quoi vous lui demandez de calculer la racine d'un nombre négatif (ce qui est impossible dans le cas de nombres réels).
  * Il n'est pas possible de lui passer un nombre nul et un exposant nul en même temps ($0^0$ n'est pas calculable).
* Il n'est pas possible de lui transmettre un nombre nul et un exposant négatif sans quoi vous lui demandez de diviser un nombre par zéro (ce qui est mathématiquement impossible).

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double x, y, z;

    x = pow(5, 2);
    y = pow(2, -2);
    z = pow(3.14, 4);

    printf("x = %f\ny = %f\nz = %f\n", x, y, z);
    return 0;
}
```
```console
x = 25.000000
y = 0.250000
z = 97.211712
```

### Racine carrée ###

L'en-tête ```<math.h>``` fournit aussi une fonction de calcul de la racine carrée d'un nombre. Ils 'agit de la fonction *sqrt*. Son prototype est le suivant : 

```c
double sqrt(double x);
```

La fonction *sqrt* renvoie la racine carrée du réel positif passé en paramètre. Elle renverra une erreur si vous tentez de calculer la racine carrée d'un réel négatif.

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double x = sqrt(25);
    printf("x = %f\n", x);
    return 0;
}
```
```console
x = 5.000000
```

### Fonctions d’arrondis ###

Cette rapide présentation de la bibliothèque mathématiques standard du C touche à sa fin, il ne nous reste plus qu'une poignée de fonctions à voir, notamment les fonctions d'arrondis.

* ```double ceil(double x);```
* ```double floor(double x);```

La première, *ceil*, renvoie la partie entière supérieure du nombre *x*. À l'inverse, la fonction *floor* la partie entière inférieure du nombre passé en paramètre. Voici un petit code d'exemple :

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double x, y;

    x = ceil(42.7);
    y = floor(42.7);

    printf("x = %f\ny = %f\n", x, y);
    return 0;
}
```
```console
x = 43.000000
y = 42.000000
```

### Autres fonctions sur les flottants ###

Il nous reste ensuite quelques fonctions restantes, inclassables. J'ai nommé :

* ```double fabs(double x);```
* ```double fmod(double x, double y);```

La fonction *fabs* retourne la valeur absolue de *x*, soit $|x|$. Pour ceux qui ne connaissent pas, la valeur absolue d'un nombre représente la partie numérique de ce dernier.

*$|1| = 1$	
*$|-42|= 42$

Pour finir la fonction *fmod* quand à elle, divise *x* par *y* puis renvoie le reste. Pour simplifier, elle effectue un modulo sur deux flottants. Elle est utile car le langage C ne nous autorise pas à utiliser l'opérateur % sur des flottants.

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double x, y;

    x = fabs(-7);
    y = fmod(42, 5);

    printf("x = %f\ny = %f\n", x, y);
    return 0;
}
```
```console
x = 7.000000
y = 2.000000
```

### TP : Recodons des fonctions mathématiques
Fini la théorie, place à la pratique ! Votre mission, si vous l'acceptez : recoder quelques fonctions de la bibliothèques mathématiques, que vous connaissez bien désormais. Bien entendu, je vous aiderai à chaque fois en vous expliquant l’algorithme à utiliser par exemple. Enfin, avant de commencer, je vous livre une petite astuce : pour tester si votre fonction fonctionne correctement, pourquoi ne pas la comparer avec celle de la bibliothèque standard ? Et pour ce faire, pourquoi ne pas créer une **macro** qui donnerait le résultat retourné par votre fonction et par celle de la bibliothèque standard ?

### Racine carrée ###

La première fonction que nous allons recoder est la racine carrée d'un réel positif. Pour cela, nous allons utiliser un très vieil algorithme appelé [la méthode de Héron](https://fr.wikipedia.org/wiki/Méthode_de_Héron), du nom du mathématicien grec qui l'a découverte. 

Cette méthode est relativement simple : pour trouver $\sqrt{A}$, on prend un nombre au hasard qu'on nomme $x_{n}$, et on utilise cette formule : $x_{n+1} = \frac{x_n + \frac{A}{x_n}}{2}$. Il suffit de répéter cette opération plusieurs fois, en remplaçant $x_{n}$ par la valeur calculée au tour d'avant. En faisant ainsi, le résultat converge vers $\sqrt{A}$, la précision dépendant du nombre de répétitions de la récurrence. On doit calculer cette suite jusqu’à ce qu'on aie atteint une précision suffisante.

Vous avez maintenant toutes les clefs en main pour recoder la fonction *sqrt*. Si vous avez du mal, jetez un œil à l'algorithme se trouvant [ici](http://paste.awesom.eu/informaticienzero/RXe&ln). Quant à ceux qui veulent comparer leur code à la correction, en voici [une](http://paste.awesom.eu/informaticienzero/PQs&ln). Testez donc si les valeurs retournées sont correctes.

### Exponentielle ###

La deuxième fonction que nous allons faire sera l'exponentielle de base $e$, notée $\exp(x)$ ou $e^x$. Une implémentation naïve serait d'utiliser la fonction *pow*. C'est une idée, facile et rapide à coder, mais pas très optimisée : en effet, *pow* est une fonction assez lourde, autant choisir une autre solution : le [développement limité](http://fr.wikipedia.org/wiki/Développement_limité).

La formule est la suivante : $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \ldots+ \frac{x^n}{n!} + o(x^n)$. En gros, on doit calculer cette somme jusqu’à ce qu'on aie atteint une précision suffisante. Pour ceux qui ne savent pas, $n!$ est [la factorielle](http://fr.wikipedia.org/wiki/Factorielle) d'un nombre et vaut $1 \times 2 \times 3 \times \ldots \times (n - 1) \times n$ soit $\prod_{i = 0}^n i$.

Avant de vous lancer, je vous donne une dernière astuce : vous n'avez pas besoin de la fonction *pow*, ni de faire une fonction calculant la factorielle d'un nombre. Bon courage, vous pouvez y arriver !

[secret]{
Si vous ne voyez pas comment se passer de *pow* ou d'une fonction factorielle, dîtes-vous qu'il n'est pas nécessaire de recalculer toutes les puissances à chaque fois. En effet, $x^{n+1} = x^n \times x$. Il suffit de connaître $x^n$. Le principe est le même pour la factorielle : $(x+1)! = x! \times (x + 1)$.
}

Pour ceux qui auraient besoin, l'algorithme est disponible [à cette adresse](http://paste.awesom.eu/informaticienzero/IkA&ln). Enfin, pour ceux qui ont fini ou qui veulent s'aider de la correction, elle se trouve [ici](http://paste.awesom.eu/informaticienzero/O96&ln).

### Autres ###

Pour votre information, le calcul des fonctions logarithme, sinus, cosinus, tangente, et leurs réciproque, peut s'effectuer aussi avec des développements limités. Les formules sont facilement trouvables sur la toile : Wikipédia est votre allié.

Ce chapitre a peut-être été indigeste pour ceux qui détestent les maths, mais au moins il nous a permit d'apprendre de nouvelles fonctions et de découvrir le principe des bibliothèques. Et puis dites vous que faire des maths de temps en temps n'a jamais tué personne.

## La gestion d'erreur
Dans les chapitres précédents, nous vous avons présenté des exemples simplifiés afin de vous familiariser avec le langage. Aussi, nous avons pris soin de ne pas effectuer de vérification quant à d'éventuelles rencontres d'erreurs. 

Mais à présent : c'est fini ! Vous disposez désormais d'un bagage suffisant pour affronter la dure réalité d'un programmeur : des fois, il y a des trucs qui foirent et il est nécessaire de le prévoir. Nous allons voir comment dans ce chapitre.

### Détection des erreurs
La première chose à faire pour gérer d'éventuelles erreurs lors de l'exécution, c'est avant tout de les détecter. Par exemple, quand vous executez une fonction, et qu'une erreur a lieu lors de son exécution, celle-ci doit vous prévenir d'une manière ou d'une autre. Et elle peut le faire de deux manières différentes.

### Valeurs de retour

Peut-être l'avez vous déjà remarqué : certaines fonctions, comme *scanf*() et *printf*(), retournent un nombre (souvent un entier) alors que nous n'attendons finalement aucune valeur de celles-ci. Pourquoi diable ces dernières retournent-elles quelque chose alors qu'elles ne calculent par exemple pas un résultat comme la fonction *pow*() ? *Hé* bien, je vous le donne en mille : ces valeurs servent en fait à vous signifier si l'exécution de la fonction s'est bien déroulée. 

#### Scanf

Prenons l'exemple de la fonction *scanf*() : cette dernière retourne le nombre de conversions réussies ou un nombre inférieur si elles n'ont pas toutes été réalisée ou enfin un nombre négatif en cas d'erreur.

Ainsi, si nous souhaitons récupérer deux entiers et être certains que *scanf*() les a récupéré, nous pouvons utiliser le code suivant :

```c
#include <stdio.h>


int main(void)
{
    int x;
    int y;

    printf("Entrez deux nombres : ");
    if (scanf("%d %d", &x, &y) == 2)
    {
        printf("Vous avez entre : %d et %d\n", x, y);
    }
    return 0;
}
```

```text
Entrez deux nombres : 1 2
Vous avez entre : 1 et 2

Entrez deux nombres : 1 a
```

Comme vous pouvez le constater, le programme n'exécute pas l'affichage des nombres dans les deux derniers cas, car *scanf*() n'a pas réussi à réaliser deux conversions.

#### Main

Maintenant que vous savez cela, regarder bien votre fonction *main*() :

```c
int main(void)
{
    return 0;
}
```

Vous ne voyez rien qui vous interpelle ? :)

Oui, vous avez bien vu, elle retourne un entier qui, comme pour *scanf*(), sert à indiquer la présence d'erreur. En fait, il y a deux valeurs possibles : 

- EXIT_SUCCESS (ou zéro, cela revient au même), qui indique que tout s'est bien passé ; et
- EXIT_FAILURE, qui indique un échec du programme.

Ces deux constantes sont définies dans l'en-tête **<stdlib.h\>**).

#### Les autres fonctions

Sachez que *scanf*(), *printf*() et *main*() ne sont pas les seules fonctions qui retournent des entiers, en fait quasiment toutes les fonctions de la bibliothèque standard le font.

-- *Ok, mais je fais comment pour savoir ce que retourne une fonction ?*

À l'aide de la documentation. Vous disposez de [la norme](http://flash-gordon.me.uk/ansi.c.txt) (enfin, du brouillon de celle-ci) qui reste la référence ultime, sinon vous pouvez également utiliser un moteur de recherche avec la requête `man nom_de_fonction` afin d'obtenir les informations dont vous avez besoin.

**Note :**

1. Si vous êtes anglophobe, une traduction française de diverses descriptions est disponible à [cette adresse](http://perkamon.traduc.org/), vous les trouverez à la section trois.

### Variable globale errno

Le retour des fonctions est un vecteur très pratique pour signaler une erreur. Cependant, il n'est pas toujours utilisable. En effet, nous avons vu au chapitre précédent différentes fonctions mathématiques. Or, ces dernières utilisent *déjà* leur retour pour transmettre le résultat d'une opération. Comment faire dès lors pour signaler un problème ?

Une première idée serait d'utiliser une valeur particulière, comme zéro par exemple. Toutefois, ce n'est pas satisfaisant puisque, par exemple, les fonctions *pow*() ou *sin*() peuvent parfaitement retourner zéro lors d'un fonctionnement normal. Que faire alors ?

Dans une telle situation, il ne reste qu'une seule solution : utiliser un autre canal, en l'occurrence une variable globale. La bibliothèque standard fourni une variable globale nomée *errno* (elle est déclarée dans l'en-tête **<errno.h\>**) qui permet à différentes fonctions d'indiquer une erreur en modifiant la valeur de celle-ci.

**Note :**

1. Une valeur de zéro indique qu'aucune erreur n'est survenue.

Les fonctions mathématiques recourent abondamment à cette fonction. Prenons l'exemple suivant :

```c
#include <errno.h>
#include <stdio.h>


int main(void)
{
    double x;

    errno = 0;
    x = pow(-1, 0.5);
    if (errno == 0)
    {
        printf("x = %f\n", x);
    }
    return 0;
}
```

Le calcul demandé revient à demander le résultat de l'expression $-1^\frac{1}{2}$, autrement dit, de cette expression : $\sqrt{-1}$, ce qui est impossible dans l'essemble des réels. Aussi, la fonction *pow*() modifie la variable *errno* pour vous signifier qu'elle n'a pas pu calculer l'expression demandée.

Une petite précision concernant ce code et la variable *errno* : celle-ci doit *toujours* être mise à zéro *avant* d'appeler une fonction qui est susceptible de la modifier, ceci afin de vous assurez qu'elle ne contient pas la valeur qu'une autre fonction lui a assignée. Imaginez que vous ayez auparavant appelé *pow*() et que cette dernière à échoué, si vous l'appelez à nouveau, la valeur de *errno* sera toujours celle assignée par lors de l'appel précédent.

**Note :**

1. La bibliothèque standard ne prévoit en fait que deux valeurs d'erreur possibles pour *errno* : EDOM (pour le cas où le résultat d'une fonction mathématique est impossible) et ERANGE (en cas de dépassement de capacité, nous y reviendrons plus tard). Ces deux constantes sont définies dans l'en-tête **<errno.h\>**.

### Prévenir l'utilisateur
Savoir qu'une erreur s'est produite, c'est bien, le signaler à l'utilisateur, c'est mieux. Ne laisser pas votre utilisateur dans le vide, s'il se passe quelque chose, dite le lui.

```c
#include <stdio.h>

int main(void)
{
    int x;
    int y;

    printf("Entrez deux nombres : ");
    if (scanf("%d %d", &x, &y) == 2)
    {
        printf("Vous avez entre : %d et %d\n", x, y);
    }
    else
    {
        printf("Vous devez saisir deux nombres !\n");
    }
    return 0;
}
```

```text
Entrez deux nombres : a b
Vous devez saisir deux nombres !

Entrez deux nombres : 1 2
Vous avez entre : 1 et 2
```

Simple, mais tellement plus agréable. ;)

Dans l'exemple situé plus haut, nous avons affiché les messages d'erreurs à grand coup de printf(). Nous verrons plus tard dans le tutoriel qu'il existe d'autres façons un peu plus propres d'afficher des messages d'erreurs. Nous ne pouvons pas en dire plus pour le moment, vu qu'il nous faudrait aborder les notions de flux (et notamment le flux stderr),ce qui ne peut être fait que bien plus tard dans ce cours.

### Un exemple d'utilisation des valeurs de retour
Maintenant que vous savez tout cela, il vous est possible de modifier le code utilisant la fonction *scanf*() pour vérifier si celle-ci a réussi et, si ce n'est pas le cas, préciser à l'utilisateur qu'une erreur est survenue *et* quitter la fonction *main*() en retournant la valeur EXIT_FAILURE.

```c
#include <stdio.h>


int main(void)
{
    int x;
    int y;

    printf("Entrez deux nombres : ");
    if (scanf("%d %d", &x, &y) != 2)
    {
        printf("Vous devez saisir deux nombres !\n");
        return EXIT_FAILURE;
    }
    printf("Vous avez entre : %d et %d\n", x, y);
    return 0;
}
```

Ceci nous permet de réduire un peu la taille de notre code en éliminant directement les cas d'erreurs.

Bien, vous voilà à présent fin prêt pour la deuxième partie du cours et ses *vrais* exemples. Plus de pitié donc : gare à vos fesses si vous ne vérifiez pas le comportement des fonctions que vous appeler !

Cette première partie nous a présenté de nombreuses notions, n'hésitez pas à la relire si vous en ressentez le besoin. Cependant, le C ne se limite pas qu'à ces notions de bases. En effet, il existe des concepts plus poussés, plus complexes mais plus puissants que nous allons découvrir dans la partie 2.

# Les agrégats
Dans cette seconde partie, nous allons aborder des aspects du C certes plus complexes mais aussi beaucoup plus puissants que ceux que nous avons vu : les **agrégats**, c'est à dire un regroupement de plusieurs notions différentes. Ne soyez pas rebutés s'il y a des choses que vous ne comprenez pas de prime abord : c'est normal, tout le monde est passé par là. Relisez à tête reposée, testez, lisez sur Internet, bref, ne restez pas bloqués. Vous verrez que le jeu en vaut la chandelle puisque nous pourrons faire beaucoup plus de choses dans nos programmes avec ces nouveaux concept !

## Les pointeurs
Bon, dans les chapitres précédents, on a vu pas mal de choses : comment créer et utiliser des variables, des structures de contrôle, ou des fonctions. Ces opérations sont assez basiques, et on n'est pas vraiment rentré dans le vif du sujet. Mais maintenant, cela va changer !

Nous allons aborder les pointeurs, un mécanisme du langage C qui fait peur à certains. Pourtant, elle est derrière une grande partie des fonctionnalités des langages de programmation actuels : on en trouve partout ! Le C n'échappe pas à cette règle, et les pointeurs sont une fonctionnalité majeure du langage. Mais contrairement au langage C, la plupart des langages les cachent et les camouflent plus ou moins efficacement. Il faut dire que les pointeurs ont une très mauvaise réputation : ils seraient difficiles à comprendre, difficiles à maitriser, et d'une complexité qui ferait fuir tous les débutants. Mais il s'agit bien évidemment d'idées reçues.

La raison à cette mauvaise réputation qu'ont les pointeurs est simple : les pointeurs sont ce qu'on appelle une **fonctionnalité bas niveau**. En clair, il s'agit d'un mécanisme qui nécessite de comprendre quelques détails sur le fonctionnement d'un ordinateur pour être comprise ou utilisée correctement. En effet, pour comprendre les pointeurs, il suffit de comprendre un tout petit peu ce qu'est la mémoire RAM. Rien de bien compliqué : seuls quelques rappels suffiront. Vous allez voir, contrairement à ce qu'on pense, ces pointeurs ne sont pas compliqués : c'est même le contraire !

### C'est quoi ?
Tout d'abord, nous allons devoir parler de l'utilité de ces pointeurs. Et quelques rappels sont nécessaires.

### Utilité ###

Comme nous l'avons vu dans le chapitre sur les variables, une donnée est stockée dans une **mémoire** bien particulière de notre ordinateur : registre, RAM, etc. Seulement, pour pouvoir utiliser cette donnée, nous avons besoin de savoir où elle se situe exactement dans la mémoire. Ce moyen s'appelle une **référence**. 

Nos variables simples, comme des ```int```, ```float```, ```double```, ou ```char``` individuels sont directement gérées par le compilateur, qui les charge le plus souvent dans les registres. On n'a pas besoin de manipuler de références vers ces derniers : les noms de variables suffisent pour le programmeur.

#### Créations de structures de données ####

Mais pour les autres données, c'est une autre histoire. Eh oui : en C, il est possible d'utiliser des données plus grosses que des simples variables. Ces données complexes sont crées en regroupant ensemble des variables de type ```int```, ```float```, ```double```, ou ```char```.

L'ensemble est souvent trop gros pour être stocké dans des registres, et est placé en mémoire RAM. Conséquence : on ne peut pas manipuler ces regroupements directement, et on est obligé de manipuler les variables élémentaires unes par unes, ce qui demande de connaitre la position en RAM de celles-ci.

#### Allocation dynamique ####

Enfin, il faut savoir qu'il est possible de réserver temporairement une portion inutilisée de la mémoire pour stocker temporairement des données ou des variables. Quand on n'a plus besoin de cette portion de mémoire, il la libère, et elle sera réutilisable à volonté. C'est ce qu'on appelle l'allocation dynamique. Le seul problème, c'est que l'emplacement de la portion de mémoire change à chaque réservation. On doit donc se souvenir de cet emplacement, sans quoi le manipuler sera impossible. Et c'est encore une fois au programmeur de gérer cela, du moins en partie.

#### Passage de données complexes en argument de fonctions ####

Autre exemple : si je veux qu'une fonction manipule une donnée, je peux passer celle-ci en argument de ma fonction. Elle sera alors recopiée, et ma fonction manipulera la copie. Dans certains cas, on voudra programmer une fonction qui modifie directement l'original et non une copie. Mais pour envoyer l'original à notre fonction, on doit dire à notre fonction où est l'original dans la mémoire.

### La RAM ###

Bref, c'est (entre autres) à cela que servent les pointeurs : ils servent à donner l'emplacement en mémoire RAM d'une donnée précise pour qu'on puisse la manipuler. Reste à savoir comment ils font.

Dans notre RAM, les données sont découpées en "paquets" contenant une quantité fixe de bits : des "**cases mémoires**", aussi appelées *bytes*. Généralement, nos mémoires utilisent un byte de 8 bits, aussi appelé **octet**. Avec un octet, on peut stocker 256 informations différentes. Pour stocker plus d’informations (par exemple les nombres de -1024 à 1023), on peut utiliser plusieurs octets, et répartir nos informations dedans. Nos données peuvent prendre un ou plusieurs octets qui se suivent en mémoire, sans que cela pose problème : nos mémoires et nos processeurs sont conçus pour gérer ce genre de situations facilement. En effet, nos processeurs peuvent parfaitement aller lire 1, 2, 3, 4, etc. octets consécutifs d'un seul coup sans problème, et les manipuler en une seule fois. Mais cela ne marche que pour des données simples.

Chacun de ces octets se voit attribuer un nombre unique, **l'adresse**, qui va permettre de la sélectionner et de l'identifier celle-ci parmi toutes les autres. Il faut imaginer la mémoire RAM de l'ordinateur comme une immense armoire, qui contiendrait beaucoup de tiroirs (les cases mémoires) pouvant chacun contenir un octet. Chaque tiroir se voit attribuer un numéro pour le reconnaitre parmi tous les autres. On pourra ainsi dire : je veux le contenu du tiroir numéro 27 ! Pour la mémoire c'est pareil. Chaque case mémoire a un numéro : son adresse.


| Adresse | Contenu mémoire    |
| ------- | ------------------ |
| 0       | 11101010 01011010  |
| 1       | 01111111 01110010< |
| 2       | 00000000 01111100  |
| 3       | 01010101 0000000<  |
| 4       | 10101010 00001111  |
| 5       | 00000000 11000011  |

En fait, on peut comparer une adresse à un numéro de téléphone (ou à une adresse d'appartement) : chacun de vos correspondants a un numéro de téléphone et vous savez que pour appeler telle personne, vous devez composer tel numéro. Ben les adresses mémoires, c'est pareil !

![Exemple : on demande à notre mémoire de sélectionner la case mémoire d'adresse 1002 et on récupère son contenu (ici, 17)](http://uploads.siteduzero.com/files/379001_380000/379202.png)

### Pointeurs ###

Nous y voilà : ce qu'il nous faut, c'est donc réussir à stocker l'adresse mémoire à laquelle commence une donnée, et la manipuler comme bon nous semble. Pour cela, on a inventé les **pointeurs** : ce sont des variables dont le contenu est une adresse mémoire. 

![Exemple, avec une variable a qui est un pointeur sur une variable b](http://uploads.siteduzero.com/files/382001_383000/382908.png)

C'est aussi simple que cela. Leur utilité ne semble pas évidente au premier abord, mais sachez que cela deviendra plus clair après quelques exemples. De plus, nous utiliserons beaucoup les notions vues dans ce chapitre une fois qu'on parlera des tableaux et des structures de données. Cela ne se voit pas au premier abord, mais les pointeurs sont importants dans le langage C.

### Utilisation
Avant de rentrer dans le vif du sujet, il faut encore faire quelques remarques sur nos fameux pointeurs. Cette fois-ci, on va rentrer vraiment dans la pratique : finie la théorie, on va parler de choses spécifiques au langage C.

En C, les pointeurs sont typés : les pointeurs qui stockent l'adresse d'un ```int``` ou d'un ```char``` seront différents. C'est comme ça, les pointeurs vont stocker les adresses mémoires d'une donnée simple, qui peut être un ```int```, un ```char```, un ```float``` ou un ```double```. Le type du pointeur sert à préciser si l'adresse contenue dans ce pointeur est l'adresse d'un ```int```, d'un ```char```, d'un ```float```, etc.

Vous vous demandez surement à quoi peut bien servir cette bizarrerie. Tout ce que je peux dire pour le moment, c'est que c'est dû au fait que des données de type différent n'occuperont pas la même quantité de mémoire : suivant la machine, un ```int``` peut ne pas avoir la même taille qu'un ```short```, par exemple. Pour éviter les ennuis lors des manipulations de pointeurs, les pointeurs sont donc typés. Vous verrez quand on abordera l'arithmétique des pointeurs : on devra calculer des adresses mémoires, et la taille des types jouera beaucoup lors de ces calculs. Vous comprendrez alors l'utilité du typage des pointeurs.

### Déclaration ###

Pour déclarer un pointeur, il suffit de lui donner un nom, et de préciser son type, c'est-à-dire le type de la donnée dont on stocke l'adresse dans le pointeur. La syntaxe de la déclaration est celle-ci :

```c
type * nom_du_pointeur;
```

Par exemple, si je veux créer un pointeur sur un ```int``` (c'est-à-dire un pointeur pouvant stocker l'adresse d'une variable de type ```int```) et que je veux le nommer *ptr*, je devrais écrire ceci :

```c
int * ptr;
```

#### Un pointeur particulier ####

Nous venons de dire qu'un pointeur devait forcément pointer sur un objet d'un type donné. A priori, il semble impossible de faire un pointeur qui pourrait pointer sur n'importe quel type d'objet sans problème. Pourtant, les concepteurs de la norme C89 ont pensé à nous : ils ont introduit un pointeur un peu spécial appelé **pointeur universel** : ```void *```. Ce dernier peut se voir assigner n'importe quel type de pointeur et peut lui-même être converti en n'importe quel type de pointeur.

```c
int * p = 0;
void * uni = p; /* (int *) -> (void *) */
int * q = uni; /* (void *) -> (int *) */
```

Dans cet exemple, le pointeur `uni` se voit assigner un pointeur sur `int` et est ensuite assigner au pointeur `q` sans que cela pose le moindre problème. __Faites attention cependant__ : un pointeur générique ne peut pas être déréférencé (voyez la section qui y est dédiée un peu plus bas), il doit faire l'objet d'une conversion explicite auparavant.

Pour la touche culturelle, sachez qu'avant l'apparition de la norme C89 le pointeur universel n'existait pas. On utilisait à la place un pointeur sur ```char```.

### Référencement ###

Le référencement est une opération qui permet de récupérer l'adresse d'un objet. Pour se faire, il suffit de placer l'opérateur ```&``` devant la variable dont on souhaite récupérer l'adresse. Pour l'afficher, on utilise *printf* avec un nouvel indicateur de conversion : ```%p``` qui affiche le résultat en hexadécimal. Il y a cependant une petite contrainte : il faut convertir le pointeur en ```void*```.

```c
int ma_variable;
printf("Adresse de ma_variable : %p\n", (void *)&ma_variable);
```
```console
Adresse de ma_variable : 0x7fff9ee178ac
```

Cette valeur change à chaque exécution, ne vous inquiétez pas si vous n'obtenez pas le même résultat que moi. 

### Initialisation et pointeur  nul  ###

Un pointeur, comme une variable, ne possède pas de valeur par défaut. Il pointe donc sur n'importe quoi, n'importe où en mémoire. Il est donc important de l'initialiser pour éviter d'éventuels problèmes. Pour se faire, il y a deux possibilités : soit l'initialiser à une valeur nulle, soit l'initialiser avec une adresse.

#### Initialisation avec une adresse valide ####

Pour commencer, on peut initialiser un pointeur avec une adresse, que ce soit celle d'une variable ou le retour d'une fonction renvoyant un pointeur.

```c
int ma_variable = 10;
int *mon_pointeur;
mon_pointeur = &ma_variable;
```

Ou même ainsi :

```c
int ma_variable = 10;
int *mon_pointeur = &ma_variable;
```

#### Pointeur NULL ####

Mais il arrive qu'on doive déclarer un pointeur sans savoir quelle adresse mettre dedans, cette adresse étant disponible plus tard, plus loin dans le code. Dans ce cas, on peut donner une valeur particulière au pointeur pour faire en sorte qu'il ne pointe nulle part et qu'il soit considéré comme invalide. Cette valeur particulière s'appelle *NULL*.

```c
/* maintenant ptr est un pointeur invalide */
int * ptr = NULL;
```

### Déréférencement ###

S'il est possible de récupérer l'adresse d'un objet grâce au référencement, il est également possible d'accéder et de modifier cet objet grâce au **déréférencement**. Sans cette possibilité, les pointeurs n'auraient aucune utilité.

Cette opération se fait avec l’opérateur ```*```. Avec la syntaxe ```*mon_pointeur```, nous avons accès à la donnée contenue à l'adresse de *mon_pointeur* aussi bien en lecture qu'en écriture. C'est le cas dans le premier exemple ci-dessous où l'on affecte à une variable la valeur du contenu du pointeur, c'est-à-dire la valeur de *ma_variable*.

```c
int a = 0;
int ma_variable = 10;
int *mon_pointeur = &ma_variable;

a = *mon_pointeur ;

printf("Valeur contenue a l'adresse '%p' : %d\n", (void *)mon_pointeur, a);
```
```console
Valeur contenue à l'adresse '0x7ffa2ee591a7' : 10
```

Dans le deuxième exemple, on modifie la valeur de l'objet pointé par *mon_pointeur*, c'est à dire qu'indirectement on modifie *ma_variable*.

```c
int ma_variable = 10;
int *mon_pointeur = &ma_variable;

printf("Valeur contenue à l'adresse '%p' : %d\n", (void *)mon_pointeur, *mon_pointeur);

*mon_pointeur = 20;

printf("Valeur contenue à l'adresse '%p' : %d\n", (void *)mon_pointeur, *mon_pointeur);
```
```console
Valeur contenue à l'adresse '0028FF18' : 10
Valeur contenue à l'adresse '0028FF18' : 20
```

### Des pointeurs comme arguments dans des fonctions ###

Il existe deux manières d'utiliser les pointeurs avec les fonctions. Voici la première :

```c
#include <stdio.h>

void ma_fonction(int *mon_pointeur)
{
    *mon_pointeur = 20;
}

int main(void)
{
    int ma_variable = 10;
    ma_fonction(&ma_variable);

    printf("Valeur de ma_variable : %d\n", ma_variable);
    return 0;
}
```

Là, il n'y a rien de très difficile : on envoie l'adresse de *ma_variable* à *ma_fonction* puis celle-ci modifie la valeur de *ma_variable* directement en mémoire par l'intermédiaire de *mon_pointeur*.

Quel est l'intérêt d'utiliser les pointeurs à la place de ```return``` ? On peut par exemple modifier la valeur de plusieurs variables dans une fonction au lieu de ne pouvoir en modifier qu'une qu'on retourne.

Passons maintenant à la deuxième technique pour envoyer un ou plusieurs pointeurs à une fonction :

```c
#include <stdio.h>

void ma_fonction(int *mon_pointeur)
{
    *mon_pointeur = 20;
}

int main(void)
{
    int ma_variable = 10;
    int *mon_pointeur = &ma_variable;

    ma_fonction(mon_pointeur);

    printf("Valeur de ma_variable : %d\n", ma_variable);
    printf("Valeur contenue a l'adresse de mon_pointeur : %d\n", *mon_pointeur);
    return 0;
}
```

Sans exécuter ce code, essayez de deviner quel sera le résultat de ces deux *printf*. Trouvé ? Si ce n'est pas le cas, relisez entièrement et très attentivement ce chapitre. Voici le résultat attendu :

```console
Valeur de ma_variable : 20
Valeur contenue à l'adresse de mon_pointeur : 20
```

Un grand bravo à tous ce qui ont compris cela dès le premier coup ! Pour les autres, ne vous en faites pas, ça va venir petit à petit.

### Exercice
Pour le moment, vous vous dites surement que les pointeurs ne sont pas forcément nécessaires, et qu'on peut surement s'en passer. De nombreux débutants en C se disent cela, et c'est une des raisons qui fait que certains ne comprennent pas facilement les pointeurs. À ce stade du tutoriel, il sera difficile de vous montrer leur utilité, même si la suite du tutoriel vous prouvera le contraire.

Néanmoins, cet exercice va vous montrer que les pointeurs peuvent parfois être utiles. En effet, nos pointeurs sont utiles en argument des fonctions. C'est ainsi : dans une fonction, il est impossible de modifier les arguments : on ne fait que manipuler une copie de ceux-ci ! Si jamais notre fonction doit manipuler un ou plusieurs des arguments pour le modifier, on ne peut pas le faire avec une fonction. Du moins, pas sans nos pointeurs.

### Énoncés ###

Pour mieux comprendre, on va vous donner un exemple pratique. Vous aller devoir programmer une fonction nommé *swap*, qui va échanger le contenu de deux variables. Cette fonction ne semble pas bien méchante, mais sachez qu'elle est assez utilisée, mine de rien. Par exemple, si vous voulez trier un gros paquet de données, vous aurez absolument besoin de cette fonction. Mais je n'en dit pas plus. Quoiqu'il en soit, on va supposer que dans notre exemple, nos deux variables sont des ```int```.

Bonne chance !

### Correction ###

Celle-ci se trouve sur [à la même adresse que d'habitude](http://paste.awesom.eu/informaticienzero/cmb&ln).

Bref, nous en avons fini avec les pointeurs. Du moins, pour le moment. Car après tout, les pointeurs sont omniprésents en langage C et nous n'avons pas fini d'en entendre parler. Mais pour le moment, nous allons découvrir ces fameuses données complexes dont nous avons parlé en début de chapitre avec ce qu'on appelle les **structures**.

## Structures
Dans le chapitre précédent, nous avions dit que les pointeurs étaient utiles pour manipuler des données complexes. Les structures sont les premières que nous allons étudier. Qu'est ce qu'une structure ? Il s'agit d'un regroupement de variables différentes sous le même nom. En gros, une structure est une grosse boite qui regroupe plein de données différentes. 

Plein de parallèles avec le monde réel sont possibles. Prenez un salarié par exemple : il a un sexe, un âge, un salaire, un véhicule de fonction ou non, etc. Au lieu de créer une variable pour chaque donnée, on les regroupe toutes dans une sorte de "grosse variable" qui contient toutes les autres, la structure. Si cette illustration vous parait abstraite, lisez la suite qui montre une utilisation concrète en C.

### Déclaration, définition et initialisation
Pour gérer ces structures, on va devoir apprendre à en définir le contenu, puis à déclarer des variables de type structure et les initialiser. Commençons par la définition.

### Définition ###

Par définir une structure, nous ne voulons pas dire créer une variable qui soit une structure. Cela sera pour plus tard. Avant de créer des variables structurées, nous devons indiquer à notre compilateur comment est organisée la structure que l'on veut créer. Cela veut simplement dire quels sont les types des variables qu'on rassemble, comment est organisée la structure, etc. 

Le squelette de toute structure est le suivant :

```c
struct Identificateur
{
    /* les variables à déclarer */
};
```

Décortiquons le tout. Le mot-clef ```struct``` est important, il permet d'indiquer au compilateur que l'on déclare une structure. Notez également que le point-virgule à la fin est obligatoire, sinon vous aurez des erreurs à la compilation. Les objets que l'on défini dans le bloc de code vu au-dessus sont quant à eux appelés les **champs** ou les **membres** de la structure. Je suppose que vous vous demandez s'il y a une limite. Je laisse la norme vous répondre :

> The implementation shall be able to translate and execute at least one program that contains at least one instance of every one of the following limits :
>     127 members in a single structure or union
> -- C89 - 2.2.4.1 Translation limits

Ne vous inquiétez pas de cette limite, vous n'aurez sûrement jamais à déclarer une structure regroupant 127 variables ou plus.

Ensuite, il faut savoir qu'on initialise aucun membre à l'intérieur même de la structure. C'est interdit par le C. En effet, quand nous définissons une structure, aucune variable n'est en jeu : le compilateur ne réserve aucune place en mémoire. Il est donc insensé d'initialiser des variables qui n'existent pas en mémoire. Mais rassurez-vous, nous verrons plusieurs méthodes dans la suite du chapitre pour initialiser nos membres. 

Enfin, sachez que l'on peut définir une structure tant dans un fichier d'en-tête que dans un fichier source. Cela dépend en fait du contexte : est-ce que la structure est interne à un fichier parce qu'elle a un usage très particulier, ou bien veut-on la partager de manière modulaire (dans ce cas, on la met dans un fichier d'en-tête) ? C'est à vous de voir.

#### Exemple ####

Pour donner un exemple de définition, voici celle d'une structure *Personne* qui stocke des informations administratives sur quelqu'un :

```c
struct Personne
{
    double poids ;
    double taille ;
    unsigned int nombre_enfants ;
    unsigned int age;
    double salaire;
};
```

### Déclaration ###

Ensuite, pour déclarer dans notre code un objet de type structure, il suffit de suivre ce schéma :

```c
struct NomDeLaStructure identificateur;
```

La méthode est la même que pour une variable d'un type de base, si ce n'est que le mot-clef ```struct``` est obligatoire. Avec notre exemple de la structure *Personne*, cela donnerait ça :

```c
int main(void)
{
    struct Personne ma_structure;
    return 0;
}
```

### Initialisation ###

Comme je l'ai dit plus haut, il est interdit d'initialiser les champs d'une structures dans le bloc de code vu plus haut. Conséquence : on ne peut pas initialiser ces structures de cette manière et donc il est possible que l'on se retrouve avec des valeurs fantaisistes.. Heureusement, il existe une technique pour initialiser dès la déclaration :

```c
struct NomDeLaStructure identificateur = {valeurs que l'on veut donner aux membres};
```

Il faut bien sur qu'il y ait autant de valeurs que de membres, et qu'elles soient déclarées dans le même ordre que les membres. Un petit exemple pour mieux visualiser ? C'est d'accord.

```c
struct Personne ma_structure = {60.2, 175.0, 0, 24, 25000};
```

Bien entendu, on peut aussi initialiser chacun des membres à la main si l'on veut. Mais pour le moment, on ne sait pas comment accéder à un membre de notre structure, donc laissons cela pour plus tard.

### typedef ###

Peut-être certains ce sont déjà posés la question : n'y a t-il pas un moyen d'enlever le mot-clef ```struct``` lors de la déclaration ? Eh bien la réponse est oui ! il existe un moyen : ```typedef```. Ce mot-clef sert à définir des synonymes ou *alias* de types existants. C'est assez utile pour simplifier des déclarations complexes ou longues. Le modèle est le suivant :

```c
typedef struct Identificateur Alias;
struct Identificateur
{
    /* champs de la structure */
};
```

Désormais, écrire ```struct Identificateur``` ou ```Alias``` revient au même pour le compilateur. A noter qu'il existe une autre possibilité, un peu plus rapide à écrire :

```c
typedef struct
{
    /* champs de la structure */
} Identificateur;
```

Avec cette forme, écrire ```struct Identificateur``` ou ```Identificateur``` est identique. Le choix de l'une ou l'autre manière n'est pas vraiment important, c'est à vous de choisir celle que vous préférez. Ce tutoriel utilisera quand à lui la seconde forme. Il est aussi important de savoir que certains programmeurs, par soucis de clarté, n'utilisent jamais de ```typedef``` pour bien montrer qu'ils utilisent des structures.

### Utilisation et pointeurs
### Accès à un membre ###

Pour l'instant, on sait définir une structure, la déclarer, l'initialiser mais on ne sait toujours pas comment accéder aux membres qui la composent. La méthode est très simple, il suffit de faire comme ça :

```console
Identificateur.membre;
```

Pour information, si vous utilisez un IDE, lorsque vous taperez le point, il se peut qu'on vous propose une liste des champs de votre structure : c'est *l'auto-complétion*. 

#### Modification d'un membre ####

Il est possible de les modifier les membres d'une structure. Pour cela, on procède ainsi :

```console
structure.membre = valeur_à_placer_dans_le_membre;
```

En gros, le membre subit une affectation comme une variable classique.

### Pointeurs sur structures ###

Comme certains d'entre vous s'en sont peut-être déjà douté, il est possible de déclarer des pointeurs de structures. Le fonctionnement est exactement le même que pour les pointeurs sur des variables "classiques". Voici le code précédent qui déclare cette fois un pointeur de structure :

```c
struct X * ptr;
```

Quel est l'intérêt ? Nous l'avons déjà dit dans le chapitre sur les pointeurs : tout argument d'une fonction est recopié, et c'est cette copie qui est utilisée dans la fonction. Vouloir éviter cette recopie peut se justifier dans deux cas : soit on a absolument besoin de manipuler l'original, soit on veut éviter des copies inutiles. Comme justification pour le second cas, il faut savoir qu'une recopie de la structure est une opération qui peut être lourde si la structure est grosse. En utilisant des pointeurs, on accède non plus à une copie mais à la structure elle-même, ce qui est plus rapide et efficace dans une grande majorité de cas.

#### Accès via un pointeur ####

Bon, on sait déclarer des pointeurs sur structures pour passer celles-ci dans nos fonctions. Seulement, accéder à un membre d'une structure via l'identificateur d'une structure, et passer par un pointeur sur structure, ce n'est pas la même chose. Prenons un exemple : je dispose d'une structure qui contient des informations médicales sur une personne. La structure est déclarée comme ceci :

```c
typedef struct
{
    double poids; /* en kilo-grammes */
    unsigned int taille; /* en centimètres */ 
    unsigned int age;
} Personne;
```

Supposons que je veuille passer cette structure à une fonction chargée de calculer l'IMC de la personne. L'IMC, c'est l'Indice de Masse Corporelle : c'est un indicateur inventé par des statisticiens pour évaluer les risques de mortalité d'une personne en fonction de son poids et de sa taille. Il sert à évaluer si le poids d'une personne est à surveiller ou pas, et est utilisé par certains médecins, combiné avec d'autres analyses. Cet IMC se calcule assez simplement : il suffit d'élever la taille au carré, et de diviser par le poids.

On va supposer que je passe cette structure à ma fonction via un pointeur (on pourrait éventuellement faire autrement, mais passons). L'accès aux membres ne pourra pas se faire directement, en utilisant la syntaxe vue plus haut. Ainsi, une fonction comme ceci n'est pas valable :

```c
double IMC (Personne * personne)
{
    taille = personne.taille;
    poids = personne.poids;

    return (taille * taille) / poids;
}
```

La raison est simple : dans ce code, personne est un pointeur, pas une structure. Pour accéder à un membre, je dois d'abord déréférencer le pointeur pour accéder à ma structure, et ensuite accorder au membre. Soit, faisons-le. Naïvement, on pourrait croire qu'il suffit de faire ceci :

```c
double IMC (Personne * personne)
{
    taille = *personne.taille;
    poids = *personne.poids;

    return (taille * taille) / poids;
}
```

Mais là encore, vous vous trompez. En fait, il y a un petit piège qui vient des différentes priorités du point et de l'opérateur * (regardez [ici](http://www.siteduzero.com/forum-83-125906-p5-foire-aux-questions-langage-c.html#r7288084) pour en apprendre plus). Pour éviter tout problème, vous devez placer des parenthèses autour du * et de l’identificateur. Voici ce que cela donne dans l'exemple :

```c
double IMC (Personne* personne)
{
    taille = (*personne).taille;
    poids = (*personne).poids;

    return (taille * taille) / poids;
}
```

#### Syntaxe alternative ####

Vu que faire ce genre de manipulations est quelque chose de courant, les concepteurs du C ont ajoutés un raccourci qui permet d'aller plus vite. Ainsi, la syntaxe ```(*structure).membre``` peut s'écrire aussi ```structure->membre```. Sur l'exemple du haut, cela donnerait :

```c
double IMC (Personne * personne)
{
    taille = personne->taille;
    poids = personne->poids;

    return (taille * taille) / poids;
}
```

Retenez bien cette syntaxe, vous l'utiliserez certainement assez souvent. En fait, c'est même celle qu'utilisent tous les programmeurs.

### Exercice ###

Nous avons vu dans la partie précédente une syntaxe pour initialiser les structures à leur déclaration. Cependant, ce n'est pas toujours très pratique, notamment quand il y a de nombreux champs à préciser. Une meilleure solution serait de faire une fonction qui prendrait notre structure en paramètre et qui initialiserait tous ces membres. Pour vous entrainer, essayez de faire cette fonction pour la structure *Personne*.

Pour information, si vous connaissez des langages orientés objets, vous reconnaitrez sans doute cette fonction qui n'est d'autre qu'une sorte de constructeur.

[secret]{
```c
/* Je n'ai pas mis de typedef pour 
vous montrer la différence au niveau 
de la fonction */

struct Personne
{
    double poids;
    double taille;
    unsigned int nombre_enfants;
    unsigned int age;
    double salaire;
};

void Personne_Init(struct Personne * employe)
{
    employe->poids = 55;
    employe->taille = 175;
    employe->nombre_enfants = 2;
    employe->age = 30;
    employe->salaire = 25000;
}

int main(void)
{
    struct Personne employe;
    Personne_Init(&employe);
    return 0;
}
```

J'ai fixé des valeurs dans mon code par choix, mais rien ne vous empêche de les changer. C'est à vous d'adapter le code à vos besoins.
}

Vous pouvez aussi vous entrainer en codant une fonction affichant les données, une modifiant certains champs voire tous, etc. Votre imagination est la seule limite.

### Un peu de mémoire
On sait maintenant utiliser nos structures. C'est bien, et pour être franc, on n'a pas vraiment besoin d'en savoir beaucoup plus pour utiliser celles-ci de manière basique. Mais un peu de culture générale ne fait pas de mal. 

### Représentation en mémoire ###

Savez-vous comment sont représentées nos structures en mémoire ? Rien de plus simple : en théorie, les variables d'une structure sont placées les unes après les autres en mémoire. J'ai bien dit en théorie, mais laissons cela pour plus tard. Par exemple, prenons une structure bidon.

```c
struct Exemple
{
    double flottant;
    char lettre;
    unsigned int entier;
};
```

On va supposer qu'un ```double``` prend 8 octets, qu'un ```char``` en prend 1, et qu'un ```unsigned int``` en prend 4. Voici ce que donnerait cette structure en mémoire :

![](http://uploads.siteduzero.com/files/411001_412000/411992.png)

Du moins, c'est de la théorie, comme nous allons bientôt le voir.

### sizeof ###

Maintenant, supposons que vous vouliez connaitre la taille que votre structure prend en mémoire. Pour le savoir, vous pouvez utiliser l'opérateur ```sizeof```. Cet opérateur donne la taille en bytes d'un type et s'utilise comme ceci : ```sizeof (char)```, ```sizeof (int)```, etc. Bref, il suffit de placer ```sizeof``` et de préciser le type dont on veut connaitre la taille entre parenthèses juste après (pour être plus exact, les parenthèse sont obligatoires dans le cas d'un type mais pas d'un identificateur, mais faisons comme si elles étaient tout le temps obligatoires, plus simple à retenir).

Petite remarque : le résultat de l'opérateur ```sizeof``` est de type ```size_t``` et non de type ```int``` ou ```unsigned int``` comme on serait tenter de le penser de prime abord. La raison est très simple : cela est dû aux bornes de ces types. En effet, pour connaitre la taille d'un type simple comme ```int``` ou ```char```, les bornes d'un ```unsigned int``` ou d'un ```int``` ne pose pas de problèmes. Mais ```sizeof``` peut aussi servir pour récupérer autre chose comme la taille de données plus élaborées. Et sur certains ordinateurs, on peut parfaitement avoir des données dont la taille dépasse les bornes d'un ```unsigned int``` ou d'un ```int```. Aussi, pour résoudre ce problème, le type ```size_t``` a été crée et permet de contenir la taille de n'importe quelle donnée.

À ce sujet, je vous propose un petit exercice : essayer d'afficher la taille de tous les types que vous connaissez. En C89, il n'existe pas d'indicateur de conversion spécifique à ```size_t```. Il vous faudra donc utiliser celui prévu pour le type ```unsigned long``` (pour rappel, ```"%lu"```) et convertir le résultat de l'opérateur ```sizeof```.

[secret]{
```c
#include <stdio.h>

int main(void)
{
    printf("Taille d'un char = %lu\n", (unsigned long) sizeof(char));
    printf("Taille d'un short = %lu\n", (unsigned long) sizeof(short));
    printf("Taille d'un int = %lu\n", (unsigned long) sizeof(int));
    printf("Taille d'un long = %lu\n", (unsigned long) sizeof(long));
    printf("Taille d'un float = %lu\n", (unsigned long) sizeof(float));
    printf("Taille d'un double = %lu\n", (unsigned long) sizeof(double));
    printf("Taille d'un long double = %lu\n", (unsigned long) sizeof(long double));
    return 0;
}
```

Que l'on se mette d'accord : ceci est le comportement rigoureux que l'on vous enseigne. Sans le cast, le comportement est indéterminé. Néanmoins, il reste assez lourd, et sachez que si vous n'êtes pas sur un ordinateur trop exotique (un PC par exemple), vous pouvez vous passer de cette technique.
}

Ceci étant fait pour des types simples, vous pouvez aussi le faire pour des structures. Par exemple, reprenons notre structure Exemple :

```c
struct Exemple
{
    double flottant;
    char lettre;
    unsigned int entier;
};
```

Avec ce qu'on a dit plus haut, notre structure devrait prendre 8 octets pour un  ```double```, un octet pour le ```char```, et 4 pour le ```unsigned int```, ce qui donne un total de 13 octets. Essayons ce que cela donne :

```c
typedef struct Exemple
{
    double flottant;
    char lettre;
    unsigned int entier;
} Exemple;

int main (void)
{
    printf ("%d", sizeof(Exemple));
    return 0;
}
```

Et ce code affiche :

```console
16
```

... 

Hé hé, je dois avouer que je suis vraiment fier de mon coup. Et oui, vous êtes encore tombés dans un piège dont vous ne pouviez pas soupçonner l’existence. Je suis machiavélique !

### Alignement en mémoire ###

J'avoue que je vous dois des explications. Mais tout d'abord, sachez que ce 16 ne sort pas de n'importe où et qu'il est parfaitement normal. Mais autant prévenir : l'explication va paraitre assez déroutante. On va en effet aller regarder ce qui se passe au plus profond de la mémoire !

#### Mots ####

Lorsque notre processeur va vouloir manipuler un champ de notre structure, il va d'abord commencer par la lire depuis la mémoire. Cette donnée sera alors transmise au processeur. Cette transmission se fait par un intermédiaire. Cet intermédiaire, c'est un ensemble de fils qui relient la mémoire et le processeur, et par lequel les données vont s’échanger entre processeur et mémoire. On l'appelle le **bus de donnée**.

Ce bus de donnée permet souvent de charger plusieurs octets depuis la mémoire. Le processeur peut ainsi charger 2, 4 ou 8 octets d'un seul coup (parfois plus). On dit que le processeur accède un **mot** en mémoire. Ce mot n'est rien d'autre qu'une donnée qui a la même taille que le bus de donnée. Suivant le processeur, il existe parfois des restrictions sur la place de chacun de ces mots en mémoire.

#### Alignement ####

Certains processeurs ou certaines mémoires imposent des restrictions assez drastiques dans la façon de gérer ces mots. Certains processeurs (ou certaines mémoires) regroupent les cases mémoires en "blocs" de la taille d'un mot : ceux-ci utilise un certain **alignement mémoire**. On peut voir chacun de ces blocs comme une "case mémoire" fictive un peu plus grosse que les cases mémoires réelles et considérer que chacun de ces blocs possède une adresse. L'adresse d'un de ces groupes est l'adresse de l'octet de poids faible. Les adresses des octets situé dans le groupe (c'est à dire autre que l'octet de poids faible) sont inutilisables : on ne peut adresser qu'un groupe, via son octet de poids faible, et charger l'intégralité de ce mot sur le bus, mais pas accéder à un octet en particulier.

![](http://uploads.siteduzero.com/files/411001_412000/411996.png)

L'adressage de la mémoire est donc moins "fin" : on travaille sur des blocs de plusieurs bits, plutôt que sur des petits paquets. Dans la réalité, ces blocs ont une taille égale à une puissance de deux : cela permet de faire quelques bidouilles sur le bus d'adresse pour économiser des fils et de simplifier le design de la mémoire. Des mots de 8 octets (64 bits) ne sont pas rares sur nos ordinateurs actuels.

#### Accès mémoires non-alignés ####

Bon, maintenant imaginons un cas particulier : je dispose d'un processeur utilisant des mots de 4 octets. Je dispose aussi d'un programme qui doit manipuler un caractère stocké sur 1 octet, un entier de 4 octets, et une donnée de 2 octets. Mais un problème se pose : le programme qui manipule ces données a été programmé par quelqu'un qui n'était pas au courant de ces histoire d'alignement, et il a répartit mes données dans la structure comme ceci :

```c
typedef struct Exemple
{
    char lettre;
    unsigned int entier_long;
    short entier_court ;
} Exemple;
```

Supposons que cet entier soit stocké à une adresse non-multiple de 4. Par exemple :

| Adresse | Octet 4   | Octet 3 | Octet 2 | Octet 1 |
| ------- | --------- | ------- | ------- | ------- |
| A       | Caractère | Entier  | Entier  | Entier  |
| A + 4   | Entier    | Donnée  | Donnée  | -       |
| A + 8   | -         | -       | -       | -       |

Pour charger mon caractère dans un registre, pas de problèmes : celui-ci tient dans un mot. Il me suffit alors de charger mon mot dans un registre en utilisant une instruction de mon processeur qui charge un octet. Pour ma donnée de 2 octets, pas de problèmes non plus, vu que celui-ci est dans un mot. Mais si je demande à mon processeur de charger mon entier, ça ne passe pas ! Mon entier est en effet stocké sur deux mots différents, et on ne peut le charger en une seule fois : mon entier n'est pas *aligné en mémoire*. Dans ce cas, il peut se passer des tas de choses suivant le processeur qu'on utilise. Sur certains processeurs, la donnée est chargée en deux fois : c'est légèrement plus lent que la charger en une seule fois, mais ça passe. Mais sur d'autres processeurs, la situation devient nettement plus grave : le programme responsable de cet accès mémoire en dehors des clous se fait sauvagement planter le faciès sans la moindre sommation. 

#### Padding ####

Pour éviter ce genre de choses, les compilateurs utilisés pour des langages de haut niveau préfèrent rajouter des données inutiles (on dit aussi du *padding*) de façon à ce que chaque donnée soit bien alignée sur le bon nombre d'octets. En reprenant notre exemple du dessus, et en notant le *padding* X, on obtiendrait ceci :

| Adresse | Octet 4   | Octet 3 | Octet 2 | Octet 1 |
| ------- | --------- | ------- | ------- | ------- |
| A       | Caractère | X       | X       | X       |
| A + 4   | Entier    | Entier  | Entier  | Entier  |
| A + 8   | Donnée    | Donnée  | X       | X       |

Ce sont ces données de *padding* qui ont fait passer notre structures de 13 à 16 octets. Comme quoi, l'explication était au final très simple. Comme vous le voyez, ces données de *padding* prennent un peu plus de place, et de la mémoire est gâchée inutilement. 

#### Économies ####

Mais dans certains cas, on peut éviter de gaspiller de la mémoire inutilement en faisant attention à l'ordre de déclaration de nos variables. Par exemple, si on reprend l'exemple du dessus, on peut gagner 4 octets facilement. Il suffit de déclarer la structure comme ceci :

```c
typedef struct Exemple
{
    unsigned int entier_long;
    short entier_court ;
    char lettre;
} Exemple;
```

Si on regarde bien, cette structure donnerait ceci en mémoire :

| Adresse | Octet 4 | Octet 3 | Octet 2   | Octet 1 |
| ------- | ------- | ------- | --------- | ------- |
| A       | Entier  | Entier  | Entier    | Entier  |
| A + 4   | Donnée  | Donnée  | Caractère | X       |

Ce qui prend seulement 8 octets au lieu de 12. Certains octets de *padding* ont étés éliminées. Moralité : programmeurs, si vous voulez économiser de la mémoire, faites gaffe à bien gérer l'alignement en mémoire ! Essayez toujours de déclarer vos variables de façon à remplir un mot intégralement ou le plus possible. Renseignez-vous sur le *padding*, et essayez de savoir quelle est la taille de vos données avec ce cher ```sizeof```.

### Compléments
### Structures contenant des structures ###

Il est possible qu'une structure contienne des variables de type structure. Rien n’empêche d'imbriquer des structures dans d'autres. Pour vous en convaincre, sachez que l'exemple suivant est tout à fait légal en C.

```c
struct Point2D
{
    int x;
    int y;
};

struct Point3D
{
    struct Point2D point2D;
    int z;
};
```

Il y a deux conditions, la première étant bien sûr que la structure inclue soit définie avant celle l'incluant ; la deuxième est qu'une structure ne peut pas contenir des structures de son propre type : il semble évident qu'une structure de type X ne puisse pas contenir des structures de type X.

### Déclarations anticipées et pointeurs de structures ###

La norme autorise le fait que l'on puisse déclarer une structure sans en préciser les champs si le compilateur n'a pas besoin de connaître la description de la structure (comme dans le cas des pointeurs sur structures). Ainsi, une déclaration anticipée de notre structure d'exemple de ce chapitre serait ```struct Personne;``` tout simplement. Bien entendu, il faut que dans le code il existe au moins une description complète des champs de la structure.

Quel est l'intérêt des déclarations anticipées ? Eh bien il y en a deux. Le premier est **en cas d'interdépendance entre structures**. Imaginez deux structures A et B : la première contient un pointeur sur une structure de type B, et vice-versa. Illustration avec ce code :

```c
struct A;

struct B
{
    struct A * var_a;
};

struct A
{
    struct B * var_b;
};
```

Le deuxième intérêt des déclarations anticipées est si une structure contient des pointeurs sur des structures de son propre type. Ça parait obscur ? Il s'agit simplement de ce cas là :

```c
struct A;

struct A
{
    struct A * ptr_a;
};
```

Ce code constitue une exception à la deuxième condition que nous avions énoncé dans la sous-partie précédente : il est possible de déclarer **un pointeur** (mais seulement un pointeur) sur une structure du même type que la structure que nous sommes en train de créer. Nous aurons l'occasion d'utiliser des structures de ce genre dans les chapitres sur les listes chainées. 

On va quand même faire un test : supprimer la déclaration anticipée du code précédent et constatez ... qu'il marche ! Encore une exception ? Eh bien il faut savoir que la portée d'une structure (revoyez le chapitre [Découper son projet](http://progdupeu.pl/tutoriels/voir/15-le-langage-c/1-introduction/9-decouper-son-projet) si vous avez oublié ce que c'est) démarre à l'accolade ouvrante du début et non au point-virgule à la fin. Ainsi, dès que je fais ceci :

```c
struct Identificateur
{
```

Je peux créer des pointeurs sur des structures de type *Identificateur* sans avoir à utiliser une déclaration anticipée. Tout ça est compliqué ? Alors n'hésitez pas à reprendre cette partie à tête reposée, car même si elle est théorique elle permettra de mieux comprendre la partie 5.

Les structures en elles-même ne sont pas compliquées à comprendre, mais l'intérêt est parfois plus difficile à saisir. Ne vous en faîtes pas, nous aurons bientôt l'occasion de découvrir des cas où les structures se trouvent être bien pratiques. En attendant, n'hésitez pas à relire le chapitre s'il vous reste des points obscurs.

Continuons notre route et découvrons à présent un deuxième type de données complexes : les **tableaux**.

## Les tableaux
Continuons notre découvertes des données complexes en abordant cette fois la notion de **tableaux**. Comme le nom l'indique, un tableau est une regroupement de données, tout comme les structures. Mais alors, y'a t-il des différences et si oui quelles sont-elles ? La réponse se trouve à la suite, mais sachez que comme les structures, les tableaux sont très utilisés en C.

### C'est quoi un tableau ?
En C, un tableau est une suite contigüe de données de même type. Cela implique deux choses que nous allons expliciter.

* **Une suite contigüe de données**. Cela veut dire que les données d'un tableau sont rangées les unes à la suite des autres en mémoire : on ne laisse pas le moindre vide. Les adresses sont par conséquent également consécutives. En clair, tout se passe comme si on avait rassemblé plusieurs variables de même type les unes à côté des autres. Un tableau est donc un gros bloc de mémoire qui commence à une adresse déterminée (celle de son premier élément) et qui contient un nombre fini d’éléments.

* **Tous les éléments d'un tableau sont de même type**. On ne peut donc pas se retrouver avec un ```int``` au beau milieu d'un tableau de ```char```, par exemple. Du fait que les éléments sont de même type, ces derniers ont également tous la même taille et il est dès lors possible de déterminé la taille occupée en mémoire par un tableau : elle est égale au produit du nombre d’éléments, sa **longueur**, par la taille d'un élément.

![](http://uploads.siteduzero.com/files/382001_383000/382971.png)

### Leur utilité ###

Le principal intérêt des tableaux est de rassembler plusieurs variables de même type ensemble pour les regrouper dans un seul objet.

Par exemple, supposons que vous vouliez créer un petit programme pour calculer la moyenne de votre année scolaire. Vous aurez besoin de stocker toutes vos notes quelque part dans votre ordinateur. Bien entendu, vous pourriez utiliser autant de variables que vous avez de notes, mais cela serait très long à écrire. À la place, vous pouvez créer un tableau qui contiendra toutes vos notes, chaque élément de votre tableau étant une note (que vous pourrez stocker dans un nombre flottant ou un entier, par exemple), et manipuler directement ce tableau.

### Déclaration et initialisation
Maintenant que nous avons vu ce qu'était un tableau, nous allons voir comment déclarer une variable de type tableau et comment l'utiliser.

### Déclaration ###

La déclaration d'un tableau nécessite trois informations : 

* la première est **le type** des éléments du tableau (rappelez vous qu'un tableau est une suite de données de même type) ;	
  * la seconde est le nom du tableau, son **identificateur** ;
* la dernière est **la longueur** du tableau (son nombre d'éléments). Cette dernière doit obligatoirement être une constante entière (il est cependant possible d'utiliser une macroconstante, comme nous le verrons).

```console
type identificateur[longueur];
```

Comme vous le voyez, la syntaxe de la déclaration d'un tableau est similaire à celle d'une variable, la seule différence étant qu'il faut préciser le nombre d’éléments entre crochets à la suite de l'identificateur du tableau.

#### Exemples ####
Ainsi, si je souhaite par exemple déclarer un tableau contenant 20 ```int```, je dois procéder comme suit :

```c
int tableau[20];
```

C'est aussi simple que ça. Entrainons-nous avec quelques exemples simples pour voir si vous avez bien compris. Essayez de déclarer un tableau :

* de 15 ```char``` ;
* de 25 ```float``` ;
* de 4 ```unsigned int``` ;
* de 10 ```short``` ;
* de 5 ```struct Personne``` (celle vue dans le chapitre précédent) ;
* de 7 pointeurs sur ```int``` ;

Et voilà [la correction](http://paste.awesom.eu/informaticienzero/wCT&ln). Comme vous pouvez le voir, il est possible de déclarer un tableau de n'importe quel type, aussi complexe soit-il. 

#### Macroconstante ####

Concernant la taille, il est également possible de la définir à l'aide d'une macroconstante, comme ceci :

```c
#define N 5

int tab[N];
```

En effet, après le pasage du préprocesseur, la macroconstante sera remplacée par sa définition (à savoir la constante entière 5 dans notre cas), ce qui est parfaitement valide.

### Initialisation ###

Lorsque l'on déclare un tableau, il se passe la même chose que pour les variables : si celui-ci n'est pas déclaré avec le mot-clé ```static```, ses éléments ont une valeur indéterminée. L'ordinateur a juste réquisitionné un bloc de mémoire pour stocker ce tableau et c'est tout, il n'a pas modifié son contenu.

Comme pour les variables, il est possible d’initialiser un tableau, ce qui n'est rien de moins qu'initialiser tout ou partie de ses éléments. Pour ce faire, il y a deux manières de procéder, mais dans les deux cas, il est nécessaire de préciser les valeurs des éléments du tableau une par une. Ces valeurs seront séparées par une virgule, et l'ensemble de ces valeurs est entouré d'accolades. Le tout est affecté au tableau lors de sa déclaration. 

#### Initialisation avec longueur explicite ####

Le premier type d'initialisation consiste à initialiser un tableau dont la longueur est précisée entre crochets. Dans ce cas, il est indispensable de respecter cette longueur pour éviter des erreurs (pour un tableau de longueur $x$, on doit initialiser au plus $x$ éléments).

```console
type identificateur[longueur] = {valeurs};
```

Prenons l'exemple d'un tableau de 3 entiers, dont on veut initialiser le premier élément à 5, le second à -48 et le dernier à 972.

```c
int tableau[3] = {5, -48, 972};
```

Dans cet exemple, on a un tableau de 3 ```int```, on est donc obligé de respecter cette longueur, et on ne peut initialiser que 3 éléments au maximum. Mettez-en plus et vous risquez d'avoir des problèmes. 

Petite remarque : il est possible de n'initialiser que certains éléments d'un tableau déclaré de cette façon. Il suffit de ne pas préciser les valeurs des autres éléments.

```c
int tableau[5] = {2, 3};
```

Dans cet exemple, je définis un tableau de 5 ```int```, mais je n'initialise que les deux premiers éléments. Que deviennent dès lors les autres ? Ils sont automatiquement mis à zéro. Du coup, pour initialiser tous les éléments d'un tableau à zéro, il suffit d'écrire :

```console
type identificateur[longueur] = {0};
```

#### Initialisation avec longueur implicite ####

Le second type d'initialisation consiste à initialiser un tableau dont la longueur n'est pas fixée.

```console
type identificateur[] = {valeurs};
```

Dans ce cas, la longueur est précisée de façon implicite : c'est le nombre d'éléments entre accolades qui la déterminera.
Prenons l'exemple ci-dessous :

```c
int tableau[] = {7, 8, 9, -41, 213, 945};
```

Dans ce dernier, 6 éléments sont initialisés, on obtient donc au final un tableau de 6 ```int```

### Accès aux éléments
Si on sait maintenant déclarer et initialiser des tableaux, il faut encore que ceux-ci servent à quelque chose. Et pour cela, on doit pouvoir modifier ou récupérer les éléments de celui-ci. Pour cela, chaque élément d'un tableau est identifié par sa place dans le tableau. On peut choisir d’accéder au premier élément d'un tableau, au second, au troisième, ..., au n-ième élément, etc. Pour cela, chacun de ces éléments se voit attribuer un **indice** (un nombre entier) qui détermine sa place dans le tableau. 

Mais il y a une petite subtilité : ces indices commencent toujours à 0. Le premier élément est celui d'indice 0, le second a pour indice 1, le troisième est à l'indice 2, etc. Pour un tableau de $x$ éléments, les indices vont donc de 0 à $x - 1$. On peut notamment se demander pourquoi le premier élément d'un tableau se voit attribuer l'indice zéro. Après tout, il aurait été plus logique de faire commencer nos indices à 1. D'ailleurs, c'est le cas dans d'autres langages de programmation : le premier indice d'un tableau n'est pas le zéro, mais le 1. Et certains langages vont encore plus loin, mais passons. 

### Calcul d'adresse ###

Alors pourquoi ce choix contre-intuitif ? Cela vient de la façon dont sont stockés les tableaux en mémoire. En fait, pour accéder à un élément, vous devrez connaitre l'adresse de celui-ci. Heureusement, déterminer l'adresse d'un élément d'un tableau se fait assez simplement. En effet, puisque tous les éléments se suivent en mémoire, leurs adresses peuvent toutes se calculer à l'aide d'un indice et de l'adresse du début du tableau (celle de son premier élément).

Manipuler les éléments d'un tableau se fait avec des pointeurs. Pour accéder à un élément d'un tableau, vous devrez connaitre l'adresse de celui-ci, et donc avoir un pointeur sur cet élément. Déterminer l'adresse d'un élément dans un tableau se fait assez simplement: quelques calculs suffisent. Eh oui, vous avez bien lu : notre adresse peut être calculée. Pour calculer l'adresse d'un élément, vous avez besoin de deux choses : son indice, et l'adresse de début du tableau. Pour calculer cette adresse, on utilise le fait que les éléments d'un tableau ont une taille fixe et sont rangés dans des adresses mémoires consécutives.

Prenons un exemple : un tableau d'entiers, prenant chacun 4 octets. Le premier élément d'indice zéro est placé à l'adresse $A$ : c'est l'adresse à laquelle commence le tableau en mémoire. Le second élément est placé 4 octets après (vu que le premier élément prend 4 octets) : son adresse est donc $A+4$. Le troisième élément est placé 4 octets après le second élément, ce qui donne l'adresse $(A+4) + 4$. 

Si vous continuez ce petit jeu pour quelques valeurs, on obtiendrait quelque chose dans le genre :

| Indice i | Adresse de l'élèment |
| -------- | -------------------- |
| 0        | A                    |
| 1        | A+4                  |
| 2        | A+8                  |
| 3        | A+12                 |
| 4        | A+16                 |
| 5        | A+20                 |
| ...      | ...                  |

Vous remarquerez surement que l'on ajoute toujours un multiple de quatre (puisque dans cet exemple la taille d'un ```int``` est de quatre octets) et que l'on peut dès lors reformuler la table ci-dessus comme suit :

| Indice i | Adresse de l'élèment |
| -------- | -------------------- |
| 0        | A + (0 * 4)          |
| 1        | A + (1 * 4)          |
| 2        | A + (2 * 4)          |
| 3        | A + (3 * 4)          |
| 4        | A + (4 * 4)          |
| 5        | A + (5 * 4)          |

On peut donc formaliser cette remarque mathématiquement en posant $T$ la taille d'un élément du tableau, $i$ l'indice de cet élément, et $A$  l'adresse de début du tableau (l'adresse du premier élément) : l'adresse de l’élément d'indice $i$ vaut toujours $A + T \times i$.

Avec cette formule, on voit bien que l'indice du premier élément ne peut pas être autre chose que 0. Le premier élément a la même adresse que le début du tableau : c'est-à-dire A. On est obligé d'avoir i = 0 pour que cette formule convienne. Après, rien n’empêche de faire quelques bidouilles arithmétiques sur l'indice pour que le premier élément ait un indice différent de 0, mais le calcul de l'adresse sera alors plus compliqué, plus long à effectuer. Et dans un langage comme le C, conçu pour être performant, c'est niet !

Quoi qu'il en soit, pour effectuer ce calcul d'adresse, nous avons besoin de trois éléments :

* la taille du type de chaque élément ;
  * l'adresse de début du tableau ;
* l'indice.

#### Adresse du premier élément ####

Pour effectuer ce calcul d'adresse, il nous manque encore l'adresse du début de notre tableau. Cette adresse n'est rien d'autre que l'adresse de son premier élément. Reste à savoir comment le C nous permet d'obtenir cette adresse. 

La solution est sous vos yeux : regardez l'identificateur de votre tableau, c'est ça votre adresse. Hé oui, c'est choquant, et pourtant c'est la vérité ! En effet, dans une expression, l’identificateur d'un tableau se comporte comme un pointeur constant sur le début du tableau. Du moins, ce n'est valable qu'en dehors des déclarations et à l'exception de deux cas que nous allons voir tout de suite.

Remarquez que puisque l'identificateur d'un tableau se comporte comme un pointeur **constant** sur son premier élément, il est dès lors impossible de lui assigner quoi que ce soit.

```c
int tab1[3] = {-78, 4688, 5};
int tab2[3];

tab2 = tab1; /* interdit */
```

La première exception est l'application de l'opérateur ```&``` à un identificateur de type tableau. En effet, les expressions ```&nom_du_tableau``` et ```nom_du_tableau``` contiennent toutes les deux l'adresse du premier élément. La preuve : essayez ce petit code, pour vous en convaincre.

```c
#include <stdio.h>

int main (void)
{ 
    int tab[5] = {5, 5, 5, 5, 5};

    printf ("%d", tab == &tab);
    return 0; 
}
```

La seconde exception est l'utilisation de l'opérateur ```sizeof``` qui, lorsqu'il est appliqué à un identificateur de type tableau, donne bien la taille de tout le tableau et non la taille d'un pointeur comme on serait tenter de le penser. L'exemple ci-dessous illustre cette propriété.

```c
#include <stdio.h>

int main(void)
{
    int tab[10];

    printf("sizeof(int) = %lu\n", (unsigned long)sizeof(int));
    printf("sizeof(int *) = %lu\n", (unsigned long)sizeof(int *));
    printf("sizeof(tableau) = %lu\n", (unsigned long) sizeof(tab));
    return 0;
}
```
```console
sizeof(int) = 4
sizeof(int *) = 4
sizeof(tableau) = 40
```

On observe que la troisième ligne affiche bien la taille du tableau en octets ($10 \times 4$ octets) et non celle d'un pointeur comme la deuxième ligne. Cette particularité est utile pour obtenir la longueur d'un tableau : il suffit de diviser la taille totale du tableau par la taille d'un élément.

```c
#include <stdio.h>

int main(void)
{
    int tab[10];

    printf("nombre d'éléments = %lu\n", (unsigned long)(sizeof(tab) / sizeof(int)));
    return 0;
}
```

#### Arithmétique des pointeurs ####

Ensuite, malins comme vous êtes, vous vous êtes dit que calculer l'adresse se faisait en utilisant directement la formule vue au-dessus. Prenons un exemple : vous voulez accéder à l’élément d'indice 7 d'un tableau de ```int``` nommé *tab*. Vous êtes donc tentés d'écrire quelque chose comme : ```tab + (7 * sizeof(int))```.

Le seul problème, c'est que cela ne marchera pas ! Pourtant, vous n'avez rien fait de mal. Vous êtes juste tombé dans un piège : en C, les pointeurs sont typés. Un pointeur sur un ```int``` n'est pas vraiment la même chose qu'un pointeur sur un ```char```. La différence tient dans le fait que le compilateur tient compte du type du pointeur pour faire les calculs. En C, si j'ai un pointeur sur un ```int``` nommé *ptr*, *++ptr* ne pointe pas sur l'adresse suivante, mais sur l'adresse du ```int``` placé juste après. Et c'est la même chose pour les additions : ```ptr + 7``` pointera sur l'adresse du 7ème ```int``` suivant *ptr*. En clair : dans notre calcul d'adresse, on n'a pas besoin de mentionner la taille prise par un élément. Le compilateur le fait pour vous. Pour accéder à un élément d'indice i dans un tableau nommé *tab*, il suffit donc de calculer son adresse en faisant ```(tab + i)```, et de déréférencer le tout. On obtient alors l'expression ```*(tab + i)```. 

#### Formalisme tableaux ####

Calculer des adresses à la main de cette façon est tout de même assez lourd. Heureusement, le C fournit une syntaxe un peu plus simple afin d'accéder à un élément d'un tableau en fonction de son indice. Il ne vous est donc pas nécessaire de vous soucier de tout ce calcul d'adresse, le compilateur s'en chargera pour vous. Cette syntaxe est la suivante :

```c
identificateur[indice];
```

Notez qu'il est également possible d'utiliser la syntaxe suivante qui est strictement équivalente :

```c
*((identificateur) + (indice))
```

Cependant, comme vous le voyez, la syntaxe à base de ```[]``` est beaucoup plus lisible, et il n'y a aucune raison de s'en passer : elle est plus lisible, n'est pas plus lente (au contraire), elle est plus rapide à taper, etc. C'est ce qu'on appelle un sucre syntaxique, à savoir une petite fonctionnalité qui permet de rendre un langage plus agréable et plus facile à lire ou à écrire. Maintenant que vous connaissez cette syntaxe, sachez que c'est celle-ci qu'il est préférable d'utiliser pour accéder à un élément dans un tableau. Afin d'être tout à fait clair, voici un exemple affichant les valeurs respectives des différents éléments d'un tableau.

```c
#include <stdio.h>

int main(void)
{
    int tab[4] = {10, 20, 30, 40};

    printf("%d\n", tab[0]);
    printf("%d\n", tab[1]);
    printf("%d\n", tab[2]);
    printf("%d\n", *((tab) + (3))); /* équivalent à tab[3] */
    return 0;
}
```

#### Le cas des structures ####

Les tableaux de structures s'utilisent en même temps comme un tableau et comme une structure. Si l'on prend un tableau de $n$ structures, alors on accède aux éléments comme ceci s'il s'agit d'un tableau de structures :

```c
identificateur[indice].champs;
```

et comme ceci s'il s'agit d'un tableau de pointeurs de structures :

```c
identificateur[indice]->champs;
```

Ce n'est pas très compliqué, mais mieux vaut clarifier pour ceux qui auraient des doutes.

### Débordement de tableaux ###

Une des plus grandes erreurs en C est le débordement de tableaux à cause des indices. En effet, si vous tentez d'accéder à une case qui n'appartient pas à votre tableau, vous vous retrouvez face à un comportement indéterminé. C'est certainement le point le plus important du chapitre, mais aussi celui qui entraine le plus de problèmes : si par inadvertance, vous essayez d'accéder à un élément qui n'appartient pas au tableau sur lequel vous êtes en train de travailler, vous aurez de gros soucis. 

#### Exemple ####

Regardez ce code par exemple, volontairement erroné : 

```c
#include <stdio.h>

int main(void)
{
    int tableau[5] = {784, 5, 45, -12001, 8};
    int somme = 0;
    size_t i; 

    for(i = 0; i <= 5; ++i)
    {
        somme += tableau[i];
    }
    
    printf("%d\n", somme);
    return 0;
}
```

Le problème de ce code se situe comme vous l'aurez compris au niveau de la boucle. En effet, le tableau contient 5 cases et le programme en parcours 6 (```i <= 5``` à la place de ```i < 5```) ! Donc on tente d'accéder à une zone qui ne nous appartient pas. C'est une erreur assez courante et qu'on peut éviter simplement : il suffit de ne pas oublier que pour un tableau à $n$ éléments, les indices valides vont de 0 à $n-1$. Soyez donc prudent quand vous utilisez les boucles pour parcourir des tableaux. 

### Tableaux et fonctions
Dans ce qu'on a vu précédemment, on sait comment déclarer et initialiser des tableaux, et récupérer un élément avec un indice. Mais cela ne suffit pas pour savoir comment manipuler nos tableaux : on doit encore voir comment faire fonctionner ensemble tableaux et fonctions. Il existe en effet quelques petites singularités qu'ont les tableaux quand on cherche à les utiliser avec des fonctions. Il est parfois impossible de le retourner, et passer des tableaux en argument faire apparaitre certains comportements assez déroutants. Voyons un peu ce qu'il en est.

### Passer un tableau en paramètre de fonction ###

Pour envoyer un tableau dans une fonction, il nous faut passer en argument le tableau, et éventuellement sa taille. Ce dernier paramètre est obligatoire dès lors que vous voulez faire une boucle : il faut bien transmettre la taille du tableau pour que la boucle ne dépasse pas le nombre de case du tableau.

Pour passer un tableau à une fonction, il suffit de la déclarer comme ceci :

```console
type_fonction identificateur(type_tableau tableau[]);
```

Voici un exemple banal de fonction :

```c
void fonction(int tableau[], size_t taille);
```

Pourquoi ne précise-t-on pas la taille du tableau entre crochets ? Car le compilateur n'en tient pas compte. Peu importe la taille entre crochets, le compilateur l'ignore. Si vous connaissez la taille et que le tableau ne change jamais, vous pouvez la mettre. Si vous n'êtes pas sûrs, dans le doute, ne mettez rien.

#### Une histoire de copie ####

Au fait : si vous vous souvenez de ce qu'il y a écrit plus haut, vous savez qu'en dehors de deux exceptions, un tableau est souvent converti en un pointeur sur son premier élément. Si vous passez un tableau en argument d'une fonction, ce sera le cas. Grâce à cette conversion, il est également possible de passer un tableau en argument d'une fonction comme ceci :

```c
int fonction(int * tableau);
```

Cette forme est strictement équivalente à l'autre forme vue plus haut. Le choix de telle ou telle forme est personnel et ne change rien ; moi-même, j'utilise la première forme, que je trouve plus explicite. Quoi qu'il en soit, dans les deux cas on passe l'adresse du tableau à la fonction, ce qui fait qu'on travaille **toujours sur l'original** et non sur une simple copie comme c'est le cas avec les variables.

### Retourner un tableau ###

De la même manière que pour les arguments, si vous retournez un tableau, votre fonction retournera au final l'adresse de son premier élément et donc un pointeur sur son premier élément. Cependant, garder à l'esprit que les variables définies au sein d'une fonction sont détruites à la fin de celle-ci et que, par conséquent, vous retourner dès lors l'adresse d'un tableau qui n'existe plus.
​		

### Exercices
Comme nous avons vu plein de nouveautés dans ce chapitre, il faut pratiquer pour bien retenir toutes ces notions. Je vous propose donc toute une série d'exercices pour manipuler les tableaux. À chaque fois, je vous donne l'énoncé, puis c'est à vous de coder. Vous pourrez alors comparer avec la correction. Sachez que mes codes ne sont pas les meilleurs, et si vous arrivez à faire l'exercice, c'est déjà très bien. Donc pas d'inquiétude si votre code est différent du mien.

### Somme ###

Pour commencer, essayez de calculer la somme d'un tableau, c'est-à-dire la somme de tous ses éléments, et de retourner le résultat. Bon courage. Si vous avez fini, alors voici [la correction](http://paste.awesom.eu/informaticienzero/0nD&ln).

### Maximum et minimum ###

On peut aussi faire un peu plus complexe que simplement calculer la somme d'un tableau. Dans cet exercice, vous allez devoir créer une fonction qui donne le maximum et le minimum d'un tableau. Comme on veut récupérer deux valeurs, on ne peut pas utiliser de ```return```. Un conseil : commencer par créer une fonction qui trouve le maximum (ou le minimum) d'un tableau et cherchez à l'améliorer pour qu'elle puisse gérer aussi le minimum. Mais attention : souvenez-vous qu'une fonction ne peut renvoyer qu'une seule valeur à la fois. Gérer maximum et minimum nécessitera une astuce.

Voici [ma solution](http://paste.awesom.eu/informaticienzero/BNA&ln) parmi tant d'autres. Comme vous le voyez, j'ai utilisé des pointeurs pour fournir le maximum et le minimum de mon tableau. Comme quoi, les pointeurs sont utiles.

### Recherche d'un élément dans un tableau ###

Dans cet exercice-ci, vous allez devoir créer une fonction qui prend en entrée un nombre, un tableau de ```int``` et la longueur du tableau. Celle-ci teste la présence de ce nombre dans le tableau passé en entrée. La fonction doit renvoyer 0 si le nombre n'est pas dans le tableau, et 1 s’il y est présent.

À vos claviers ! Voici [la correction](http://paste.awesom.eu/informaticienzero/7UT&ln). Pour information, on peut faire bien plus rapide si jamais le tableau passé en entrée de notre fonction est trié. On peut alors utiliser une [recherche dichotomique](http://www.siteduzero.com/tutoriel-3-32948-recherche-dichotomique.html).

### Inverser les éléments d'un tableau ###

Cette fois-ci, on va vous demander quelque chose de plus compliqué. Vous allez devoir inverser les éléments d'un tableau : celui qui se trouve à la fin va se retrouver au début (et réciproquement), le second élément va se retrouver avant-dernier (et réciproquement), etc.  Autre détail : vous n'avez pas le droit d'utiliser un autre tableau pour résoudre cet exercice. Le seul tableau que vous devez manipuler dans cet exercice est celui qui sera passé en paramètre de notre fonction.

À vos claviers ! Je vous préviens, cela sera assez difficile. N'hésitez pas à prendre du temps sur ce problème. Pour ceux qui ont fini, voici la correction.

[secret]{
En fait, il fallait trouver une petite astuce pour ne pas avoir à utiliser de tableau supplémentaire. Il faut utiliser une fonction qui échange deux éléments dans notre tableau, et l'appliquer sur les bons éléments. Cette fonction n'est rien d'autre que la fameuse fonction *swap* qu'on a créée dans l'exercice du chapitre sur les pointeurs. Pour rappel, [la voici](http://paste.awesom.eu/informaticienzero/yVO&ln). 

Il suffit de commencer par échanger le premier élément et le dernier, puis d’échanger le second avec l'avant-dernier, etc. Plus précisément, on doit échanger l'élément d'indice i avec l'élément d'indice (longueur - i - 1). Il suffit de continuer ainsi jusqu’au milieu du tableau, [comme ceci](http://paste.awesom.eu/informaticienzero/0dD&ln).
}

Finalement, ils s'avèrent bien pratiques nos tableaux n'est-ce pas ? Ils sont très utiles pour regrouper des variables de même type, et ils permettent une manipulation plus aisée que les structures. De plus, on peut créer un tableau de n'importe quel type, même des tableaux de tableaux. C'est l'objet du chapitre suivant.

## Les tableaux multidimensionnels
Dans le chapitre précédent, nous avons vu des tableaux simples, dans lesquels on plaçait nos éléments bouts à bouts les uns derrières les autres. Si on veux représenter ceux-ci, cela peut se faire sur une seule ligne, sur laquelle on placerait nos éléments dans l'ordre de leurs indices. Il s'agissait des **tableaux à une dimension** ou uni-dimensionnel.

Mais certaines données peuvent être représentées plus simplement sous la forme de tableaux à deux dimensions, organisées en lignes et en colonnes. Par exemple, c'est le cas d'une image. Comme autre exemple, vous pouvez prendre une grille de sudoku : celle-ci est organisée en 3 lignes et en 3 colonnes. Et on pourrait encore trouver d'autres exemples de données organisées en lignes et en colonnes. Le besoin de tableaux rectangulaires se fait sentir, et nos simples tableaux à une dimension ne semblent pas suffire : on doit utiliser des tableaux à deux dimensions. Et bien sachez que le langage C fournit de quoi gérer de tels tableaux. Pire : il fournit de quoi gérer des tableaux de données encore plus complexes, qui possèdent plus de deux dimensions. Ces tableaux, légèrement plus complexes, sont appelées des **tableaux multidimensionnels**. Ce chapitre va vous parler de ces tableaux et de leur utilité. 

Grosso-modo, ces tableaux servent quand on a besoin de stocker des données organisées en lignes et colonnes, dans un joli rectangle. Les tableaux à plus de 2 dimensions sont eux beaucoup plus rares, et servent assez peu. Quoiqu'il en soit, nous allons tout de même voir ces tableaux.

### Déclaration et initialisation
Mine de rien, ces tableaux multidimensionnels se comportent comme des tableaux normaux et leur déclaration, initialisation, et utilisation s'effectue de façon similaire à ce qu'on a vu dans le chapitre sur les tableaux à une dimension. Voyons maintenant comment déclarer ces tableaux.

### Déclaration ###

Pour déclarer un tableau à plusieurs dimensions, on procède comme pour les tableaux à une dimension, avec une toute petite différence. Il faut commencer par indiquer le type des éléments du tableau, puis spécifier l'identificateur, et enfin placer des crochets. 

Seule différence : on doit utiliser autant de crochets qu'on veut de dimensions. Exemple : si je veux un tableau à deux dimensions, je dois préciser le nombre de lignes, et le nombre de colonnes. Le nombre de lignes sera indiqué entre crochets, et même chose pour le nombre de colonnes.

Exemple : un tableau de ```int``` de 20 lignes et de 35 colonnes donnera ceci : 

```c
int tableau2D [20][35] ;
```

Et l'on doit mettre autant de crochets que l'on veut de dimensions. En indiquant bien sur la taille entre les crochets, si besoin.

#### Exemples ####

Exemple avec un tableau à deux dimensions :

```c
int tableau2D [2][3];
```

Et avec un tableau à trois dimensions :

```c
int tableau3D [2][3][2];
```

Le principe est très simple puisque c'est le même que pour les tableaux à une dimension, mais adapté.

### Initialisation ###

Initialiser un tableaux à plusieurs dimensions se fait à peu prêt de la même façon qu'avec les tableaux à une dimension. 

#### Avec la taille de la première dimension ####

Comme pour les tableaux à une dimension, on peut initialiser ceux-ci en indiquant la taille du tableau. La différence est que cette précision doit se faire pour toutes les dimensions du tableau. Pour un tableau à deux dimensions, on doit ainsi indiquer le nombre de ligne et le nombre de colonnes. 

La syntaxe pour l'initialisation des tableaux multidimensionnels ressemble à celle utilisée pour les tableaux à une dimension. Mais il y a tout de même une petite différence. Avec un tableau uni-dimensionnel, on effectuait une initialisation avec la syntaxe suivante :

```console
type identificateur [nombre d’éléments] = { Valeurs par défaut, séparées par des virgules }
```

Cette syntaxe est réutilisée, mais ce qui est entre les {...} va changer. Ce qu'on initialisera, ce sont des lignes. Chacune de ces lignes est un tableau comme un autre, et notre tableau multidimensionnels peut être vu comme un tableau de tableaux. Et en conséquence, la syntaxe pour initialiser plusieurs lignes va être un peu spéciale. Prenons un exemple :

```c
int tableau[2][2] = {{0,1}, {2,3}};
```

Ici, on demande à initialiser la première dimension avec les valeurs 0 et 1, et la deuxième dimension avec les valeurs 2 et 3. Pour faire simple, en gros, tout ce qui est entre { } sert à préciser le contenu d'un tableau. On trouve donc un paquets de { valeur , valeur, valeur , etc } pour chaque ligne. Et ce principe est le même pour tous les tableaux, multidimensionnels ou pas.

Il est également possible de ne préciser que certaines valeurs :

```c
int tableau[2][2] = {{0}, {2}};
```

Toutes les valeurs non-précisées seront automatiquement mises à zéro. On peut d'ailleurs procéder à une mise à zéro de tout le tableau très rapidement et facilement :

```c
int tableau[2][3][4] = {{{0}}};
```

#### Sans la taille de la première dimension ####

Il est possible lors de la déclaration de ne pas préciser la taille de la première dimension. Ainsi, ce code est parfaitement valide :

```c
int tableau[][3] = {{1, 2, 3, 4, 5}, {6, 7, 8}};
```

Et dans ce cas, la première dimension vaudra 5. Cependant, cela ne marche qu'avec la première dimension. Si vous ne précisez pas la taille des autres dimensions, vous aurez une erreur.

### Accès à un élèment
Maintenant que l'on sait comment déclarer et initialiser nos tableaux à plusieurs dimensions, il nous reste à voir comment manipuler leur contenu. On sait déjà le faire avec nos tableaux à une dimension, et passer à plusieurs dimensions n'est pas vraiment compliqué. La différence entre les tableaux à une dimension et ceux à plusieurs dimensions tient dans le nombre d'indices nécessaires pour repérer un élément dans notre tableau. Par exemple, si je prends un tableau à deux dimensions, je dois préciser l'indice de notre élément dans la ligne, et celui de la colonne. J'ai donc besoin de deux indices. Pour un tableau à trois dimensions, j'aurais besoin de trois indices. Et ainsi de suite : pour un tableau à N dimensions, j'aurais besoin de N indices. Pour rappel, tous les indices commencent à zéro. 

Pour accéder à un élément, on doit faire la même chose que dans le cas d'un tableau à une dimension : on doit calculer son adresse, et déréférencer celle-ci. Pour ce faire, on peut tout à fait se contenter d'utiliser le formalisme tableau vu dans le chapitre précédent, d'une façon un peu adaptée. Mais il y a tout de même quelques subtilités cachées que nous avons décidés, nous auteurs, de vous révéler. Toutes ces subtilités viennent de la façon dont on calcule l'adresse d'un élément d'un tableau à deux dimension. Et pour calculer cette dernière, on est obligé de savoir comment nos tableaux à plusieurs dimensions sont stockés en mémoire.

### Row Major Order ###

Prenons le tableau à deux dimensions suivant :

![](http://uploads.siteduzero.com/files/404001_405000/404726.png)

Comme vous le voyez, il s'agit d'un tableau d'entiers, à deux dimensions, comprenant trois lignes et trois colonnes. Comme on l'a dit plus haut, l'indice des lignes commence à zéro, tout comme l'indice des colonnes, et ceux-ci vont de 0 à 2. On peut de demander comment ses données sont organisées en mémoire. Et bien le langage C nous dit que toutes les données du tableau sont stockées les unes à coté des autres en mémoire. En clair : les données stockées dans un tableau à plusieurs dimensions sont rassemblées dans un tableau à une seule dimension.

Nous avons donc bien avancé. Ceci dit, il nous reste un petit détail à régler. Si je prends le tableau au-dessus, je peux parfaitement stocker celui-ci dans un seul tableau, mais deux deux façons différentes. Je peux tout stocker dans un tableau en mettant les colonnes les unes après les autres.

![](http://uploads.siteduzero.com/files/404001_405000/404728.png)

C'est cette solution qui est utilisée dans des langages de programmation comme FORTRAN, mais ce n'est pas le cas en C. En C, nos tableaux sont stockés lignes par lignes.

![](http://uploads.siteduzero.com/files/404001_405000/404729.png)

Maintenant que l'on sait cela, reste à savoir comment cela nous aide pour calculer l'adresse d'un élément.

### Calcul d'adresse ###

Pour illustrer ces histoires de calcul d'adresse, nous allons prendre le cas des tableaux à deux dimensions. Passer aux dimensions supérieures est vraiment facile une fois qu'on sait ce qu'il faut faire pour les tableaux à deux dimensions.

Pour localiser une donnée dans un tableau à deux dimensions, on doit d'abord localiser le début de la ligne voulue, puis localiser la donnée dans cette ligne. Vu que nos lignes sont stockées les unes après les autres en mémoire, on peut considérer qu'un tableau à deux dimension est un tableau de ligne. Calculer l'adresse d'une ligne se fait alors très simplement en utilisant la formule vue dans le chapitre précédent. On pose $L$ la longueur d'une ligne, $i$ l'indice de la ligne, et $A$ l'adresse de début du tableau (l'adresse du premier élément). L'adresse de la ligne d'indice $i$ vaut $A + L \times i$.

Ensuite, il nous reste à localiser la donnée dans la ligne à partir de son second indice. Pour cela, on réutilise la formule vue dans le chapitre précédent. On pose $L$ la longueur de la donnée, $j$ l'indice de la ligne, et $AL$ l'adresse du début de la ligne. L'adresse de la donnée ayant pour second indice $j$ vaut $AL + T \times j$.

En combinant ces deux formules, on obtient la formule finale qui nous permet de calculer l'adresse de l’élément d'indice i et j : l'adresse de la donnée d'indices $i$ et $j$ vaut $A + L \times i + T \times j$.

En clair, cette adresse est assez difficile à calculer. On préférera le formalisme tableau pour accéder à un élément d'un tableau à deux dimensions (ou plus). Cela donne donc des expressions du style ```tab[i][j]```, voyez de vous-même :

```c
#include <stdio.h>

#define N 3
#define M 5

int main (void)
{
    int tab[N][M] = {{0}};
    int i, j;

    /* Pour chaque ligne */
    for (i = 0; i < N; i++)
    {
        /* Pour chaque case */
        for (j = 0; j < M; j++)
        {
            printf("%d ", tab[i][j]);
        }

        printf("\n");
    }

    return 0;
}
```

Ce programme affiche le contenu d'un tableau de dimension *N* et *M*.

### Débordements chaotiques ###

Comme pour les tableaux à une dimension, déborder d'un tableau à plusieurs dimensions n'est pas sans conséquences. Le langage C ne fait aucune vérification, et il est facile de déborder d'un tableau à plusieurs dimensions sans s'en rendre compte. Et là encore, ce débordement est toujours un comportement indéterminé.

### Envoi à une fonction
### Formalisme pointeur ###

La première possibilité est celle-ci :

```c
void fonction(int (*tab)[taille_dimension_2]);
```

Cette possibilité exploite juste le lien pointeurs-tableaux (```*tab == tab[]```). Les parenthèses sont importantes car si on ne les mets pas, on obtient un tableau de pointeurs à la place d'un pointeur de tableau ce qui est totalement différent. Pour des tableaux de dimension supérieure, le principe est le même :

```
void fonction(int (*tab)[taille_dimension_2][taille_dimension_3]);
```

### Formalisme tableau ###

On peut aussi utiliser le formalisme tableau, comme ceci :

```c
void fonction(int tab[taille_dimension_1][taille_dimension_2]);
```

Pour des tableaux de dimension supérieure, le principe est le même :

```c
void fonction(int tab[taille_dimension_1][taille_dimension_2][taille_dimension_3]);
```

Encore une fois, le choix est votre concernant telle ou telle forme. Dans ce cours, nous utiliserons le formalisme tableau par soucis de clarté.

### Exercices
Comme à l'accoutumée, voici une petite liste d'exercices vous permettant de bien retenir tout ce que vous avez après lors de ce chapitre.

### Somme, produit, moyenne ###

Je vous propose en premier lieu de réaliser un programme qui calcule la somme et la moyenne de toutes les valeurs d'un tableau à deux dimensions, puis ensuite le produit de chaque ligne. Enfin, vous trouverez la valeur minimum et maximum du votre tableau multidimensionnel.

#### Somme des éléments d'un tableau ####

L'algorithme est très facile à trouver, donc je ne le donnerai pas. En revanche, la correction se trouve [ici](http://paste.awesom.eu/informaticienzero/rlO&ln) (à ne regarder qu'après avoir cherché suffisamment ou bien si vous voulez comparer avec votre code).

#### Moyenne des éléments ####

Pour bien fixer les choses, on va dire que calculer la moyenne d'un tableau, c'est calculer la somme de tous les éléments divisé par le produit des dimensions. Si c'est bien clair, vous devriez trouver le code très rapidement ! Sinon, il reste [la solution](http://paste.awesom.eu/informaticienzero/lJI&ln).

#### Produit des lignes ####

Cet exercice n'est pas très compliqué, là encore si vous réfléchissez à ce qu'il faut faire et aux fonctions déjà codées, vous y arriverez sans problème. Besoin quand même d'une correction ? Elle est [ici](http://paste.awesom.eu/informaticienzero/uOE&ln).

#### Minimum et maximum ####

Le but de cet exercice est le même que celui du chapitre précédent : retrouver le maximum et le minimum d'un tableau à deux dimensions. Néanmoins il y a plusieurs dimensions à parcourir. Je n'en dis pas plus, la solution est [là](http://paste.awesom.eu/informaticienzero/sst&ln) au cas où.

### Triangle de Pascal ###

Les triangles de Pascal sont des objets mathématiques amusants. Voici une petite animation qui expliquera mieux le principe que je ne pourrais le faire.

![Explication des triangles de Pascal en image](http://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

Le but va être de pouvoir générer des triangles de Pascal de la taille que l'utilisateur veut (il faut néanmoins que celle-ci soit inférieure ou égale aux dimensions du tableau). Pour cela, je vais vous donner un algorithme que nous allons décrypter ensemble (oui implémenter bêtement des algorithmes tous faits a un intérêt assez limité).

Tout d'abord, la première case est toujours à 1, donc nos boucles ne commenceront pas à 0 puisqu'on ne s'en occupera pas. Ensuite, la première et la dernière case de chaque ligne vaut 1, donc on peut écrire ça déjà. Mais entre ces deux bouts, que se passe t-il ? Eh bien c'est simple : chaque case [i,j] est la somme de la case précédente ([i - 1 , j - 1]) et de la case [i + 1 , j]. Un pseudo-code vous aidera à y voir plus clair.

```console
n = taille du triangle de Pascal
Mettre la première case du tableau à 1

Pour i = 1, i < n, i = i + 1
    Mettre la première case de la ligne à 1

    Pour j = 1, j < n - i, j = j + 1
         La case [i,j] prend la valeur [i - 1, j - 1] + [i - 1, j]

    Mettre la dernière case de la ligne à 1
```

Enfin, n'hésitez pas à faire une petite fonction qui affiche le tableau pour vérifier. Bon courage, vous allez progresser !

[secret]{
Le [code](http://paste.awesom.eu/informaticienzero/YJ0&ln) est relativement simple, reprenez-le à tête reposée s'il y a des choses que vous ne comprenez pas. Notez que dans la fonction d'affichage, j'évite d'afficher les 0 afin de rendre l'affichage plus lisible (bien entendu, il faut que le tableau de départ soit nul avant d'être passé à ces deux fonctions).
}

Finalement, ils ne sont pas si terribles que ça ces tableaux multi-dimensionnels n'est-ce-pas ? Ils sont certes beaucoup moins utilisés que les tableaux uni-dimensionnels, mais il était important pour nous de vous montrer leur existence et leur utilité. Si vous ne deviez retenir qu'une chose de ce chapitre, ce serait "Les tableaux multi-dimensionnels s'utilisent comme les tableaux uni-dimensionnels, il faut donc toujours faire attention aux indices".

Dans le chapitre suivant, nous aborderons un nouveau type d'agrégat, un peu particulier puisqu'il se base sur les tableaux : les **chaînes de caractères**.

## Les chaînes de caractères
Dans ce chapitre, nous allons passer aux choses sérieuses : nous allons apprendre à manipuler du texte en langage C. Ce texte, il faut bien trouver une solution pour le représenter dans notre ordinateur. Et pour cela, le langage C fournit ce qu'on appelle des chaînes de caractères. Nous allons donc voir en détail ces chaînes, expliquer ce qu'elles sont, montrer comment en créer et donner quelques fonctions de base pour les manipuler. Que la fête commence !

### Qu'est ce qu'une chaîne de caractères ?
Dans le chapitre sur les variables, j'avais mentionné le type ```char```. Pour rappel, une variable de type ```char``` peut contenir une donnée qu'on peut interpréter soit comme un nombre, soit comme une lettre. Le seul problème, c'est qu'une variable de type ```char``` ne peut stocker qu'une seule lettre. Cela ne suffit pas pour stocker un roman de Victor Hugo dans son intégralité. Un vrai texte est composé de plusieurs lettres. Si on veut stocker un texte dans notre ordinateur, on doit trouver un moyen pour rassembler plusieurs lettres dans un seul objet, manipulable dans notre langage. 

Rassembler plusieurs ```char``` serait difficile si on n'avait pas vu les chapitres précédents. Grâce à lui nous avons vu comment rassembler plusieurs variables d'un même type dans un seul objet : les tableaux. La solution à notre problème est toute trouvée. Pour rassembler plusieurs ```char``` ensemble, il suffit d'utiliser un tableau de ```char```. Et c'est ainsi que le texte est géré en C. bien sûr, il y a moyen de faire autrement. On peut aussi représenter du texte par d'autres structures de données, mais passons. Quoi qu'il en soit, on obtient ainsi ce qu'on appelle des **chaines de caractères**, aussi appelées *strings* en anglais.

### Pascal Strings

Quoi qu'il en soit, gérer des chaines de caractère stockées sous la forme de tableaux de ```char``` peut se faire de diverses manières. Ces manières se différencient par la façon dont on indique la fin de la chaine de caractère. Dans certains langages de programmation, les chaines de caractères sont stockées sous la forme d'un tableau de ```char``` auquel on a ajouté un entier pour indiquer sa longueur. Ainsi, notre chaine de caractère connait elle-même sa longueur, et on peut savoir quand on a atteint la fin en effectuant une comparaison entre l'indice du caractère courant avec la longueur de la chaine. De telles chaines de caractères sont souvent appelées des *Pascal Strings*, vu qu'elles sont utilisées telles quel dans le langage de programmation Pascal.

### Null Terminated Strings

Mais ce n'est pas ce qui est fait en C ! En C, les chaines de caractères ne connaissent pas leur longueur. À la place, on préfère indiquer la fin de la chaine de caractère avec un caractère spécial. Ce caractère spécial se note ```'\0'``` (également noté ```0``` ou même ```'\x00'```). Ce caractère est appelé **caractère nul** et marque la fin d'une chaîne de caractère. Les chaines de caractères qui fonctionnent su ce principe sont appelées des ***Null Terminated Strings***, ou encore des *C-Strings*.

On peut se demander quelles sont les raisons qui ont mené à un tel choix, celui-ci ayant quelques désavantages. En effet, lorsqu'on manipule des chaines de caractères, on a souvent besoin de leur longueur : cela permet d'éviter de déborder de la chaine pendant qu'on travaille dessus. Avec des chaines à la Pascal, cette longueur est immédiatement disponible. Mais avec des chaines à la C, on doit parcourir toute la chaine de caractère jusqu'au caractère nul pour en déduire sa longueur. C'est plus lent. D'ailleurs, presque tous les langages modernes (plus récents que le C) préfèrent utiliser des chaines à la Pascal.

Si les concepteurs du C ont choisi d'utiliser des *Null Terminated Strings*, c'est pour pouvoir gérer des chaines de caractères de plus grandes tailles sur le PDP-11, l'ordinateur sur lequel le C a été conçu. En effet, cet ordinateur possédait pas mal de mémoire, et pouvait gérer des chaines de grande taille. Mais, il ne pouvait gérer que des entiers non signés de 16 bits, qui allaient donc de 0 à 65535. S'ils avaient utilisé des chaines à la Pascal, ils auraient été limités par la taille de l'entier qui stocke la longueur. Avec les *Null Terminated Strings*, ce n'est pas le cas. De plus, les concepteurs du C trouvaient plus simple d'avoir à gérer des *Null Terminated Strings*.

### Déclaration et initilisation
Déclarer une chaine de caractère, c'est déclarer un tableau de ```char```, et cela peut se faire de deux manières différentes. 

### Première méthode

Avec la première méthode, il suffit de placer le mot-clé ```char```, suivi de l'identificateur de la chaine de caractère à créer, et encadrer le tout par un [ suivi d'un ]. On doit aussi indiquer la taille de notre chaine entre les [ ], mais passons. Il n'y a rien de bien compliqué : relisez le chapitre sur les tableaux si vous avez oublié, vous verrez que c'est très simple.

```c
char identificateur[taille];
```

#### Initialisation sans la taille

Reste que l'on peut aussi initialiser notre chaine de caractère. Cela se fait comme pour un tableau, à un détail prêt. Quand on initialisait un tableau, on le déclarait, et on lui affectait des valeurs placées entre deux accolades et séparées par une virgule. Le tableau était alors initialisé avec les valeurs placées entre accolades.

```c
int tableau[25] = { 2, 5, 6, 878, 7897, 9 };
```

Pour déclarer et initialiser une chaîne de caractères, on remplace les accolades par deux ```"```, entre lesquels on place le texte que l'on veut écrire. On utilise donc la syntaxe suivante :

```c
char identificateur[] = "du texte";
```

Cette notation est de nouveau du sucre syntaxique puisque elle nous évite de devoir initialiser chaque case du tableau manuellement, même si c'est possible. Ainsi, le code ci-dessus est strictement équivalent au code ci-dessous, la seule différence étant qu'il est plus rapide d'écrire le premier que le second.

```c
char identificateur[] = { 'd', 'u', ' ', 't', 'e', 'x', 't', 'e', '\0' };
```

#### Initialisation avec la taille

Bien entendu il est possible de préciser la taille du tableau à sa création. Il faut néanmoins se souvenir d'une règle importante : Taille du tableau = Nombre de caractères + ```'\0'``` final. Ainsi, si je veux stocker la chaîne ```"Hello world!"```, je dois créer un tableau de 13 cases, car ma chaîne comporte 12 caractères (car l'espace compte comme un caractère).

```c
char chaine[13] = "Hello world!"
```
Dans ce cas, le caractère nul sera automatiquement ajouté et j'obtiendrai alors une chaîne parfaitement valide. On peut logiquement se demander ce qu'il se passe si la taille n'est pas suffisante. Il faut distinguer deux cas.

* Si la taille précisée est inférieure au nombre de caractères, alors il y a risque de plantage lors de l'utilisation de la chaîne. D'ailleurs, le compilateur devrait vous prévenir avec un message du style *« warning: initializer-string for array of chars is too long »*, ce qui signifie que la chaîne que l'on veut stocker est trop grande par rapport à la taille du tableau.

* Si la taille précisée est égale au nombre de caractères, alors on obtient non pas une chaîne de caractère, mais un **tableau de caractères**. Il s'agit simplement d'un tableau qui contient divers caractères, mais qui n'est pas terminé par le caractère nul. Bien entendu, cela peut également amener des problèmes quand on tente de les manipuler.

### Une autre manière de faire

Cependant, il existe une autre façon de déclarer de d'initialiser une chaîne de caractères : un pointeur sur ```char```. La syntaxe est similaire à celle du tableau :

```c
char * ptr = "du texte" ;
```

Alors qu'elles semblent identiques à première vue, les deux formes possèdent des différences assez importantes. 

#### Constantes chaînes

Considérons les deux déclarations suivantes.

```c
char tab[20] = "hello";
char * ptr = "hello";
```

Hormis les différences vues dans le chapitre précédent, c'est surtout le contenu des deux déclarations qui est intéressant. Dans le premier cas, la notation ```"hello"``` correspond à ```{ 'h', 'e', 'l', 'l', 'o', '\0' }``` alors que la deuxième notation est ce que l'on appelle une **constante de type chaîne**.

Une constante de type chaîne est, comme son nom l'indique, un tableau de ```char``` constant. Dès lors, le pointeur *ptr* pointe sur la première case de ce tableau qui est situé quelque part en mémoire. Cependant, comme ce tableau est constant, il est impossible de modifier ses éléments. Ainsi, dans le code suivant, la deuxième ligne provoquera une erreur lors de l'exécution du programme :

```c
tab[1] = 'a';
ptr[1] = 'a';

/* Le résultat est identique avec la forme *(ptr + 1) = 'a' */
```

Pour éviter ces problèmes, le mieux est de prendre l'habitude de déclarer constant de tels pointeurs. Ainsi, dès que l'on tentera de les modifier, la compilation avortera en affichant une erreur du type *« error: assignment of read-only location '*(ptr + 1)' »*.

```c
const char * ptr = "hello";
ptr[1] = 'a';
```

#### Affectation

L'autre différence réside dans le fait que *ptr* peut se voir affecter une nouvelle valeur, tandis que *tab* ne le peut pas (ce que nous avons dis dans le chapitre sur les tableaux s'applique ici aussi). Ainsi, dans le code suivant, la deuxième affectation est bonne à l'inverse de la première.

```c
char tab[20] = "hello";
char * ptr = "hello";

tab = "world";
ptr = "world";
```

Pour modifier un tableau de ```char```, il faut faire comme n'importe quel tableau à savoir modifier les éléments un par un :

```c
char tab[10] = "hello";

tab[0] = 'w';
tab[1] = 'o';
tab[2] = 'r';
tab[3] = 'l';
tab[4] = 'd';
tab[5] = '\0';
```

**Note :**

1. Si cela vous intéresse vous pouvez trouver un complément d'information [sur ce sujet](http://www.siteduzero.com/forum-83-508979-p1-difference-entre-char-tab-et-char-tab.html).

### Lire et écrire dans une chaîne
Il est évidemment possible de saisir des chaînes de caractères au clavier ou de les afficher à l'écran (dans la console). 

### Printf et scanf

Les fonctions *printf*() et *scanf*() disposent d'un indicateur de conversion qui permet d'afficher ou de demander une chaîne de caractère : ```%s```. Le programme suivant permet d'afficher « *Bonjour* » à l'écran :

```c
/* ou mieux : const char * chaine = "Bonjour"; */
char chaine[] = "Bonjour";
printf("%s", chaine);
```

### Chaînes et scanf

Pour interagir avec l'utilisateur avec la fonction *scanf*(), on utilise le même indicateur de conversion. Cependant, il faut penser à réserver un espace suffisant lors de la création du tableau pour permettre à l'utilisateur de rentrer une chaîne de caractères sans écraser des données en écrivant après le tableau. Comme il n'est pas possible de connaitre la taille exacte de ce que l'utilisateur va rentrer, on est obligé de créer un grand tableau de ```char``` :

```c
char chaine[256];

printf("Donnez votre prenom : ");
if (scanf("%s", chaine) == 1)
{
    printf("Vous vous appelez %s\n", chaine);
}
```

Petite remarque : pour les chaînes de caractères, on utilise pas le ```&``` dans le *scanf*() car on donne déjà l'adresse de la première case du tableau. Ce code affichera par exemple : 

```text
Donnez votre prénom : Litchi
Vous vous appelez Litchi
```

#### Chaîne de caractères trop longue

Cependant, tout n'est pas si rose ! En effet, dans cet exemple, l'utilisateur peut rentrer jusqu'à 255 caractères (car la dernière case est réservée pour le ```'\0'```). Toutefois, si jamais il dépasse cette limite, il va écrire au-delà du tableau et donc potentiellement écraser des données du programme. C'est ce que l'on appel un « dépassement de tampon » (ou *buffer overflow en anglais*).

Nous disons « *potentiellement* » parce que le plus souvent, le système d'exploitation empêchera votre programme d'écrire dans une zone mémoire qui ne lui est pas réservée. Néanmoins, ce n'est pas automatique, ni
garanti, ce qui rend ce type de problème particulièrement vicieux.

Pour éviter ce problème, il est possible de spécifier une taille maximale à la fonction *scanf*(). Pour ce faire, il suffit de placer un nombre entre le symbole `%` et le format `s`, comme ceci :

```c
char chaine[256];

printf("Donnez votre prenom : ");
if (scanf("%255s", chaine) == 1)
{
    printf("Vous vous appelez %s\n", chaine);
}
```

**Attention !**

1. La fonction *scanf*() ne compte pas le `\0` final ! Il vous est donc nécessaire de lui indiquer la taille de votre tableau diminuée de un.

#### Chaîne de caractères avec des espaces

Mais, ce n'est pas tout !  

Le format `%s` signifie en fait : « *la plus longue suite de caractère ne comprenant pas d'espaces* ». Les espaces étant ici entendu comme une suite d'un ou plusieurs des caractères suivant : `' '`, `'\f'`, `'\n'`, `'\r'`, `'\t'`, `'\v'`. Autrement dit, si vous entrez : « *bonjour tout le monde* », *scanf*() va s'arrêter à « *bonjour* » (car il y a un espace juste après).

Pour éviter ce problème, il est possible d'utiliser un format particulier où vous pouvez spécifier les caractères qui vous intéressent. Celui-ci se présente comme suit : `%[liste_de_caracteres]`.

Par exemple, si vous souhaitez uniquement une suite de nombre, il est possible d'utiliser ce code :

```c
char nombre[16];

printf("Entrez un nombre : ");
if (scanf("%15[0123456789]", nombre) == 1)
{
    printf("Vous vous entrez : %s\n", nombre);
}
```

Qui donne :

```text
Entrez un nombre : 123
Vous vous entrez : 123

Entrez un nombre : 1bbbb
Vous vous entrez : 1
```

Comme vous pouvez le constater, les caractères non numériques ne sont pas lus
par *scanf*() lors de la dernière saisie.

-- *D'accord, mais si je veux récupérer du texte avec des espaces et de la ponctuation, je fais comment ? J'utilise le format : *`%[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#%&'()*+,-./:;<=>?[\\\]^_{|}~ ]` *?!* o_O

Suivant ce que nous venons de voir, oui. ^^  
Cependant, il y a une autre solution (*ouf* !) : la négation.  
Si le symbole `^` est placé juste après le premier `[` alors le format signifie : « *la plus longue suite de caractères ne comprenant **pas** les caractères indiqués* ».

Ainsi, si je souhaite récupérer une ligne entière, celle-ci étant terminée par un `\n`, le code suivant peut être employé :

```c
char chaine[256];

printf("Donnez votre prenom : ");
if (scanf("%255[^\n]", chaine) == 1)
{
    printf("Vous vous appelez %s\n", chaine);
}
```

Ce qui donne :

```text
Donnez votre prénom : Charles Henri
Vous vous appelez Charles Henri
```

Magnifique ! Problème résolu. :)

#### Une histoire de vidange

Mais en fait, non. :p  

Nous vous avons dit que lorsque *scanf*() n'a plus assez de place pour lire des caractères ou que ceux-ci ne correspondent pas à ceux attendus par le format courant, ces derniers ne sont pas lus. Cependant, ils ne disparaissent pas dans l'hyperespace, ils sont toujours bien là, prêt à être lu au prochain appel, en témoigne ce petit exemple :

```c
char chaine1[16];
char chaine2[16];

printf("Un morceau : ");
if (scanf("%15[^\n]", chaine1) == 1)
{
    printf("Un autre morceau : ");
    if (scanf("%15[^\n]", chaine2) == 1)
    {
        printf("\n%s, %s\n", chaine1, chaine2);
    }
}
```

```text
Un morceau : une phrase trop longue
Un second morceau :
une phrase trop, longue
```

Étant donné que la première saisie comportait trop de caractères, ceux-ci sont restés en attente jusqu'à la suivante, ce qui explique que vous ne pouvez rien entrer lors de la deuxième, la fonction *scanf*() ayant encore de quoi lire.

**Note :**

1. Nous avons anticipé ce fait en ajoutant un `\n` avant le résultat afin qu'il soit sur la troisième ligne. Cependant, ceci est purement cosmétique.

-- *Oui, mais on s'en débarrasse comment de ces caractères surnuméraires ?*

En les lisant, tout simplement. :)  
Étant donné qu'une ligne se termine par un `\n`, il est possible de lire le reste comme suit :

```c
int c;

while ((c = getchar()) == '\n' && c != EOF)
    ;
```

Une fois cette boucle exécutée, il vous est loisible d'appeler à nouveau *scanf*() sans que des caractères non lus ne viennent vous gêner.

**Note :**

1. La fonction *getchar*() permet de lire un caractère à la fois, nous la verrons plus en détail un peu plus loin. Pour information, celle-ci peut retourner la constante EOF (déclarée dans l'en-tête **<stdio.h\>**) en cas d'erreur, d'où la seconde condition.

### Autres fonctions de stdio.h

Pour lire et écrire des données, nous avons vu entre autre *printf*() et *scanf*(), qui permettent respectivement d'écrire et de lire autant de données que l'on souhaite. Sachez que ces deux fonctions font en réalité partie d'une famille de plusieurs fonctions, toutes définies dans **<stdio.h\>**. Nous allons en découvrir deux.

#### sprintf() - Écrire dans une chaîne

La fonction [sprintf()](http://pwet.fr/man/linux/fonctions_bibliotheques/printf), *s* signifiant *string*, est comme son nom l'indique une fonction qui permet d'écrire des données dans une chaîne de caractères. Son prototype, qui est un peu particulier, requiert certaines connaissances que vous pouvez acquérir en lisant [ce tutoriel](http://www.siteduzero.com/tutoriel-3-93219-les-fonctions-a-nombre-variable-de-parametres.html) . N'hésitez pas à le garder dans un coin, il pourra toujours vous être utile un jour. Le voici :

```c
int sprintf (char * str, const char * format, ...);
```

Elle fonctionne exactement comme *printf*(), à ceci près que les arguments seront écrits dans *str*, qui bien entendu doit être de taille suffisante. Enfin, elle retourne le nombre de caractères inscrits (sans compter le `\0` final) ou bien un nombre négatif en cas d'erreur. 

Une question vous vient peut-être à l'esprit : « *mais à quoi peut bien servir cette fonction ?* ». En effet, à première vue, écrire dans une chaîne de caractères n'a pas grand intérêt. Je vais vous prouver le contraire avec un exemple. Dans la partie précédente, nous avons vu comment convertir une chaîne de caractères en nombre. Grâce à *sprintf*(), il est possible de faire l'inverse.

```c
#include <stdio.h>

int main(void)
{
    char str[10];
    int n = 5;

    sprintf(str, "%d", n);
    puts(str);

    return 0;
}
```

Essayez ce programme et vous verrez que *sprintf*() a bien écrit le chiffre 5 dans *str*. Vous pouvez maintenant convertir les nombres en chaînes de caractères de manière portable et efficace !

Cependant, comme pour *scanf*(), il est nécessaire de faire attention à ne pas dépasser les limites du tableau. Comment s'en assurer ? Malheureusement, il n'est pas possible de spécifier une taille comme pour *scanf*(), aussi, deux solutions s'offrent à vous :

* vérifier que le nombre en question ne dépasse pas un certains seuil ;
* compter la quantité de chiffres composant le nombre avant d'appeler *sprintf*().

Ainsi, l'exemple ci-dessous ne pose pas de problème puisque je sais que si le nombre est inférieur ou égal à 999 999 999, il n'excèdera pas neuf caractères (**n'oubliez pas de compter le `\0` final !**).

```c
#include <stdio.h>

int main(void)
{
    char str[10];
    int n;

    printf("Entrez un nombre : ");
    if (scanf("%d", &n) == 1)
    {
        if (n <= 999999999L)
        {
            sprintf(str, "%d", n);
            puts(str);
        }
    }
    return 0;
}
```

#### sscanf() - Lire dans une chaîne

La fonction [sscanf()](http://pwet.fr/man/linux/fonctions_bibliotheques/scanf) permet, comme sa cousine, de manipuler des chaînes de caractères mais cette fois pour les lire et récupérer des données. Voici son prototype :

```c
int sscanf (const char * str, const char * format, ...);
```

Elle renvoie le nombre de formats correctement lus, ou bien un nombre négatif ou inférieur au nombre attendu respectivement si rien n'a pu être converti ou uniquement une partie. Voici un exemple d'utilisation dans lequel on récupère des données dans une chaîne de caractères :

```c
#include <stdio.h>

int main(void)
{
    char str[10];
    int n = 0;
    const char * s = "5 abcd";

    if (sscanf(s, "%d %9s", &n, str) == 2)
    {
        printf("%d %s\n", n, str);
    }
    return 0;
}
```

Si vous exécutez le programme, vous remarquerez que la variable *n* vaut maintenant 5 et que *str* contient bien ```"abcd"```. L'intérêt de cette fonction ? Elle permet par exemple de récupérer des données rentrées par un utilisateur comme dans le cas d'une calculatrice ou d'un serveur.

**Note :**

1. La fonction *sscanf*() ne souffre pas du même problème que *scanf*() en ce qui concerne de potentiels caractères non lus, nous y reviendrons un peu plus tard.

### Conversion de chaînes de caractères en nombres
Dans ce qui va suivre, nous allons vous montrer quelques fonctions simples qui manipulent des chaines de caractère. Ces fonctions que nous allons voir permettent de convertir une chaîne de caractères en nombre. Elles sont définies dans **<stdlib.h\>**. A quoi peuvent-elles bien servir ? Elles s'avèrent utiles dans le cas d'une calculatrice par exemple : l'utilisateur rentre une chaîne de caractère qui contient des nombres, ceux-ci sont convertis en valeurs numériques, et on peut effectuer des calculs sur eux.

### strtol - Convertir une chaîne en long

Commençons par *strtol*. Cette fonction lit une chaîne de caractères et tente de la convertir en ```long```. Elle s'arrête au premier caractère qui n'est pas un chiffre (sont toutefois tolérés : des espaces ainsi qu'un signe `+` ou `-` avant le nombre). 

#### Paramètres

Cette fonction prend trois paramètres :

* le premier est la chaîne de caractères que l'on souhaite convertir ;
* le deuxième est l'adresse d'un pointeur sur `char` qui servira à savoir où la fonction à rencontrer une erreur (si elle en rencontre une). Notez que l'on peut ne pas l'utiliser en passant un pointeur nul ;
* la base dans laquelle on veut convertir la chaîne, qui doit être comprise entre deux et trente-deux.

La fonction retourne le nombre converti si elle réussi, sinon zéro en cas d'échec ou LONG_MIN/LONG_MAX si la conversion donne un nombre trop petit/grand pour être stocké dans un `long` (auquel cas la variable *errno* est mise à ERANGE).

```c
long strtol(const char * nptr, char ** endptr, int base);
```

### stroul

Il existe une variante de cette fonction pour convertir une chaîne en ```unsigned long``` cette fois : *strtoul*(). Cette fonction prend les mêmes paramètres que *strtol*(), seul la valeur de retour change :

```c
unsigned long int strtoul(const char * nptr, char ** endptr, int base)
```

Voici un programme qui demande une chaîne de caractères et une base avant de tenter de convertir cette chaîne en nombre, suivi de quelques résultats.

```c
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>


int main(void)
{
    char tab[256];
    char * ptr;
    int base;
    long n;
    int c;

    printf("Entrez une chaine : ");
    if (scanf("%255s", tab) != 1)
    {
        printf("Erreur lors de la saisie du nombre.\n");
        return EXIT_FAILURE;
    }

    while ((c = getchar()) != '\n' && c != EOF)
        ;

    printf("Entrez une base : ");
    if (scanf("%d", &base) != 1)
    {
        printf("Erreur lors de la saisie de la base.\n");
        return EXIT_FAILURE;
    }

    errno = 0;
    n = strtol(tab, &ptr, base);
    if (*ptr == '\0' && errno != ERANGE)
        printf("%s en base %d = %ld\n", tab, base, n);
    else
    {
        printf("Une erreur s'est produite lors de la conversion.\n");
        printf("Il reste : %s\n", ptr);
    }
    return 0;
}
```

```text
Entrez une chaine : 12345
Entrez une base : 10
12345 en base 10 = 12345

Entrez une chaine : 12345
Entrez une base : 16
12345 en base 16 = 74565

Entrez une chaine : 3615salut
Entrez une base : 10
Une erreur s'est produite lors de la conversion.
Il reste : salut

Entrez une chaine : 999999999999999999999999999
Entrez une base : 10
Une erreur s'est produite lors de la conversion.
Il reste : 
```

### strtod - Convertir une chaîne en double

Ensuite, on doit parler de la fonction *strtod*(). Cette fonction va convertir une chaine de caractère en ```double```. Elle fonctionne presque comme les fonctions *strtol*() et *strtoul*(). Le comportement est identique mais les paramètres sont néanmoins différents.

Le premier paramètre est toujours la chaîne de caractère que l'on souhaite convertir, le deuxième est toujours l'adresse d'un pointeur sur ```char``` qui sert à repérer les erreurs, mais le troisième n'existe plus. 

```c
double strtol(const char * nptr, char ** endptr);
```

Voilà, nous venons de découvrir les chaînes de caractères. De nouvelles possibilités s'offrent à nous ! Enfin ... pour l'instant, on est limité. Comment récupérer la longueur d'une chaîne par exemple, ou encore comparer deux chaînes pour savoir si elles sont identiques ou différentes ? Heureusement, nous allons combler ce manque dans le chapitre suivant consacré à la découverte d'une bibliothèque consacrée aux chaînes de caractères : **<string.h\>**

## L'en-tête <string.h>
Nous savons déclarer des chaînes de caractères et les initialiser, mais pour l'instant, ça s'arrête là. Dans cette partie, nous allons découvrir quelques fonctions de la bibliothèque standard qui permettent d'effectuer des opérations diverses sur les chaînes, comme calculer la taille ou bien copier une chaîne dans une autre. Tous les prototypes de ces fonctions sont définis dans le fichier d'en-tête ```<string.h>```. Pour pouvoir les utiliser, vous allez devoir 'inclure comme ceci :

```c
#include <string.h>
```

Chose étonnante, ```<string.h>``` ne contient pas que des fonctions qui manipulent des chaînes de caractères : ce fichier d'en-tête fourni aussi des fonctions qui travaillent directement sur des blocs de mémoire. Nous allons découvrir tout cela au cours de ce chapitre.

### Longueur
La première fonction que nous allons examiner est *strlen*, comme **str**ing **len**gh, soit *longueur de chaîne*. Cette fonction va nous permettre de récupérer la taille de n'importe quelle chaîne de caractères sans compter le ```'\0'``` final.

#### Résultat ####

La fonction retourne un ```size_t```. Pour ceux qui ne se rappellent pas, ```size_t``` est un type qui sert à stocker les tailles de données assez grosses, comme les tableaux ou les chaînes de caractères. C'est donc normal que *strlen* donne un résultat de type ```size_t```. Il a été inventé parce que sur certaines machines, il est possible de créer des données tellement grosses qu'on ne peut pas stocker leur taille dans un simple ```int``` ou un ```unsigned int```. 

#### Argument ####

Comme on le déduit de son utilité, cette fonction va prendre en argument une chaine de caractère dont il faut donner la taille. Ce paramètre est de type ```const char *``` : on a un pointeur sur ```char``` constant. Le lien entre pointeurs et tableaux se retrouve encore une fois. A notez la présence de ```const```, qui empêchera toute modification, volontaire ou non, de la chaîne.

#### Prototype ####

De ce qu'on vient de dire précédemment, on en déduit que son prototype est le suivant :

```c
size_t strlen (const char * str);
```

#### Exemple ####

Illustrons ce code par un exemple. Je veux connaitre la taille de cette chaîne : ```"Bonjour les amis!"```. J'utilise donc *strlen* qui me renverra le nombre de caractères de cette chaîne.

```c
char chaine[] = "Bonjour les amis!";

printf("Taille de la chaîne = %u\n", (unsigned) strlen(chaine));
```
```console
Taille de la chaine = 17
```

### Copie
### strcpy - Copier une chaîne ###

Après *strlen*, qui permet de connaitre la longueur d'une chaine, voici le tour de *strcpy*. La fonction *strcpy* copie une chaîne dans une autre chaîne et renvoie un pointeur sur cette dernière. Elle copie tous les caractères, y compris le caractère nul ```'\0'```. Pour vous souvenir de ce que cette fonction fait, vous devez savoir que *strcpy* est l'abréviation de **str**ings **c**o**py** soit *copie de chaînes*.

#### Prototype ####

Son prototype est le suivant :

```c
char * strcpy(char * dest, const char * src);
```

Ses deux arguments sont d'abord la chaine de destination, puis la chaine source.

#### Débordements chaotiques ####

Cependant, *strcpy* a un léger problème. Elle ne fait aucune vérification sur les longueurs des chaînes sources et de destination. Si la chaîne de destination est trop petite pour recevoir toute la chaîne d'origine, la fonction *strcpy* ne s'en aperçoit pas. Conséquence : elle écrase les données situées après. Par exemple, voici un exemple de copie qui fonctionne, mais qui écrase des données :

```c
char bug[5];

/* chaîne de destination trop petite donc problème */
strcpy(bug, "bonjour");
```

Pour information, certains pirates utilisent ce comportement pour faire exécuter des programmes malicieux. C'est ce qu'on appelle l'attaque par [buffer overflow](http://fr.wikipedia.org/wiki/Dépassement_de_tampon). Cela peut sembler ennuyeux, et dans les faits ça l'est.

Autre détail : si jamais les deux chaines se recouvrent (c'est-à-dire si un morceau de la première chaine est inclus dans la seconde ou réciproquement), le comportement de *strcpy* est indéfini. En clair : les deux chaînes doivent être séparées et bien distinctes et doivent occuper des zones de mémoire bien séparées, sans recouvrements. Par exemple, si on souhaite copier une chaine dans elle-même, le résultat de *strcpy* est indéterminé. Même chose si on veut copier un morceau d'une chaine dans elle-même.

Si les concepteurs du C ont décidés que *strcpy* aurait ce comportement, c'est encore une fois pour des raisons de performances. Effectuer des vérifications sur les longueurs des chaînes sources et de destinations, ça prend du temps. Et dans un langage conçu pour la performance, c'est niet !

### strncpy - Copie partielle d'une chaîne ###

Passons maintenant à la fonction *strncpy*. Cette fonction est quasiment identique à la précédente, sauf que *strncpy* ne copie qu'un certain nombre de caractères. Au lieu de copier toute la chaine source dans la chaine de destination (comportement de *strcpy*), on peut demander à *strncpy* de ne copier que $n$ caractères.

#### Prototype ####

Voici le prototype de cette fonction :

```c
char * strncpy(char * dest, const char * src, size_t n);
```

Comme on le voit, la valeur de retour est la même que pour la fonction *strcpy* : il s'agit d'un pointeur qui pointe sur la chaine de destination.

#### Arguments ####

Passons maintenant aux arguments. Les deux premiers arguments sont, dans l'ordre, la chaine de destination, suivie de la chaine source. Le troisième argument est le nombre de caractères à copier. 

#### Conséquences imprévues ####

Si cette fonction peut appraraître comme une bonne alternative à la fonction strcpy de prime abord, sachez qu'il n'en est rien ! Tout d'abord, celle-ci souffre des même problèmes que strcpy : d'une part, elle ne fait aucune vérification sur la longueur respective des chaines et, d'autre part, si jamais les deux chaines se recouvrent, son comportement est indéterminé. Ensuite, elle dispose de son propre lots de problèmes : si la chaîne source est plus petite que la chaîne de destination, elle ajoute des caractères nuls en lieu et place des caractères manquants (ce qui nuit aux performances) ; à l'inverse, si la chaîne de destination est plus petit que la chaîne source et que la taille maximale spécifiée correspond à celle de la chaine de destination, cette dernière ne sera pas terminée par un caractère nul.

Vous me demanderez sans doute pourquoi cette fonction existe si elle pose autant problème ? La réponse est simple : elle n'a en vérité pas été conçue pour la manipulation de chaîne de caractères, mais pour la manipulation de champ de taille fixe (la notion de champ sera discutée dans le chapitre consacré aux structures). En bref, oubliez cette fonction lorsque vous manipulez des chaînes de caractères.

### Comparaisons
### strcmp - Comparer deux chaînes ###

La fonction *strcmp* permet de comparer deux chaînes de caractères, lettre par lettre. Pour s'en souvenir, il suffit de se dire que *strcmp* est l'abréviation de **str**ings **c**o**mp**are, qui veut dire *comparaison de chaînes* en anglais.

#### Argument ####

Cette fonction *strcmp* prend deux arguments : ces deux arguments ne sont rien d'autre que les deux chaînes à comparer. Comme on ne modifie pas les chaînes, ils sont tous les deux constants.

#### Valeur de retour ####

Petit détail : cette fonction ne renvoie pas un booléen, comme on pourrait s'y attendre. Elle renvoie une valeur entière qui sera négative, nulle ou positive si la première chaîne est respectivement plus petite, de même taille ou plus grande que la deuxième chaîne. Elle se base sur l'ordre alphabétique des lettres pour comparer les deux chaines de caractères.

#### Prototype ####

Voici donc son prototype : 

```c
int strcmp(const char * chaine1, const char * chaine2);
```

#### Exemple ####

Illustrons son utilisation par un exemple très simple où je compare deux chaînes :

```c
char chaine1[] = "bonjour";
char chaine2[] = "bonsoir";

if (strcmp(chaine1, chaine2) == 0)
{
    puts("Les chaines sont identiques.");
}

else
{
    puts("Les chaines sont differentes.");
}
```

Ce code affiche, sans surprise :

```console
Les chaines sont différentes.
```

### strncmp - Comparer deux chaînes partiellement ###

Il existe une variante de la fonction *strncmp* qui permet de comparer des portions de chaines de caractères au lieu de chaines de caractères complètes. Plus précisément, *strncmp* permet de ne comparer que les $n$ premiers ```char``` de nos deux chaînes. Cela permet de vérifier que les $n$ premiers caractères sont identiques ou différents.

#### Valeur de retour ####

Son comportement est identique à *strcmp* : elle renvoie une valeur entière qui sera négative, nulle ou positive si la première chaîne est respectivement plus petite, de même taille ou plus grande que la deuxième chaîne. 

#### Arguments ####

Cette fonction prend 3 paramètres. Elle prend notamment des pointeurs vers les deux chaînes de caractères à comparer. Le dernier paramètre est le nombre de ```char``` qu'il faut comparer, le fameux nombre $n$ mentionné plus haut. Par exemple, si jamais je ne veux comparer que les 3 premières lettres, j'enverrais 3 comme paramètre. Si au contraire je veux en comparer 5, alors j'enverrais 5 à la fonction.

#### Prototype ####

Voici son prototype :

```c
int strncmp(const char * s1, const char * s2, size_t n);
```

#### Exemple ####

```c
char chaine1[] = "bonjour";
char chaine2[] = "bonsoir";
const int n = 3;

if (strncmp(chaine1, chaine2, n) == 0)
{
    puts("Les deux chaines sont identiques.");
}

else
{
    puts("Les deux chaines sont differentes.");
}
```
```console
Les deux chaines sont identiques.
```

On demande à comparer les 3 premiers octets, et vu que les trois premiers caractères sont identiques, l'ordinateur affiche que les chaînes sont identiques. Si on avait pris une valeur plus élevée, il aurait affiché *« Les deux chaines sont différentes »*.

### Recherche
### strchr - Rechercher un caractère ###

La fonction *strchr* permet de rechercher un caractère en particulier dans une chaîne. Pour vous en souvenir plus efficacement, il suffit de savoir que *strchr* est l'abréviation de **str**ing **ch**aracte**r**.

#### Valeur de retour ####

Si notre fonction trouve le caractère à chercher, elle renvoie un pointeur sur ce caractère, sinon elle renvoie NULL ; si le caractère est présent plusieurs fois, elle renvoie un pointeur sur la première occurrence de ce caractère. Chose importante à retenir : toujours bien vérifier que la fonction ne retourne pas NULL et agir en conséquence si c'est le cas.

#### Paramètres ####

Le premier paramètre est la chaîne dans laquelle on doit effectuer la recherche, le deuxième paramètre étant le caractère à rechercher. Il est de type ```int```, ce qui ne change rien car au final les lettres sont des chiffres pour l'ordinateur. 

#### Prototype ####

De ce qu'on vient de dire précédemment, on en déduit que son prototype est le suivant :

```c
char * strchr (const char * str, int c);
```

#### Exemple ####

Illustrons par un exemple : je veux chercher la première occurrence de la lettre ```'l'``` dans la phrase ```"Cours sur le langage C"```.

```c
char chaine[] = "Cours sur le langage C";
char * str = strchr(chaine, 'l'); 

if (str != NULL)
{
     /* notation équivalente à str[0], revoyez le chapitre
      sur les tableaux si vous ne vous en rappelez plus */
     printf("%c\n", *str);
}
```

Comme *strchr* a trouvé le caractère que je cherchais, elle a retourné un pointeur sur ce caractère. 

#### Remarque ####

Au fait, petite astuce : rien n’empêche de considérer ce pointeur comme un pointeur sur une chaine. Dans ce cas, ce pointeur pointe sur le reste de la chaine de caractère, lettre ```'l'``` inclue.  Ainsi, le code suivant :

```c
char chaine[] = "Cours sur le langage C";
char * str = strchr(chaine, 'l'); 

if (str != NULL)
{
     puts(str);
}
```

affiche ceci : 

```console
le langage C
```

#### strrchr - La cousine de strchr ####

Au fait, *strchr* possède une cousine. La fonction *strrchr* fait la même chose mais elle retourne un pointeur sur le dernier caractère rencontré. C'est la seule différence ; tout ce qui a été dit précédemment est valable aussi pour *strrchr*.

### strpbrk - Rechercher une liste de caractères ###

Avec la fonction *strchr* vue précédemment, on sait trouver la première occurrence d'un caractère dans une chaine (ou la dernière, avec *strrchr*). C'est très bien, mais on peut faire mieux. Imaginez que je veuille faire la même chose, non pas avec une seule lettre, mais avec plusieurs. Par exemple, avec *strchr*, je peux savoir où se situe le premier ```'l'``` dans une chaine. Mais pour trouver où se situe la première lettre qui est soit un ```'l'```, soit un ```'a'```, je ne peux le faire avec *strchr* tout seul. On peut ruser, et utiliser un petit bout de code, mais le fait est que cette situation a déjà été prévue par les concepteurs du C. Pour ce faire, on a inventé la fonction *strpbrk*.

#### Valeur de retour ####

Cette fonction est différente de *strchr* et *strrchr* en un point : au lieu de ne rechercher qu'un seul caractère, elle recherche le premier caractère parmi une liste de caractères. Si elle trouve un des caractères à chercher, elle renvoie un pointeur sur ce caractère. Sinon elle renvoie NULL. 

#### Prototype ####

Son prototype est le suivant : 

```c
char * strpbrk(const char * str, const char * c);
```

#### Paramètres ####

Le premier paramètre est la chaîne dans laquelle on doit effectuer la recherche, le deuxième paramètre étant la liste de caractères à rechercher. 

#### Exemple ####

Prenons un exemple : je veux chercher les caractères ```'u'```, ```'t'``` et ```'l'``` dans la phrase ```"Salut aux lecteurs !"```.

```c
char chaine[] = "Salut aux lecteurs !";
char * str = strpbrk(chaine, "utl");

if (str != NULL)
     printf("Premiere occurrence de u, t ou l : %s\n", str);
```

Comme la fonction a trouvé un des caractères que l'on voulait, elle s'arrête et renvoie un pointeur sur ce caractère :

```console
Première occurrence de u, t ou l : lut aux lecteurs !
```

Là encore, la seule chose à retenir est de vérifier le retour de la fonction.

### strstr - Rechercher une chaîne dans une autre ###

Et enfin, nous terminons cet aperçu des fonctions de recherche en parlant de *strstr*. La fonction *strstr* va rechercher si une chaîne de caractères est inclue dans une autre. Son rôle est donc de rechercher des sous-chaînes.

Par exemple, si je prends la chaine ```"le langage C"```, je sais que la chaîne ```"langage"``` est inclue dedans. Pareil pour les chaînes ```"lang"```, ```"gage C"```, etc. 

#### Valeur de retour ####

Si elle trouve la chaîne à chercher, elle renvoie un pointeur sur cette chaîne, sinon elle renvoie NULL. 

#### Paramètres ####

Le premier paramètre est la chaîne dans laquelle il faut effectuer la recherche, et le deuxième est la chaîne à rechercher. 

#### Prototype ####

Son prototype est le suivant :

```c
char * strstr(const char * str1, const char * str2);
```

#### Exemple ####

Supposons que je veuille chercher le mot ```"langage"``` dans la phrase ```"Cours sur le langage C"```.

```c
char chaine[] = "Cours sur le langage C";
char * str = strstr(chaine, "langage");

if (str != NULL)
     puts(str);
```

Comme la fonction a trouvé la chaîne à chercher, elle s'arrête et renvoie un pointeur sur cette chaîne : 

```console
langage C
```

Il n'y a pas beaucoup de différence avec la fonction précédente, si ce n'est que *strstr* recherche toute la chaîne et pas seulement un ou plusieurs caractère(s).

### Autres
### strcat - Concaténer deux chaînes ###

La fonction *strcat* sert à concaténer deux chaînes, c'est à dire simplement coller deux chaînes l'une à la suite de l'autre. Par exemple, si je concatène les chaînes ```"im"``` et ```"puissant"```, j'obtiendrais la chaîne ```"impuissant"```. Autre exemple : si je concatène la chaîne ```"abc"``` avec la chaîne ```"def"```, j'obtiendrai ```"abcdef"```.

Pour vous souvenir de ce que fais cette fonction, sachez que *srtcat* est l'abréviation de **str**ings **c**onc**at**enation, ce qui signifie *concaténation de chaînes* en anglais.

#### Prototype ####

Le prototype de *strcat* est le suivant :

```c
char * strcat(char * dest, const char * src);
```

Ce prototype est assez instructif. Il nous apprend que notre fonction *strcat* va concaténer le contenu d'une chaîne source à la suite d'une chaîne de destination. Elle renvoie un pointeur sur cette dernière. La chaîne source n'est pas modifiée, mais la chaîne de destination l'est. 

#### Exemple ####

Illustration avec un exemple dans lequel je veux concaténer les phrases ```"bon"``` et ```"jour"``` :

```
char dest[50] = "bon";
const char * src = "jour";

printf("Avant : %s\n", dest);
strcat(dest, src);    /* on concatène */
printf("Apres : %s\n", dest);
```

Ce qui donne ceci à l'écran :

```console
Avant : bon
Après : bonjour
```

#### Attention ! ####

Tout comme *strcpy*, la fonction *strcat* ne contrôle pas la longueur des chaînes passées en paramètre. Soyez donc prudent pour ne pas écraser des données.

### strncat - Concaténer partiellement ###

Je ne sais pas si vous vous souvenez (mais vous devriez), mais *strcpy* avait une cousine du nom de *strncpy*, qui ne copiait qu'une partie de la chaîne à copier. Et bien *strcat* possède aussi une cousine du même genre. Il s'agit de la fonction *strncat*.

Cette fonction fait la même chose que la précédente, sauf qu'elle ne concatène qu'une partie de la chaîne de destination. Au lieu de placer toute la chaîne source à la suite de la chaine de destination (comportement de *strcat*), on peut demander à *strncat* de ne copier que $n$ caractères.

#### Prototype ####

Voici son prototype :

```c
char * strncat(char * dest, const char * src, size_t n);
```

Comme on le voit, son prototype est identique à celui de *strcat*, le seul nouvel argument étant le nombre de caractères à concaténer.

#### Exemple ####

```c
char dest[50] = "bon";
const char * src = "jour";
int n = 2;

printf("Avant : %s\n", dest);

strncat(dest, src, n);
printf("Resultat : %s", dest);
```
```console
Avant : bon
Resultat : bonjo
```

#### Attention bis ####

Tout comme *strcat*, la fonction *strncat* ne vérifie pas la taille des chaînes passées en paramètres. Évitez donc de déborder.

### Exercices
### Palindromes  ###

Un palindrome, vous savez ce que c'est ? Non, ce n'est pas une race de lutin. C'est simplement un texte qui se lit de la même façon qu'on le lise de droite à gauche. Par exemple, le mot RADAR est un palindrome. Mais cela fonctionne aussi pour les phrases. C'est le cas pour les phrases suivantes : "un art luxueux ultra nu", "Engage le jeu que je le gagne", etc. D'ordinaire, on ne tient pas compte des accents, trémas, cédilles ou des espaces. Mais pour cet exercice, on utilisera une définition plus stricte d'un palindrome : on tiendra compte des espace, trémas, etc.

#### Énoncé ####

Votre mission, si vous l'acceptez, sera de créer une fonction capable de vérifier si une chaîne de caractères est un palindrome. Celle-ci renverra 1 si la chaîne de caractère passée en entrée est bien un palindrome ou zéro si non.

#### Correction ####

Ne regardez [la correction](http://paste.awesom.eu/informaticienzero/26x&ln) qu'après avoir vraiment cherché.

### Changeons de registre, jouons au validateur ###

Connaissez-vous le [validateur de xHTML](http://validator.w3.org/">validateur de xHTML) ? Il s'agit d'un programme, présenté sous la forme de site web, qui vérifie que le code HTML d'une certaine page web est **valide**, autrement dit que c'est bel et bien du HTML. 

Les pages sont composées de **balises**, comme ```<strong>``` ou ```<h1>```, qui doivent *impérativement être refermées* (respectivement par ```</strong>``` et ```</h1>```). C'est la première règle du HTML et d'ailleurs la première vérifiée par le validateur : toutes les balises doivent être refermées. Nous allons tenter d'écrire un programme qui vérifie cette règle.

#### Votre mission ####

Cependant, le HTML est un langage trop compliqué pour notre niveau actuel. Nous allons donc considérer un langage simplifié : celui des parenthèses. Eh oui, les programmeurs et les mathématiciens connaissent bien cette règle qui veut que *toutes les parenthèses doivent être refermées*. Nous allons donc écrire un vérificateur de parenthèses. C'est certes moins exaltant que le validateur, mais le principe de base est rigoureusement le même, le reste étant des détails concernant la lecture des balises.

Écrivez un programme qui lit une ligne constituée de parenthèses, et vérifie que chaque parenthèse est bien refermée. Par exemple,

```console
Entrez une expression avec des parenthèses :
> )))(((
L'expression n'est pas bien parenthésée.
```

Pour corser le travail, vous pouvez également ajouter des crochets ```[]``` et des accolades ```{}```. Ce travail est réalisé par toutes sortes de compilateurs et validateurs.

#### Un indice ? ####

Encore et toujours, il faudra lire les caractères en boucle. Mais après ? Compter les parenthèses ouvrantes et les parenthèses fermantes ne suffit pas. Autrement, une expression telle que ```")))((("``` serait acceptée, alors qu'elle n'est pas bien parenthésée. En réalité, il suffit de compter le nombre de parenthèses encore à refermer. S'il vous en reste zéro à la fin, tout va bien. Sinon, ou si vous en avez un nombre négatif, problème !

#### Correction ! ####

Tada ! Et voici [la correction](http://paste.awesom.eu/informaticienzero/sdr&ln) ! 

Cette correction est un petit peu plus longue que les autres. N'hésitez pas à l'expérimenter chez vous, à essayer de l'améliorer. Si cet exercice vous a plus, sachez qu'il est inspiré d'un domaine appelé les langages formels. Nous avons écrit un automate reconnaissant le langage de Dyck. C'est plus impressionnant dit comme cela, mmh ?

### Recodons la bibliothèque standard ###

Pour s'entraîner, on va recoder quelques fonctions que l'on a vu dans ce chapitre. Pour que ce ne soit pas trop long, je vous propose d'en recoder quatre : *strlen*, *strcpy*, *strcat* et *strcmp*. Si vous le souhaitez, vous pouvez également coder leurs cousines respectives,voire coder les autres fonctions que nous avons vu dans ce chapitre.

L'exercice n'est pas compliqué, réfléchissez simplement à ce que fait la fonction de la bibliothèque standard et comment reproduire son comportement. Bonne chance à tous !

#### Correction ####

Alors cet exercice, ça été ? Oui, non ? L'essentiel est que vous ayez cherché, même si vous n'avez pas trouvé, ou seulement à moitié. N'hésitez pas à réessayer plus tard, avec d'autres fonctions, c'est comme ça que vous y arriverez. En attendant, voilà la correction :

* [de *my_strlen*](http://paste.awesom.eu/informaticienzero/Y4f&ln) ;
* [de *my_strcpy*](http://paste.awesom.eu/informaticienzero/tji&ln) ;
* [de *my_strcat*](http://paste.awesom.eu/informaticienzero/O5O&ln) ;
* et [de *my_strcmp*](http://paste.awesom.eu/informaticienzero/pXw&ln).

Malgré quelques désagréments, la bibliothèque ```<string.h>``` est quand même bien pratique. En plus, les fonctions qui la composent sont intéressantes à recoder. Si d'ailleurs vous voulez continuer à vous entrainer, il reste plein de fonctions à recoder. Vous pouvez même en inventer de nouvelles, c'est à vous de voir.

Dans le prochain chapitre, nous replongerons dans la mémoire et nous verrons un autre façon de déclarer ses variables : **l'allocation dynamique**.

## L'allocation dynamique
Dans les chapitres précédents, nous avons vu comment créer des structures, des tableaux et des chaînes de caractères. Mais il y a un petit problème : comment faire si on désire avoir un tableau (ou une chaîne de caractère) dont la taille n'est pas fixée une bonne fois pour toute ? C'est possible, mais on ne sait pas encore comment.

De plus, nos structures de données complexes, comme les tableaux, chaînes de caractères, et structures, n'ont pas besoin d'exister durant toute la vie d'un programme. Pas mal d'entre elles doivent avoir une vie éphémère : ces données complexes peuvent être crées et disparaitre suivant les besoins. 

On peut se demander pourquoi ce comportement. La raison est simple : nos données complexes prennent de la mémoire RAM, qui est en quantité limitée. Réserver de façon permanente de la mémoire pour chaque donnée dont on aurait besoin reviendrait à se tirer une balle dans le pied. Pour limiter la casse, il est possible de réserver une portion inutilisée de la mémoire pour stocker temporairement des données complexes. Quand un programme a besoin d'un peu plus de mémoire pour stocker une donnée complexe, il peut ainsi réserver une partie vide de la mémoire, et se l'approprier pour stocker une donnée. Quand on n'a plus besoin de cette mémoire, on la libère, et elle sera réutilisable à volonté. C'est ce qu'on appelle l'**allocation dynamique**. 

Comme vous vous en doutez, ce chapitre parlera de cette fameuse allocation dynamique. Vous verrez qu'il en existe plusieurs formes, et vous verrez aussi comment l'utiliser. Vous apprendrez notamment à utiliser certaines fonctions d'allocation dynamique disponibles en C.

### Durée de vie
Jusqu'à présent, nous vous avons simplement expliqué qu'il existe plusieurs type de mémoire (registre, mémoire cache, RAM et disque dur) et que vos variables sont stockées soit dans des registres, soit dans la RAM. 

Mais nos variables, tableaux et structures ne sont pas éternelles. Variables et données peuvent exister durant un certain temps et disparaitre ensuite. Elles occupent ainsi temporairement de la mémoire, qui peut être réutilisée lors de leur disparition. 

Cette portion de mémoire, utilisée pour stocker une variable, un tableau, ou une structure, c'est ce qu'on appelle un **objet**. Ce n'est rien de moins qu'un gros bloc de mémoire, placé en RAM, qui va servir à stocker notre donnée. La différence entre variable, tableau, structure, etc, et un objet est assez simple : c'est la différence entre le contenant et le contenu.

Cet objet a quelques particularités. Il stocke une certaine donnée : ```int```, ```char```, tableau, structure, etc. Mais il a aussi une **durée de vie**. La durée de vie d'un objet détermine la portion de l'exécution du programme durant laquelle son espace mémoire est réservé pour une donnée ou une variable. Dit plus simplement, elle détermine la période durant laquelle un objet existe, à savoir quand est-il réservé et quand est-il libéré. 

Durant cette durée de vie, notre objet est utilisé pour une variable ou une donnée en particulier. Une fois sa durée de vie terminée, la mémoire occupée par la variable / donnée est libérée et peut être utilisée pour autre chose, une autre variable, etc.

Il existe trois durées de vie pour les objets :

* automatique ;	
  * statique ;
* dynamique.

Voyons ces trois durées de vie dans l'ordre, en commençant par la durée de vie automatique.

### Automatique ###

La durée de vie automatique est celle qui correspond aux variables, structures, tableaux, etc ; déclarés dans un bloc d'instruction. Un objet de durée de vie automatique est crée lors de l'entrée dans le bloc d'instructions auquel il appartient et est détruit à la fin de l'exécution de celui-ci.

Il en va donc ainsi des variables locales aux fonctions de même que de leurs paramètres. Pour illustrer le principe, le code suivant est donc incorrect car **p* essaye d'accéder à un objet qui n'existe plus (la variable *n* a été détruite lors de la sortie de la fonction *ptr*).

```c
static int * ptr(void)
{
    int n = 10;

    return  &n;
}

int main(void)
{
    int * p = ptr();
    *p = 20;

    return 0;
}
```

La zone mémoire qui contient des objets automatiques est appelée **la pile **. Au passage, un objet à durée de vie automatique est initialisé à chaque fois qu'il est crée. Par exemple, si vous initialisez des variables locales dans une fonction, elles le sont à chaque appel ; ainsi, la pile se vide et se remplit au fur et à mesure du programme.

### Statique ###
Vient ensuite la durée de vie statique. Un objet de durée de vie statique est crée lors du lancement du programme et est détruit à la fin de celui-ci. C'est donc un objet qui existe de façon "permanente". Vous avez certainement du tilter en voyant le mot statique, et cela vous a surement rappelé quelque chose qu’on a vu dans les chapitres précédents. 

Et bien vous avez raison : les variables déclarées avec le mot-clé ```static``` à l'intérieur d'un bloc d'instruction a bel et bien une durée de vie statique. Mais ce ne sont pas les seules : les variables déclarées en dehors de tout bloc d'instruction ont elles aussi une durée de vie statique.

#### Initialisation automatique ####

Au fait : ces données statiques sont initialisées une seule fois lors de l'exécution du programme. Si le programmeur ne les initialise pas lui-même, ces dernières le seront automatiquement. Pour les entiers, cette initialisation les met à 0. Pour les flottants, ils sont initialisés à 0.0. Quand aux pointeurs, ceux-ci sont initialisés à NULL.

#### Exemple ####

Ainsi, ce code :

```c
#include <stdio.h>


static int plus(void)
{
    static int i;
    return i++;
}


int main(void)
{
    int i;

    for (i = plus(); i < 5; i = plus())
        printf("%d\n", i);

    return 0;
}
```

vous affichera :

```console
0
1
2
3
4
```

Étant donné que la variable *i* de la fonction *plus* est automatiquement initialisée à zéro et qu'elle n'est détruite qu'à la fin du programme (elle conserve donc sa valeur lors des appels successifs à la fonction *plus*).

### Dynamique ###

Un objet de durée de vie dynamique est crée et détruit à la demande du programmeur et est stocké dans **le tas**. L'intérêt de pouvoir gérer la durée de vie de différents objets est d'éviter les inconvénients propres aux objets de durée de vie automatique et statique. 

Du côté des objets de durée de vie automatique, le problème est qu'ils sont détruits à la fin du bloc auquel ils appartiennent. Il est donc impossible de les utiliser en dehors du bloc de code dans lesquels on les a crées. 

On peut citer l'exemple des variables locales d'une fonction. Pour ces dernières, ce n'est pas trop grave si on n'a qu'une seule donnée simple, vu qu'on peut le retourner : on peut retourner un ```int```, un ```char```, ou autre chose sans problème. Mais si on veut en retourner plusieurs, ou retourner une donnée plus complexe comme un tableau ou une structure, c'est impossible s'il sont déclarés avec une durée de vie automatique.

Le problème pourrait être contourné à l'aide d'objets de durée de vie statique, mais ce n'est pas très pratique car ces derniers sont persistants (ils ne sont détruits qu'à la fin du programme). De ce fait, si vous manipulez des données de tailles importantes, mais dont vous n'avez besoin que durant un certain temps, vous monopolisez de la mémoire pour rien. 

Et c'est sans compter les cas où la taille de la donnée n'est pas connue à la compilation et dépend de paramètres extérieurs : difficile de réserver de la mémoire si on ne sait pas de quelle quantité on a besoin.

La solution consiste donc à pouvoir créer et détruire des objets sur demande. Pour permettre au programmeur d'en créer, le langage de programmation doit fournir de quoi réserver de la mémoire. Cette réservation est plus ou moins bien cachée suivant le langage. Et en C, rien n'est masqué : vous pouvez vous même allouer (réserver) de la mémoire à la main et la libérer. Bien sûr, cela n'est pas sans conséquences : si vous oubliez de libérer la mémoire quand vous n'en avez plus besoin, vous allez rapidement la remplir, ce qui risque d'entrainer de sérieux problèmes.

Pour éviter de laisser la gestion de la mémoire au programmeur, certains langages sont capables de libérer eux-même la mémoire : ils incorporent ce qu'on appelle un garbage collector, un petit morceau de programme qui se charge de détecter les blocs de mémoire réutilisables et de les libérer à votre place. C'est le cas en Java par exemple, mais pas en C. Aussi, vous devez apprendre à gérer la mémoire à la main, en utilisant des fonctions fournies par le langage C.

*[garbage collector]: ramasse-miette

### Malloc et consoeurs
Le C fourni diverses fonctions qui permettent de réserver un bloc de mémoire afin de pouvoir l'utiliser comme bon nous semble. Ces fonctions d'allocation dynamique sont au nombre de quatre, et elles sont définies dans l'en-tête ```<stdlib.h>```. Pensez donc bien à l'inclure dans vos programmes en utilisant la déclaration de fichier d’en-tête suivante : 

```c
#include <stdlib.h>
```

Maintenant, il faut voir comment nous allons devoir utiliser ces fonctions d'allocation mémoire. 

### Schéma à suivre ###

Lorsque l'on souhaite faire une allocation dynamique, il y a un certain nombre d'étapes à suivre. Certaines peuvent sembler lourdes et inutiles, mais c'est à l'ardeur et la rigueur qu'il code que l'on reconnaît un bon programmeur. Ce schéma, que je vous invite fortement à suivre, est le suivant :

* **Déclarer un pointeur** : le pointeur va servir à contenir l'adresse de l'élément que l'on va allouer.
* **Appeler la fonction d'allocation** : cette fonction va s'occuper d'allouer un espace mémoire en fonction des paramètres qu'on lui passe.
* **Vérifier le retour de la fonction** : si la fonction a réussi à allouer un espace mémoire, elle retourne un pointeur sur cet espace. Cependant il se peut que dans certains cas (pas assez de mémoire, demande d'allocation trop importante, etc), la fonction échoue, et dans ce cas elle retourne NULL. Il faut donc tester notre pointeur : s'il vaut NULL, l'allocation a échoué, et on quitte le programme.
* Une fois que l'on ne souhaite plus utiliser l'espace mémoire, **on libère la zone allouée** : c'est important, sinon on retombe sur le risque vu précédemment à savoir une saturation du tas.

Examinons à présent ces quatre fonctions.

### malloc - Allouer de la mémoire ###

La première de ces fonctions est *malloc*. C'est la plus simple de toute. Cette fonction va simplement réserver un gros bloc de mémoire pour que l'utilisateur puisse l'utiliser comme il le souhaite. Petite remarque : le bloc de mémoire réservé par *malloc* n'est pas modifié ni initialisé. Celui peut donc contenir n’importe quoi.

#### Arguments ####

Évidemment, si on veut réserver de la mémoire, on doit préciser quelle est la taille du bloc de mémoire voulu. Pour cela, il suffit de préciser la taille du bloc en argument de *malloc*, et la fonction réservera celui-ci. L'argument de *malloc* sert donc à préciser sa taille. 

On pourrait se dire naïvement que cette taille est un nombre entier strictement positif et que le type de cet argument est un ```int``` ou un ```unsigned int```. Et bien pas du tout ! *malloc* a besoin que la taille qu'on lui envoie soit de type ```size_t```. Pourquoi ? Parce que `size_t` est le type utilisé par l'opérateur `sizeof` et est par conséquent le type naturel pour représenter la taille des objets

#### sizeof ####

Nous venons de le dire, *malloc* attend une certaine taille en argument. Autant prévenir tout de suite : **cette taille est exprimée en *bytes*.** Ainsi, si j'envoie 2000 en argument à *malloc*, celle-ci réservera 2000 *bytes* de mémoire. Seulement voilà, comment faire si je veux stocker 2000 ```int```, ou 2000 ```double``` ? En effet, si je ne connais pas la taille du type de données à allouer avec *malloc*, il me sera impossible de connaitre la taille en octets de la mémoire à réserver avec *malloc*. Et cette la taille varie suivant l'ordinateur, le compilateur, le système d’exploitation, et l'âge du capitaine. 

Heureusement, on a déjà vu qu'il existe un opérateur qui permet de récupérer la taille d'un type : c'est ```sizeof```. Grâce à cet opérateur, il est possible de connaître le nombre de *bytes* occupé par n'importe quel type (sauf ```void```). On peut ainsi allouer des zones mémoires de la bonne taille, grâce à cet opérateur. Ainsi, si on veut allouer $n$ éléments, il suffit de passer ```n * sizeof(Type d'un element)``` en argument de *malloc*. 

#### Retour de malloc ####

Cette fonction va retourner un pointeur qui stocke l'adresse du début du bloc réservé. Ce pointeur est un pointeur sur ```void```. Il faut dire que lorsque l'on réserve un bloc de mémoire, celui-ci peut être utilisé pour un tas de choses : des ```int```, des ```char```, des ```float```, ou un mélange de données hétérogènes. Bref, *malloc* pouvant être utilisé pour tout et n'importe quoi, elle doit fatalement retourner un pointeur qui peut pointer sur tout et n'importe quoi. En clair, un pointeur sur ```void```.

Avec ce qu'on a dit au-dessus, on peut donc déduire facilement le prototype de notre fonction malloc. Le voici :

```c
void * malloc(size_t size);
```

#### Exemple ####

Maintenant, exerçons-nous en suivant le schéma introduit ci-dessus. On doit créer un pointeur et appeler *malloc*. 

```c
int * ptr = malloc(sizeof(int));
```

Je déclare ici un pointeur sur un ```int```, qui va servir à stocker l'adresse de la zone mémoire réservée par *malloc*. La règle est simple : pour allouer dynamiquement un objet de type **T**, il faut créer un pointeur de type **T**.

Pour connaître la taille de l'objet que je veux allouer (ici un ```int```), j'utilise ```sizeof```. Grâce à cet opérateur, on peut allouer des objets de taille différente très facilement.

Maintenant, il faut pense à bien vérifier que l'adresse est valide. En effet, même s'il y a peu de chance que l'allocation échoue, le risque est toujours là, et pour s'en protéger il n'y a qu'une solution : vérifier que le pointeur est bien valide. Il suffit de tester si le pointeur est différent de NULL et d'agir en conséquence. Essayons avec notre code :

```c
int main(void)
{
    int * ptr = malloc(sizeof(int));

/* si malloc a retourné NULL... */
    if (ptr == NULL)
    {
    /* ...on affiche l'erreur grâce à perror */
        perror("Malloc");
    }

/* sinon c'est que l'allocation a réussi et on peut continuer */
    puts("Malloc a reussi !");
    return 0;
}
```

Ce code présente une nouveauté : si jamais l'allocation a échoué et que le pointeur vaille NULL, on appelle la fonction *perror*. Cette fonction décrit la dernière erreur rencontrée durant un appel système ou une fonction de bibliothèque. Ainsi, si *malloc* échoue, *perror* affichera la raison de l'échec. Si au contraire l'allocation s'est bien passée, le programme affichera : *« Malloc a reussi ! »*.

Mais que doit-on faire si *malloc* échoue hormis afficher l'erreur ? En général, on préfère quitter le programme. Pour cela, on utilise la fonction *exit*, également définie dans ```<stdlib.h>```, que voici :

```c
void exit(int status);
```

L'unique argument de cette fonction est *status*.  Il peut être une des deux valeurs suivantes (définies aussi dans ```<stdlib.h>```) :

* ```EXIT_SUCCESS``` : À utiliser pour quitter le programme avec succès.	
* ```EXIT_FAILURE``` : À utiliser pour quitter le programme en cas d'échec.

Sachez néanmoins que dans le cas général, *malloc* a très peu de chance d'échouer. Ceci dit, on est jamais trop prudent, donc continuez de vérifier le retour de *malloc* et agissez en conséquence.

Maintenant, on peut utiliser l'espace que l'on a alloué comme l'on veut. Mais une fois qu'on en a plus besoin, comment le libérer ?

### free - Libérer un espace alloué dynamiquement ###

Comme je l'ai déjà dit, si on réserve de la mémoire avec l'allocation dynamique, c'est de façon plus ou moins temporaire. Au bout d'un certain temps, la mémoire qu'on a réservée ne nous sert plus. On doit alors la libérer pour la rendre réutilisable. Pour libérer la mémoire allouée, on a besoin d'une fonction dédiée à ça : *free*. Cette fonction libère la mémoire déjà réservée par un *malloc*, un *calloc* ou un *realloc*.

Surtout, retenez bien une chose très importante : à chaque appel à *malloc* doit correspondre un appel à *free*. Autrement dit : **un malloc == un free**.

Voici son prototype :

```c
void free(void * ptr);
```

On remarque que la fonction *free* ne retourne rien, et c'est tout à fait normal (que voulez-vous retourner ?).

#### Argument ####

L'unique paramètre qu'elle prend est l'adresse de la zone mémoire à libérer. Ce paramètre est donc un pointeur. Et bien sur, vu qu'on ne sait pas ce pour quoi le bloc de mémoire utilisé a été utilisé, ce pointeur est un pointeur sur ```void```, qui ne précise pas le type des données stockées dans le bloc de mémoire à libérer.

Petite précision : si on passe un pointeur qui vaut NULL en argument de *free*, celle-ci ne fait rien. En revanche, quand on vous passez à *free* un pointeur sur un bloc de mémoire qui a déjà libéré, le comportement est indéterminé. Généralement, libérer plusieurs fois de la mémoire correspond à une erreur de programmation, mais il faut savoir que cela arrive parfois, et que savoir gérer ce genre de cas correctement est impératif. Pour éviter ce genre de problème, il y a une solution simple : une fois que vous avez effectué un *free* sur un pointeur, mettez-celui-ci à NULL. Comme ça, si jamais vous avez mal programmé et que vous libérez plusieurs fois un même pointeur, vous n'aurez pas de problèmes, vu que le pointeur à libérer sera un pointeur NULL : *free* ne fera rien.

### calloc - Allocation et mise à zéro ###

La fonction *malloc* n'est pas la seule fonction qui permet d'allouer de la mémoire. Elle a des petites sœurs : *calloc* et *realloc*. Voyons un peu la fonction *calloc*. Cette fonction va simplement réserver un gros bloc de mémoire pour que l'utilisateur puisse l'utiliser comme il le souhaite. Son rôle est donc similaire à celui de *malloc*, à un détail près : *malloc* ne faisait rien sur le bloc de mémoire réservé et ne initialisait pas ; *calloc* fait exactement le contraire : elle va initialiser le bloc de mémoire réservé avec des zéros.

Cependant, il est déconseillé de l'utiliser pour initialiser des données contentant des flottants ou des pointeurs, car selon les architectures, il se peut que mettre la zone mémoire à 0 ne mette pas des flottants ou des pointeurs à 0. Ceci est assez compliqué à expliquer sans rentrer dans les détails, mais nous devions néanmoins vous avertir.

Voici le prototype de *calloc* :

```c
void * calloc(size_t n, size_t size);
```

#### Arguments ####

La fonction *calloc* attend deux paramètres. Le premier paramètre, noté *n*, n'est rien d'autre que le nombre d'éléments à allouer. Le second paramètre, noté *size* dans le prototype du dessus, indique la taille d'un élément. Ces deux paramètres sont de type ```size_t```.

#### Retour ####

Comme pour *malloc*, *calloc* va renvoyer un pointeur qui contient l'adresse du début du bloc réservé. Il va de soit que ce pointeur est un pointeur sur ```void```, exactement pour les mêmes raisons que *malloc*.

### realloc - Réallouer à volonté ###

Passons maintenant à la cadette de la fratrie des fonctions d'allocation. Il s'agit de la plantureuse *realloc*. Celle-ci sert à agrandir ou rétrécir un bloc de mémoire qui a été préalablement réservé par *malloc* ou *calloc*.

Voici son prototype :

```c
void * realloc(void * ptr, size_t size);
```

#### Arguments ####

Cette fonction prend donc deux arguments. Le premier est un pointeur qui pointe vers la zone de mémoire dont on veut changer la taille. Il est important de noter que le pointeur passé en argument doit obligatoirement avoir été alloué avec *malloc*, *calloc* ou *realloc*, sinon le comportement est indéterminé. Autre détail : si *realloc* reçoit un pointeur nul en argument, elle se comporte comme *malloc*.

Le deuxième paramètre n'est rien d'autre que la nouvelle taille qu'on veut attribuer à ce bloc de mémoire. Petit détail : si *realloc* reçoit une taille nulle en argument, elle se comporte comme *free*.

#### Retour ####

Cette fonction retourne un pointeur qui pointe sur le bloc de mémoire. Il faut dire que le pointeur renvoyé par *realloc* n'est pas forcément le même que celui passé en paramètre : rien n’empêche *realloc* d'allouer un nouveau bloc de mémoire, déplacer les données de l'ancien vers le nouveau et libérer l'ancien. Il faut donc que *realloc* renvoie un pointeur vers ce nouveau bloc. Ce pointeur est un pointeur sur ```void```, pour les mêmes raisons que *malloc* et *calloc*.

Bien entendu, comme avec les deux autres fonctions, il faut vérifier que la fonction a réussie. Mais il y a également autre chose à prendre en compte, que nous allons illustrer avec un exemple.

```c
int * ptr = malloc(10 * sizeof(int));

ptr = realloc(ptr, 30 * sizeof(int));
```

Dans notre code d'exemple, on ré-alloue directement la zone mémoire, ce qui a première vue est logique et normal. Mais si jamais la ré-allocation venait à échouer on se retrouverait avec un pointeur invalide (car *realloc* retournera NULL), mais aussi avec une zone mémoire qu'on ne pourra pas libérer, car on a perdu son adresse : c'est une [fuite mémoire](http://fr.wikipedia.org/wiki/Fuite_de_mémoire). Le seul moyen d'éviter cet accident est de passer par un pointeur intermédiaire :

```c
int * ptr = malloc(10 * sizeof(int));
int * temp;

/* On veut agrandir la zone mémoire en passant de 10 int à 30 int. */
temp = realloc(ptr, 30 * sizeof(int));
if (temp != NULL)
{
/* Si l'allocation a marché, alors on peut faire pointer ptr sur la nouvelle zone mémoire ... */
    ptr = temp;
}
else
{
/* ... sinon on libère ptr, on le met à NULL, et on écrit l'erreur. */
    free(ptr);
    ptr = NULL;
    perror("Realloc");
}

/* On oublie pas de libérer à la fin. */
free(ptr);
ptr = NULL;
```

#### Précisions ####

On a dit plus haut qu'on pouvait agrandir ou rétrécir un espace avec *realloc*. Il faut savoir que dans les deux cas, les valeurs présentes dans le bloc de mémoire avant la ré-allocation seront conservées. Dans le cas d'un agrandissement, elles le sont intégralement. Et dans le cas d'un rétrécissement, on ne conserve que les valeurs des cases restantes.

Ces fonctions d'allocation dynamique sont quand même bien pratique pour réserver de la mémoire quand on veut et dans la quantité qu'on veut, ce qui est bien pratique dans les cas où on ne sait pas d'avance combien réserver, comme par exemple quand c'est l'utilisateur qui rentre les données. Elles ne sont pas compliquées à utiliser, il faut simplement faire attention au retour de la fonction et ne pas oublier de tout libérer à la fin.

Voilà, c'est la fin de la partie 2, qui a été bien dense et pleine de nouveaux concepts bien puissants. Si jamais certaines parties vous posent des soucis, relisez-les autant qu'il faut, puisque les informations contenues dans cette partie sont vitales pour bien programmer en C et comprendre la suite de ce tutoriel. D'ailleurs, nous allons voir dans les parties suivantes que ces concepts combinés ensembles peuvent être très pratiques.

# Les entrées-sorties
Pour l'instant, nous ne connaissons rien aux entrées-sorties hormis les quelques fonctions vues dans les parties précédentes. Et pourtant la bibliothèque standard contient foule de fonctions capables de pleins de choses, dont ouvrir des fichiers, écrire dedans, signaler des erreurs, etc. Cette partie sera donc l'occasion non seulement des les découvrir, mais également d'apprendre à sécuriser les flux d'entrées et de sorties pour éviter les bêtises. L'un des principes du C est en effet de ne jamais croire l'utilisateur, celui-ci pouvant potentiellement faire n'importe quoi.

## Les flux
Avez-vous remarqué que tout ce que nous avons fait jusqu'à maintenant n'était que temporaire et disparaissait dès qu'on quittait le programme ou qu'on éteignait l'ordinateur ? Il était impossible de stocker des informations de manières permanentes. Il est grand temps de réparer cette injustice et c'est le but de ce chapitre : vous apprendre à manipuler les fichiers en C. Il sera désormais possible de stocker des scores à un jeu vidéo ou les numéros de téléphone d'un carnet d'adresse par exemple.

### Un peu de théorie
### Préambule ###

En informatique, un fichier est une collection, un ensemble d'informations numériques stockées sur un support de mémoire, comme un disque dur par exemple. Cette collection d'informations est réunie sous un même nom, et manipulées comme une unité.

Afin de faciliter la localisation des fichiers, ces derniers sont classés dans des **systèmes de fichier**. Un système de fichiers est une façon de stocker les informations et de les organiser dans des fichiers. Une telle gestion des fichiers permet de traiter, de conserver des quantités importantes de données ainsi que de les partager entre plusieurs programmes informatiques. Un système de fichiers permet à l'utilisateur de **localiser des données à partir d'un chemin d'accès**.

Le nom du fichier sert à décrire le contenu. Ce nom est souvent construit de la manière suivante : **suffixe**.*extension*. Une extension renseigne sur la nature des informations et le logiciel utilisé pour les manipuler. L'extension d'un fichier est facultative. Par exemple, sous les systèmes de type UNIX ou GNU/Linux, il n'est pas rare de trouver des noms de fichiers sans extension. Chaque fichier comporte un certain nombre de métadonnées, c'est à dire des informations concernant des informations sur le fichier en question telles que :

* sa longueur ;	
* son auteur ;
  * ses droits d'accès (les personnes autorisées à le manipuler) ;
* sa date de la dernière modification ;

Le plus important dans un fichier est les informations qu'il contient. Le **format d'un fichier** est la convention selon laquelle les informations ainsi que les métadonnées sont écrites dans le fichier. Selon la nature et le format du contenu, les fichiers peuvent être qualifiés d'exécutables, de textes, de documents, d'images, d'audio, de vidéos etc.

Voici quelques formats courants :

* **Textes et documents** : `.txt` ; `.asc` ; `.doc` ; `.htm` ; `.html` ; `.msg` ; `.xls` ; `.odt`	
  * **Images** : `.gif` ; `.jpg` ; `.bmp` ; `.png` ; `.eps` ; `.tif`
* **Audio** : `.mp3` ; `.wav` ; `.au` ; `.ra` ; `.ram`
* **Vidéo** : `.avi` ; `.mpg` ; `.mov`
  * **Exécutables** : `.exe` ; `.com` ; `.bat`
* **Compressés** : `.arc` ; `.zip` ; `.z` ; `.arj` ; `.tar` ; `.sit` ; `.gz` ; `.bz2` ; `.rar` ; `.xz`

Seulement, certains formats de fichiers peuvent être propriétaire et donc difficilement exploitables. Un format propriétaire est un format de fichier dont les spécifications sont contrôlées par une entité privée. Un tel format n'est pas libre d'utilisation.

Dernier point : le chemin d'accès d'un fichier. Nous en avons déjà parlé brièvement plus haut, attardons-nous maintenant sur les petites particularité de ce dernier. Le chemin d'accès d'un fichier (ou d'un répertoire) est une chaîne de caractères décrivant la position de celui-ci dans le système de fichiers. Nous n'avons pas encore parler de la racine des répertoires. Sans entrer dans les détails, le répertoire racine est la base des répertoires de tout fichiers. Ensuite, c'est le séparateur de répertoire qui entre en jeu; c'est lui qui permet de localiser un fichier situé dans plusieurs sous-dossiers. Petit résumé :

| OS        | Répertoire racine | Séparateur de répertoire |
| --------- | ----------------- | ------------------------ |
| UNIX-like | `/`               | `/`                      |
| Windows   | `lecteur:\`       | `\`                      |

Il est possible d'utiliser sous Windows le même séparateur de répertoire que les systèmes dérivés d'UNIX, à savoir : '/'. Cette pratique a pour effet de facilement rendre portable vos programmes. En effet, si l'on prévoit les grands deux séparateur de répertoire, la création d'une fonction à part et/ou l'utilisation du préprocesseur devient indispensable. Or là, tout est plus simple. Il existe deux moyens pour indiquer le chemin d'un fichier :

* Le chemin absolu, vous le connaissez bien, indique que le fichier va être cherchée en partant de la racine du système de fichiers. Par exemple :
```console
C:/Users/paraze/prog/fichiers/test.txt
/home/paraze/prog/tuto/main.c
/home/paraze/prog/tuto/fichier.txt
/home/paraze/prog/tuto/ressources/scores.scr
```
* Le chemin relatif qu'en à lui, est identique au précédant à l’exception près qu'au lieu de partir de la racine, on commence au répertoire courant. En pratique, le répertoire courant est généralement celui où ce trouve l’exécutable.
```console
fichier.txt
maximal_crazy.mp3
ressources/scores.scr
```

Chacun possède ses défauts et qualités. Le chemin absolu est le plus sûr et le moins flexible. Le chemin relatif est bref, flexible, mais n'est pas sans danger.

### En langage C ###

La bibliothèque standard du C fournie plusieurs fonctions qui permettent de réaliser des entrées/sorties de manière portable. Ici, c'est ```<stdio.h>``` qui travaille puisque, je vous le rappelle, ce fichiers d'en-tête signifie *standard input-output*, soit *entrée-sortie standard*. 

Les entrées/sorties en langage C se font par des **flux** (*stream* en anglais), qui représentent des objets externes au programme, appelés fichiers. Selon la manière dont on veut réaliser les opérations d'entrées/sorties sur le fichier, on distingue deux grandes catégories de flux : les **flux de textes** et les **flux binaires**.

En C, un flux est représenté par un pointeur sur une une structure de type ```FILE```. Cette structure contient des informations concernant un fichier. Voici les trois flux pré-définis par ```<stdio.h>``` :

* **stderr** : Flux d'erreurs standard, par défaut, l'écran.
* **stdout** : Flux de sortie standard, par défaut, l'écran.
* **stdin** : Flux d'entrée standard, par défaut, le clavier.

### Ouverture et fermeture de flux
### fopen - Ouverture d'un flux ###

L'ouverture d'un flux est nécessaire à la manipulation de ce dernier, et pour ce faire, la fonction [fopen](http://www.linux-kheops.com/doc/man/manfr/man-html-0.9/man3/fopen.3.html) est tout indiquée.

#### Explication ####

Voici son prototype :

```c
FILE * fopen(const char * path, const char * mode);
```

La chaîne de caractères constante *path* signifie *chemin* en français. Il faut donc passer en premier paramètre une chaîne de caractère contenant le chemin (absolu ou relatif, comme vous voulez). Petit rappel : certaines fonction du C comme *printf* considère le caractère ```'\'``` comme un caractère spécial (ce caractère est en fait utilisé pour la manipulation de caractères d'échappements, comme ```'\n'``` ou ```'\t'```). Donc, pour ouvrir un fichier situé dans un sous-dossier, vous devrez doubler de l'antislash (```"\\"```) afin de bien faire comprendre au compilateur qu'on souhaite utiliser ce symbole.

La seconde variable, nommée *mode*, indique le mode d'ouverture du fichier : veut-on simplement lire un fichier ou bien l'éditer ? Veut-on supprimer tout son contenu avant ? Voici différents modes d'ouvertures disponibles :

* ```"r"``` : **lecture** à partir du début du fichier. Le fichier indiqué par le premier argument doit obligatoirement exister, sinon la fonction échoue.
* ```"w"``` : **écriture** à partir du début du fichier. Si le fichier n'existe pas, il sera créé. Si il existe, son contenu est effacé.
* ```"a"``` : **écriture** à partir de la fin du fichier. Si le fichier n'existe pas, il sera créé.
* ```"r+"``` : **lecture et écriture** à partir du début du fichier. Le fichier indiqué par le premier argument doit obligatoirement exister, sinon la fonction échoue.
* ```"w+"``` : **lecture et écriture** à partir du début du fichier. Si le fichier n'existe pas, il sera créé. Si il existe, son contenu est effacé.
* ```"a+"``` : **lecture et écriture** à partir de la fin du fichier. Si le fichier n'existe pas, il sera créé.

Ces six modes sont très important, et à savoir par cœur ; ils permettent d'ouvrir de simples flux de textes. Sachez qu'il en existe encore six autres. En effet, nous avons déjà brièvement parlé des flux binaires, ceux-ci sont manipulables grâce à des modes dit *non formaté*. Nous aurons l’occasion d'en reparler plus loin dans le chapitre.

La fonction retourne un pointeur sur le flux demandé si l'ouverture a réussi ou bien NULL si elle a échoué. Comme pour les fonctions d'allocation dynamique, il faudra penser à vérifier le retour de *fopen* et agir en conséquence.

#### Application ####

Je vous mets [au défi](http://paste.awesom.eu/informaticienzero/dLm&ln) d'ouvrir un fichier quelconque localisé dans le répertoire courant en lecture simple ! Ces codes, d'apparences corrects, sont pourtant de véritables bombes à retardements. En effet, il suffit que l'ouverture échoue (ce qui arrive souvent, si le fichier n'est pas présent ou si vous avez fait une faute de frappe) pour que votre programme crash. Nous parlions tout à l'heure de la très utile valeur de retour de la fonction *fopen*. Comme un code vaut 42 mots, voici un exemple possible montrant la vérification du retour de cette fonction :

```c
#include <stdio.h>

int main(void)
{
    FILE * fichier = fopen("fichier.txt", "r");
    if(fichier == NULL)
    {
        perror("fopen");
        /* ... */
    }

    /* Opérations sur le fichier ... */

    return 0;
}
```

Faut-il là aussi quitter le programme si *fopen* échoue ? C'est à vous de décider, mais en général l'échec de *fopen* est dû au fait que soit le fichier n'existe pas, soit le chemin est incorrect, donc mieux vaut retenter en proposant à l'utilisateur de modifier le chemin ou de créer le fichier. Fermer le programme est une façon un peu trop brutale de dire à l'utilisateur qu'il a fait n'importe quoi.

### fclose - Fermer un fichier ###

Vous savez ouvrir un flux de texte et même vérifier son ouverture, mais le plus important, et le plus simple en passant, reste à voir. Vous vous souvenez du chapitre sur l'allocation dynamique, avec *malloc*, *free* et tout ce qui va avec ? Si vous êtes observateur, vous avez sûrement remarqué que l'on répète le même schéma :

* **Déclarer un pointeur sur ```FILE```** : déclarer un pointeur ;	
  * **Appeler la fonction *fopen*** : appeler la fonction d'allocation 
* **Vérifier le retour de la fonction** : idem.

Que manque t-il ? La libération de la zone de mémoire. Cette fonction la voici : 

```c
int fclose (FILE * stream);
```

La fonction *fclose* libère le flux nommé *stream*. Il est impossible d'y accéder par la suite, sous peine d'un comportement indéterminé. Elle renvoie 0 en cas de réussite, et EOF si la fonction ne réussit pas à fermer correctement le fichier. La constante EOF signifie **E**nd **O**f **F**ile et est la plupart du temps retournée lorsque lit un fichier et que l'on arrive à la fin de celui-ci. Cependant, il arrive aussi qu'elle représente une erreur de traitement (comme dans le cas ici présent). Il est rare de voir cette fonction planter sans raison apparente, évitez juste de lui passer en paramètre un pointeur sur ```FILE``` déjà libéré ou non-alloué.

Je vous donne le code final commenté :

```c
#include <stdio.h>

int main(void)
{
    FILE * fichier = fopen("fichier.txt", "r");
    if(fichier == NULL)
    {
        perror("fopen");
        /* ... */
    }
    
    /* Opérations sur le fichier ... */
    
    fclose(fichier);
    fichier = NULL;
    return 0;
}
```

### Ouvrir plusieurs fichiers à la fois ###

Certains se sont peut-être déjà demandés s'il est possible d'ouvrir plusieurs flux en même temps. La réponse est oui. Le code suivant vous montre un exemple où l'on ouvre 5 fichiers à la fois à l'aide d'un tableau de ```FILE*```. Inutile de préciser que les règles sont les mêmes que précédemment. 

```c
#include <stdio.h>

#define TAILLE_MAX 20
#define NB_FICHIER 5

int main(void)
{
    FILE * fichier[NB_FICHIER];
    char s[TAILLE_MAX];
    size_t i;

    for(i = 0; i < NB_FICHIER; ++i)
    {
        sprintf(s, "fichier%d.txt", i + 1);

        fichier[i] = fopen(s, "r");
        if(fichier[i] == NULL)
        {
            printf("Erreur lors de l'ouverture du fichier %d\n", i + 1);
            perror("fopen");
            /* ... */
        }
    }

    /* ... */

    for(i = 0; i < NB_FICHIER; ++i)
    {
        fclose(fichier[i]);
    }

    return 0;
}
```

Y'a t-il une limite au nombre de flux ouvrables en même temps ? Il y a effectivement une limite, mais celle-ci peut être variable. Pour nous aider, nous avons deux constantes de préprocesseur définies dans ```<stdio.h>``` que voici :

* ```FOPEN_MAX``` : elle indique le nombre maximum ouvrables en même temps par un programme. La norme garantit qu'elle vaut au minimum 8 (en comptant les trois flux standards) :
> The value of the macro FOPEN_MAX shall be at least eight, including the three standard text streams
>  -- C89 - 4.9.3 Files 
* ```FILENAME_MAX``` : elle indique la taille maximum du nom d'un fichier pour qu'on soit sûr qu'il soit ouvert. Sous certaines implémentations, une taille supérieure marchera, mais dans le doute, essayez de limiter la taille du nom de vos fichiers.

Ces deux constantes vous serons utiles pour faire un code portable et sans risque de comportement indéterminé quand vous serez amenés à manipuler de nombreux fichiers.

### Lecture d'un flux
### fgetc - Lecture d'un caractère ###

Commençons doucement avec la fonction [fgetc](http://pwet.fr/man/linux/fonctions_bibliotheques/gets) qui lit un caractère depuis un flux. Voici son prototype :

```c
int fgetc(FILE * stream);
```

Avant de continuer, il faut savoir que lire un fichier réclame quelque chose d'important : un **indicateur de position**. Il faut savoir que lorsque l'on parcourt un flux, un indicateur de position est utilisé pour indiquer où on en est dans le flux. Imaginez-vous un curseur virtuel que l'on avance d'une case à chaque caractère lu par *fgetc*, et vous aurez compris le principe. 

*fgetc* renvoie donc le caractère lu si tout s'est bien passé ou la macro EOF si l'indicateur de position est tout à la fin du fichier (ou en cas d'erreur).

Afin d'effectuer des opération sur un fichier, il faut toujours réfléchir sur le meilleur mode d'ouverture à choisir. Nous souhaitons lire un fichier, ce qui nous laisse que 4 possibilités :

* ```"w+"``` : supprime le contenu du fichier précédemment ouvert ;
  * ```"a+"``` : place l'indicateur de position est  à la fin de celui-ci ;
* ```"r+"``` : ouvre le fichier en lecture et en écriture, l'indicateur de position est placé au début ;
* ```"r"``` : ouvre le fichier en lecture, l'indicateur de position est placé au début ;

Deux modes d'ouvertures sembles correspondre : le simple ```"r"``` et ```"r+"```. Les deux sont corrects pour notre utilisation, je recommande cependant l'utilisation du premier, qui nous assure que le fichier ne sera pas modifié ; c'est une mesure de protection. 

Voici donc un code lisant la première lettre d'un fichier nommé `salutation.txt` contenant la phrase *Salut* :

```c
#include <stdio.h>

int main(void)
{
    FILE * fichier;
    int c;

    fichier = fopen("salutation.txt", "r");
    if(fichier == NULL)
    {
        perror("fopen");
        /* ... */
    }

    c = fgetc(fichier);
    putchar(c);

    fclose(fichier);
    fichier = NULL;
    return 0;
}
```

Voilà ce que cela donne :

```console
S
```

Cette fonction peut lire un caractère de n'importe quel flux, nous pouvons donc faire ceci pour récupérer un caractère depuis le flux d'entrée standard :

```c
c = fgetc(stdin);
```

L'appel de la fonction [getchar](http://pwet.fr/man/linux/fonctions_bibliotheques/gets) est strictement identique à l'utilisation de *fgetc* sur ```stdin```.

Néanmoins, la grande limite de *fgetc* est le fait qu'elle ne lis qu'un seul caractère. Afin de lire tout le contenu d'un fichier, l'utilisation d'une boucle est tout indiqué. Rappelez-vous, EOF est retourné en cas de fin de fichier.

```
int main(void)
{
    FILE * fichier;
    int c;

    fichier = fopen("fichier.txt", "r");
    if(fichier == NULL)
    {
        perror("fopen");
        /* ... */
    }

    /* Tant que le caractère actuel n'est pas la fin du fichier */
    while((c = fgetc(fichier)) != EOF)
    {
        putchar(c);
    }

    fclose(fichier);
    fichier = NULL;
    return 0;
}
```
```console
Salut ! 
Je m'appelle paraze.
```

### fgets - Lecture d'une chaîne de caractères ###

Voici le prototype de la fonction [fgets](http://pwet.fr/man/linux/fonctions_bibliotheques/gets) :

```c
char * fgets(char * s, int size, FILE * stream);
```

Cette fonction est un peu plus compliquée que la précédente. Elle lit une ligne de caractère depuis le flux *stream*. Plus précisément, elle lit le flux caractère par caractère (en comptant le ```'\0'```) puis s'arrête lorsqu'elle a déplacé l'indicateur de plus de ```size - 1``` (le nombre voulu de caractères). La fonction *fgets* possède encore deux autres conditions d'arrêt : lorsqu'elle rencontre un retour à la ligne ou lorsqu'elle lit EOF. Le pointeur *s* contient la chaîne lue par *fgets*.

La fonction retourne ... le pointeur *s*. À l'instar de la fonction *fgetc*, le retour de cette fonction permet de savoir s'il y a eu un problème de lecture ou si l'on est à la fin du fichier. Ces deux cas conduiraient simplement au retour de la valeur NULL. Voici un code possible utilisant *fgets* :

```c
#include <stdio.h>

#define TAILLE_MAX 100

int main(void)
{
    FILE * fichier;
    char chaine[TAILLE_MAX];

    fichier = fopen("fichier.txt", "r");
    if(fichier == NULL)
    {
        perror("fopen");
        /* ... */
    }

    fgets(chaine, TAILLE_MAX, fichier);
    puts(chaine);

    fclose(fichier);
    fichier = NULL;
    return 0;
}
```
```console
Salut !
```

Remarquez l'utilisation de la constante TAILLE_MAX. L'utilisation d'une telle macro est très courante lorsque l'on manipule des flux, car elle permet de créer une chaîne de caractère aussi grande que le nombre de caractère maximum que l'on va lire sur une ligne. Comme la première ligne de mon fichier fait moins que 100 caractères, elle est entièrement lue. Essayez de faire varier cette constante (c'est là que l'on voit bien son utilité : on évite de modifier à deux reprises cette valeur) et vous verrez, la chaîne lue est tronquée ; de plus, aucun débordement de mémoire n'est fait. C'est une sorte de sécurité.

Vous avez toutes les clés en main, lire entièrement le fichier ne devrait pas être trop difficile :

```c
#include <stdio.h>

#define TAILLE_MAX 100

int main(void)
{
    FILE * fichier;
    char chaine[TAILLE_MAX];

    fichier = fopen("fichier.txt", "r");
    if(fichier == NULL)
    {
        perror("fopen");
        /* ... */
    }

    /* Tant que la fin du fichier n'est pas rencontrée */
    while((fgets(chaine, TAILLE_MAX, fichier)) != NULL)
    {
        puts(chaine);
    }

    fclose(fichier);
    fichier = NULL;
    return 0;
}
```

Puisque *fgets* déplace l'indicateur de conversion d'une ligne lors d'un appel, la future lecture (voyez par là le futur appel) débutera à partir du début de la ligne suivante.

Dernier point concernant cette fonction : le caractère ```'\n'``` est inclut dans la chaîne précédemment lue. C'est pour cela que notre code ci-dessus affichait correctement le fichier, avec des retours à la ligne. Cela peut vite devenir un problème, si l'on essaie de comparer la chaîne lue avec une autre chaîne de caractères quelconque par exemple. Le ```'\n'``` sera pris en compte lors de la comparaison et risque d'altérer le comportement de notre fonction d'analyse. Comment palier à ce problème ? Il faut chercher le caractère ```'\n'``` et le remplacer par ```'\0'```. Pourquoi ne pas créer une fonction tant qu'à faire ? Cela fera un très bon exercice.

### La grande famille de scanf ###

Concluons cette sous partie sur l'une des sœurs de *scanf* : [fscanf](http://pwet.fr/man/linux/fonctions_bibliotheques/scanf). Cette dernière aura le même fonctionnement que *scanf*, à l’exception près que l'on doit lui indiquer le flux à lire. La fonction de base lis le flux *stdin* ; dans notre cas, avec *fscanf*, ce sera le fichier à analyser. Voici son prototype :

```c
int fscanf(FILE * stream, const char * format, ...);
```

Voici un exemple concret d'utilisation, en supposant que j'ai sous la main un fichier nommé *scores.txt* contenant :

```console
paraze 100
Pouet_forever 96
SofEvans 95
informaticienzero 42
tib92 37
```

Afin de récupérer le noms des joueurs ainsi que leurs points, voici comment je procéderai :

```
#include <stdio.h>

int main(void)
{
    FILE * fichier;
    char nom[5][50];
    int score[5];
    int i;

    fichier = fopen("scores.txt", "r");
    if(fichier == NULL)
    {
        perror("fopen");
       /* ... */
    }

    for(i = 0; i < 5; i++)
    {
        fscanf(fichier, "%s %d", nom[i], &score[i]);
        printf("%s : %d\n", nom[i], score[i]);
    }

    fclose(fichier);
    fichier = NULL;
    return 0;
}
```

La fonction *fscanf* lit le symbole ```"%s"```, puis cherche la première chaîne de caractère présente à partir de l'indicateur de position, soit ```"paraze"```. Ce curseur justement, est déplacé de 6 caractères (la longueur de la chaîne). Ensuite, elle cherche un nombre (présence de l'indicateur de conversion ```"%d"```), la valeur 100 est sélectionnée. L'appel de cette fonction est terminée, et nous avons finalement récupéré et stocké une chaîne de caractère et un nombre entier. Elle procède ainsi pour chaque ligne.

Coupler les structures avec *fscanf* est une idée très judicieuse. En effet, imaginez un fichier construit avec la structure suivante :

```console
<pseudo> <commentaire> <nb_partie> <score>
```

Se balader avec 4 tableaux serait un peu lourd, alors pourquoi ne pas utiliser la puissance des structures ?

```c
#define TAILLE_MAX 100

typedef struct
{
    char pseudo[TAILLE_MAX];
    char com[TAILLE_MAX];
    unsigned nb_parties;
    unsigned score;
} Info;
```

Serez-vous capable de remplir les champs de cette structure à partir d'un fichier ?

### Écriture dans un flux
Vous vous en doutiez sûrement, après la découverte de trois fonctions permettant de lire un flux, nous allons travailler sur des fonctions d'écriture. Vous pourrez facilement observer la similitude entre ces fonctions et celles vues à l'instant.

### fputc - Écriture d'un caractère ###

La fonction [fputc](http://www.linux-france.org/article/man-fr/man3/putc-3.html) écrit un et seulement un seul caractère dans fichier :

```c
int fputc (int c, FILE * stream);
```

Vous l'aurez bien compris, cette fonction écrit le caractère *c* de type ```int``` dans le flux *stream*. Elle renvoie la plupart du temps le caractère qui vient d'être écrit ; en cas d'erreur, EOF est retourné.

Nous avions déjà débattu sur le mode d'ouverture à choisir, et je vous propose de recommencer. Afin d'écrire dans un fichier vierge, je vous recommande le mode ```"w"``` et ```"w+"```, ces deux-là créent le fichier s'il n'existe pas, efface son contenu et bien sûr permettent l'écriture dans ce dernier. Les modes ```"a"``` et ```"a+"``` sont tout aussi intéressant : si le fichier est inexistant, il sera créé ; de plus, son contenu n'est pas effacé et l'indicateur de position est placé à la fin du fichier (et donc au début dans le cas d'un fichier vide). Le dernier mode d'ouverture acceptant l'écriture d'un flux est ```"r+"```, le curseur virtuel est je vous le rappelle placé au début du fichier, rien est effacé mais le fichier doit obligatoirement être présent, sous peine d’échec de la fonction. Dans cet exemple, le mode choisi sera ```"w"``` puisque l'on a pas besoin de lire le fichier, ni d'ajouter du texte à un endroit précis.

Le code suivant écrit le texte ```"Salut"``` dans un fichier nommé *test.txt* :

```c
#include <stdio.h>

int main(void)
{
    FILE * fichier;

    fichier = fopen("test.txt", "w");
    if(fichier == NULL)
    {
        perror("fopen");
        /* ... */
    }

    /* Écriture de "Salut" */
    fputc('S', fichier);
    fputc('a', fichier);
    fputc('l', fichier);
    fputc('u', fichier);
    fputc('t', fichier);

    fclose(fichier);
    fichier = NULL;
    return 0;
}
```

Vous exécutez le programme, et rien ne se passe ... en apparence. Effectivement, si vous ouvrez le fichier *test.txt* avec un éditeur de texte, vous verrez que la chaîne ```"Salut"``` s'est bel et bien créée. 

Comme vous pouvez le constater, la fonction *fputc* n'est pas très pratique pour écrire de longue chaîne de caractères. On pourrait imaginer l'utilisation d'une boucle comme ceci pour pallier à ce problème :

```c
const char * s = "Salut";
const size_t taille = strlen(s);
size_t i;

/* Je passe l'ouverture du fichier et la vérification */

for(i = 0; i < taille; ++i)
{
    fputc(s[i], fichier);
}
```

C'est déjà mieux, bien que peu pratique. L'idéal serait d'avoir une fonction qui puisse écrire une chaîne de caractères entière d'un coup. Heureusement cette fonction existe.

### fputs - Ecriture d'une chaîne de caractères ###

Voici le prototype de [fputs](http://www.linux-france.org/article/man-fr/man3/puts-3.html), semblable à *puts*, sa sœur que nous avions rencontré au début de ce tutoriel :

```c
int fputs (const char * s, FILE * stream);
```

La fonction écrit la chaîne *s* dans le flux *stream* et retourne un nombre non négatif si elle réussit. Dans le cas contraire, elle retourne EOF. Le code suivant fait la même chose que celui juste avant, mais en utilisant une fonction plus adaptée pour ça.

```c
#include <stdio.h>

int main(void)
{
    FILE * fichier = fopen("test.txt", "w");
    if(fichier == NULL)
    {
        perror("fopen");
        /* ... */
    }

    fputs("Salut", fichier);

    fclose(fichier);
    fichier = NULL;
    return 0;
}
```

Pour terminer, sachez que contrairement à *puts*, la fonction *fputs* n'ajoute pas de ```'\n'``` final.

### La grande famille de printf ###

Tout comme *scanf*, la fonction *printf* a une sœur permettant d'écrire sur un flux quelconque : [fprintf](http://www.linux-kheops.com/doc/man/manfr/man-html-0.9/man3/fprintf.3.html). En voici le prototype :

```c
int fprintf (FILE * stream, const char * format, ...);
```

Elle écrit tous les arguments passés en paramètres dans le fichier *stream* : elle fonctionne exactement comme *printf*, à la différence près que le premier argument est un ```FILE*```. Voici un exemple qui écrit dans un flux le pseudo et le score d'un joueur :

```c
#include <stdio.h>

int main(void)
{
    FILE * fichier;
    const char * pseudo = "Lecteur";
    const int score = 50;

    fichier = fopen("test.txt", "w");
    if(fichier == NULL)
    {
        perror("fopen");
        /* ... */
    }

    fprintf(fichier, "%s %d\n", pseudo, score);

    fclose(fichier);
    fichier = NULL;
    return 0;
}
```

Vous pouvez vérifier dans le fichier, le nom et le score du joueur ont bien été inscrits, suivis d'un retour à ligne. Afin de vous entrainez, pourquoi ne pas reprendre notre structure de la sous-partie précédente et s'entrainer à écrire chacun des membres dans un flux ?

Enfin, sachez que *fprintf* est également très utile pour signaler les erreurs. Il suffit d'écrire dans le flux ```stderr```. Pourquoi un simple *printf* / *puts* ne suffirait-il pas ? Tout d'abord, *printf* / *puts* écrivent sur ```stdout```. Dans notre cas, que l'on écrive sur ```stderr``` ou ```stdout```, cela revient au même puisque tout est affiché sur la console. Or, si jamais vous utilisez plus tard des bibliothèques graphiques, il se peut que les deux flux soient bien distincts. Il sera donc important de bien séparer les messages d'erreur des messages informatifs. Il se peut également que la console ne se lance pas (c'est le cas dans la grande majorité des applications). Comment faire alors pour afficher des messages ? Voilà pourquoi on préfère utiliser ```fprintf``` pour remonter les erreurs.

### D'autres fonctions
En plus de nous permettre de lire et d'écrire dans un fichier, la bibliothèque standard définie d'autres fonctions pour manipuler les flux. Nous allons en voir quelques-unes.

### Manipuler le curseur ###

Nous avons parlé tout au long de ce chapitre du curseur virtuel qui indique où l'on se situe dans un fichier. Les fonctions que nous avons vu déplace le curseur pour nous, mais il existe des fonctions qui nous permettent de le faire manuellement. Nous allons en voir trois.

### ftell - Déterminer la position du curseur ###

Cette fonction renvoie la position actuelle du curseur dans le flux passé en paramètre. Son prototype est :

```c
long ftell(FILE * stream);
```

Je pense que vous n'avez pas besoin d'exemple, la fonction parle d'elle-même.

### fseek - Repositionner le curseur ###

Voici le prototype de la fonction :

```c
int fseek (FILE * stream, long offset, int whence);
```

Détaillons ces trois paramètres un par un. Comme à l'accoutumée, l'argument *stream* correspond au flux sur lequel on souhaite agir. Ensuite, il s'agit de la valeur du déplacement du curseur. En mode texte, cette valeur doit être obligatoirement une valeur retournée par *ftell* ou 0. C'est le seul comportement garantit par la norme. Si l'on passe une autre valeur, alors on dit que le comportement *dépend de l'implémentation* : ça marchera sous une plate-forme X avec un compilateur Y mais pas avec une autre. C'est donc quelque chose à éviter, sauf si vous visez une plate-forme particulière.

Pour finir, *whence*, qui signifie « d'où » en français, représente l'origine , le point de départ utilisé par *offset* pour déplacer le curseur. Trois constantes sont fournies :

* ```SEEK_SET``` : début du fichier ;
* ```SEEK_CUR``` : position actuelle du curseur ;
* ```SEEK_END``` : fin du fichier ;

Dans le cas du mode texte, pour avoir un code conforme à la norme, ce paramètre doit obligatoirement être ```SEEK_SET```. Une autre valeur rendra le comportement du programme dépendant de l'implémentation.

La fonction retourne 0 si elle réussit, une valeur différente de 0 si elle échoue. 

#### rewind - Repositionner le curseur au début ####

Cette fonction sert simplement à remettre le curseur au tout début du fichier. Voici son prototype, qui parle pour lui :

```c
void rewind(FILE * stream);
```

Préférez l'appel de cette dernière que *fseek* (pour cet emploi du moins), pour des raisons de clarté et de simplicité.

### Opérations diverses ###
#### rename - Renommer un fichier ####

Cette fonction permet de renommer un fichier passé en paramètre par un nouveau nom :

```c
int rename (const char * oldname, const char * newname);
```

Si *newname* désigne un fichier déjà existant, la fonction peut soit échouer, soit écraser l'autre fichier déjà présent, tout dépend du système d'exploitation. Si la fonction échoue, elle retourne encore une fois une valeur différente de 0.

### remove - Supprimer un fichier ###

Cette fonction supprime tout simplement du disque dur le fichier désigné par la chaîne de caractères passée en paramètre, sans confirmation ni possibilité de récupération (donc prudence). Voici son prototype :

```c
int remove (const char * filename);
```

Si elle réussit, elle retourne la valeur 0 sinon une autre valeur.

Ce chapitre nous aura fait découvrir encore d'autres fonctions de ```<stdio.h>``` et pourtant elle en contient d'autres, certes moins utilisées, mais qui peuvent toujours servir un jour. Si vous voulez les découvrir, jetez un œil sur [ce site](http://www.cplusplus.com/reference/cstdio/), certes en anglais (vous pourrez vous entraîner) mais de très bonne qualité.

Le chapitre suivant est la suite logique de celui-ci : nous savons manipuler des flux, mais comment les manipuler de façon sécurisée ? Comment empêcher l'utilisateur de rentrer des valeurs fausses ? Comment empêcher les dépassements de tampons ?

## Entrées sécurisées
L'une des plus grandes règles dans le monde de la programmation est de ne jamais faire confiance à l'utilisateur. Cette règle est particulièrement importante lorsqu'on demande des informations : qui nous prouve que l'utilisateur va répondre correctement, qu'il ne va pas nous envoyer une chaîne de caractères au lieu d'un ```int``` ? Il est donc important d'apprendre à sécuriser le mieux possible ses entrées, et c'est le but de ce chapitre.

### Les dangers de scanf
Depuis le début de ce cours nous utilisons la fonction *scanf* dès qu'il y a besoin de récupérer des informations auprès de l'utilisateur. Elle est relativement simple à première vue, et c'est pour cela que nous l'avons utilisée depuis le début, mais elle est en réalité complexe et potentiellement dangereuse. C'est ce que nous allons illustrer dans cette partie.

### Chaîne de caractères avec des espaces ###

Le premier problème vient d'une chaîne de caractères qui contiendrait des espaces. En effet, avec l'utilisation du format ```%s``` (qui sert à récupérer des chaînes de caractères), *scanf* supprime les espaces avant et après le premier mot de la chaîne. Du coup, lorsque que l'utilisateur rentre une chaîne avec des espaces, *scanf* ne va prendre que le premier mot. 

```c
#include <stdio.h>

int main(void)
{
    char chaine[20];

    printf("Ecris une phrase s'il-te-plait : \n");
    scanf("%s", chaine);
    printf("Entree : '%s'\n", chaine);

    return 0;
}
```
```console
Écris une phrase s'il-te-plait :
Salut ca va ?
Entrée : 'Salut'
```

Où est passé le reste des caractères rentrés ? Il sont stockés dans le **buffer stdin**, c'est à dire la zone mémoire qui stocke tous les caractères rentrés par l'utilisateur. Et le problème est que la prochaine fois que *scanf* sera appelée, elle ne demandera rien à l'utilisateur et les caractères non-extraits seront stockés dans la chaîne, ce qui est assez embêtant :

```c
#include <stdio.h>

int main(void)
{
    char chaine[20];

    printf("Ecris une phrase s'il-te-plait : \n");
    scanf("%s", chaine);
    printf("Entree : '%s'\n", chaine);

    printf("Une autre : \n");
    scanf("%s", chaine);
    printf("Entree : '%s'\n", chaine);

    return 0;
}
```
```console
Écris une phrase s'il-te-plait :
Salut ça va ?
Entrée : 'Salut'
Une autre :
Entrée : 'ça'
```

On ne peut même pas rentrer quoi que ce soit, *scanf* va directement dans le buffer chercher le prochain mot, et ainsi de suite jusqu'à ce qu'elle ait tout récupéré. Nous verrons dans une partie suivante comment vider le buffer.

### Chaîne de caractères trop longue ###

Un des plus grands dangers avec *scanf* est lorsque l'on rentre une chaîne de caractères trop longue. Imaginons par exemple que l'on définisse un tableau de 10 ```char```. On peut donc rentrer au maximum 9 caractères. Regardez ce qui se passe lorsqu'on dépasse cette limite.

```c
#include <stdio.h>

int main(void)
{
    char chaine[10];

    printf("Ecris une phrase s'il-te-plait : \n");
    scanf("%s", chaine);
    printf("Entree : '%s'\n", chaine);

    return 0;
}
```
```console
Écris une phrase s'il-te-plait :
Anticonstitutionnellement
Entrée : 'Anticonstitutionnellement'
```

Ce qui semble anodin à première vue cache un problème grave : en effet, *scanf* a écrit tous les caractères en mémoire, alors qu'il n'y avait pas la place pour. Où les a t-elle écrit ? A la suite, mais sur des cases mémoires qui n'appartient pas au programme. C'est un dépassement de tampon (*buffer owerflow*). Et bien souvent, le système d'exploitation arrête le programme afin de l'empêcher de faire des dégâts. Il est donc très facile de causer des plantages si l'on n'y prend pas garde.

### Entrée erronée ###

Un autre problème, que vous avez peut-être déjà constaté, arrive lorsque *scanf* attend un certain type de données (des nombres par exemple) et qu'on rentre autre chose (des caractères). Tout peut alors arriver :

```c
#include <stdio.h>

int main(void)
{
    int n;

    printf("Donne un nombre : ");
    scanf("%d", &n);
    printf("Merci pour le nombre %d\n", n);

    return 0;
}
```
```console
Donne un nombre : dfdf
Merci pour le nombre 2147348480
```

La fonction fait parfaitement son boulot : elle récupère ce qui est entré et le stocke. Sauf que ça peut être problématique dans certains cas. Je n'ai eu ici qu'une simple valeur erronée (que j'aurais pu éviter en initialisant la variable à 0), mais j'aurais pu avoir plus grave : bugs latents, boucle infinie et même plantage.

Comme vous avez pu vous en rendre compte, *scanf* est potentiellement dangereuse si l'on n'y prend pas garde. Il est donc important d'apprendre à construire des entrées solides.

### Des alternatives
### Récupérer une chaîne ###

Pour pouvoir sécuriser les entrées de chaînes de caractères, nous allons réutiliser une fonction que nous avons vu dans le chapitre précédent : *fgets*. Je vous rappelle le prototype de cette fonction : 

```c
char * fgets(char * s, int size, FILE * stream);
```

Cette fonction lit un certain nombre de caractères d'un flux et écrit ce qu'elle lit dans une chaîne de caractères. On s'en sert habituellement pour lire dans les fichiers, mais on peut aussi lui passer le flux **stdin** pour récupérer ce que tape l'utilisateur. Essayons de coder un programme qui récupère pile-poil le bon nombre de caractères. On peut pour cela s'aider de ```sizeof```. Voici mon code :

```c
#include <stdio.h>

int main(void)
{
    char chaine[20];
    size_t n = sizeof(chaine);

    printf("Entrez une chaine : ");
    fgets(chaine, n, stdin);
    printf("Voici la chaine rentree : %s\n", chaine);

    return 0;
}
```
```console
Entrez une chaine : Salut ca va ?
Voici la chaine rentrée : Salut ca va ?
```

Notez que j'utilise une variable intermédiaire pour stocker la taille du tableau. Dans notre exemple c'est inutile (on aurait pu mettre ```sizeof(chaine)``` directement dans l'appel de *fgets*), mais je prévois si jamais on devait appeler *fgets* dans une fonction : comme un tableau est converti en pointeur constant sur son premier élément, en faisant ```sizeof``` nous aurions eu la taille du pointeur et non de tout le tableau. En passant par une variable, on est sur de conserver tout le temps la taille du tableau.

Comme *fgets* limite le nombre de caractères lus, il n'y a pas de risque de dépassement, même si la chaîne rentrée est plus grande que le tableau :

```console
Entrez une chaine : Anticonstitutionnellement
Voici la chaine rentrée : Anticonstitutionnel
```

Le seul problème, c'est que les caractères non-lus sont toujours dans le buffer, et il faut le vider sinon *fgets* lira directement le buffer sans demander quoi que ce soit à l'utilisateur. Il faut donc que nous codions nous-mêmes une fonction.

#### Une fonction de saisie ####

L'idée est de coder une fonction qui va lire une chaîne de caractère en appelant *fgets*, mais qui va en plus supprimer le retour à la ligne et vider le buffer. Mais comment vide t-on un buffer ?

##### Vider un buffer #####

Grâce à *fflush*. Cette fonction, dont le prototype est juste en dessous, permet de vider un buffer des caractères qu'il contient.

```c
int fflush (FILE * stream);
```

Elle est utilise notamment dans le cas des sorties. Je m'explique. Pour qu'un flux soit affiché à l'écran, il faut que l'une des trois conditions suivantes soit remplie.

* Le buffer est plein. On ne peut pas contrôler cet évènement.
* Il faut qu'il y ait le caractère ```'\n'```.
* Ou bien il faut que *fflush* soit appelée.

Ainsi, on s'en sert par exemple après un appel d'une fonction de sortie quand la chaîne de caractères passée en argument ne contient pas de ```'\n'```. En effet, il se peut que ça marche sans appeler cette fonction, mais rien ne garantit que ça marchera tout le temps. Pour s'en assurer, on appelle *fflush*. Exemple avec un code tout bête :

```c
#include <stdio.h>

int main(void)
{
    int var = 42;

    printf("Entrez un entier : ");
    fflush(stdout);
    scanf("%d", &var);
    printf("Voici l'entier : %d\n", var);

    return 0;
}
```

L'idée est de coder une fonction qui va lire une chaîne de caractère en appelant *fgets*, mais qui va en plus supprimer le retour à la ligne et vider le buffer. Si notre fonction *fflush* marche parfaitement avec les flux de sortie, en revanche il est impossible de l'utiliser sur les flux d'entrées. Pourquoi cela ? Parce que la norme ne précise pas le comportement de cette fonction sur un flux d'entrée. Son utilisation peut donc aussi bien marcher que planter ; c'est un comportement indéterminée. Puisque c'est ainsi, nous allons coder nous-mêmes une fonction capable de vider *stdin*. Et nous allons utiliser *getchar*, cette fonction qui lit un caractère de *stdin*. Il suffit de boucle tant qu'on obtient pas ```'\n'``` ou EOF pour vider entièrement le buffer. On obtient donc ceci :

```c
void fflush_stdin(void)
{
    int c;

    do
    {
        c = getchar();
    } while (c != '\n' && c != EOF);
}
```

##### Notre fonction de saisie #####

Maintenant que nous savons vider *stdin*, vous avez toutes les clefs pour coder notre propre fonction de saisie sécurisée. Pensez à éliminer le ```'\n'``` final. Bon courage !

Voici [ma version de la fonction](http://paste.awesom.eu/informaticienzero/38f&ln). Elle est simple : on lit une chaîne avec *fgets*, on recherche le caractère ```'\n'``` et si on le trouve on le supprime, sinon on vide le buffer et on retourne -1 pour signaler l'erreur. Si tout s'est bien passé, on retourne 0.

### Récupérer une valeur ###

Notre fonction ne sait lire pour l'instant que des chaînes de caractères. Si jamais on veut convertir une chaîne en nombre, il existe des fonctions que nous avons déjà vus dans le chapitre des chaînes de caractères : il s'agit de *strtol* et *strtod*. Il existe cependant une autre fonction capable de faire la même chose : *sscanf*.

Comme son nom l'indique, *sscanf* lit des caractères dans une chaîne. Voici son prototype :

```c
int sscanf (char * chaine, const char * format, ...);
```

Son fonctionnement est le même que *scanf*, sauf qu'elle lit les caractères dans une chaîne et non dans stdin. Tout ce que vous savez de *scanf* s'applique à *sscanf*.

```c
int main (void)
{
    char chaine[20];
    size_t n = sizeof(chaine);
    int temp = 0;

    printf("Entrez un nombre : ");
    fgets(chaine, n, stdin);
    sscanf(chaine, "%d", &temp);
    printf("temp = %d\n", temp);

    return 0;
}
```
```console
Entrez un nombre : 45
temp = 45
```

Mais là encore, les dangers qui nous guettaient avec *scanf* nous guettent aussi avec *sscanf*. Il nous faut donc apprendre à manier correctement *scanf*.

### Comment bien utiliser scanf ?
Il se peut que la méthode que nous avons vu avec *fgets* vous paraisse trop lourde, et vous préféreriez continuer à utiliser *scanf*. Dans ce cas, je vais vous montrez qu'il est possible, mais parfois compliqué, d'utiliser correctement *scanf*.

### Limiter le nombre de caractères lus ###

Tout comme *fgets*, on peut limiter le nombre de caractères que doit lire *scanf*. On peut ainsi limiter la lecture à 5, 10 ou 100 caractères par exemple. Pour se faire, il suffit de préciser le nombre de caractères à lire entre le ```%``` et l'indicateur de conversion. Comme une image vaut mille mots, voici un code qui limite la saisie à 7 caractères :

```c
int n;

scanf("%7d", &n);
printf(">> %d\n", n);
```
```console
125
>> 125
-45
>> -45
123456789
>> 1234567
```

On a par contre le même problème que *fgets* : les caractères non-lus restent dans le buffer. Il faut donc le vider en utilisant la fonction *fflush_stdin*, définie plus haut.

Cette technique marche aussi parfaitement avec les chaînes de caractères, sous réserve là encore de vider le buffer après la saisie.

```c
char chaine[10];

printf("Entrez une chaine : ");
scanf("%9s", chaine);
fflush_stdin();
printf("Vous avez entre : %s\n", chaine);
```
```console 
Entrez une chaine : Anticonstitutionnellement
Vous avez entre : Anticonst
```

### Les regexs ###

Abordons à présent le point le plus compliqué de *scanf* : les expressions régulières (de l'anglais **reg**ular **ex**pressions). Elles ne marchent que pour les chaînes de caractères et sont placées entre crochets. Grâce à elles, on peut choisir quel type de caractères récupérer (des chiffres, des minuscules, des majuscules, etc). Voici des exemples de regexs (vous noterez qu'on ne met plus le ```s``` comme on en avait l'habitude pour les chaînes de caractères) :

```c
char chaine[81] = {0}; /* doit pouvoir contenir tous les caractères dont le '\0' de fin */

/* Les chiffres de 0 à 9. */
scanf("%80[0-9]", chaine);

/* Les minuscules de 'a' à 'z'. */
scanf("%80[a-z]", chaine);

/* Les minuscules de 'a' à 'z' et les majuscules de 'A' à 'Z'. */
scanf("%80[a-zA-Z]", chaine);

/* Que les lettres de 'd' à 'y' (et de 'H' à 'L') et les chiffres de 2 à 7. */
scanf("%80[d-yH-L2-7]", chaine);
```

Essayez par exemple de faire un programme qui ne lit que les minuscules de ```'a'``` à ```'m'```, et les chiffres de 4 à 9. Il faut bien sur penser à vider le buffer après l'appel de *scanf*. Avec [mon code](http://paste.awesom.eu/informaticienzero/wwK&ln), vous devriez obtenir une exécution semblable à celle ci-dessous.

```console
Entrez une chaine : abcdtmh785
Vous avez entre : abcd
```

On peut aussi faire lister les caractères **que l'on ne veut pas** récupérer en utilisant le symbole ```^``` :

```c
char chaine[81];

/* On récupère tout sauf les chiffres de 4 à 9. */
scanf("%80[^4-9]", chaine);
```

Cela permet de vider le buffer d'une autre façon. Il suffit de ne lire aucun caractère sauf le retour à la ligne et l'éliminer à l'aide de *getchar*.

```c
char chaine[21];

/* On récupère 20 caractères. */
scanf("%20s", chaine);

/* Puis on vide le buffer en ne gardant aucun caractère ... */
scanf("%*[^\n]");
/* ... avant de supprimer le '\n' final.*/
getchar();
```

Il est donc possible de faire des entrées sécurisées avec *scanf*, mais cela reste assez complexe et réclame de la rigueur. Enfin, sachez que ce que nous venons de voir est conforme à la norme et marchera partout. Il existe d'autres expressions régulières qui ne sont pas standards et que nous n'aborderons donc pas ici.

Malgré les méthodes que nous venons de voir, il est impossible de sécuriser à 100 % ses entrées, donc restez raisonnables, ne tentez pas de tout sécuriser. Après tout, si l'utilisateur fait n'importe quoi, tant pis pour lui ! Vous noterez que c'est comme ça que font beaucoup de programmes.

Il est maintenant temps de mettre tout ça en pratique avec un petit TP.

## T.P - zAnalyse
### Énoncé
### zAnalyse ###

Cet exercice vous permettra de manipuler des chaînes de caractères et des fichiers. En effet, vous serez amené à analyser un texte (compter le nombre de paragraphes, de lignes, de mots, de caractères).

Tout d'abord, fixons les règles. Un mot est une suite de caractères suivie ou précédant un espace. Un caractère peut représenter une lettre minuscule, une lettre majuscule, un chiffre ou un signe de ponctuation, mais aussi une espace typographique, une tabulation, un retour à la ligne, etc. Une ligne se finit par un retour à la ligne. Un paragraphe représente ici deux retours à la lignes consécutifs.

#### Niveau facile ####

Tout d'abord, l'utilisateur entrera une chaine de caractères, vous *ne* compterez *seulement que* :

* Le nombre de paragraphes
* Le nombre de lignes
* Le nombre de mots
* Le nombre de caractères

Voici un exemple possible d'exécution :

```console
Votre fichier contient :
    n paragraphes
    n lignes
    n mots
    n caractères
```

#### Niveau intermédiaire ####
Un peu plus compliqué, vous devez désormais compter :

* **Le niveau facile**
* Le nombre de chacune des lettres de l'alphabet (sans distinguer les majuscules, les minuscules et les accents).
* Le nombre de caractères autres (ponctuation, slash, chiffres, etc). L'espace, le retour à la ligne, la tabulation horizontale et le retour chariot ne seront pas pris en compte.

Si il n'y a aucune occurrence d'un certain caractère, ne pas l'indiquer. Voici un exemple possible d'exécution :

```console
Votre fichier contient :
    n paragraphes
    n lignes
    n mots
    n caractères
        dont :
            n fois la lettre a
            n fois la lettre b
            ...
            n fois la lettre z
        et n autres caractères
```

#### Niveau difficile ####

Vous en voulez encore, ça tombe bien, j'ai plusieurs idées. La chaîne de caractères est toujours dans un fichier, vous devrez **écrire** le résultat dans un autre fichier :

* **Le niveau facile ainsi que le niveau intermédiaire**
* Le nombre moyen de caractères par mot
* Le ou les mot(s) le(s) plus long(s) ainsi que le nombre de caractères qu'il contient

Voici un exemple possible d'exécution :

```console
Votre fichier contient :
    n paragraphes
    n lignes
    n mots
        dont :
            n fois le mot "et"
            n fois le mot langage
            ...
        avec n caracteres par mot en moyenne
        ainsi que le mot le plus long est programmation (n caracteres)
    n caractères
        dont :
            n fois la lettre a
            n fois la lettre b
            ...
            n fois la lettre z
        et n autres caractères
```

Prenez votre temps, réfléchissez, ce n'est pas une course. Bonne chance !

Finalement, les flux ce n'est pas toujours une partie de plaisir, surtout en C. Nous avons vu par exemple comment sécuriser les entrées, mais ce n'est pas parfait. Ce que vous devez retenir de cette partie, c'est qu'il faut savoir garder un équilibre : certes il faut sécuriser ses entrées, mais ne passez pas votre temps à ça.

# Pour aller plus loin
Comme vous devez vous en douter, nous ne pouvons tout vous montrer sur le C ni prétendre être exhaustif. En effet, un langage de programmation, c'est comme un langue, on en apprend toujours un peu plus au fur et à mesure, mais on ne peut jamais vraiment le maitriser. Nous avons donc décidé dans cette partie finale de vous parler de quelques points du C que nous n'avions pas abordés jusqu'ici, utilisés un peu plus rarement que tout ce que nous avons vu jusqu'à maintenant, mais qu'il est toujours bien et utile d'apprendre. Nous ferons également une présentation des normes C99 et C11 ainsi qu'un bref aperçu de quelques bibliothèques connues pour ceux qui veulent continuer à apprendre. C'est parti pour la dernière ligne droite !

## Opérations bit à bit et champs binaires
Le C est souvent qualifié de *langage bas-niveau* et ce terme n'est pas usurpé. En effet, en plus des pointeurs qui nous font souvent mettre les mains dans le cambouis, le C propose un mécanisme de **manipulation de bits** que nous allons découvrir dans ce tutoriel. Un [autre tutoriel](http://progdupeu.pl/tutoriels/57/les-operations-bit-a-bit-et-le-branch-free-code/) plus général existe sur PDP ; n'hésitez pas à le consulter en parallèle pour approfondir vos connaissances. Quant à nous, nous allons voir ces opérations *bitwise* à travers le C.

Mais avant de commencer, et afin d'éviter de dire répéter plusieurs fois le même contenu dans différents tutoriels, je vous encourage, si jamais les notions de décalages, de XOR et autres vous sont inconnues, à lire [la première partie](http://progdupeu.pl/tutoriels/57/les-operations-bit-a-bit-et-le-branch-free-code/#1-instructions-bit-a-bit-et-decalages) du tutoriel de  [mewtow](http://progdupeu.pl/membres/voir/mewtow) et [Lucas-84](http://progdupeu.pl/membres/voir/Lucas-84).

### Les opérateurs bitwise
Le langage C définit six opérateurs dit *bitwise*. Les voici :

* `&` : correspond au ET bitwise (AND) ;
* `|` : correspond au OU bitwise (OR) ;
* `^` : correspond au OU exclusif bitwise (XOR) ;
* `~` : correspond au NON bitwise (NOT) ;
* `>>` : correspond à un décalage vers la droite (*right shift*) ;
* `<<` : correspond à un décalage vers la gauche (*left shift*) ;

Les opérateurs ET bitwise (`&`) et OU bitwise (`|`) ne doivent pas être confondus avec les opérateurs ET logique (`&&`) et OU logique (`||`). Ce sont deux choses aussi différentes que le sont l'opérateur d'affectation `=` et l'opérateur de comparaison `==`.

### Les opérateurs appliqués en C ###

Voici un simple code qui illustrera bien mieux le sujet que milles mots.

```C
#include <stdio.h>

#define OP(x, y, op) printf("%x " #op " %x = %x\n", (x), (y), (x) op (y))

int main(void)
{
    int a = 0xF0; /* == 1111 0000 */
    int b = 0x0F; /* == 0000 1111 */
    int c = 0x0; /* == 0000 0000 */

    /* 1111 0000
    &  0000 1111
    =  0000 0000 */
    OP(a, b, &);

    /* 1111 0000
    &  0000 0000
    =  0000 0000 */
    OP(a, c, &);

    /* 1111 0000
    |  0000 1111
    =  1111 1111 */
    OP(a, b, |);

    /* 1111 0000
    |  0000 0000
    =  1111 1111 */
    OP(a, c, |);

    /* 1111 0000
    ^  0000 1111
    =  1111 1111 */
    OP(a, b, ^);

    /* 1111 0000
    ^  0000 1111
    =  1111 1111 */
    OP(a, c, ^);

    return 0;
}
```

Enfin, avant de continuer, sachez que, de même que la plupart des opérateurs que nous avons vu, il existe une forme raccourcie que voici.

* `a = a & b` est équivalent à `a &= b` ;
* `a = a | b` est équivalent à `a |= b` ;
* `a = a ^ b` est équivalent à `a ^= b` ;
* `a = a >> b` est équivalent à `a >>= b` ;
* `a = a << b` est équivalent à `a <<= b`.

### Les opérateurs de décalage ###
#### Bit de poids fort / faible ####

Avant toute chose, il est important de définir ce qu'est un **bit de poids fort** (en anglais *Most significant bit*) et un **bit de poids faible** (en anglais *Least significant bit*). C'est très simple.

* Le bit de poids faible est le bit de moindre importance du nombre ; en clair, le bit le plus à droite dans la réprésentation usuelle.
* Le bit de poids fort est le bit de plus forte importance du nombre ; en clair, le bit le plus à gauche dans la réprésentation usuelle.

Ceci étant dit, vous comprendrez mieux les sous-parties suivantes.

#### Décalage à droite ####

L'opération `a >> b` décale *b* bits de *a* vers la droite. Les bits de poids faible sont perdus ; on complète le nombre avec des bits de poids fort valant 0.  Exemple :

```c
int a = 0xA0; /* == 1010 0000 == 160*/

a >> 3; /* == 0001 0100 == 0x14 ==  20*/
```

Si l'expression est signé, le résultat peut être signé. Mais comme le résultat dépend de l'implémentation, il est conseillé de ne pas faire de décalage vers la droite sur un entier négatif.

Autre remarque : décaler de $n$ bits vers la droite revient à diviser par $2^n$. En effet, dans notre exemple, $160 = 20 \times 2^3 = 20 \times 8$.

#### Décalage à gauche ####

L'opération `a << b` décale *b* bits de *a* vers la gauche. Les bits de poids fort sont perdus ; on complète le nombre avec des bits de poids faible valant 0.  Exemple :

```c
int a = 0xA0; /* == 1010 0000 == 160*/

a << 3; /* == 0101 0000 0000 == 0x500 ==  1280*/
```

A l'opposé du décalage vers la droite, cette fois, décaler de $n$ bits vers la gauche revient à multiplier par $2^n$. En effet, dans notre exemple, $1280 = 160 \times 2^3 = 160 \times 8$.

### Exercice : afficher la représentation base 2 d'un entier ###

Il serait quand même plus pratique de pouvoir obtenir la représentation binaire d'un nombre pour mieux visualiser les opérations que l'on fait. Or, si *printf* fournit des indicateurs de conversions pour l'octal (`%o`) et pour l'hexadécimal (`%x`, avec la représentation en majuscules avec `%X`), elle ne fournit rien pour le binaire. Soit, nous allons le faire nous mêmes dans ce cas.

Réfléchissons. Comment tester, tout d'abord, si un bit est à 1 ou à 0. Quel opérateur bitwise allons-nous utiliser ? L'opérateur ET (`&`) ? Oui, c'est bien lui. Pourquoi ? Parce que cet opérateur ne renvoie 1 que si le bit testé vaut 1 ; il renvoie 0 dans les autres cas. Ainsi, en testant sa valeur, nous savons si le bit vaut 1 ou 0.

D'accord, mais un nombre est constitué de plusieurs bits. Comment tous les tester ? Réfléchissons. Quels opérateurs vient-on tout juste de découvrir ? Les opérateurs de décalage. En quoi vont-ils nous être utiles ? Le code ci-dessous devrait vous aider à trouver comment nous allons procéder.

```c
printf("0x%x", 1 << 3);
```

Ce code affiche `0x8`. Or, quelle est la représentation en binaire de ce nombre ? C'est 0b1000. Avez-vous remarqués la particularité de ce nombre ? Seul le bit n°3 vaut 1, tous les autres valent 0. Et alors ? Eh bien avec ce nombre, on peut tester le bit n°3 d'un autre nombre. Exemple ci-dessous.

```c
int a = 0x8;
int b = 0x10;

printf("bit n°3 de a = %d\n", a & (1 << 3));
printf("bit n°3 de b = %d\n", b & (1 << 3));
```

On obtient les valeurs 8 et 0. Qu'en déduit-on ? Posons l'opération en utilisant la représentation binaire. On sait que 0x8 est équivalent à 0b1000. Si on applique la table de vérité de l'opérateur ET, on obtient $0b1000 & 0b1000 = 0b1000$. On comprend donc que l'on obtienne 8. De même, 0x10 est équivalent à 0b10000, donc $0b10000 & 0b1000 = 0b00000$. On comprend donc que l'on obtienne 0.

Avez-vous saisi le principe ? Il suffit de faire une boucle pour tester tous les bits du nombre et nous obtiendrons sa représentation binaire.  D'ailleurs, si on peut commencer par le bit de poids faible et progresser vers le bit de poids fort avec l'opérateur `<<`, rien ne nous empêche de faire l'inverse, c'est à dire de commencer par le bit de poids fort et progresser vers le bit de poids faible avec l'opérateur `>>`. Seulement, comment connaître le nombre de bits composant un `unsigned int` par exemple ?

Heureusement pour nous, le langage C nous fournit les limites des types entiers dans le fichier d'en-tête `<limits.h>`. Une des constantes en particulier nous intéresse : `UINT_MAX`, qui donne la valeur maximum que peut contenir un `unsigned int`. Comme c'est la valeur maximum, tous ces bits sont à 1. Tel quel, on peut se demander à quoi cela va nous servir. Mais essayez de décaler cette valeur d'un rang vers la droite. Cette fois, le bit de poids fort est à 0 ; tous les autres bits restent à 1. Ceci est normal, puisque décaler d'un rang vers la droite équivaut à diviser par 2.

Et maintenant, essayons de lui appliquer l'opérateur NOT (`~`). Cette fois, le premier bit sera le seul à 1, tous les autres seront à 0. Tiens, mais c'est parfait ! Grâce à cette valeur, nous pouvons tester le bit de poids fort. Il suffit ensuite de décaler d'un rang vers la droite à chaque tour de boucle pour tester le bit suivant, jusqu'à arriver au bit de poids faible. Cela vous parait un peu compliqué ? Alors ce code C devrait vous aider à y voir plus clair.

```c
#include <stdio.h>
#include <limits.h>

void bin_print_int(unsigned number)
{
    unsigned mask = ~(UINT_MAX >> 1);

    putchar('0');
    putchar('b');
    while (mask != 0)
    {
        if (number & mask)
        {
            putchar('1');
        }
        else
        {
            putchar('0');
        }
        mask >>= 1;
    }
    putchar('\n');
}

int main(void)
{
    bin_print_int(UINT_MAX);
    bin_print_int(UINT_MAX >> 1);
    bin_print_int(~UINT_MAX);
    bin_print_int(~(UINT_MAX >> 1));

    return 0;
}
```

Avez-vous remarqué la variable *mask*, ou *masque* en français ? Nous allons voir tout de suite qu'elle porte parfaitement bien son nom.

### Le masquage et les champs de bits
### Les masques ###

Qu'est ce qu'un masque ? Il s'agit d'une valeur binaire de la même taille que la valeur à masquer qui permet de modifier un ou plusieurs bits en une seule opération à l'aide des opérateurs bitwise. Nous en avons vu un exemple dans la partie précedente. En effet, pour tester le bit n°3 d'un nombre, nous avons utilisé la valeur `1 << 3`, qui vaut 0b1000 ; seul le bit n°3 vaut 1, les autres étant à 0. Nous pouvions ainsi tester le bit n°3 de n'importe quel nombre. De même, dans notre fonction *bin_print_int*, nous avons utilisé des masques pour tester chaque bit de notre nombre et ainsi afficher sa représentation en binaire.

A quoi peuvent bien servir les masques, en plus de ce que nous avons vu ? Eh bien grâce à eux, nous allons pouvoir modifier directement un ou plusieurs bits d'un entier !

#### Mettre un bit à 1 ####

Commençons par trouver quel opérateur nous servira dans ce cas précis. Si vous relisez les tables de vérités des opérateurs (disponibles dans le tutoriel cité en introduction), vous remarquerez que l'opérateur OR (`|`) convient très bien pour cela, puisque `x | 0 = x` et `x | 1 = 1`. Reste à définir notre masque.

Prenons notre valeur de test 0xF0. Sa représentation binaire usuelle vaut 0b1111 0000. Supposons que l'on veuille mettre le bit n°8 à 1. Il faut donc un masque où seul le bit n°8 est à 1, soit 0b0001 0000 0000 ou encore 0x100. En appliquant l'opérateur OR, on obtient bien la valeur souhaitée, soit 0b0001 1111 0000. 

```c
int main(void)
{
    int a = 0xF0;
    int masque = 0x100;
    bin_print_int(a);
    bin_print_int(masque);

    a |= masque;
    bin_print_int(a);
    printf("a = 0x%x\n", a);

    return 0;
}
```

#### Mettre un bit à 0 ####

De nouveau, examinons les tables de vérités. Il nous faut un opérateur qui transforme les 1 en 0 et ne touche pas aux 0. Et l'opérateur AND (`&`) fait exactement ce que nous voulons : `x & 1 = x` et `x & 0 = 0`. 

Reprenons encore notre valeur 0xF0, mais cherchons cette fois à mettre le bit n°5 à 0. Nous avons donc besoin d'un masque où tous les bits valent 1, sauf le bit n°5 qui vaudra 0. Nous obtenons donc le masque 0b1101 1111 soit 0xDF. En appliquant l'opérateur AND, nous obtiendrons la valeur 0b1101 0000, ce qui est bien ce que nous recherchons.

```c
int main(void)
{
    int a = 0xF0;
    int masque = 0xDF;
    bin_print_int(a);
    bin_print_int(masque);

    a &= masque;
    bin_print_int(a);
    printf("a = 0x%x\n", a);

    return 0;
}
```

#### Se fabriquer un masque plus facilement ####

Il n'est pas toujours évident de trouver de tête le masque, de faire des conversions dans tous les sens entre plusieurs bases, et même si il existe des outils comme la calculatrice fournie avec la plupart des systèmes d'exploitation, nous n'avons pas envie de jongler entre plusieurs fenêtres. Non, ce que nous voulons, c'est que ce soit le programme qui nous fournisse le masque adapté en fonction du bit à changer.

Dans le cas d'une mise à 1 à l'aide de l'opérateur OR, on remarque que le masque s'obtient en faisant `1 << n`où n est le numéro du bit que l'on veut modifier. On peut donc se définir une petite fonction qui nous fera ce calcul à notre place.

```c
int or_mask(int n)
{
    return 1 << n;
}
```

Et dans le cas d'une mise à 0 à l'aide de l'opérateur AND ? Si on observe bien, c'est le même masque que le précédent, à la seule différence que les bits 0 sont transformés en 1 et vice-versa. Or, quel opérateur permet d'inverser la valeur des bits ? C'est l'opérateur NOT (`~`). On en déduit donc que notre masque s'obtient en faisant `~(1 << n)`. Nous pouvons donc écrire notre petite fonction.

```c
int and_mask(int n)
{
    return ~(1 << n);
}
```

Testons donc avec ce petit code.

```c
int main(void)
{
    int a = 0xF0;
    int masque_ou = or_mask(8);
    int masque_et = and_mask(5);

    bin_print_int(a | masque_ou);
    bin_print_int(a & masque_et);
    return 0;
}
```

On obtient les mêmes valeurs que précédemment. Nous pouvons donc nous épargner du travail supplémentaire en laissant l'ordinateur nous donner le masque. Cette méthode présente néanmoins des inconvénients, comme par exemple le fait de ne pas pouvoir créer directement un masque modifiant plusieurs bits. Il faudra pour cela faire des opérations sur les résultats de la fonction.

```c
int main(void)
{
    int a = 0xF0;
    int masque_ou = or_mask(8) | or_mask(10);
    int masque_et = and_mask(5) & and_mask(6);

    bin_print_int(a | masque_ou);
    bin_print_int(a & masque_et);
    return 0;
}
```

### Les champs de bits ###

Nous le savons, lorsque l'on créé une structure, sa taille est la somme de la taille de tous ces éléments plus quelques bits de padding en fonction des cas. Pourtant, il est possible de définir une structure qui contiendra **des portions d'entiers** ! Comment est-ce possible ? Eh bien cela marche comme une structure classique sauf qu'en plus on précise, pour chaque champ, la taille en bits qu'il occupera. Exemple.

```c
struct bit_field
{
    unsigned field1 : 3; /* 1er champs : 3 bits */
    unsigned field2 : 1; /* 2ème champ : 1 bit */
    unsigned field3 : 7; /* 3ème champs : 7 bits */
};
```

Bien entendu, la taille d'un champ de bits ne peut dépasser celle d'un entier et les champs de bits ne sont applicables de façon définie et portable qu'aux entiers non-signés. Hormis ces contraintes, ces structures s'utilisent comme des structures habituelles.

Mais quel est donc l'intérêt de cette technique ? Il n'est pas très évident à voir, car hormis certains cas précis, vous ne la verrez que très rarement. Elle sert principalement quand on a besoin de stocker beaucoup d'informations et qu'on dispose de peu de mémoire. Prenons un exemple tiré du [tutoriel de mewtow et Lucas-84](http://progdupeu.pl/tutoriels/57/les-operations-bit-a-bit-et-le-branch-free-code/#6-champs-de-bits), celui d'un développeur qui veut stocker une date (constitué d'un jour, d'un mois et d'une année).

On sait qu'un jour sera toujours compris entre 1 et 31. Or 31 s'écrit aussi 0b11111 ; 5 bits suffisent donc. De même, un mois sera toujours compris entre 1 et 12. Ce dernier s'écrivant 1100, on en déduit que 4 bits suffisent. Enfin, en supposant qu'on stocke l'année jusqu'en 2047, qui s'écrit 0b11111111111, on obtient 11 bits. Notre structure s'écrira donc ainsi :

```c
struct date
{
    unsigned jour : 5;
    unsigned mois : 4;
    unsigned annee : 11;
};
```

Chez moi, `sizeof(struct date)` retourne 4. Sans préciser les champs de bits, j'obtiens 12. Nous avons donc économisé 8 octets. Une micro-poussière pour nous qui développons sur des ordinateurs communs, mais ces gains peuvent être utiles sur des processeurs embarqués ou sur des machines où la quantité de mémoire se compte en centaines d'octets.

Sachez que l'on peut également laisser des bits inutilisés ; il suffit simplement de ne pas donner de nom au champ. Cela est utile pour décrire certaines choses lorsque l'on fait de la programmation système. Par exemple, le registre d'état du *MC 68030* de Motorola est décrit comme suit dans la documentation.

* bit 0 : carry ;
* bit 1 : overflow ;
* bit 2 : zéro ;
* bit 3 : négatif ;
* bit 4 : extension ;
* bits 5-7 : inutilisés ;
* bits 8-10 : masque des interruptions ;
* bit 11 : inutilisé ;
* bits 12-13 : niveau de privilège ;
* bits 14-15 : état des traces.

La structure qui décrit ce registre d'état peut s'écrire ainsi :

```c
struct sr
{
    unsigned int trace : 2;
    unsigned int priv : 2;
    unsigned int : 1;       /* inutilisé */
    unsigned int masque : 3;
    unsigned int : 3;       /* inutilisé */
    unsigned int extend : 1;
    unsigned int negative : 1;
    unsigned int zero : 1;
    unsigned int overflow : 1;
    unsigned int carry : 1;
};
```

Mais gardez bien en tête que c'est **une méthode particulière réservée à des cas particuliers**. Si vous développez sur un ordinateur commun, n'utilisez pas les champs de bits, qui ne ferons que compliquer la relecture du code sans rien apporter d'autre.

### Quelques astuces
Jusqu'ici, nous avons vu majoritairement de la théorie, mais concrètement, à quoi ça sert vraiment tout ça ? Eh bien pour être honnête, dans la plupart des cas, ça ne vous servira pas vraiment. Cela ne veut pas dire que ça ne sert jamais, bien au contraire ! et je vais même vous le prouver à travers quelques exemples.

### Gestion des flags ###

Pour définir ce que sont les flags et leur intérêt, imaginons un instant que nous soyons en train de développer une bibliothèque multimédia. Celle-ci peut ouvrir des fenêtres, jouer de la musique, manipuler le lecteur CD, les ports USB, se connecter au réseau, etc. Bref, elle contient énormément de modules complets et utiles. Seulement voilà : comment faire, lorsqu'on initialise le programme, pour ne charger que les modules qui nous intéressent ? Il est hors de question de créer une fonction prenant autant de paramètres qu'il n'y a de modules : imaginez un instant si nous avons 20 modules ! Il est également hors de question de charger tous les modules ; on ne veut payer que ce que l'on veut utiliser.

L'idéal serait de n'avoir qu'un seul paramètre et que, en fonction de ce que l'utilisateur rentre, on ne charge que les modules demandés. Eh bien les flags servent à ça ; ce ne sont rien d'autres que des valeurs qui, combinées ensembles, vont nous permettre de déterminer quels sont les modules à charger.

Mais ça ne nous rappelle pas quelque chose ? Regardez ce chapitre. Nous avons découvert les opérateurs bitwise et c'est encore eux qui vont nous servir ici. Et puis combiner des valeurs ensembles, ça ne nous rappelle pas un peu nos histoires de masques et d'opérateur OR ? Eh oui ! il nous suffit de combiner plusieurs valeurs à l'aide de l'opérateur OR pour n'avoir à passer qu'un seul paramètre.

Mais quelles valeurs donner à nos flags ? Il faut être certains qu'en les combinant, on ne puisse pas avoir de doute quant aux flags qui forment la combinaison. Nous pouvons par exemple ne prendre comme flags les puissances de 2, qui ont comme particularité de n'avoir qu'un seul bit à 1 et jamais le même qu'une autre puissance de 2.

```c
#define NO_MODULE       (1 << 0)
#define AUDIO_MODULE    (1 << 1)
#define VIDEO_MODULE    (1 << 2)
#define NETWORK_MODULE  (1 << 3)
#define WINDOW_MODULE   (1 << 4)
#define MATHS_MODULE    (1 << 5)
```

Maintenant, nous avons un système simple qui nous permet de combiner les paramètres aussi facilement que l'on veut. Ainsi, si l'on veut charger le module de fenêtres et le module audio, il suffit de faire comme ceci :

```c
int pdp_init(int flags)
{
    
}

int main(void)
{
    pdp_init(AUDIO_MODULE | WINDOW_MODULE);
    return 0;
}
```

Par contre, il faut que la fonction qui reçoit notre combinaison de flags puisse extraire chaque flag pour pouvoir faire ce qu'on lui demande. Et une fois n'est pas coutume, la réponse a été apporté dans ce chapitre : l'opérateur AND. En effet, si notre flag est présent dans l'argument de la fonction, alors `argument & FLAG != 0`. Dans notre exemple, voici ce que ça donnerait :

```c
int pdp_init(int flags)
{
    if (flags & AUDIO_MODULE)
    {
        /* On charge le module audio. */
    }
    
    if (flag & VIDEO_MODULE)
    {
        /* On charge le module vidéo. */
    }
    
    /* Etc */
}
```

Pour information, ce mécanisme est par exemple utilisé par la bibliothèque graphique [SDL](http://www.libsdl.org). Voici les flags qu'elle utilise :

```c
#define	SDL_INIT_TIMER		0x00000001
#define SDL_INIT_AUDIO		0x00000010
#define SDL_INIT_VIDEO		0x00000020
#define SDL_INIT_CDROM		0x00000100
#define SDL_INIT_JOYSTICK	0x00000200
#define SDL_INIT_NOPARACHUTE	0x00100000	
#define SDL_INIT_EVENTTHREAD	0x01000000	
#define SDL_INIT_EVERYTHING	0x0000FFFF
```

### Puissances de 2 ###

Nous l'avons dit il y a quelques instants : les puissances de 2 on la particularité de n'avoir qu'un bit à 1, tous les autres étant à 0. En particulier, $2^n$ a $n$ zéros à droite de son unique bit 1. Et si on retire 1 à ce nombre, on obtient l'inverse : un 0 suivit de $n$ 1 ; $2^n$ et $2^n - 1$ ont tous leurs bits opposés. C'est une particularité des puissances de deux (et de zéro, mais zéro n'étant pas une puissance de 2, il ne sera pas compté). Sachant cela, on peut donc créer une fonction disant si un nombre est une puissance de 2 ou non.

```c
int is_power_of_two(unsigned int n)
{
    return n && (n & (n - 1)) == 0;
}
```

Pour continuer à voir l'intérêt des opérateurs bitwise et à vous entrainer, essayez de faire les calculs proposés dans [cette partie](http://progdupeu.pl/tutoriels/57/les-operations-bit-a-bit-et-le-branch-free-code/#3-les-puissances-de-deux) du tutoriel cité en introduction.

### Obtenir la valeur maximum d'un type non-signé ###

Une petite astuce : puisque 0, peut importe le type, a tous ses bits à 0, si on fait `~0`, tous les bits passent à 1. On peut ainsi obtenir la valeur maximum d'un entier non-signé.

```c
printf("%hu =?= %hu\n", ~0, USHRT_MAX);
printf("%lu =?= %lu\n", ~0, ULONG_MAX);
```

Les opérateurs bitwise ne sont pas très courant dans la plupart des codes, mais ils peuvent être très puissants, alors gardez-les dans un coin de votre tête, ils pourront vous servir un jour. Mais n'oubliez pas que cette puissance a un coût : une perte en lisibilité. Trop d'opérateurs bitwise rendent le code plus long à comprendre. Illustration d'un cas très tordu tiré du code source de **Quake 3 Arena**.

```c
float Q_rsqrt(float number)
{
    long i;
    float x2, y;
    const float threehalfs = 1.5F;
    
    x2 = number * 0.5F;
    y = number;
    i = *(long *)&y;
    i = 0x5f3759df - (i >> 1);
    y = *(float *)&i;
    y = y * (threehalfs - (x2 * y * y));
}
```

Ce code est particulièrement long à expliquer ; sachez simplement qu'il permet de calculer l'inverse d'une racine carrée et est extrêmement rapide. Mais il est fort à parier que vous n'aurez jamais à faire de code pareil. Tout ça pour dire que utilisez les opérateurs quand c'est nécessaire.

Dans le chapitre suivant, nous verrons une autre structure de données ainsi qu'un nouveau moyen de déclarer des constantes.

## Enumérations et unions
Les énumérations et les unions sont des types composés un peu moins courant que les structures (surtout les unions) mais néanmoins utiles. Nous avons choisi d'en parler parce qu'on les retrouve suffisamment souvent pour qu'on les remarque, dans les codes anciens ou un peu "poussés" et parce qu'ils sont puissants quand on sait bien les utiliser.

### Les énumérations
### Les bases ###

Les énumérations sont à première vue semblables aux ```#define``` puisqu'on s'en sert pour déclarer des constantes. Avant d'examiner plus en détail l'intérêt de cette nouvelle façon de faire, voici tout d'abord la syntaxe d'utilisation ci-dessous.

```c
enum identificateur {nom_1, nom_2, ..., nom_n};

/* Voici la façon de créer une variable de type enum identificateur */
enum identificateur variable = nom_x;
```

En règle générale, on écrit les noms de valeurs entièrement en majuscules. Ainsi, si on souhaite énumérer les quatre axes d'une boussole, on procèdera comme dans l'exemple suivant.

```c
enum Direction {NORD, SUD, EST, OUEST};

enum Direction urss = EST;
enum Direction usa = OUEST;
```

Peut-être êtes-vous en train de vous demander quel est le rapport avec les constantes de préprocesseur ? Eh bien il y a des points communs mais aussi des différences, dont la plus grande est sans doute la suivante : le compilateur associe automatique à chaque nom de valeur une constante entière en en commençant par zéro. Ainsi, dans notre exemple, NORD vaut 0, SUD vaut 1, EST vaut 2 et OUEST vaut 3. Et si cela ne nous convient pas, on peut associer nous-mêmes les valeurs que l'on veut, tant que celle-ci est entière.

```c
enum Direction {NORD = 4, SUD, EST = 42, OUEST};
```

Que deviennent les constantes de valeurs auxquelles nous ne précisons rien ? Eh bien le compilateur leur associe la valeur supérieure à la valeur de la constante précédente : SUD vaudra donc 5 et OUEST vaudra 43.

### Les énumérations face au préprocesseur ###

Maintenant vient la question fatidique : mais à quoi cela sert-il puisque nous avons déjà le préprocesseur qui fait un travail semblable et qui en plus nous permet d'utiliser autre chose que des constantes entières ? Tout d'abord, [comme pour les variable ou les fonctions](https://progdupeu.pl/tutoriels/15/le-langage-c/introduction/decouper-son-projet/), les énumérations (ainsi que les constantes énumérées) peuvent disposer de différentes portées suivant le lieu de leur déclaration. Il est donc possible de limiter cette dernière à un bloc ou d'utiliser le mécanisme du masquage.

```
#include <stdio.h>

enum Couleur {VERT = -42};

int main(void)
{
    printf("VERT = %d\n", VERT);
    {
        enum Couleur {VERT = 42};

        printf("VERT = %d\n", VERT);
        {
            enum Couleur {VERT = 7};
            printf("VERT = %d\n", VERT);
        }
        printf("VERT = %d\n", VERT);
    }
    printf("VERT = %d\n", VERT);
    return 0;
}
```

Cela n'est pas réalisable (à tout le moins pas de cette manière) dans le cas d'une constante de préprocesseur puisque le préprocesseur n'a aucune notion de bloc ou de fonctions (la seule portée possible est donc au niveau d'un fichier).

Le second avantage est qu'il est plus facile de débugger un programme qui utilise des constantes énumérées plutôt que des constantes de préprocesseur. Pourquoi ? Parce que la plupart des débuggers utilisent le type d'une constante pour retrouver son identificateur, ce qui est impossible si on a affaire à une constante de préprocesseur : il faut utiliser des outils spécialisés pour débugger des macros puisqu'elles n'existent plus après le passage du préprocesseur.

Un troisième avantage est qu'il est, dans certains cas, plus pratique et facile d'ajouter des constantes énumérées que des constantes de préprocesseur. Comparez les deux codes suivants : 

```
#define NORD 0
#define SUD 1
#define EST 2
#define OUEST 3

enum Direction {NORD, SUD, EST, OUEST};
```

Supposons que l'on veuille ajouter les directions intermédiaires (comme nord-ouest ou sud-est par exemple). Dans le premier cas, il faudra écrire huit lignes de plus, alors que dans le deuxième il suffira de rajouter ces noms de constante dans l'énumération. D'ailleurs, petite astuce, comme ce sont des constantes, on peut s'en servir pour retenir la taille d'un tableau. Ainsi, chaque fois qu'on ajoutera une constante à notre énumération, la taille augmentera elle aussi. Exemple avec des couleurs.

```c
enum Couleurs{VERT, BLEU, JAUNE, ROUGE, NB_COULEURS};
enum Couleurs jetons[NB_COULEURS];
void compter(enum Couleurs jetons[], int taille);

compter(jetons, NB_COULEURS);
```

Bien entendu, les constantes énumérées possèdent aussi des défauts. Ainsi, la valeur d'une constante énumérée doit toujours être comprise entre la valeur minimale et la valeur maximale d'un ```int```. Et s'il est besoin d'utiliser autre chose que des constantes entières, les énumérations ne peuvent rien pour nous.

Je conclus cette partie pour vous dire qu'il est possible de faire des pointeurs sur des types énumérations et qu'ils s'utilisent comme d'habitude. 

```c
enum Vins {BORDEAUX, BOURGOGNE, ALSACE};
enum Vins bordeaux = BORDEAUX;
enum Vins * vins_de_bordeaux = &bordeaux;
```

### Les énumérations anonymes ###

Les énumérations anonymes ne sont ni plus ni moins des énumérations sans identificateur. Elles sont utiles quand on veut seulement déclarer des constantes et les utiliser sans passer par un type énuméré. Un exemple ? Vous souvenez-vous des booléens ? En C, nous n'avons aucun type pour définir une variable de type booléen, au contraire d'autres langages comme C++ ou Java. Certains programmeurs, pour rendre leur code plus clair, récréer ce type grâce à un ```typedef``` et une énumération.

```c
enum {false, true};

/* On peut bien entendu utiliser le préprocesseur pour ça. */
#define false 0
#define true 1

typedef char bool;
```

C'est l'un des exemples les plus connus d'utilisation d'énumérations anonymes, mais certainement que vous en croiserez d'autres dans votre vie de programmeur.

### Les unions
Les unions sont des agrégats en apparence identiques aux structures mais qui se révèlent différentes dans leur utilisation et plus rares dans les codes. Pour commencer, voici sa syntaxe.

```c
union identificateur
{
    int entier;
    double flottant;
    char lettre;
};

union identificateur exemple;
exemple.entier = 42;
```

Pourtant, une différence majeure existe entre les structures et les unions : si la taille d'une structure est la somme de la taille de ses champs (plus éventuellement quelques bits de padding), la taille d'une union est la taille du plus grand de ses champs. Voyez par vous-mêmes en testant le code suivant (vous noterez que j'ai fait attention au padding dans la structure).

```c
#include <stdio.h>

struct my_structure
{
    double d;
    char c;
    int i;
};

union my_union
{
    int i;
    double d;
    char c;
};

#define PRINT_SIZE(type) printf("sizeof(" #type ") = %u\n", sizeof(type))
int main(void)
{
    PRINT_SIZE(int);
    PRINT_SIZE(double);
    PRINT_SIZE(char);
    PRINT_SIZE(struct my_structure);
    PRINT_SIZE(union my_union);
    return 0;
}
```

En compilant ce programme, vous verrez que l'union a la taille d'un ```double```. Les unions permettent donc d'économiser de la mémoire. En bons programmeurs que nous sommes, nous pourrions nous dire que les structures ne valent pas le coup par rapport aux unions puisqu'elles sont plus grosses. Mais ce n'est pas aussi simple car les unions ont un gros inconvénient que certains ont peut-être déjà deviné : puisque la taille est plus petite qu'une structure, toutes les champs partagent le même espace mémoire.

```c
#include <stdio.h>

struct my_structure
{
    double d;
    char c;
    int i;
};

union my_union
{
    int i;
    double d;
    char c;
};

#define PRINT_ADRS(var) printf("&" #var " = %p\n", &var)
int main(void)
{
    struct my_structure var_s;
    union my_union var_u;

    PRINT_ADRS(var_s.d);
    PRINT_ADRS(var_s.c);
    PRINT_ADRS(var_s.i);
    puts("");
    PRINT_ADRS(var_u.d);
    PRINT_ADRS(var_u.c);
    PRINT_ADRS(var_u.i);
    return 0;
}
```

Cela veut donc que quand on modifie un champ d'une union, on écrase les valeurs des autres champs. Les unions sont donc à manipuler avec précaution, car si elles le sont correctement, elles sont très puissantes, comme nous allons le voir.

### Exemple pratique : une abstraction pour les chaînes de caractères
Nous sommes d'accord pour dire que les chaînes de caractères ne sont pas toujours aisées à manipuler : il faut vérifier que l'on ne déborde pas, il faut faire attention à bien libérer la mémoire dans le cas d'une allocation dynamique, à bien mettre le caractère nul final, etc. C'est contraignant, aussi nous allons faire ce que beaucoup d'autres langages proposent de base : une abstraction pour les chaînes de caractères qui nous masquera tous ces détails agaçants.

Une bonne idée serait de faire une structure qui contienne un pointeur sur ```char``` que l'on allouera et réallouera au fil du programme. Voilà, seulement nous ne voulons pas faire des allocations dynamique inutiles, car nous savons que la majorité du temps les chaînes de caractères ont une taille inférieure à 32. Nous décidons donc de stocker la chaîne dans un tableau statique si elle fait moins de 31 caractères, sinon dans un pointeur qui sera alloué. Dans ce dernier cas, il faudra penser à conserver la taille maximale de notre tableau dynamique. Voilà un exemple pratique d'utilisation des unions.

```c
enum {false, true};
typedef char bool;

struct cstring
{
    union buffer
    {
        struct pointer { char * ptr; size_t capacity; } ptr;
        char array[32];
    } buffer;
    size_t length;
    bool is_in_ptr;
};
```

On pourra donc stocker des chaînes de n'importe quelle taille de façon totalement transparente pour l'utilisateur. C'est un bon exercice que je vous encourage à faire pour vous entrainer. Je ne vous donnerais pas de correction cette fois-ci car il existe de très nombreuses façons de créer une abstraction pour les chaînes de caractères, mais sachez que si besoin est, les forums seront là pour vous aider. Il faut surtout que vous reteniez qu'on peut utiliser soit le tableau statique, soit le pointeur alloué, mais pas les deux en même temps ; il faudra donc faire attention et bien pensez aux cas limites (lors des concaténations par exemple). Bon courage !

Finalement, les structures, les unions et les énumérations sont particulièrement puissantes quand elles sont mises ensembles de façon élégante. Vous n'aurez peut-être jamais à utiliser les trois en même temps, mais un peu de culture générale ne fait pas de mal. Nous continuerons à en parler dans le chapitre suivant pour illustrer certaines nouveautés des normes C99 et C11.

## Découvrir le C99 / C11
Le langage C, comme n'importe quel langage vivant, évolue au fil du temps. En 1999, dix ans après la normalisation par l'ANSI et neuf ans après celle de l'ISO, ce dernier comité décida de mettre à jour le langage en rajoutant certains éléments. Cette norme porte le nom  abrégé de [C99](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf). Enfin, en 2011, ce même comité décida de faire une nouvelle mise à jour du langage, notamment sur certains points bien trop compliqués pour nous, nommée [C11](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf). Néanmoins, même si nous ne présenterons pas tout des deux normes, nous avons sélectionné ce qui nous paraissait le moins compliqué et le plus intéressant. N'hésitez pas à fouiller un peu plus si le cœur vous en dit après.

Un dernier point avant de démarrer : ces normes n'ont eu que peu d'écho et contrairement au C89, elles ne sont pas supportées par certains compilateurs (Visual C++ par exemple, bien qu'il soit prévu un support du C99 pour VC++2013) ou incomplètement par d'autres. Il faudra donc faire attention si vous utilisez ces nouveautés dans l'un de vos programmes un jour.

### Avant de démarrer
Pour indiquer au compilateur que l'on souhaite compiler en C99 ou en C11, il faut modifier les options. Pour se faire, suivez les instructions ci-dessous en remplaçant XX par 99 ou 11 en fonction de la norme que vous utilisez.

* **Code::Blocks** : aller dans *Project -> Build Options -> Compiler settings -> Other options* et rajouter ```-std=cXX```.
* **GCC** en ligne de commande : rajouter l'option ```-std=cXX``` dans les options de compilation.
* **Visual Studio** : impossible pour le moment.

Ensuite, pour tester quelle version de C vous utilisez, vous pouvez utiliser la macro ```__STDC_VERSION__```. Celle-ci peut prendre les valeurs ci-dessous.

* Pas de valeur pour C90.
* ```199901L``` pour C99.
* ```201112L``` pour C11.

Enfin, voici quelques liens pour savoir quelles fonctionnalités sont supportés par quel compilateur.

* **GCC** : [C99](http://gcc.gnu.org/c99status.html) et [C11](http://gcc.gnu.org/wiki/C11Status)

### Découvrir le C99
### Les commentaires mono-lignes ###

Il est maintenant possible d'utiliser la syntaxe du C++ pour les commentaires sur une seule ligne à savoir ```//```. Comme leur nom l'indique, il n'est pas possible de faire un commentaire de plusieurs lignes avec excepté en rajoutant ```//``` à chaque nouvelle ligne ; personnellement je continue d'utiliser les commentaires du C90.

### Le mot-clef ```long long``` ###

L'entier ```long long``` et son pendant non-signé ```unsigned long long``` sont conçus pour faire au minimum 64 bits de taille, ce qui permet de stocker de grands nombres.

### Les booléens ###

Pour utiliser les macros définies par C99, il faudra inclure le fichier d'en-tête ```<stdbool.h>```. Celui contient le type ```bool``` ainsi que deux macros ```true``` et ```false``` valant respectivement 1 et 0 et une macro ```__bool_true_false_are_defined``` valant 1 si les trois macros précédentes sont définies. Si jamais il n'est pas possible d'utiliser ce fichier d'en-tête ou que vous ne souhaitez pas le faire, il est possible d'utiliser le mot-clef ```_Bool``` qui peut prendre les valeurs 0 ou 1.

### Les nombres complexes ###

C99 inclut un nouveau mot-clef pour manipuler les [nombres complexes](http://fr.wikipedia.org/wiki/Nombre_complexe) avec l'en-tête [<complex.h>](http://pubs.opengroup.org/onlinepubs/009604499/basedefs/complex.h.html) : ```complex```. Celui-ci doit être précédé de ```float```, ```double``` ou ```long double```. Cet en-tête fournit également la macro ```I```, dont le type peut changer en fonction de l'implémentation mais qui vaudra toujours $\sqrt{-1}$, ainsi  que de nombreuses fonctions, comme par exemple le projeté, la racine carrée, le conjugué, le cosinus, le sinus, la tangente, la puissance, etc. Voici un exemple qui converti un complexe de sa forme cartésienne en sa forme polaire.

```c
#include <stdio.h>
#include <complex.h>

int main(void)
{
    double complex z = -4.4 + 3.3 * I;
    double radius = cabs(z);
    double argument = carg(z);

    double x = creal(z);
    double y = cimag(z);

    printf("cartesien(x, y) : (%f, %f)\n", x, y);
    printf("polaire(r, theta) : (%f, %f)\n", radius, argument);
    return 0;
}
```

### Le mot-clef ```inline``` ###

Ce mot-clef permet de remplacer les macros dans un certain nombre de cas. En effet, nous avons vu dans le chapitre sur le préprocesseur que les macros peuvent provoquer des effets de bord indésirables et qu'elles ne vérifient absolument pas les types. En ajoutant inline devant la déclaration d'une fonction, on demande au compilateur de remplacer l'appel de la fonction par son corps, exactement comme les macros, mais tout en gardant les avantages des fonctions. Le code suivant illustre ce qui se passe.

```c
inline unsigned int abs(int x)
{
    return (x < 0) ? -x : x;
}

int f(int x)
{
    int var = abs(x);
}

/* Le compilateur transformera le code en ceci : */

int f(int x)
{
    int var = (x < 0) ? -x : x;
}
```

Il y a tout de même quelques restrictions. Tout d'abord, il faut toujours définir une fonction ```inline``` dans un fichier d'en-tête (ce sont les seules fonctions que l'on doit définir dans un fichier d'en-tête, toutes les autres doivent être définies dans les fichiers sources). Enfin, rien ne force le compilateur à remplacer l'appel de la fonction par son corps. Ce mot-clef informe le compilateur mais ne le force absolument pas et il ne le fera que s'il le peut.

### Le mot-clef ```restrict``` ###

Ce mot-clef permet de définir ce que l'on appelle des **pointeurs restreints**. Un pointeur définit comme restreint est le seul à pointer sur une certaine zone mémoire. Cela permet au compilateur de faire des optimisations, mais tout comme ```inline```, le compilateur peut l'ignorer. Vous trouverez un tutoriel qui présente ce mot-clef et la solution qu'il apporte à certains problèmes de mémoire et de données [ici](http://progdupeu.pl/tutoriels/45/aliasing-et-pointeurs-restreints/).

### Mélange déclaration / code ###

En C90, il est obligatoire de déclarer toutes ses variables au début du bloc d'instruction courant. En C99, cette règle est abolie et on peut déclarer ses variables où on veut. Pour certains, cela augmente la lisibilité du code puisqu'on déclare les variables juste avant leur utilisation. Pour d'autre, cela y nuit puisqu'on mélange les déclarations et le code. C'est à vous de choisir si vous utiliserez cette modification de la syntaxe ou non.

```c
int main (void)
{
   printf ("Hello world!\n");
   int i = 10;
   printf ("i = %d\n", i);
   return 0;
}
```

Dernier point : maintenant on peut déclarer une variable temporaire pour la boucle ```for```. Celle-ci disparait à la fin de la boucle.

```c
for (size_t i = 0; i < 10; ++i)
{
    /* Ici, i existe. */
}
/* Ici, i n'existe plus. */
```

### Les VLA ###

Les tableaux à taille variable, de l'anglais **Variable Length Array**, sont des tableaux dont la taille peut être définie par une variable. Jusqu'à maintenant, la taille devait impérativement être connue à la compilation, sinon il fallait passer par l'allocation dynamique. Maintenant, le code suivant est parfaitement valide.

```c
void foobar(size_t n)
{
    int array[n];
    for (size_t i = 0; i < n; ++i)
    {
         array[i] = i;
    }

    /* Faire quelque chose avec le tableau. */
}
```

Cette fonctionnalité marche aussi pour les prototypes et déclarations de fonctions, à condition que la variable qui sert de taille soit définie avant le tableau.

```c
int foo(int n, int array[n]); // valide
int bar(int array[n], int n); // invalide
```

D'ailleurs, comme il n'est pas obligatoire d'écrire la taille d'un tableau "classique" lorsqu'on écrit le prototype d'une fonction, il n'est pas obligatoire de le faire dans le cas d'un VLA. Dans ce cas, il faudra juste mettre une étoile entre les crochets, comme dans l'exemple ci-dessous.

```c
int foobar(int n, int array[*]);
```

#### Les limitations de ce mécanisme ####

La première limitation et sans doute la plus importante est l'endroit où doit être stocké le tableau. Nous avons vu dans le chapitre sur l'allocation dynamique la pile pour les objets automatiques et le tas pour les objets dynamiques. Puisque c'est un tableau, il devrait en toute logique être stocké sur la pile ; c'est d'ailleurs ce que fait GCC. Le problème est que rien n'est garanti ; il se peut qu'il soit stocké sur le tas. Vous devez donc faire attention à ne pas demander une trop grande taille pour ne pas faire déborder la pile. 

La deuxième limitation est que la portée d'un VLA est limitée au fichier. Il est impossible d'utiliser dans un fichier un VLA définit dans un autre ou même de définir un VLA dont la taille est une variable externe. Les deux exemples suivants sont donc invalides.

```c
extern int n;
int a[n];
extern int b[n];
```

Troisième limitation : il est impossible de déclarer un VLA statique. Enfin, quatrième limitation, il est impossible d'utiliser un tableau à taille variable dans une structure ou une union, sauf dans un cas bien particulier.

#### Tableau incomplet dans une structure ####

Il est possible de ne pas préciser la taille d'un tableau membre d'une structure, mais celui-ci doit absolument être le dernier champ de la structure en question. De plus, on ne pourra utiliser que des pointeurs sur cette structure alloués dynamiquement. Le code suivant (tiré de [Developpez](http://nicolasj.developpez.com/articles/c99/#LIV-G)) illustre ce qu'on peut faire avec.

```c
#include <stdio.h>
#include <stdlib.h>

struct incomplet
{
    int n;
    int tab[];
};

int main (void)
{
    struct incomplet * a = malloc (sizeof(*a) + 3 * sizeof(int));
    if (a != NULL)
    {
        a->n = 3;
        for (size_t i = 0; i < a->n; i++)
        {
            a->tab[i] = i;
        }
        
        printf ("a->tab = { ");
        for (size_t i = 0; i < a->n; i++)
        {
            printf ("%d, ", a->tab[i]);
        }
        printf (" };\n");
        free (a), a = NULL;
    }

    struct incomplet * b = malloc (sizeof(*b) + 5 * sizeof(int));
    if (b != NULL)
    {
        b->n = 5;
        for (size_t i = 0; i < b->n; i++)
        {
            b->tab[i] = i;
        }
        
        printf ("b->tab = { ");
        for (size_t i = 0; i < b->n; i++)
        {
            printf ("%d, ", b->tab[i]);
        }
        printf (" };\n");
        free (b), b = NULL;
    }
    return 0;
}
```
```console
a->tab = { 0, 1, 2,  };
b->tab = { 0, 1, 2, 3, 4,  };
```

### La variable ```__func__``` ###

Cette variable contient le nom de la fonction courante. Elle est très utile pour débugger, par exemple pour connaître le nom de la fonction qui était en cours d'exécution quand le programme a planté.

### Les nombres flottants ###

Le plus gros apport de C99 concerne sans aucun doute les nombres flottants. Alors que C90 laissait dans le flou, C99 supporte la norme [IEEE 754](http://fr.wikipedia.org/wiki/IEEE_754). Comme le sujet est imposant, je vous renvoie au [tutoriel](http://web.archive.org/web/20121123125844/http://www.siteduzero.com/tutoriel-3-526564-maitrisez-les-nombres-a-virgule-en-c.html) de [Maëlan](http://progdupeu.pl/membres/voir/Maëlan) sur le sujet. En plus, celui-ci vous formera de façon approfondie aux flottants et à leurs dangers, ainsi qu'à leur bonne utilisation en C. Que demande le peuple ?

### Découvrir le C11
### La suppression de *gets* ###

Cette fonction ressemble beaucoup à *fgets* sauf qu'elle n'est pas du tout sécurisée : si on dépasse la taille du buffer, elle continue à écrire comme si de rien n'était. C11 la supprime et la remplace par la fonction *gets_s*.

```c
char * gets_s (char * restrict buffer, size_t nch);
```

### Les structures et les unions anonymes ###

Jusqu'ici, lorsqu'on déclarait une structure ou une union, elle devait obligatoirement avoir un nom, même lors d'imbrications. Avec C11, ce n'est plus obligatoire. Ainsi, la structure du chapitre précédent deviendra comme ci-dessous.

```c
enum {false, true};
typedef char bool;

struct cstring
{
    union buffer
    {
        struct { char * ptr; size_t capacity; };
        char array[32];
    };
    size_t length;
    bool is_in_ptr;
};
```

Dès lors, comment accéder aux membres de ces unions et structures anonymes ? Comme n'importe quel autre membre. Exemple ci-dessous.

```c
struct cstring var;
var.ptr = "Hello world";
var.capacity = 42;
var.length = strlen(var.ptr);
```

### Une nouvelle interface pour *fopen* ###

La fonction *fopen* peut désormais être ouverte avec un nouveau mode : ```"...x"```. Ce mode permet la création et l'ouverture du fichier en question. Si jamais le fichier existe déjà, alors la fonction échouera ; ce mode garanti donc de ne pas écraser de fichier. Ce mode se décline en quatre version. 

* ```"wx"``` : créé une fichier texte et permet d'écrire avec un accès exclusif à ce fichier.
* ```"wbx"``` : pareil, sauf qu'on créé cette fois ci un fichier binaire.
* ```"w+x"``` : créé un fichier texte avec accès exclusif et possibilité de lecture et d'écriture.
* ```"wb+x"``` : de même, sauf qu'on créé un fichier binaire.

Enfin, sachez qu'un version plus sécurisée de *fopen* fait son apparition : *fopen_s*. 

```c
errno_t fopen_s (FILE ** pFile, const char * filename, const char *mode);
```

### Les macros génériques ###

Le principe est simple : une macro générique pour les utilisateurs qui en interne appelle la bonne fonction selon le type de l'expression passée en paramètre. Un exemple sera plus parlant. Nous voulons faire la racine cubique d'un flottant. Nous avons donc *cbrtf* pour ```float```, *cbrt* pour ```double``` et  *cbrtl* pour ```long double```. La macro se présentera donc comme ci-dessous.

```c
#define cbrt(X) _Generic((X), long double : cbrtl, default : cbrt, float : cbrtf)(X)

/* Ou en version plus lisible : */
#define cbrt(X) _Generic((X), long double: cbrtl, \
                              default: cbrt, \
                              float: cbrtf)(X) \
```

Ainsi, en fonction de X, la bonne fonction sera appelée. Grâce à cette macro, on peut faire des choses amusantes, comme récupérer le type  d'une variable (bien que ce soit rarement utile) ou bien le format pour *printf*.

```c
#define TYPE_OF(var) _Generic((var), \
    int : "Entier", \
    double : "Flottant", \
    default : "Inconnu")

#define printf_dec_format(x) _Generic((x),  \
    char : "%c", \
    signed char : "%hhd", \
    unsigned char : "%hhu", \
    signed short : "%hd", \
    unsigned short : "%hu", \
    signed int : "%d", \
    unsigned int : "%u", \
    long int: "%ld", \
    unsigned long int : "%lu", \
    long long int : "%lld", \
    unsigned long long int : "%llu", \
    float : "%f", \
    double : "%f", \
    long double : "%Lf", \
    char * : "%s", \
    void * : "%p")

#define print(x) printf(printf_dec_format(x), x)
#define printnl(x) printf(printf_dec_format(x), x), puts("")
```

Pour aller plus loin, je vous encourage à lire [cet article](http://www.robertgamble.net/2012/01/c11-generic-selections.html) en anglais qui présente de façon complète ce nouveau système de macros génériques.

### Le mot-clef ```_Noreturn``` ###

Ce mot-clef se met pour préciser qu'une fonction ne retourne rien. Cela peut sembler bête à nos yeux puisque ```void``` sert déjà à indiquer que la fonction ne retourne aucune valeur. En fait, ce mot-clef servira au compilateur qui pourra optimiser le code ; sans lui, certaines optimisations sont impossibles. 

```c
 _Noreturn void foobar();
```

Vous trouverez de la documentation sur ce mot-clef sur [open-std.org](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1453.htm).

### Améliorations des complexes ###

Pour faciliter la création de nombres complexes, C11 offre trois macros très simples d'utilisation : CMPLXF pour utiliser des parties réelles et imaginaires de type ```float```, CMPLX pour ```double``` et CMPLXL pour ```long double```.

```c
double _Complex z = CMPLX(3, -2);
```

Vous pouvez en apprendre un peu plus sur le [site d'IBM](http://www.ibm.com/developerworks/rational/library/support-iso-c11/).

Finalement, le C n'est pas le vieux langage des années 1970, c'est un langage qui évolue encore aujourd'hui et qui propose des améliorations intéressantes. Malheureusement, vu le recul du C par rapport à d'autres langages dans les applications grand public, ces normes ne sont supportées complètement ou partiellement par peu de compilateur. Si vous voulez utiliser une des fonctionnalités proposée par C99 ou C11, veillez à vérifier que votre compilateur la supporte. 

Enfin, pour conclure, je vous donne une liste de quelques liens qui abordent ces normes de façon plus complète que nous ; en effet, certaines améliorations demandent des connaissances que vous n'avez pas acquises dans ce tutoriel, il aurait donc été inutile de les présenter ici.

* [Les nouveautés du C99](http://nicolasj.developpez.com/articles/c99/)
* [C's New Ease of Use](http://www.drdobbs.com/cpp/cs-new-ease-of-use-and-how-the-language/240001401?pgno=1)
* [C11: A New C Standard Aiming at Safer Programming](http://blog.smartbear.com/codereviewer/c11-a-new-c-standard-aiming-at-safer-programming/)

## Des bibliothèques par milliers
Nous avons vu une petite partie de la bibliothèque standard durant ce cours. Non seulement nous n'avons pas tout vu, mais sachez qu'il existe en plus des milliers de bibliothèques dites **tierces**, c'est-à-dire des bibliothèques qui se rajoutent par-dessus la bibliothèque standard. Il en existe une quantité indénombrable qui permettent de tout faire ou presque. Toutes les montrer serait impossible et surtout inutile, donc nous en avons choisis quelques unes des plus connues. Nous ne ferons que les présenter ; si vous voulez les utiliser, il faudra apprendre par vous-mêmes en lisant la documentation, ou si vous avez de la chance, d'autres tutoriels.

### Le reste de la bibliothèque standard
La bibliothèque standard que propose le langage C est toute petite comparée à certains langages comme Java, et pourtant, nous sommes loin d'en avoir fait le tour. Ce petit sous-chapitre a pour but de vous montrer quelques-uns des fichiers d'en-têtes les plus utilisés en C. Sachez néanmoins que même en limitant le nombre de fichiers que nous allons montrer, il n'est pas possible d'être exhaustif. Voilà pourquoi je vous encourage à continuer vos recherches sur la bibliothèque standard par vous mêmes par la suite. [Wikipédia](http://en.wikipedia.org/wiki/C_standard_library) et [cplusplus.com](http://www.cplusplus.com/reference/clibrary/) sont de bons départs.

### ```<assert.h>``` - Intercepter les erreurs de programmation ###

Ce fichier d'en-tête est tout simple : il ne contient qu'une seule macro : ```assert```, qui signifie assertion. Qu'est ce qu'une assertion ? C'est une évaluation d'une condition qui, si jamais elle se révèle fausse, quitte le programme. Cela permet d'intercepter les erreurs de programmation mais pas les erreurs d'utilisation ou d'exécution. Voilà pourquoi les assertions ne sont utiles que lors des phases de test et sont désactivées lorsque cette phase est terminée.

Pour l'utiliser en C, il suffit de faire ```assert(condition)``` : si celle-ci est vraie, alors le programme continue normalement ; si elle est fausse, on affiche un message comme celui ci-dessous.

```console
Assertion failed: expression, file f, line x
```

Voici un exemple de code en apparence correct mais qui comporte un problème (exemple tiré du [site](http://www.bien-programmer.fr/notes.php#assert) de Emmanuel Delahaye) : il affiche une valeur en trop.

```c
#include <stdio.h>

static void afficher (int const t[], size_t n)
{
    size_t i;
    for (i = 0; i <= n; i++)
    {
        printf ("%d", t[i]);
    }
    puts("");
}

int main (void)
{
    int tab[] = {1, 2, 3, 4};
    afficher (tab, sizeof(tab) / sizeof(*tab));
    return 0;
}
```
```console
1 2 3 4 2
```

On décide donc de tester la validité de l'itérateur grâce à notre macro.

```
static void afficher (int const t[], size_t n)
{
    size_t i;
    for (i = 0; i <= n; i++)
    {
        assert(i < n);
        printf ("%d", t[i]);
    }
    puts("");
}
```
```console
1   2   3   4 Assertion failed: i < n, file main.c, line 10

This application has requested the Runtime to terminate it in an unusual way.
Please contact the application's support team for more information.

Press ENTER to continue.
```

On se rend compte que l'itérateur a dépassé la taille maximale du tableau ; on comprend donc qu'il faut remplacer ```i <= n``` par ```i < n```. En exécutant de nouveau le programme, l'affichage sera cette fois correct.

Une fois que l'on a fini de tester le programme et qu'on veut le distribuer, on doit désactiver toutes les assertions. Et au lieu de tout supprimer à la main, nous avons un moyen très simple : il suffit de définir la macro ```NDEBUG```. En effet, si cette macro est définie, alors les assertions ne feront absolument rien. Et si jamais un problème est découvert, il suffit de supprimer cette macro pour réactiver les assertions.

### ```<ctype.h>``` - Test sur les caractères ###

Cet en-tête définit tout un tas de macros permettant de savoir si le caractère à tester est un chiffre, une lettre, s'il est considéré comme un caractère imprimable, etc. Il fournit également deux macros permettant de convertir une minuscule en majuscule et vice-versa. Chaque macro fait appel à une fonction qui prend un caractère en paramètre et renvoie 0 si la condition testée et fausse, une autre valeur si elle est vraie. En voici la liste avec une brève explication.

* ```isalnum``` : teste si le caractère est un chiffre, une majuscule ou une minuscule.
* ```isalpha``` : teste si le caractère est une lettre de l'alphabet latin.
* ```iscntrl``` : teste si le caractère est un caractère dit **de contrôle**, c'est à dire l'inverse d'un caractère dit **imprimable**. Parmi eux, on compte le retour à la ligne et la tabulation.
* ```isdigit``` : teste si le caractère est un chiffre.
* ```isgraph``` : teste si le caractère a une représentation graphique. Tous les caractères imprimables en ont une à l'exception de l'espace.
* ```islower``` : teste si on a affaire à une minuscule.
* ```isprint``` : teste si un caractère est imprimable.
* ```ispunct``` : teste si le caractère est un signe de ponctuation.
* ```isspace``` : teste si le caractère est un *white-space character*, à savoir ```' '```, ```'\t'```, ```'\n'```, ```'\v'```, ```'\f'``` ou ```'\r'```.
* ```isupper``` : teste si on a affaire à un majuscule.
* ```isxdigit``` : teste si le caractère est un chiffre hexadécimal, c'est à dire s'il fait partie de cette liste : ```0 1 2 3 4 5 6 7 8 9 a b c d e f A B C D E F```.
* ```tolower``` : convertit une lettre majuscule en minuscule ; ne fait rien si déjà en minuscule.
* ```toupper``` : convertit une lettre minuscule en majuscule ; ne fait rien si déjà en majuscule.

### ```<limits.h>``` - Connaître les limites des types entiers ###

Nous le savons, les types entiers ont une taille minimale et une taille maximale pour les valeurs qu'ils peuvent prendre. Nous le savons aussi, ces limites dépendent de l'implémentation. Ce fichier d'en-tête sert donc à fournir à tous les utilisateurs une liste de macros pour connaître les limites de chaque type, même si en interne les valeurs changent en fonction de l'environnement.

### ```<float.h>``` - Limites des flottants et de ce qui les concerne ###

Cet en-tête donne les limites des types flottants, mais en plus de tout ce qui se rapporte à eux : la mantisse, l'exposant, l'arrondi utilisé, etc. Très utile pour une gestion poussée des flottants, surtout avec C99.

### ```<stddef.h>``` - Définition d'alias ###

Ce fichier d'en-tête contient la définition de ```size_t``` et de ```ptrdiff_t```. Nous connaissons le premier mais pas le second. C'est un alias qui permet de représenter la différence de deux pointeurs. Vous aurez sans doute moins l'occasion de l'utiliser que ```size_t``` mais il est utile de le connaître. Ce fichier est en tout cas très utile quand vous n'avez besoin de rien d'autre que ces deux alias.

### ```<stdint.h>``` - Définitions d'entiers spéciaux et leurs limites (C99) ###

Il arrive que l'on veuille un entier qui fasse précisément 8 bits ou 32 bits par exemple. Comment faire puisque la taille d'un type peut varier selon l'implémentation ? C'est ce que propose ce fichier d'en-tête avec les ```intx_t``` (où x vaut 8, 16, 32 ou 64) et leur pendant non-signé ```uintx_t```. Mais ce n'est pas tout. Il nous propose également un type ```intmax_t``` (ainsi que ```uintmax_t```) qui est le plus grand entier que le système propose, ainsi qu'un type ```intptr_t``` (```uintptr_t```) qui permet de représenter une adresse ; on peut convertir une adresse ```void*``` en une adresse ```intptr_t``` et vice-versa sans perte.

Ce fichier contient également les limites de tous ces types, ainsi que celles d'autres types comme ```size_t``` ou ```ptrdiff_t``` par exemple.

### Les bibliothèques tierces
### Les bibliothèques pour 2D ###
#### SDL - Simple DirectMedia Layer ####

![Logo de la SDL](http://uploads.siteduzero.com/thb/373001_374000/373384.png)

La [SDL](http://www.libsdl.org) est une bibliothèque multimédia employée pour créer des applications multimédias comme des émulateurs, des jeux vidéos 2D ou des lecteurs audio par exemple. Elle peut même être utilisé conjointement avec une bibliothèque 3D. Elle permet un accès de bas niveau à l'audio, au clavier, à la souris, au joystick, à la gestion du temps et bien d'autres choses encore. Elle est portable sur de très nombreux systèmes différents. Elle est gratuite et libre d'utilisation et de modification de par sa licence *GNU LGPL version 2*.

Voici une capture d'écran du jeu [Mini Slug Project](http://fr.openclassrooms.com/forum/sujet/jeucsdl-mini-slug-project-84292) par [joe78](http://fr.openclassrooms.com/membres/joe78-72216).

![Aperçu du jeu Mini Slug Project](http://uploads.siteduzero.com/files/372001_373000/372183.png)

#### SFML - Simple and Fast Multimedia Library ####

![Logo de la SFML](http://upload.wikimedia.org/wikipedia/fr/f/f3/Sfml-logo.png)

La [SFML](http://www.sfml-dev.org/index-fr.php) est une bibliothèque graphique originalement développée en C++ mais utilisable en C en autres. Elle fournit elle aussi l'accélération matérielle. Elle diffère de la SDL en ce qu'elle est divisée en modules : Système, Fenêtre, Graphique, Son et Réseau. Son plus grand avantage est qu'elle est développée par un français et donc possède une documentation dans la langue de Molière ainsi que de nombreux tutoriels. Ci-dessous, un exemple de jeu réalisable avec la SFML.

![Arkanoid - The revival](http://uploads.siteduzero.com/files/253001_254000/253764.jpg)

### Les bibliothèques pour la 3D ###
#### OpenGL - Open Graphics Library ####

![Logo d'OpenGL](http://uploads.siteduzero.com/thb/373001_374000/373189.jpg)

[OpenGL](http://www.opengl.org) est une bibliothèque multimédia qui permet de développer des applications aussi bien en 2D qu'en 3D. Elle est portable, libre et gratuite. OpenGL est la version libre de l'avant-dernière version de GL (si par exemple GL en est à la version 2.3, OpenGL en est à la version 2.2). Cette bibliothèque permet de tirer profit de l'accélération 3D des cartes graphiques. 

OpenGL est une bibliothèque bas-niveau qui ne traite que des rendus graphiques et ne gère pas les animations, le temps, les fenêtres, etc. C'est pour cette raison que OpenGL est utilisé conjointement avec une autre bibliothèque, comme la SDL, qui sert à créer une fenêtre dans laquelle OpenGL va travailler, à recevoir des entrées clavier, etc. Il faut quelques connaissances en mathématiques pour l'utiliser (pour les matrices par exemple).

Certains jeux connus utilisent OpenGL, comme [Xonotic](http://www.xonotic.org/) ou encore le fameux [Quake 3](http://www.quake3arena.com/).

![Capture d'écran de Quake 4 qui utilise lui aussi OpenGL](http://uploads.siteduzero.com/thb/373001_374000/373387.jpg)

#### DirectX ####

![Logo de DirectX](http://uploads.siteduzero.com/thb/373001_374000/373193.jpg)

[DirectX](http://directx.softonic.fr) est une collection de bibliothèques destinée au multi-média et particulièrement aux jeux vidéos. Elle est développée par Microsoft, elle ne marche donc que sur Windows et Xbox. DirectX permet de gérer non seulement la 3D, mais aussi la 2D, les entrées (clavier, souris, joysticks), le réseau, le son, les vidéos et bien d'autres choses. C'est la bibliothèque favorite de beaucoup de studios, et c'est l'une des raisons pour laquelle la majorité des jeux vidéos commercialisés ne sont jouables que sous Windows.

Il faut cependant faire attention aux différentes versions de DirectX, les toutes dernières n'étant plus supportées par les systèmes les plus anciens : DirectX 10 n'est supportée que par Vista et Seven.

### Les bibliothèques pour le son ###

![Logo de FMOD](http://uploads.siteduzero.com/thb/373001_374000/373351.png)

[FMOD](http://www.fmod.org) est une bibliothèque très puissante de gestion du son, utilisée par de très nombreux jeux commerciaux. Plus de 10 systèmes d'exploitations sont supportés, de Windows à GNU/Linux, en passant par la Wii et la PS3. FMOD est gratuite pour une utilisation personnelle et non commerciale. Si l'envie vous prend de vendre un logiciel qui utilise FMOD, vous devrez dépenser quelques milliers de dollars.

### Bibliothèques pour faire des applications graphiques ###
#### API Windows ####

![Logo de l'API Windows](http://uploads.siteduzero.com/thb/373001_374000/373359.png)

L'API Windows est conçue pour les langages de programmation C et C++ et est la manière privilégiée pour une application d'interagir avec les systèmes d'exploitation Windows. Une API, comme son nom l'indique, est une interface de programmation : elle contient un ensemble de fonctions bas niveau permettant de programmer des applications haut niveau. Elle permet d'interagir avec Windows de manière poussée : récupération des informations sur le système (version, nombre de processeurs, taille de la RAM, etc), création de fenêtres et d'utilitaires (pratique car les programmes ainsi créés ressembleront aux autres programmes Windows), accès au shell, aux services réseaux, etc.

Il existe plusieurs version de cette bibliothèque :

* **Win16** était la première API pour les versions 16-bits du système.	
  * **Win32** est la version 32-bits de l'API pour les systèmes plus récents.
* **Win32s** est une extension de Win32 pour les systèmes Windows 3.x qui a été introduite comme sous-ensemble de Win32. Le "s" est pour sous-ensemble (*subset* en anglais).
* **Win32 pour les éditions 64 bits** précédemment appelée Win64 est la version pour les ordinateurs 64-bits, avec les versions Windows XP Professional x64 Edition pour les processeurs x86-64 ainsi que Windows XP 64-bit Edition et Windows Server 2003 pour les processeurs Itanium. Cette version apporte juste le support pour ces deux nouvelles plateformes.

#### Xlib ####

![Logo de Xlib](http://uploads.siteduzero.com/files/373001_374000/373363.png)

La bibliothèque Xlib réalise l'interfaçage entre le protocole X et les applications X. Elle contient des fonctions de bas niveau pour interagir avec un serveur X. Peu d'applications utilisent la Xlib directement ; en général, elles exploitent d'autres bibliothèques qui reposent sur la Xlib pour fournir des éléments d'une interface graphique. En utilisant Xlib, nous pouvons gérer les tâches suivantes : 

* la gestion des fenêtres ;
* le texte : fontes, tailles, styles, etc ;
  * le graphisme : fonctions de dessin 2D ;
  * la couleur ;
  * les communications avec le serveur ;
  * la gestion des évènements et des erreurs (coupures réseau, etc ...) ;
* et bien d'autres choses encore.

X11 ou simplement X est un environnement graphique de type « fenêtré » qui gère l'interaction homme-machine par l'écran, la souris et le clavier de certains ordinateurs en réseau. Les célèbres bibliothèques GTK et Qt sont basées sur X.

#### Gtk+ ####

![Logo de Gtk+](http://uploads.siteduzero.com/thb/373001_374000/373371.png)

GTK+ est une bibliothèques permettant de réaliser des interfaces graphiques. Cette bibliothèque a été développée originellement pour les besoins du logiciel de traitement d'images The GIMP. GTK+ est maintenant utilisé dans de nombreux projets, dont les environnements de bureau GNOME, Xfce et ROX. GTK+ est un projet libre (licence GNU LGPL 2.1), gratuit et multiplate-forme.

### Autres bibliothèques ###
#### GMP ####

GMP est une bibliothèque de calcul précis sur des très grands nombres comme $4242^{6014}$, le tout rapidement. Les principaux domaines d'applications de GMP sont la recherche et les applications en cryptographie, les logiciels applicatifs de sécurité pour Internet et les systèmes de calcul formel. Par exemple, le célèbre [chiffrement RSA](http://fr.wikipedia.org/wiki/Chiffrement_RSA) utilise la bibliothèque GMP afin de gérer de grands nombres.

GMP est notamment utilisée dans le logiciel de calcul formel Maple à partir de la version 9 et Mathematica depuis la version 5.

*[API] : Application Programming Interface
*[Gtk+] : The GIMP Toolkit
*[GMP] : GNU Multiple Precision

Au cours de votre route, vous croiserez des centaines de bibliothèques différentes. Vous n'aurez pas toujours le luxe d'avoir un tutoriel dessus, il faudra donc se reposer sur la documentation et éventuellement les ressources Internet. Nous avons essayé de vous inculquer ce réflexe tout au long de ce tutoriel et nous vous encourageons d'ailleurs à continuer vos recherches pour approfondir vos connaissances sur la bibliothèque standard. Vous serez d'ailleurs étonnés qu'au fil des ans on continue toujours à découvrir, voire rédécouvrir, de nouvelles choses sur le C ou sa bibliothèque standard. Comme quoi, le C ne finira jamais de surprendre !

Sachez qu'il vous reste encore beaucoup à apprendre sur le C ; en fait, personne ne peut se vanter de maîtriser complètement le C. N'hésitez donc pas à poursuivre vos recherches, approfondir ce que nous avons vu, mais également découvrir d'autres surprises que le C vous cache encore !

Ainsi s'achève ce tutoriel, mais pas votre parcours dans le monde de la programmation. En effet, même si vous avez appris certaines choses, vous ne connaissez pas tout : le C est un langage fabuleux qui réserve bien des surprises. Pour continuer votre apprentissage, je vous donne quelques conseils ci-dessous.

* **Soyez curieux** : fouillez sur Internet pour découvrir de nouvelles méthodes, approfondissez celles que vous connaissez, renseignez-vous, testez de nouveaux outils, etc.
* **Codez et lisez du code** : entrainez-vous, c'est le seul moyen de progresser. Faites des projets qui vous tiennent à cœur, implémentez des algorithmes connus, faites des exercices, des défis et [exercez-vous](http://www.france-ioi.org/index.php). Pensez aussi à visiter les forums et à lire le code des autres, découvrez comment ils procèdent, apprenez d'eux de nouvelles techniques ou façon de faire, progressez en suivant leurs conseils.
  * **Cherchez toujours à en savoir plus** : la programmation est un monde merveilleux où l'on en apprend un peu plus chaque jour, sans jamais s'arrêter. Lisez des tutoriels pour découvrir de nouveaux points. Lisez des codes pour découvrir de nouvelles façons de faire. Expérimentez.
* Et surtout le plus important, **amusez-vous** !

### Remerciements ###

Avant de conclure, les auteurs aimeraient remercier plusieurs personnes :

* **Pouet_forever** et **SofEvans** pour le soutien apporté à la rédaction dans les débuts ;
* toute l'équipe de PDP ;
* tous ceux qui au fil du temps et de la rédaction nous ont apporté leurs avis, leurs conseils, leurs points de vue et qui nous ont aidé à faire de ce tutoriel ce qu'il est aujourd'hui ;
* et surtout vous, lecteurs !

Bon courage dans votre apprentissage, car la route est infinie mais pleine de satisfactions !
