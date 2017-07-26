Title: Trouver et supprimer les goulots d'étranglement en Erlang
Order: 9
Date: 2014-09-27
Slug: trouver-et-supprimer-les-goulots-detranglement-en-erlang
Author: Black
Display: true

[TOC]

## Introduction

Implanter des systèmes distribués est une tâche complexe qui requiert de bons outils et une bonne méthode afin que ces systèmes puissent passer à l'échelle.

Nous verrons comment réaliser un [Two-phase commit](http://en.wikipedia.org/wiki/Two-phase_commit_protocol) en Erlang et comment, en deux itérations, nous pouvons le rendre plus performant.

## Erlang

[Erlang](http://www.erlang.org/) est un langage de programmation fonctionnel basé sur le modèle à acteur, développé par Ericsson, afin de pouvoir construire des systèmes distribués et fiables. Erlang était destiné au domaine des télécommunications.

### Modèle à acteur

Le [modèle à acteur](http://en.wikipedia.org/wiki/Actor_model) est une approche qui vise à concevoir un système sous la forme d'un ensemble de **processus** concurrents.

Ces processus sont nommés **Acteur**s et lls communiquent par envoi de messages (*ou [message passing](http://en.wikipedia.org/wiki/Message_passing)*).

Chaque acteur est l'unique propriétaire de ses propres données et il possède une messagerie comme point d'entrée où sont stockés les messages qui lui sont adressés et qu'il traitera par *ordre d'arrivée*.

### Programmation fonctionnelle

La programmation fonctionnelle est à opposer à la programmation procédurale : il s'agit d'exprimer les relations entre les données plutôt que de décrire l'ordre des traitements qui leur seront appliqués.

Le point principal à retenir est que les modifications de variables sont impossibles et, de ce fait, les boucles sont simulées par récursion. De plus, pour pouvoir représenter la progression d'un taitement, il faut impérativement construire une [machine à états finis](http://en.wikipedia.org/wiki/Finite-state_machine).

### Machine virtuelle

De la même manière que les programmes JAVA et C\# sont compilés vers du *[bytecode](http://en.wikipedia.org/wiki/Bytecode)*, pour être exécutés par une machine virtuelle, respectivement la JVM et la CLR. Les programmes Erlang sont compilés vers un format BEAM pour être exécutés par le *Erlang runtime system*.

L'avantage de ce système est que la gestion des serveurs et des nœuds du système (ainsi que tous les aspects de gestion de pannes et de répartition de charge) soit confiée à la machine virtuelle et non au programme, ce qui le simplifie grandement.

Tous ces aspects font que la machine virtuelle est en mesure de répartir la charge et les acteurs en fonction de leur communication, ce qui assure un passage à l'échelle quasi-linéaire, pour peu que le système ne comporte pas de problème de goulots d'étranglement.

## Two-phase commit

Le Two-phase commit est un protocole utilisé pour permettre un consensus distribué, ici nous cherchons à garantir la cohérence des données d'un système.

Pour les besoins de notre étude, nous allons implanter un Two-phase commit dans le cadre d'une gestion de comptes bancaires, de la manière suivante :

-   Il y aura un **Coordinateur** chargé de relier les différentes banques entre elles.
-   À cette fin, les **Banques**, lors de leur création, vont se déclarer au **Coordinateur**.
-   Un **Client** s'inscrira alors auprès d'une **Banque** qui lui ouvrira un compte créditeur de 10 unités.
-   Le **Client** fera, auprès de sa **Banque**, une demande de transfert d'une unité vers un autre **Client**.
-   La **Banque** transmettra cette demande au **Coordinateur**.
-   Le **Coordinateur** contactera toutes ses **Banques** pour savoir laquelle gère le compte du bénificiaire.
-   La **Banque**, gestionnaire du compte du **Client** destinataire, répondra au **Coordinateur**.
-   Le **Coordinateur** demandera à la **Banque** du **Client** émetteur de s'assurer qu'il dispose de suffisament d'argent pour effectuer le virement.
-   Le **Coordinateur** effectuera un **commit** en émettant deux demandes d'actions : respectivement ajouter et retirer une unité.
-   Si la **Banque** du **Client** émetteur ne possède plus suffisament d'unités, elle le signalera au **Coordinateur**.
-   Le **Coordinateur** émettra alors une demande de **rollback** auprès de la **Banque** du destinataire qui lui retirera une unité.

![Le Coordinateur est le point central, il mène les transactions](http://progdupeu.pl/media/galleries/62/922c3375-ff0f-46c7-bd47-212a71fb1279.png)

## Méthodologie de suppression des goulots d'étranglement

Pour supprimer les goulots d'étranglement, il faut chercher les acteurs qui ont beaucoup de données ou qui reçoivent beaucoup de messages et en extraire une responsabilité dans un nouvel acteur.

## Itérations

En partant de ce concept, trois versions, détaillées ci-dessous, ont été dérivées.

Toutes les sources se trouvent à cette adresse : [https://github.com/blackheaven/bottleneck-buster](https://github.com/blackheaven/bottleneck-buster).

### Itération 1 : Approche naïve

Comme son nom l'indique, il s'agit juste d'une implantation brute de l'algorithme.

Les sources de la version se trouvent dans le répertoire [dirty](https://github.com/blackheaven/bottleneck-buster/tree/master/dirty).

### Itération 2 : Extraction de la transaction

Le but ici est de décharger le **Coordinateur**, qui était devenu le goulot d'étranglement du système, du fait qu'il conduisait toutes les transactions, en créant un acteur chargé de gérer une **Transaction**.

Le rôle du **Coordinateur** se limite à trouver la **Banque** du **Client** destinataire.

Qui plus est, la **Transaction** est en mesure de se relancer par elle-même, en cas d'échec.

![La Transaction se gère de manière autonome, elle communique beaucoup avec les Banques](http://progdupeu.pl/media/galleries/62/8c5d2765-de94-41df-81c2-239a47dba755.png)

Les sources de la version se trouvent dans le répertoire [clean](https://github.com/blackheaven/bottleneck-buster/tree/master/clean).

### Itération 3 : Extraction du Compte client

Le but ici est de décharger les **Banques**, devenues, à leur tour, le goulot d'étranglement du système, car elles géraient tous les mouvements bancaires, par la création d'un acteur chargé de la gestion d'un
**Compte client**.

Le rôle de la **Banque** se borne à trouver les **Comptes clients**.

![Les Transactions communiquent directement avec les Comptes clients, ce qui permet d'éviter les banques](http://progdupeu.pl/media/galleries/62/5c6a632e-c1e7-48d9-8232-0c09cb86cf48.png)

Les sources de la version se trouvent dans le répertoire [extreme](https://github.com/blackheaven/bottleneck-buster/tree/master/extreme).

## Bilan

### Comparaison des performances

Pour comparer les performances, nous allons utiliser le module `sim` qui se chargera de créer un **Coordinateur** et un nombre paramétrable de **Banques** et de **Clients** par **Banque**.

Puis, pour générer un nombre suffisant de **Transactions**, le module va ordonner, pour chaque **Client**, un transfert vers tous les autres **Clients**.

Pour ce faire, dans le Shell d'Erlang (lancé via `$ erl`) nous entrerons
les commandes suivantes :

    Erlang R16B03 (erts-5.10.4) [source] [smp:2:2] [async-threads:10] [kernel-poll:false]

    Eshell V5.10.4  (abort with ^G)
    1> c(coordinator). c(bank). c(client). c(sim).
    {ok,coordinator}
    2> c(bank). c(client). c(sim).
    {ok,bank}
    3> c(client). c(sim).
    {ok,client}
    4> c(sim).
    {ok,sim}
    5> sim:run(1,1). % Préchauffe
    ok
    6> timer:tc(sim, run, [5, 10]). % Crée 5 banques avec 10 clients par banque
    {470612,ok} % Temps en µs

Pour chaque mesure, 3 lancements successifs ont été réalisés et la moyenne obtenue donne le résultat reporté.

Tous les tests ont été réalisés à l'aide d'un ordinateur doté d'un **i7 870 @ 2.93 GHz** avec l'**HyperThreading activé**, ce qui représente **8 cœurs logique**, ainsi que **16 Gio** de mémoire vive.

L'ordinateur tourne sous **FreeBSD 9.2-AMD64 GENERIC** et Erlang est en version **16.b.03**.

#### Comparaison par itération et nombre de clients/banques
Il s'agit de mettre en évidence la capacité du système à gérer d'avantage de demandes avec un nombre fixe de ressources, pour observer si sa montée en charge est linéaire ou non.

Chaque **ligne** représente le nombre de **Banques** et chaque **colonne** le nombre de **Clients par Banque**.

Chaque **cellule** indique le résultat en **millisecondes**.

##### Itération 1 : Approche naïve

    \# | 2 |        4 |     6 |     8 |     10
    --- | --- | --- | --- | --- | ---
    **1** | 0 | 0 | 0 | 1 | 3
    **2** | 0 | 1 | 5 | 16 | 37
    **3** | 1 | 5 | 24 | 84 | 231
    **4** | 2 | 18 | 105 | 342 | 931
    **5** | 3 | 54 | 241 | 1021 | 2740

##### Itération 2 : Extraction de la transaction

    \# | 2 |        4 |     6 |     8 |     10
    --- | --- | --- | --- | --- | ---
    **1** | 0 | 0 | 0 | 1 | 2
    **2** | 0 | 1 | 2 | 3 | 6
    **3** | 0 | 1 | 3 | 7 | 17
    **4** | 1 | 2 | 6 | 16 | 30
    **5** | 1 | 4 | 11 | 27 | 49


##### Itération 3 : Extraction du Compte client

    \# | 2 |        4 |     6 |     8 |     10
    --- | --- | --- | --- | --- | ---
    **1** | 0 | 0 | 1 | 1 | 1
    **2** | 0 | 1 | 1 | 2 | 4
    **3** | 1 | 1 | 2 | 5 | 10
    **4** | 1 | 2 | 5 | 11 | 24
    **5** | 1 | 3 | 9 | 21 | 50

On constate que le fait d'avoir extrait la **Transaction** a augmenté drastiquement les performances, puisqu'on observe des performances jusqu'à **60 fois supérieures**.

En revanche, l'écart n'est pas significatif pour l'extraction du **Compte client**, mais nous pouvons pondérer ceci par le fait que les échelles de temps étant tellement faibles, le moindre événement système peut fausser les résultats. Il faudrait comparer avec un jeu d'essais plus importants.

#### Comparaison par nombre de cœurs alloués

Il s'agit de mettre en évidence la capacité du système à gérer d'avantage de demandes avec un nombre fixe de ressources, pour observer si sa montée en charge est linéaire ou non.

Chaque **ligne** représente le nombre de **Banques** et chaque **colonne** le nombre de **Clients par Banque**.

Il s'agit de mettre en évidence la capacité du système à gérer une demande fixe (**8 Banques avec 10 Clients chacune**) avec un nombre croissant de ressources, pour observer sa capacité à passer à l'échelle.

Chaque **ligne** représente une itération et chaque **colonne** le nombre de **cœurs CPU alloués**.

Chaque **cellule** indique le résultat en **millisecondes**.

    \#  |   1  |    2  |    3  |    4  |    5  |    6  |    7  |    8
    --- | --- | --- | --- | --- | --- | --- | --- | ---
    **1** | 1 | 14 | 76 | 272 | 793 | 2152 | 4105 | 8019
    **2** | 1 | 3 | 7 | 13 | 25 | 44 | 90 | 168
    **3** | 1 | 4 | 8 | 16 | 30 | 60 | 75 | 190


![Benchmark des trois itérations, pour 8  banques et 10 clients par banque](http://progdupeu.pl/media/galleries/62/d72b69ec-2c27-45ea-aa57-69f5e474510a.png)

Les remarques sont les mêmes qu'à la section précédente : on constate que la perte en performances (par rapport à un gain linéaire en performances), due à l'ajout de ressources, est jusqu'à **70 fois moindre** pour les itérations 2 et 3.

De la même manière, on ne constate pas de différences flagrantes entre les deux dernières itérations.

### Comparaison de la taille des codes

Ici, nous tentons de déterminer si l'accroissement de la vitesse du système et de sa capacité à passer à l'échelle ne s'est pas fait au détriment d'un ajout de complexité dans le-dit système.

Nous allons donc comparer le nombre de lignes de code non-vides nécessaires à chaque acteur.

Chaque **ligne** représente une itération et chaque **colonne** un acteur.

Chaque **cellule** indique le **nombre de lignes de code**.

    \#  |   Coordinateur  | Banque  |       Client  |       Transaction  |  Compte client  |        Total
    --- | --- | --- | --- | --- | --- | --- | --- | ---
    *1* |   44 |    76 |    23 |    - |     - |     143
    *2* |   14 |    76 |    15 |    27 |    - |     132
    *3* |   14 |    39 |    15 |    29 |    28 |    125


Le système a vu son nombre de lignes diminué de plus de 10%, ce qui implique une simplification de celui-ci. De plus, le nombre moyen de lignes par acteur est, lui, passé de 48 à 25, ce qui indique une diminution de près de la moitié, rendant ainsi les acteurs plus simples, plus compréhensibles et donc plus maintenables.

## Conclusion

Nous avons vu qu'Erlang nous permettait de construire, simplement et rapidement, des systèmes concurrents et distribués : cela s'avère utile pour tester des protocoles et des architectures.

Nous avons vu que la diminution du nombre de données par acteur et leur simplification augmentait la capacité du système à passer à l'échelle.

### Notes

Toutes les sources se trouvent à cette adresse : [https://github.com/blackheaven/bottleneck-buster/](https://github.com/blackheaven/bottleneck-buster/).

Cette étude n'a pas pris en compte toute une partie de la détection des goulots d'étranglement basée sur le profiling car La [documentation officielle](http://www.erlang.org/doc/efficiency_guide/profiling.html) présente un certain nombre d'outils qui ne permettent de mettre en valeur que les sous-fonctions consommant le plus de ressources CPU, comme tous les outils de profiling de langages standard. Cette approche n'est plus pertinente\* dans ce genre de systèmes où des métriques, comme le nombre de ressources consommées par acteur, le nombre de messages envoyés et reçus par acteur ainsi que son nombre de liens (nombre d'acteurs auxquels il a envoyé un message ou qui lui en ont envoyé un), sont plus utiles pour trouver les goulots d'étranglement.

\* Cependant, une [intervention](http://www.erlang-factory.com/conference/SFBay2013/speakers/AlexanderGounares) faite par [Concurix](http://concurix.com/home) lors du [Erlang Factory SF Bay Area 2013](http://www.erlang-factory.com/conference/SFBay2013/) durant laquelle a été présenté un [outil de visualisation graphique des goulots d'étranglement](http://www.youtube.com/watch?v=GyHXLIHtPDM&feature=youtu.be&t=19m40s) qui semble plus adapté à la recherche de goulots d'étranglement. Malheureusement, le-dit outil comporte deux parties : une partie à installer en local (nommée [concurix\_runtime](https://github.com/Concurix/cx_runtime)) et une autre partie hébergée sur les serveurs de Concurix, désactivée suite à un changement d'API, mais qui sera, après un échange de courriels avec Concurix, remise en place dans les prochains mois.

## Pour aller plus loin
Nous avions vu plus haut que les deux dernières itérations étaient tellement efficaces que leurs performances ne pouvaient pas être appréciées sur un si petit échantillon (**8 Banques avec 10 Clients chacune**) et surtout pas en présence de la première itération, il est temps de muscler notre jeu.

### Comparaison par nombre de cœurs alloués

Il s'agit de mettre en évidence la capacité du système à gérer d'avantage de demandes avec un nombre fixe de ressources, pour observer si sa montée en charge est linéaire ou non.

Chaque **ligne** représente le nombre de **Banques** et chaque **colonne** le nombre de **Clients par Banque**.

Il s'agit de mettre en évidence la capacité du système à gérer une demande fixe (**15 Banques avec 1.000.000 Clients chacune**) avec un nombre croissant de ressources, pour observer sa capacité à passer à l'échelle.

Chaque **ligne** représente une itération et chaque **colonne** le nombre de **cœurs CPU alloués**.

Chaque **cellule** indique le résultat en **millisecondes**.

    \#  |   1  |    2  |    3  |    4  |    5  |    6  |    7  |    8
    --- | --- | --- | --- | --- | --- | --- | --- | ---
    **2** | 5 | 32 | 85 | 312 | 469 | 1945 | 2037 | 2053
    **3** | 4 | 18 | 40 | 103 | 512 | 1088 | 1845 | 4016


![Benchmark des deux dernières itérations, pour 15  banques et 1.000.000 clients par banque](http://progdupeu.pl/media/galleries/62/c0f6043d-cfef-4f5f-a741-9d4dc78fba99.png)

### Remarques

Nous pourrions être surpris vis-à-vis des résultats, visiblement la simplification a nuit à la capacité de notre système à passer à l'échelle.

La cause est en partie détaillé dans [cet article](http://jlouisramblings.blogspot.fr/2013/01/how-erlang-does-scheduling.html) :
comme nous l'avons vu plus haut Erlang a été conçu pour être utilisé dans le secteur des télécommunications où l'une des notions clef de ce secteur est le temps réel, Erlang a donc intégré un cadre de [Temps-réel mou](http://en.wikipedia.org/wiki/Real-time_computing). Dans cette optique chaque fois qu'un acteur reprend son fil d’exécution il se voit attribué un **budget de réductions** de 2.000. En fonction des instructions qu'il va exécuter (conditions, envois de messages, appels de fonctions), se budget va être diminué d'un coup prédéterminé en fonction de l'instruction. Une fois ce budget épuisé, l'acteur est suspendu (on dit qu'il est *préempté*) et son exécution reprendra ultérieurement.

Nous pouvons nous demander ce que cela implique pour nous lors du passage à l'échelle, la réponse est simple, un acteur à un nombre fixe d'actions qu'il peut effectuer sur une période de temps donnée, ce qui donne son débit maximal, son nombre de messages traités par unité de temps. Lorsque tous les acteurs sont sur le même cœur, ils ont grosso-modo tous le même débit, ce qui laisse le temps à notre acteur "central" (qui communique avec un grand nombre d'autre acteurs) de traiter les messages qu'il reçoit en conservant une file de messages à une taille plus ou moins fixe. En revanche, dès qu'il y a plusieurs cœurs, tous les acteurs qui envoient des messages à notre acteur central peuvent le faire en même temps, ce qui augmente le débit entrant de notre acteur central et comme nous l'avons vu, son débit maximal n'augmente pas, sa file d'attente va donc croître, ce qui va créer une **contention** dans le système. Comme si ça n'était pas suffisant, l'incapacité de notre acteur central à répondre rapidement à toutes ces demandes va causer des attentes prolongées des acteurs demandeurs, on parle alors de **famine**.

Mais le budget de réductions va plus loin, en effet, en fonction de la localisation d'un acteur (c'est-à-dire le fait qu'il soit sur le même cœur, sur un autre cœur ou sur une autre machine), l'envoi de message ne va pas avoir le même coût de réduction. Le *Erlang runtime system* va donc tenter de rapprocher les acteurs qui communiquent le plus, ce qui est problématique dans notre cas puisque tout le monde communique avec tout le monde et tout le temps. Erlang va donc passer son temps à déplacer les acteurs de cœurs en cœurs ce qui va lui faire perdre un temps considérable.

## Conclusion 2

Nous avons vu que simplifier les acteurs pouvait entraîner une perte de capacité de passage à l'échelle.

Bien que cela arrive souvent dans les systèmes réels, les causes de ces symptômes dans exemple jouet sont bien éloignées des causes que l'on trouve dans les systèmes réels, voici ces causes :

  * les opérations effectuées sont très simples (très peu coûteuses en instructions) et ne présentent que peu d'intérêt à être distribuées
  * tout le monde communique avec tout le monde et tout le temps, ce qui n'est pas le cas dans les systèmes réels où le nombre de relation est limité et où les échanges sont répartis dans le temps

La morale de cette histoire est qu'une bonne intuition ne peut pas se permettre de ne pas être confirmée par un test, lorsque l'on tente d'optimiser un système, la méthodologie est censée être la suivante :

  * conception d'une première version
  * mesures de performances
  * optimisations
  * mesures de performances
  * comparaison des mesures

Il s'agit de l'unique moyen de savoir si nous avons contribué à améliorer les performances du système ou non.

### Notes 2
Pour pallier à ce problème, Concurix a modifié le budget des réductions, pour l'adapter au nombre de messages reçus plutôt qu'un nombre fixé à l'avance, ce qui a entraîné d'importantes accélérations dans les systèmes réels.
