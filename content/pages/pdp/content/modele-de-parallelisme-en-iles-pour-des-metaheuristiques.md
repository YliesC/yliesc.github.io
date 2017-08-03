Title: Modèle de parallélisme en îles pour des métaheuristiques
Order: 9
Date: 2015-02-03
Slug: modele-de-parallelisme-en-iles-pour-des-metaheuristiques
Author: Höd
Display: true

### Introduction

Lorsque l'on parle de parallélisme, on pensera la majorité du temps à un gain de performance se traduisant par un temps de calcul moins long. Il existe deux grands types de parallélisme qui sont le parallélisme de données et le parallélisme de tâches.    
Le premier vise à effectuer en parallèle un traitement unique et coûteux en temps sur des données. Il s’agit essentiellement de modifier un algorithme déjà existant pour l’adapter au parallélisme. Le second type préfère paralléliser des tâches qui ne dépendent pas l'une de l'autre, permettant également un gain de temps. Outre la modification d’algorithmes déjà existants, ce type de parallélisme fait naître de nouveaux algorithmes dont l’avantage n’est pas nécessairement la réduction du temps de calcul mais une meilleure
stabilité numérique, une plus grande convergence ou d’autres propriétés mathématiques intéressantes. C’est le cas par exemple du modèle en îles, qui par nature, n’existe que sur des architectures parallèles. Ces algorithmes sont évidemment plus spécifiques et ne s'appliquent que dans des domaines précis.

Ainsi, le modèle en îles s'applique uniquement à des métaheuristiques à base de population comme les algorithmes génétiques principalement ou encore les algorithme d'optimisation par essaims particulaires. 

Dans un premier temps, nous rappelerons brièvement le principe et le fonctionnement des algorithmes génétiques avant de présenter dans une seconde partie le modèle de parallélisme en îles. Nous discuterons de l'intérêt d'un tel modèle, sans entrer dans les considérations techniques ou théoriques. Enfin, dans une dernière partie, nous présenterons des résultats empiriques et leur analyse obtenus sur une implémentation du modèle en îles.

[TOC]

### Quelques rappels sur les algorithmes génétiques
#### Principe

Les algorithmes génétiques font partie des méthodes dites d'intelligence calculatoire. Ils se basent sur la théorie de l’évolution darwiniste pour résoudre un problème en faisant évoluer un ensemble de solutions à un problème donné, dans l’optique de trouver un optimum global ou, à défaut, local. Ces algorithmes sont principalement stochastiques, car ils utilisent itérativement des processus aléatoires.    
La majorité de ces algorithmes servent à résoudre des problèmes d’optimisation au sens large. On parle donc de métaheuristiques car ils ne s'appliquent pas à un problème en particulier mais sont capables de donner de bons résultats, en un sens à définir, sur une large classe de problèmes et d'instances.
Parmi les grandes méthodes largement utilisées, on note le recuit simulé, la recherche tabou, la recherche itérative locale ou encore des méthodes MCMC (Markov Chain, Monte Carlo) comme l’algorithme de Metropolis-Hastings (sur lequel se base le recuit simulé par ailleurs), et des méthodes plus spécifiques comme le NSGA-II (Non-Dominated Sorting Genetic Algorithms) et IBEA (Indicator-Based Evolutionnary Algorithm) pour l’optimisation multi-objectifs.

#### Fonctionnement

Il existe une multitude de métaheuristiques et les algorithmes génétiques en font partie. Etant donné que le modèle en îles dont fait l'objet cet article présuppose des algorithmes à base de population, nous ne présenterons que ce type de méthodes.
Nous partons d’une population initiale où chaque individu représente une solution potentielle au problème. Cette population peut ou non être générée aléatoirement. La manière de générer la population est propre au problème voire à l'instance, mais partons du principe que l'on génère la population de manière aléatoire pour simplifier.    
Ensuite, la population est évaluée, c’est à dire que l’on attribut un indicateur qualitatif à chaque individu. La manière d’évaluer est très spécifique au problème et pas toujours évidente à mettre au point. En effet, dans des problèmes d'optimisation classique, nous avons très souvent une formulation mathématique d'une fonction à minimiser ou maximiser. Ainsi l'évaluation peut très souvent se limiter à la valeur de cette fonction évaluée au point représenté par l'individu sélectionné. Cependant, il existe des problèmes où aucune formulation explicite du système à optimiser n'existe. L’évaluation est généralement l’opération la plus coûteuse pour ce genre de méthode, à tel point que dans certains cas où l'on dispose tout de même d'une formulation explicite on préfère évaluer de manière moins directe en calculant d'autres indicateurs.

![Algorithme génétique](http://img11.hostingpics.net/pics/615963algogen.png)

Les meilleurs individus sont alors sélectionnés. Là encore, les mécanismes de sélections pourraient largement être discutés : doit-on sélectionner les meilleurs individus ? aléatoirement ? combien au regard de la population totale ? Ce n'est pas l'objet de cet article mais la littérature sur le sujet est relativement riche et intéressante.

Après être sélectionnés, les individus sont croisés. C’est à dire que l’on va prendre, qu hasard, des parties de chaque individu pour en former un nouveau, tout comme un être humain se voit affublé au hasard des allèles du père ou de la mère. On effectue alors des mutations avec une probabilité assez faible. Les mutations permettent d’éviter de tomber dans des optimums locaux, mais doivent être assez rares pour conserver une convergence de l’algorithme. Enfin, les nouveaux individus sont replacés dans la population initiale, les moins bons sont supprimés pour garder une population de taille constante.

Encore une fois, il y aurait beaucoup à dire : comment croiser les individus ? comment choisir la probabilité de mutation ? quel opérateur de mutation choisir ?    
De même que la restriction sur la taille constante de la population n'est pas une nécessité.

Le processus est itéré le nombre de générations voulues ou selon des paramètres divers : temps, nombre d’évaluations, etc.

### Modèle en îles

Le théorème dit du _no_ _free_ _lunch_[^wiki] démontre qu'il n'existe pas de métaheuristique meilleure qu'une autre et que la qualité d'une métaheuristique ne peut-être établi qu'au regard de certaines classes de problèmes et dépend également des paramètres de l'algorithme voire de son implémentation.

![nfl](http://img11.hostingpics.net/pics/191049nfl.png)

Ainsi, il est difficile d'anticiper l'adéquation d'une métaheuristique sur une instance quelconque sans expérimentation ou une phase d'apprentissage. Un facteur primordial de l'efficacité d'une méthode à base de population sur une instance donnée réside dans l'équilibre entre l'intensification (c'est à dire une sélection élitiste des individus ce qui a pour conséquence de forcer la convergence) et la diversification (c'est à dire élargir le champs de recherche des solutions).    
On comprendra aisément la difficulté à allier à la fois ces deux concepts antagonistes.

Le modèle en îles consiste à lancer plusieurs algorithmes génétiques à base de population, les îles, qui vont évoluer de manière indépendante mais intéragir par moments. Cela permet des convergences locales d'algorithmes tout en conservant une diversité globale grâce à ces intéractions.

L'organisation des îles au sein du modèle est régie par une topologie qui peut influencer la tolérance à la convergence locale. En effet, une île isolée, avec peu de communications vers d'autres îles, impactera moins la convergence prématurée ou non, du modèle tandis qu'une île centrale, comme il y en a une dans une topologie en étoile, pourra avoir des effets bénéfiques ou néfastes selon la politique de l'île.    
Typiquement, le facteur principal influençant la diversification / intensification du modèle (c'est à dire à un niveau d'abstraction supérieur à celui du simple algorithme) est la politique propre à chaque île. Les intéractions entre îles sont définies par certaines règles : périodicité dans le nombre de générations, périodicité temporelle, mais également des considérations sur la qualité d'une solution, etc.    

![topo](http://img4.hostingpics.net/pics/743233islands.png)

Dans les modèles classiques, la politique et la topologie sont des attributs statiques ne permettant pas d'adapter dynamiquement les étapes de diversification ou d'intensification.    
Des travaux actuels s'intéressent à des topologies dynamiques, changeantes au cours de l'évolution des algorithmes selon certains signaux (des informations sur la convergence des individus, l'intégration des population migrantes,...).    
De la même manière, la topologie peut être stochastique. Chaque lien inter-île a une certaine probabilité d'être établi au moment d'une migration. Ces probabilités peuvent être statiques, mais également dynamique, permettant, par exemple, d'isoler des îles n'apportant rien en terme de diversité ou de qualité des solutions.

En résumé, les apports théoriques du modèle en îles résident dans une vitesse de convergence plus rapide, un domaine de recherche plus vaste et une meilleure gestion des étapes de diversification / intensification qui se traduit par la sortie potentielle de certains optimums locaux.

#### Modèle hétérogène : vers une optimisation multi-objectif ?

Rappelons qu'un individu pour un algorithme génétique représente une solution au problème. Plus exactement, il est une représentation d'une solution qu'il faut ensuite décoder pour obtenir la solution dans notre espace de solutions. Ainsi, si l'on cherche à trouver un polynôme de degré $k$ qui minimise la distance à certains points (une simple interpolation en somme), nous allons naturellement coder une solution par un vecteur de dimension $k$ où chaque composante codera un coefficient du polynôme.

Ainsi nous aurons la fonction de codage $C : \mathbb{P}_k \rightarrow \mathbb{R}^k$ avec d'éventuelles contraintes sur le domaine.

Il est important d'avoir en tête cette considération sur la représentation car il n'est pas toujours aisée d'avoir une unique manière de coder une solution. De manière générale, selon les algorithmes à base de population, le codage peut varier, notamment par l'ajout d'information supplémentaire (une vitesse dans les algorithmes d'optimisation par essaims de particules par exemple) et par l'expérience (ou la théorie) qui nous montre qu'un type de représentation est plus efficace qu'un autre pour tel problème sur tel algorithme.    

Ainsi, il est envisageable d'avoir un modèle en îles avec des îles hétérogènes, c'est à dire avec des algorithmes différents sur les îles et donc, potentiellement, un codage différent d'une île à l'autre. Il peut en effet être intéressant de chercher des solutions à l'aide de différents algorithmes et de les faire intéragir de manière à ce qu'ils s'échangent des informations utiles pour converger vers une solution de grande qualité.

Pour se faire, il faut envisager un type de représentation global, généralement celui qui code les individus de la majorité des îles, et de définir des fonctions de conversion entre les différentes représentations.

Un interêt du modèle hétérogène est qu'il permet d'avoir plusieurs codage pour une seule solution ainsi que plusieurs optimisation simultanée via des fonctions objectifs différentes selon les îles. Ainsi, il est possible d'espérer une optimisation simultannée de critères antinomiques.    
Prenons l'exemple du voyageur de commerce multi-objectifs, avec une double valuation du graphe : chaque arc porte à la fois une distance mais également un risque. Bien souvent plus le chemin est court plus le risque est élevé. L'objectif est de minimiser à la fois la distance mais également le risque. Si une solution dans l'espace des solutions est un tour muni de la double valuation des arcs, on peut imaginer deux codages, ne tenant respectivement compte que du risque ou de la distance afin d'effectuer une optimisation mono-objectif classique.

Ainsi avec le modèle d'îles nous pouvons lancer deux optimisations mono-objectifs sur plusieurs îles, avec des algorithmes différents, connectées selon une certaine topologie avec certaines politiques, de sorte à éventuellement privilégier tel ou tel objectif. Lorsqu'une île veut envoyer des individus, si son codage n'est pas le codage principal choisi, elle fait appel à sa fonction de conversion. Dans notre cas, si nous choisissons comme codage principal la valuation par les distances, alors une île qui optimise le risque convertira le tour en un tour avec les distances associées.    
De fait, les meilleurs individus seront envoyés à un algorithme pour qui normalement il ne sera pas nécessairement bon. Cependant, il se peut que l'individu soit suffisemment bon pour rester dans la nouvelle population voire interragir avec. On espère ainsi réussir à obtenir les individus appartenant au [front de Pareto](https://en.wikipedia.org/wiki/Pareto_efficiency) nous permettant ensuite de faire un choix de la meilleure solution à retenir selon certains critères.

Le modèle en îles est donc particulièrement remarquable en cela qu'il permet d'obtenir des solutions correctes à un problème d'optimisation multi-objectifs en effectuant simultanément des optimisations mono-objectifs, ce qui permet en théorie de grandement réduire le temps de calcul important des méthodes classiques de l'optimisation multi-objectif.

### Analyse des résultats des tests

Les tests de performances doivent quantifier à la fois la qualité de la programmation parallèle et vérifier les apports théoriques du modèle en île dans le but de valider l'implémentation.
Les tests de performance ont été effectués sur un problème du voyageur de commerce, avec des instances de différentes tailles (approximativement 100 villes à 13 000 villes). Il s'agit d'instances réelles.
La première série de tests est purement descriptive puisqu'elle ne fait que donner des indicateurs sur des instances déterministes, c'est à dire avec une graine fixée. La seconde partie des tests est plus intéressante parce qu'elle donne une réponse statistique quand à l'influence de certains facteurs.

#### Modèle homogène vs Sérialisé
##### Test 1

**Objectif :**    
Mettre en évidence une rapidité de convergence accrue du modèle.    

**Protocole :**    
Graine fixée    
Population de 1000 individus    
Modèles d'îles homogènes    
Politique élitiste :    
1. Envoi d'individu toutes les 25 générations.    
2. Sélection par tournoi de 2 individus parmi 100.    

**Résultats :**

||Population totale ||| 1000 meilleurs |
 ------------ | ----------- | ---------------- | ---------------- | ---------------- | --------------- | ------------
.| **Sérialisé** | **3 îles** | **4 îles** | **Sérialisé** | **3 îles** | **4 îles**
**Variance**	| 13966,68	| 688,20	| 39,00	| 13966,68	| 0,89	| 0,99	
**Ecart Moyen**	| 94,64	| 23,83	| 0,93	| 94,64	| 0,89	| 0,99	
**SCR**	| 13952716,15	| 2063928,59	| 155980,87	| 13952716,15 | 892,41	| 997,69	
**Moyenne**	| 	-2512,54	| -1340,05	| -1243,24	| -2512,54	| -1316,67	| -1242,04

![Graphique 1](http://img4.hostingpics.net/pics/499599921.png)

**Analyse des résultats : **    

Dans le cas où la graine est fixée la variance de l'échantillon diminue vraiment, tant en passant de l'algorithme sérialisé à 3 îles qu'en passant de 3 à 4 îles. Cependant, en ne considérant que les 1000 meilleurs individus, le passage de 3 à 4 îles ne semblent plus significatifs.    
L'algorithme semble avoir convergé, aussi bien pour 3 et pour 4 alors qu'il n'a vraissemblablement pas convergé pour l'algorithme seul.    
On peut également se demander si la politique très élitiste mise en place n'a pas fait converger les algorithmes vers un minimum local, ainsi si l'algorithme converge à partir de 3 îles et pour les critères d'arrêts spécifiés, alors il convergera vers le même optimum pour un nombre d'îles supérieur (sauf si par chance ces îles supplémentaires sont générés avec des individus meilleurs à la base).

Les autres métriques sont unanimes : la SCR est divisé par 10 à 100 voire par un facteur $10^6$ sur des populations constantes par exemple, montrant fitness bien meilleurs sur le modèle d'îles.    
Le graphique nous montre clairement que les modèles d'îles ont convergés alors que la fitness des individus de l'algorithme seul semble continuer de s'améliorer (cf. dernier tiers).

Le test s'avère ici plus qualititatif que quantitatif car il ne répond pas à la question suivante : quelle est le gain sur la vitesse de convergence.    
Accessoirement on peut également se demander si l'algorithme sérialisé aurait convergé vers un meilleur optimum ou non, et ce, malgré une politique très élitiste.

##### Test 2

**Objectifs :**    
Quantifier le gain sur la rapidité de convergence du modèle d'île.

**Protocole :**    
Même protocole qui ci-dessus. On changera les critères d'arrêt pour un critère sur la qualité de la solution que l'on fixera à -1350 qui correspond à peu près à la solution obtenue pour l'algorithme seul.    
On ajoutera un compteur sur le nombre de générations avant d'atteindre cette fitness.

**Résultats :**    
Sérialisé : 3361 générations    
3 îles : 1261 générations \*    
4 îles : 968 générations \*    

\* Obtenus comme moyenne sur 100 tests.    
Notons également que le nombre maximal de générations pour 4 îles est atteint pour 1401, soit plus que la moyenne pour 3 îles. A l'inverse le meilleur résultat est obtenu pour 904 générations.

**Analyse des résultats :**    

L'algorithme s'arrête au moment où l'algorithme est prêt à converger (première apparition de la meilleure fitness observée). Le résultat montre bien que les modèles d'îles convergent plus rapidemment.    
On obtient un ratio de 2,6 pour le modèle à 3 îles et un ratio de 3,47 pour le modèle à 4 îles.

#### Influence du facteur communication
##### Test déterministe

**Objectifs :**    
Mettre en avant l'intérêt des communications dans la convergence de l'algorithme et la qualité de solutions.

**Protocole :**    
Graine fixée.    
3 îles sans communication, 3 îles avec communications (topologie complète et politique élitiste).    
Partant d'une même population, on lance les deux modèles pour 1000 générations par île et on regarde la qualité finale obtenue sur l'ensemble de la population.

**Résultats :**

| .               | Communications | Sans communication |
| --------------- | -------------- | ------------------ |
| **Variance**    | 12155,66       | 170,68             |
| **Ecart Moyen** | 87,43          | 10,95              |
| **Moyenne**     | -2032,36       | -1427,54           |
| **SCR**         | 36454825,99    | 511894,45          |
| **Ratio SRC**   | 71,2155128426  |                    |

![Graphique 2](http://img4.hostingpics.net/pics/885394232.png)

**Analyse des résultats :**    

Tous les indicateurs sont favorables au modèle avec communication. On note une amélioration moyenne de 30% des solutions et une somme des carrés des résidus qui a diminué d'un facteur 70.    
Le graphique montre que le modèle sans communication n'a pas encore convergé alors que celui avec communication est en passe d'avoir complètement convergé.

##### Test non déterministe : ANOVA 1

Dans le cas général où la graine n'est pas fixée, nous voulons déterminer si les communications ont un facteur sur la qualité de la solution obtenue. Pour cela nous allons essayer de nous servir de l'ANOVA 1 : l'analyse de variance à un facteur.    
Nous avons ici un facteur, les communications, avec deux modes : avec ou sans communication.    
Nos observations seront notées $y_{ij}$ avec $i\in \{1,2\}$ respectivement sans et avec communication, et $j\in \{1...100\}$ puisque nous avons réalisé 100 expériences avec et sans communication.
Le modèle d'ANOVA 1 se basent sur des hypothèses qui ne sont pas triviales dans notre cas :

+ Les données $y_{ij}$ obtenus sont réalisations d'une variable aléatoire $Y_{ij}$ de loi normale $N(\mu _{i}, \sigma ^2)$
+ Les variables aléatoires $(Y_{ij})$ sont globalement indépendantes.

Notre modèle serait donc : $Y_{ij} = \mu _{i} + \epsilon _{ij}$

Avec $\epsilon _{ij}$ indépendants et identiquement distribués de loi normale $N(0, \sigma ^2)$.    
Les hypothèses du modèle n'étant pas trivialement vérifiées, il nous faudra dans un premier temps les vérifier avant de réaliser l'analyse de la variance à proprement parler.    
Pour cela nous allons adopter le plan qui suit :

+ Une estimation par noyau nous dira si la fitness des meilleurs individus suit une loi normale.
+ Un test de Barlett nous dira si il y a homoscédasticité (condition du modèle).
+ Nous dresserons alors un tableau d'analyse de variance.

Un test de comparaison par approche de modèle nous donnera une réponse au risque de $5\%$ quand à l'influence du facteur communication sur la différence des moyennes des deux groupes.

Les tests de normalité nous permettent de conclure à la normalité des deux échantillons. Les tests effectués sont le test de Lilliefors et le test de Shapiro-Wilk. Ils ont été réalisés sous R grâce au paquet normtest.

```
> lillie.test(t(X1))

	Lilliefors (Kolmogorov-Smirnov) normality test

data:  t(X1) 
D = 0.0599, p-value = 0.5072

> shapiro.test(t(X1))

	Shapiro-Wilk normality test

data:  t(X1) 
W = 0.9859, p-value = 0.3694

> lillie.test(t(X2))

	Lilliefors (Kolmogorov-Smirnov) normality test

data:  t(X2) 
D = 0.0547, p-value = 0.6533

> shapiro.test(t(X2))

	Shapiro-Wilk normality test

data:  t(X2) 
W = 0.992, p-value = 0.8184

```

Le seuil fixé est de $5\%$. L'hypothèse du test est que les individus suivent une loi normale. La p-value étant supérieure au seuil, on ne rejette pas l'hypothèse et on conclue donc à la normalité de l'échantillon.

```
 fligner.test(list(t(X1),t(X2)))

	Fligner-Killeen test of homogeneity of variances

data:  list(t(X1), t(X2)) 
Fligner-Killeen:med chi-squared = 15.5555, df = 1, p-value = 8.012e-05

```

Le test de variance indique une variance non-commune aux deux groupes. Cependant, cette variance non homogène est moins problématique qu'une distribution non normale des individus, surtout lorsque les groupes comportent autant d'individus. Ainsi, le test de Fisher effectué lors de l'ANOVA sera potentiellement faussé en rejettant plus facilement l'influence significative du facteur étudié.

![ANOVA](http://img4.hostingpics.net/pics/594528723.png)

**Analyse du tableau d'ANOVA :**

Nous observons une p-value de l'ordre de $10^{-62}$, très largement inférieure au seuil des 5% fixés. On peut donc conclure à l'influence significative des communications sur notre modèle.

### Conclusion

Nous avons vu comment le modèle d'îles permettait d'obtenir des propriétés intéressantes de convergence et de stabilité. Nous avons également discuté une approche potentiellement multi-objectifs grâce au modèle en îles. Enfin, nous avons analysé quelques résultats d'une implémentation du modèle d'îles afin de justifier les apports théoriques.    

Il s'agit là bien sur d'une introduction concernant le modèle d'îles et il se pose maintenant pas mal de questions quand aux choix des nombreux paramètres liés au modèle : quelles politiques choisir ? comment intégrer les migrants ? comment choisir la topologie ?    
Toutes ces questions font appels à la connaissance du problème à résoudre par l'utilisateur mais elles font également partie d'un pan de la recherche qui s'intéresse à l'optimisation de paramètres (ou plus généralement de programmes), à la fois durant le déroulement d'un algorithme, de manière autonome, mais aussi à priori ou à postériori. Cet aspect sera certainement traité dans un prochain article.

[^wiki]: "Illustration Wikipédia, by Nohjan"
