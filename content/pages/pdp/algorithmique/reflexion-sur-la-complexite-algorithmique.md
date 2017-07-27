Title: Réflexion sur la complexité algorithmique
Order: 9
Date: 2014-09-27
Slug: reflexion-sur-la-complexite-algorithmique
Author: Höd
Display: true

L'article qui suit présuppose quelques notions basiques d'algorithmique et de calcul de complexité (temporelle). Il vise à aborder deux grandes erreurs commises par les novices dans ces domaines et à en constater les effets.  
Une première partie sera dédiée à une erreur classique d'évaluation de la classe de complexité d'un problème à partir de la complexité calculée d'un algorithme, ce qui aura des conséquences désastreuses en terme de performances. La seconde partie présentera une erreur liée à l'erreur d'évaluation directe de la classe de complexité d'un problème, qui va cette fois avoir des conséquences sur la manière d'aborder un problème pour tenter de le résoudre.

Les notions utiles à la compréhension de cet article seront expliquées dans une première partie et la totalité des démonstrations sera omise (mais on peut évidemment grassement payer l'auteur pour qu'il les fasse sur le forum).

[TOC]

### Rappels sur la complexité temporelle
#### Complexité en temps
Il est coutume que de manière informelle, on enseigne aux novices de l'algorithmique que la complexité d'un algorithme correspond au nombre  d'étapes (élémentaires) de l'algorithme, qui est fonction de la taille des données du problème. Cette définition a l'avantage d'être très facile à appliquer, facilement compréhensible et de donner une borne assez fidèle dans la plupart des applications.

Cependant, cette définition est problématique, comme nous allons le voir, lorsque l'on donne la définition formelle des classes d'équivalence de complexité algorithmique. On présente souvent les classes de complexité principales : $P$ et $NP$, respectivement pour *Polynomial* et *Non-**Déterministe** Polynomial*. Le terme « non déterministe » est important puisqu'à l'heure actuelle, nous ne savons pas si $P = NP$ (et pour l'anecdote, il s'agit d'un des problèmes du prix du millénaire, récompensé par la coquette somme d'un million de dollars par le *Clay Mathematical Institute*).  
De manière formelle, un algorithme $A$ de **machine de Turing déterministe** est polynomial s'il existe un polynôme $p_A$ tel que $\forall x \in \Sigma^*, |x|=n, t_A(x) \leq p_A(n)$ où $x$ est un mot de l'alphabet $\Sigma$ (ensemble des symboles différents pour coder l'entrée), $t_A(x)$ le nombre de pas jusqu'à l'arrêt de $A$ et $n$, la longueur de l'entrée, qui est arbitrairement fixée.  
On appelle complexité en temps de $A$, le maximum des $t_A(x)$ pour un $n=|x|$ fixé. On comprend donc aisément qu'un algorithme est polynomial si sa complexité temporelle est bornée par un polynôme.  
Par extension, on dira qu'un problème $\Pi$ est polynomial s'il existe un algorithme $A$ polynomial qui résout $\Pi$.

Cette définiton est excessivement formelle et oblige à recourir aux machines de Turing. Cependant, il existe toujours des fonctions permettant de passer d'un formalisme en machine de Turing à un formalisme utilisant nos ordinateurs modernes, le tout, évidemment, en temps polynomial. Ainsi, par la suite, on ne reviendra jamais aux machines de Turing pour calculer des complexités, et heureusement !

Est-ce qu'un algorithme qui n'est pas dans $P$ est dans $NP$ ? C'est une question que l'on retrouve assez souvent et la réponse est évidemment non. Il suffit de se référer à la définition formelle d'un algorithme non-déterministe polynomial. Pour cela, nous devons introduire la notion de **certificat** et de **vérification**.  
Un certificat est une aide permettant, pour une entrée donnée, de déterminer si $x$ est reconnu par un algorithme $A$. De manière conceptuelle, il peut être vu comme une intervention divine ou une indication, comme en donnerait un professeur lors d'un examen, pour guider l'étudiant à démontrer un résultat difficile.  
La vérification est un algorithme permettant de savoir si l'entrée est reconnue sachant le certificat.  

On dira qu'un algorithme $A$ est non-déterministe polynomial s'il existe un polynome $p_A$ tel que $\forall x \in \Sigma^n$, $t_A(x) \leq p_A(n)$ où $t_A(x)$ est le temps de reconnaissance de $x$ (c'est à dire le temps minimal de reconnaissance de $x$ parmi l'ensemble des temps de reconnaissance de $x$, qui peuvent varier selon le certificat).  
De même, un problème $\Pi$ est non-déterministe polynomial s'il existe un algorithme $A$ non-déterministe polynomial qui résout $\Pi$.  

#### Réduction polynomiale et classes d'équivalence

Une dernière partie théorique permettant d'introduire la notion de **réduction polynomiale** et ainsi la notion de **classes de complexité**, de manière plus formelle.

Soient $\Pi_1$ et $\Pi_2$, deux problèmes de décision. On dit que $\Pi_1$ se réduit polynomialement en $\Pi_2$ noté $\Pi_1 \propto \Pi_2$ s'il existe une fonction $f:D_{\Pi_1} \rightarrow D_{\Pi_2}$ telle que :

+ $f$ est calculable polynomialement
+ $I\in Y_{\Pi_1} \Leftrightarrow f(I)\in Y_{\Pi_2}$

Où $D_{\Pi_1}$ et $D_{\Pi_2}$ sont, respectivement, les instances possibles (entrées possibles) pour le problème $\Pi_1$ et $\Pi_2$ et $Y_{\Pi_1}$, l'ensemble des instances de $\Pi_1$ renvoyant *VRAI* au problème de décision.  

Par exemple, on peut considérer le problème de savoir si un entier $n$ donné est pair. L'ensemble des données possibles en entrée est l'ensemble des entiers. L'ensemble renvoyant *VRAI* est, évidemment, l'ensemble des nombres pairs.

Cette relation possède quelques propriétés intéressantes mais ce n'est pas le propos de cet article. Par contre, il s'agit d'une relation d'ordre partiel sur l'ensemble des problèmes de décision, à laquelle on peut ajouter une notion de *symétrie* permettant de construire une relation d'équivalence, et par là même, définir des classes d'équivalence au sens de cette relation.  

La classe $P$ est la plus petite classe au sens de cette relation et la classe $NP$-complet est la plus grande.

Enfin, pour éclaircir le vocabulaire. On parle de problème $NP$-difficile dans le cadre des problèmes de décision. Cela signifie qu'un problème est aussi difficile que les problèmes de la classe $NP$-complet.  

#### En résumé

Que faut-il retenir de cette introduction très formelle ?

+ Un problème $\Pi$ est polynomial s'il existe un algorithme $A$ polynomial qui résout $\Pi$.
+ un problème $\Pi$ est non-déterministe polynomial s'il existe un algorithme $A$ non-déterministe polynomial qui résout $\Pi$.
+ $P \subseteq NP$.
+ Tous les problèmes d'une classe donnée sont équivalents (au sens de la réduction polynomiale).

### Erreur 1 : Évaluation de la complexité d'un algorithme
#### Le propos

Rappelez-vous de la définition formelle de la complexité temporelle. Que ce soit pour l'ensemble $P$ ou $NP$ nous avons l'inégalité suivante :  
$t_A(x) \leq p_A(n)$ où $x$ est un mot de l'alphabet $\Sigma$ (ensemble des symboles en pour coder l'entrée), $t_A(x)$ le nombre de pas jusqu'à l'arrêt de $A$, $n$, longueur de l'entrée est arbitrairement fixé et $p_A(n)$, un polynôme fonction de $n$.

C'est bien ici qu'est le propos de cette première erreur : le polynôme qui borne le temps d'éxécution n'est pas fonction de l'entrée mais de la taille de codage ou d'écriture du problème. Quelle différence ? Voyons sur un exemple très simple.

#### Exemple : Nombre composé

Un nombre est composé s'il n'est pas premier.  
Donnons nous le problème de décision suivant : Soit un entier n. Est-il composé ?

Un algorithme naïf serait le suivant :

```console
Pour i = 2 à $\sqrt{n} faire  
    Si $n \mod i = 0$ alors  
        Retourner Vrai  
Fin pour
Retourne Faux
```

La question à se poser est : quelle est la complexité de cet algorithme ?  
Au premier coup d'œil, nous parcourons une boucle dans laquelle nous effectuons une opération plus ou moins élémentaire. Bref, il semblerait que cet algorithme soit en $O(n)$ voire $O(n^{\frac{1}{2}})$ si nous voulions être plus précis. Dans les deux cas, un joli polynôme. Notre problème est donc un problème polynomial.

Ce calcul est évidemment bon mais la conclusion est fausse, pour la raison évoquée : elle ne tient pas compte de la taille d'écriture du problème.
Quelle est donc la taille d'écriture de ce problème ?  
Nous avons un entier $n$ quelconque. Quelque soit la base $b$ dans laquelle il est exprimé, sa longueur d'écriture est $\left\lfloor{log_bn}\right\rfloor + 1$, c'est à dire partie entière inférieure du logarithme en base $b$ de $n$ plus une unité.

Ainsi, le polynôme cherché est un polynôme fonction de $O(log n)$. $O(n^{\frac{1}{2}})$ n'est pas borné par un polynôme en $O(log n)$, ce qui fait que notre algorithme n'est **PAS** polynomial.  
Attention toutefois, cela n'exclut pas que le problème soit polynomial (qu'il existe un algorithme polynomial pour le résoudre), mais ce ne sera pas celui-ci. Une bonne pratique consiste à vérifier qu'il est au moins dans la classe $NP$ et ensuite d'essayer de montrer qu'il est dans $P$ ... s'il est dans $P$.

Au vu de la définition formelle de la section précédente, il suffit de trouver un bon certificat qui permette de trouver un algorithme en temps polynomial en fonction de la taille d'écriture du problème.  
On peut simplement prendre deux entiers $a$ et $b$ comme certificat et cet algorithme de vérification :

```console
Si $a*b=n$ alors  
    Retourner Vrai
```

Dans la vérification, on ne s'intéresse qu'à savoir si $x$ est vérifié, comme son nom l'indique.  
Nous avons bien un algorithme qui est cette fois borné par un polynôme et donc notre problème admet un algorithme de la classe $NP$ qui le résout. Il s'agit donc d'un problème $NP$.

Pour la petite histoire, ce problème est effectivement dans la classe $P$. Le co-problème associé est le test de primalité, dont la preuve de l'appartenance à la classe $P$ n'a été trouvée qu'en 2002, avec les algorithmes AKS (au pluriel car de nombreuses variantes se sont développées). Ne vous inquiétez pas, cela ne suffit cependant pas à casser RSA.  

#### En résumé

Ainsi s'achève cette première partie qui consistait à pointer du doigt un piège courant de l'évaluation de la classe de complexité d'un algorithme. La conclusion à en tirer est que la notion de complexité est certe relative au nombre d'étapes d'un algorithme, mais elle représente surtout une garantie que si la taille du problème augmente, le temps de calcul n'explose pas.  

### Erreur 2 : Erreur sur la classe d'un problème
#### Le propos

Lorsque l'on est face à un problème d'optimisation combinatoire ou de décision (les deux ensembles de problèmes sont équivalents), on procède généralement de la sorte :

+ Trouver un modèle mathématique du problème (hypothèses, données, limites du modèle)
+ Déterminer à quelle famille se rattache ce problème.
+ Déterminer ou concevoir un algorithme de résolution du problème.

Une technique usuelle est de se ramener à un problème modèle, dont on connait d'une part la classe mais d'autre part des algorithmes de résolution plus ou moins efficaces.

Une erreur classique est de confondre énoncé et donnée. Cette distinction est parfois peu perceptible du fait que la formulation du problème va très peu changer, pouvant induire en erreur sur la nature du problème (et potentiellement sa classe de complexité).  

#### Exemple : SAT

Nous allons à présent parler d'un problème historique de décision. Il s'agit du problème SAT pour Satisfaction de Contraintes Logiques. Voici son énoncé formel :  
__Données__ : $n$ variables logiques $x_i$ pour $0 \leq 1 \leq n$  
On appelle $x_i$ et $\overline{x_i}$ des littéraux.  
On dispose également de $p$ clauses qui sont un ensemble de littéraux.  
Exemple de clause : $\{x_1,\overline{x_3},x_8\}$.  

La question est la suivante : existe-t-il une fonction de vérité (c'est à dire une fonction qui à tout $x_i$ va associer une valeur VRAI ou FAUX) telles que les $p$ clauses soient vérifiées ?

C'est Cook qui, en 1972 fit une démonstration directe de la $NP$-Complétude de ce problème.  

Il existe un ensemble de sous-problèmes à SAT qui sont 1-SAT, 2-SAT, 3-SAT, etc.  
Ainsi pour 1-SAT nous avons le problème SAT avec des clauses à un littéral, pour 2-SAT des clauses à 2 littéraux, etc.

On pourrait penser que tous ces problèmes sont $NP$-complets sans appartenir à $P$ puisque leur énoncé est quasiment le même. On se rend vite compte que ce n'est pas le cas :  

- 1-SAT peut être résolu de manière triviale, en temps linéaire. Il suffit de parcourir l'ensemble des clauses et de retourner FAUX si l'on en rencontre une qui est fausse (cela correspond à regarder un simple booléen par clause).
- 2-SAT peut être résolu en temps polynomial. Je vous laisser chercher l'algorithme qui n'est guère compliqué.
- 3-SAT est $NP$-complet.

On peut d'ailleurs montrer que SAT $\propto$ 3-SAT pour montrer que 3-SAT est $NP$-complet.

#### Exemple : Arbre couvrant de poids minimal

Pour clore cet article sur une touche moins technique, on peut citer un second problème dont la modification d'un petit élément d'énoncé peut changer la classe du problème.  
Le problème de l'arbre couvrant de poids minimal est un problème que l'on peut formuler de la manière suivante : étant donné un graphe valué, trouver l'arbre contenant l'ensemble des sommets, pour lequel, la somme des valeurs des arcs est minimale.  
Il s'agit d'un problème avec de nombreuses applications concrètes. On peut citer par exemple l'optimisation de la longueur de câblage dans un avion ou tout autre appareil.  

Ce problème peut être résolu par l'algorithme de **Prim** ou de **Kruskal** en temps polynomial (on utilisera l'un ou l'autre selon la structure du graphe).

Voici une variante de ce problème : étant donné un graphe valué, trouver un arbre couvrant de poids minimal dont le degré des sommets de l'arbre est borné par $k$ fixé (c'est à dire que pour chaque sommet, il ne peut arriver ou partir que $k$ arcs).  
Cette variante peut modéliser une situation réelle, dans le cas du câble d'un établissement où les différents switchs ne disposent que de $k$ ports.

Cela peut paraître étonnant, mais ce problème n'est plus polynomial.  


### Conclusion

J'espère que cet article vous aura convaincu de l'intérêt de posséder des notions basiques sur le calcul de complexité algorithmique et surtout sur la connaissance des différentes classes de complexité qui conditionnent le choix des méthodes de résolution d'un problème (et également ses performances).
Un algorithme d'apparence polynomial n'en est pas forcément un, et un problème apparent à un autre problème par son énoncé n'est pas forcément dans la même classe de complexité. Seule une étude formelle de la taille d'écriture permet de répondre au premier piège et quelques techniques permettent de s'assurer que l'on peut réduire un problème à un autre (réduction polynomiale ou notion de sous-problème).  
