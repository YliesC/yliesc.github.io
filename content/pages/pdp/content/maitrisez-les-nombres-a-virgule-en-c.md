Title: Les nombres à virgule flottante
Order: 9
Date: 2015-06-12
Slug: maitrisez-les-nombres-a-virgule-en-c
Authors: informaticienzero, Maëlan
Display: true

Le langage C, comme d’autres, propose des types pour représenter les nombres réels. Cependant, leur emploi n’est pas aussi simple qu’on pourrait l’espérer. La **norme informatique IEEE 754** décrit le codage en mémoire des **nombres dits à « virgule flottante »**. On va la passer en revue pour comprendre et résoudre les difficultés liées à l’utilisation des nombres réels en informatique. On alternera parties théoriques (qui concernent l’informatique en général) et parties pratiques (avec le langage C).

Au programme :

* rappels de C ;
* la norme IEEE 754 et ses conséquences (valeurs possibles, etc.) ;
* inconvénients des nombres flottants en C ;
* comparer des nombres flottants ;
* la norme C et les implémentations.

Prérequis : le [système binaire](http://fr.wikipedia.org/wiki/Système_binaire), dont :

* les [bits, octets, etc.](https://fr.wikipedia.org/wiki/Octet),
* la [notation hexadécimale](http://fr.wikipedia.org/wiki/Système_binaire#Entre_les_bases_2.2C_8_et_16),
* et les [façons principales de coder un entier relatif](https://fr.wikipedia.org/wiki/Système_binaire#Repr.C3.A9sentation_des_entiers_n.C3.A9gatifs).

*PS : Ce tutoriel a été entièrement pensé, traité et mis en forme par Maëlan ; informaticienzero ne s’est occupé que d’adapter le tutoriel en Markdown pour le mettre en ligne sur PDP. Toutes les questions, remarques et félicitations vont donc à Maëlan !* — informaticienzero

[TOC]

# Introduction : les nombres à virgule flottante
### Virgule fixe, virgule flottante ###

Commençons par présenter ce dont on va parler en long, en large et en travers. En informatique, on parle de « **virgule flottante** » lorsque le système utilisé pour coder les nombres en mémoire permet de faire varier la place de la virgule, c’est-à-dire l’ordre de grandeur (par exemple en base 10, avec la même séquence de chiffres « 421337 », on peut coder 4,21337 ou 42,1337 ou 421,337…). Par opposition, dans un système à « virgule fixe », on aura toujours le même nombre de chiffres avant et après la virgule.

Un système à virgule fixe permettra par exemple de représenter les nombres de l’intervalle $[0\,;10[$ (un chiffre avant la virgule). En remplaçant la seule donnée du nombre $x\in[0\,;10[$ par une information de la forme $(x,p) \in [1\,;10[\times[[-5\,;5]]$ ($p$ entier), on crée un système à virgule flottante qui permet de coder les nombres de l’intervalle $[1.10^{-5}\,; 10.10^5[$ de cette façon : $x.10^p$. La contrainte sur la valeur de $x$ — il est supérieur à 1, autrement dit a exactement un chiffre avant la virgule — garantit que le codage d’un nombre est unique.

*Remarque* : Dans la suite, j’appellerai « partie significative » d’un nombre, ce nombre écrit en notation scientifique sans la puissance de 10 associée (c’est-à-dire le nombre à virgule avec un seul chiffre avant la virgule).

### Une certaine précision ###

On voit donc l’intérêt d’une représentation flottante : elle permet de coder un intervalle bien plus important, bien que toujours limité. Les contraintes physico-informatiques du monde réel fait qu’on dispose pour l’entier $p$ d’un nombre fini de valeurs, ce qui borne l’intervalle représentable. Ces mêmes contraintes font aussi que le réel $x$ présente une **précision limitée** ; ainsi, on ne code pas réellement tous les réels de l’intervalle, mais seulement des approximations à un certain nombre de chiffres. Cette idée est cruciale, comme on le verra.

Bien sûr, concrètement ce sera le binaire qui interviendra et non la base 10. Ceci nous amène à une seconde problématique.

### Des constantes inexactes… ###

Les nombres décimaux (c’est-à-dire écrits en base 10) ne sont pas toujours représentables de façon finie en binaire. De même qu’en base 10 on a 1/3 = 0,3333…, en binaire 1/10 = *0b*0,00011001100110011… avec une infinité de 0011. Ainsi, lorsqu’on écrit une constante dans un code source, on n’est pas assuré d’obtenir une valeur exacte (typiquement, 0,1 est arrondi).

En particulier, une partie significative écrite en base 10 ou une puissance de 10 négative (on divise par une puissance de 10) peuvent mener à des nombres inexacts. En fait, seuls les nombres dont la partie décimale est le résultat d’une division par une puissance de 2 (comme 0,5 = 1/2, 0,75 = 3/4 ou 0,625 = 5/8) sont représentables exactement en binaire.

# Les nombres à virgule en C
Après cette introduction aux problématiques principales des nombres à virgule flottante, je vous propose de passer en revue les fonctionnalités du langage C à leur sujet. Cela nous servira puisqu’on utilisera le C tout au long de ce cours pour illustrer notre étude théorique des nombres flottants.

### Syntaxe ###

#### Les types numériques ####

Le C met à notre disposition les types `float` et `double` (ainsi que `long double`, dont nous ne parlerons pas) pour stocker des nombres flottants. Ne rêvons pas, on fait du C donc leur taille en mémoire dépend de l’architecture de l’ordinateur, mais très souvent ce sera **32 bits** pour un `float` et **64 bits** pour un `double`. Un `sizeof` vous assurera de leur taille chez vous.

#### Intérêt des nombres flottants ####

Les types flottants ne sont pas seulement utiles pour manipuler des nombres à virgule, ils peuvent aussi servir pour stocker de **très grands nombres**. En effet, un `float` permet d’atteindre $10^{38}$, et un `double` $10^{308}$. Toutefois, comme on l’a déjà dit, la précision est limitée et ne pourra évidemment pas conserver la valeur exacte d’un nombre à 38 ou 308 chiffres, le nombre sera arrondi.

#### Écrire une constante ####

Une constante flottant s’écrit sous la forme : `-3141.59e7` (ou avec un E majuscule), ce qui signifie $-3141,59 ×10^7$. La dernière partie indique l’**e**xposant, qui peut bien sûr être négatif (comme dans `945.68e-3`). On peut omettre diverses portions de cette syntaxe, comme le signe, l’exposant, la partie fractionnaire ou même la partie entière. En revanche, sans point ni exposant, le compilateur produira une constante entière (au pire, il est possible d’écrire `42.` au lieu de `42.0`).

Le type par défaut d’une telle constante est `double`, mais on peut le changer avec un suffixe (minuscule ou majuscule) : `f` produit un `float`, `l` un `long double`. Par exemple, `.1e-3f` ou `42.1337e-3l`.

Enfin, depuis C99 on peut écrire les constantes en hexadécimal. La syntaxe est : `0xFF24.A3p17` qui signifie $\text{0x42F3,A3}\times2^{17}$. Attention, la partie significative s’écrit en base 16, mais l’exposant (obligatoire) s’écrit en base 10 et désigne une puissance de **2** ! L’intérêt ? Obtenir une valeur exacte ! On a vu dans la partie précédente qu’écrire une constante en base 10 ne garantissait pas qu’elle soit représentée exactement en binaire. Spécifier la partie significative en hexadécimal et l’exposant en termes de puissance de 2 résout ce problème (dans la limite de la capacité du type, bien sûr).


### Quelques informations pratiques ###

#### Entrée et sortie formatées : `printf` & `scanf` ####

Par commodité, voici un tableau résumé des formateurs pour lire ou écrire des nombres flottants. Bien sûr, consultez le manuel pour des informations plus complètes (le format est extrêmement configurable).

| Type       | Utilisation                              |
| ---------- | ---------------------------------------- |
| `%f`, `%F` | Écrit le `double` sous la forme usuelle : la sortie est du type **[-]XXXX.XXX**, où les **X** sont des chiffres de 0 à 9 et **[-]** symbolise le signe « moins » éventuel. |
| `%e`, `%E` | Écrit le `double` en écriture scientifique ; la sortie est du type **[-]X.XXXXXXeYY** (le formateur `%E` donne un **E** majuscule). |
| `%g`, `%G` | Un mélange des formateurs précédents : utilise le premier style si le nombre n’est pas trop grand ou trop petit, le deuxième style sinon. |

Remarquez que tous ces formateurs attendent des flottants de type `double`. Il n’en existe pas pour `float`, ce qui est sans importance car on peut effectuer la conversion pour l’affichage (elle est automatique avec la syntaxe de `printf`). Le C99 nous permet d’ajouter la lettre `L` majuscule entre `%` et le formateur afin de correspondre à un `long double`.

| Type                               | Utilisation                              |
| ---------------------------------- | ---------------------------------------- |
| `%f`, `%F`, `%e`, `%E`, `%g`, `%G` | Lit un nombre à virgule flottante et l’écrit dans la variable de type `float` indiquée. Le nombre lu doit respecter la même syntaxe que les constantes du langage C. Contrairement à `printf`, tous ces formateurs sont équivalents. |

Attention ! Contrairement à `printf`, `scanf` travaille par défaut avec des `float`. Pour lire un `double`, il faut ajouter la lettre `l` minuscule entre `%` et le formateur ; pour un `long double`, il faut ajouter `L` (ou `ll`).

#### Les fonctions mathématiques avec `<math.h>` ####

La bibliothèque standard du C met à notre disposition toute une gamme de fonctions mathématiques : valeur absolue, maximum de deux nombres, arrondis en tous sens, puissances, fonctions trigonométriques, exponentielles et logarithmes, etc. Ces fonctions sont définies dans l’en-tête `<math.h>`. Chacune des fonctions existantes se décline en trois versions :

* une qui travaille avec des `double` : celle qui porte le nom « de base » (par exemple, `floor`, qui arrondit à l’inférieur) ;
* une qui travaille avec des `float` : il faut ajouter la lettre `f` à la fin du nom de la fonction (`floorf` dans notre exemple) ;
* une qui travaille avec des `long double` : il faut ajouter la lettre `l` à la fin du nom de la fonction (`floorl`).

Attention : lors de l’édition des liens, ces fonctions ne sont pas liées automatiquement à l’exécutable avec le reste de la bibliothèque standard, il faut le faire manuellement. Sous GCC, cela se fait avec le paramètre `-lm`.

Voilà, on a fini avec les ennuyantes questions de syntaxe, et nous pouvons maintenant aborder sereinement le cœur de ce cours.

# IEEE 754 : le codage en mémoire d’un nombre flottant
On va maintenant s’intéresser à la manière dont sont **représentés** en mémoire les nombres à virgule flottante. Ce que vais vous raconter dans cette partie **n’est pas dans la norme C**. La suite de ce cours se base sur la norme IEEE 754 (ou plus précisément ANSI/IEEE Std 754-1985). Celle-ci spécifie :

* la **manière de représenter les nombres flottants en mémoire** avec plusieurs formats ;
* cinq **opérations associées** : l’addition (`+`), la soustraction (`-`), la multiplication (`*`), la division (`/`) et la racine carrée (`sqrt()`) ;
* des **modes d’arrondi** ;
* des **exceptions**.

On reparlera des deux derniers points plus tard.

Cette norme est proposée par l’IEEE (*Institute of Electrical and Electronics Engineers*), une organisation américaine devenue référence en matière d’informatique. Puisque la norme C ne précise pas le codage utilisé, on peut en théorie tomber sur une implémentation qui en utilise un autre, mais dans les faits la norme IEEE 754 est aujourd’hui ultra-majoritaire. Un point sur la norme C sera fait à la fin de ce cours (ainsi qu’une manière de déterminer si IEEE 754 est bien employé chez soi).

### Principes généraux ###

Pour coder un nombre à virgule flottante, IEEE 754 se base sur sa notation binaire scientifique. À partir du bit de poids fort, un nombre flottant se décompose donc en **trois parties** en mémoire.

- Le **bit de signe** vaut 0 si le nombre est positif, 1 s’il est négatif. Le signe des nombres flottants est donc codé par le bit de poids fort et non selon la règle du complément à 2. En conséquence, il existe deux représentations pour *zéro* (c’est néanmoins un défaut mineur, les implémentations gérant cette dualité ; par exemple, ```+0.0 == -0.0``` renverra *vrai*), et les valeurs possibles sont totalement « symétriques » par rapport à zéro (c’est la raison pour laquelle j’utiliserai souvent le symbole ± par la suite).

- L’**exposant** représente la puissance à laquelle il faut élever 2 (et non 10 !). Le nombre *e* de bits qu’il occupe dépend de la taille du type. C’est un entier relatif. Pour le représenter, on n’utilise ni la règle du bit de signe, ni celle du complément à 2 (cela compliquerait la comparaison de nombres flottants, comme on le verra ensuite) ; on **décale** la valeur codée en lui ajoutant $2^{e-1}-1$, c’est-à-dire la valeur où tous les bits sauf celui de poids fort sont à 1 (donc 127 = *0b*01111111 si l’exposant est codé sur 8 bits, ou 1023 = *0b*01111111111 s’il est codé sur 11 bits). Ainsi, avec *e* = 7, la valeur 17 sera codée par 17+127 = 144 tandis que -23 sera codé par -23+127 = 104.
  <div data-alert="" class="alert-box success">Par la suite, j’emploierai les termes d’exposant <del>*décalé* et *réel*</del> *décalé* et *codé* pour différencier l’exposant tel qu’il est codé en mémoire de l’exposant ainsi représenté.</div>

- La **mantisse** code la **partie décimale en notation binaire scientifique** du nombre flottant. Sauf cas particuliers (zéro et certains nombres très petits) dont on reparlera, la partie entière vaut forcément 1 en binaire, c’est pourquoi on ne la donne pas. On parle de ***bit implicite***. On économise ainsi un bit, ce qui permet d’avoir une précision plus grande. La mantisse occupe les bits de poids faibles restants.

IEEE 754 spécifie deux grands formats basés sur ce modèle ; les deux types principaux du C pour les nombres à virgule flottante correspondent à ces deux formats.

| Nom dans la norme IEEE 754 | Type en C | Taille totale | *s*  | *e*  | *m*  | Chiffres significatifs en base 10 | Valeur absolue minimale | Valeur absolue maximale |
| -------------------------- | --------- | ------------- | ---- | ---- | ---- | --------------------------------- | ----------------------- | ----------------------- |
| *simple précision*         | `float`   | 32 bits       | 1    | 8    | 23   | 7                                 | $1{,}2 ×10^-38$         | $3{,}4 ×10^{+38}$       |
| *double précision*         | `double`  | 64 bits       | 1    | 11   | 52   | 16                                | $2{,}2 ×10^{-308}$      | $1{,}8 ×10^{+308}$      |

*s*, *e* et *m* sont le nombre de bits occupés par le signe, l’exposant et la mantisse, respectivement. Nous détaillerons plus tard les trois dernières colonnes. En résumé (pour un ```float``` de 32 bits), la représentation de -3141,5 est :

![De l’écriture décimale à la représentation en mémoire d’un nombre flottant normalisé.](http://progdupeu.pl/media/galleries/10/042d9799-8f7f-4a1c-bb39-9d1f6bde1360.png)

### Les différents types de nombres représentables ###

Il y a cependant des cas particuliers, car un nombre à virgule flottante peut représenter autre chose que des nombres « normaux ». Il peut aussi valoir :

- l’infini positif ou négatif (noté $\infty$). C’est par exemple le résultat de la division d’un nombre non nul par zéro (le signe dépendant alors du signe du numérateur et du zéro en dénominateur) ;
- NaN (*not a number*). **NaN est une valeur spéciale utilisée pour signaler une erreur**, comme dans $0 \div 0$ ou $\sqrt{-1}$. N’importe quel calcul avec un NaN doit renvoyer NaN (sauf quelques exceptions), et n’importe quelle comparaison avec un NaN doit renvoyer *faux* (sauf `!=`) ; NaN n’est même pas égal à lui-même, c’est pourquoi `x==x` peut renvoyer *faux* ;
- enfin, on n’a pas encore réglé le problème de zéro.

Quelques calculs avec ces valeurs particulières (le symbole ± signifie que le signe du résultat dépend de celui des deux opérandes selon la règle des signes) :

- $x \div 0 = \pm\infty$ ; 
- $0 \div \infty = \pm0$ ;
- $\infty \div \infty = \text{NaN}$ ;
- $0 \times \infty = \text{NaN}$ ;
- $(+\infty) + (+\infty) = +\infty$ ; 
- $(+\infty) - (+\infty) = \text{NaN}$.

<div data-alert class="alert-box">
Ça ne nous autorise pas à écrire des choses comme <code>var / 0</code> dans un programme ! En effet, la division par zéro de nombres entiers a un comportement indéterminé, c’est-à-dire non prévu par la norme du langage C. Ça signifie qu’il peut se passer n’importe quoi, selon le bon plaisir du compilateur, du système d’exploitation… Cela provoque une erreur fatale généralement et un beau plantage dans les règles de l’art.<br/>
En fait, c’est également indéterminé pour des nombres flottants. Les règles de calcul ci-dessus ne sont en fait garanties que par la norme IEEE 754, et non par la norme C elle-même.
</div>

Pour représenter tout ce petit monde, on utilise des valeurs spéciales de l’exposant.

- Si l’exposant est maximal (tous les bits à 1) et que la mantisse n’est pas nulle, alors c’est **NaN**.
- Si l’exposant est maximal et que la mantisse est nulle, alors c’est **l’infini** (positif ou négatif selon le bit de signe).
- Si l’exposant est minimal (tous les bits à 0) et que la mantisse n’est pas nulle, alors c’est un **nombre *dénormalisé* ** : on considère que le bit implicite (la partie entière en notation scientifique) vaut 0.
- Si l’exposant décalé vaut 0 et que la mantisse est nulle, alors c’est **zéro** (positif ou négatif selon le bit de signe).
- Dans tous les autres cas, c’est un **nombre *normalisé* ** : on considère que le bit implicite vaut 1. C’est le cas « normal ».

Récapitulons avec un joli tableau pour le format 32 bits :

| Type                   | Codage binaire                           | Codage hexadécimal                       | Valeur                                   |
| ---------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| ** *Not a Number* **   | [0/1] — 11111111 — 11111111111111111111111<br/>⋮<br/>[0/1] — 11111111 — 00000000000000000000001 | [7/F]F FF FF FF<br/>⋮<br/>[7/F]F 80 00 01 | NaN                                      |
| **infini**             | [0/1] — 11111111 — 00000000000000000000000 | [7/F]F 80 00 00                          | $± \infty$                               |
| **nombre normalisé**   | [0/1] — 11111110 — 11111111111111111111111<br/>⋮<br/>[0/1] — 00000001 — 00000000000000000000000 | [7/F]F 7F FF FF<br/>⋮<br/>[0/8]0 80 00 00 | $± 3{,}4028235 ×10^{+38}$<br/>⋮<br/>$± 1{,}1754944 ×10^{-38}$ |
| **nombre dénormalisé** | [0/1] — 00000000 — 11111111111111111111111<br/>⋮<br/>[0/1] — 00000000 — 00000000000000000000001 | [0/8]0 7F FF FF<br/>⋮<br/>[0/8]0 00 00 01 | $± 1{,}1754944 ×10^{-38}$<br/>⋮<br/>$± 1{,}4012985 ×10^{-45}$ |
| **zéro**               | [0/1] — 00000000 — 00000000000000000000000 | [0/8]0 00 00 00                          | ± 0                                      |

À titre informatif, voici aussi le même tableau pour le format 64 bits (sans le binaire, ça prend trop de place).

| Type                   | Codage hexadécimal                       | Valeur                                   |
| ---------------------- | ---------------------------------------- | ---------------------------------------- |
| ** *Not a Number* **   | [7/F]F FF FF FF   FF FF FF FF<br/>⋮<br/>[7/F]F F0 00 00   00 00 00 01 | NaN                                      |
| **infini**             | [7/F]F F0 00 00   00 00 00 00            | $± \infty$                               |
| **nombre normalisé**   | [7/F]F EF FF FF   FF FF FF FF<br/>⋮<br/>[0/8]0 10 00 00   00 00 00 00 | $± 1{,}7976931348623157 ×10{+308}$<br/>⋮<br/>$± 2{,}2250738585072014 ×10{-308}$ |
| **Nombre dénormalisé** | [0/8]0 0F FF FF   FF FF FF FF<br/>⋮<br/>[0/8]0 00 00 00   00 00 00 01 | $± 2{,}2250738585072010 ×10{-308}$<br/>⋮<br/>$± 5{,}0000000000000000 ×10{-324}$ |
| **Zéro**               | [0/8]0 00 00 00   00 00 00 00            | ± 0                                      |

Notons que pour passer d’un nombre positif à son équivalent négatif, il suffit d’additionner *0x* 8000 0000 à sa représentation en mémoire (*0x* 8000 0000 0000 0000 pour un `double`). Ceci nous servira plus tard.

### Nombres dénormalisés ###

Attardons-nous sur les nombres dénormalisés. **Un nombre dénormalisé est un nombre si petit (en valeur absolue) que l’on ne peut pas le représenter en mémoire en se basant sur son écriture scientifique.** Par exemple, $0b 1011 ×2^{-133}$ (soit environ $1{,}0101905 ×10^{-39}$) a pour écriture scientifique $0b 1{,}011 ×2^{-130}$, mais on ne peut pas stocker l’exposant -130 avec le format 32 bits.

**On ruse donc en écrivant le nombre avec le plus petit exposant possible.** Quel est cet exposant pour le format 32 bits ? Si vous avez répondu -127, vous êtes tombés dans le piège ! Pourtant, -127 est bien l’exposant minimal qu’on puisse coder et qui représente les nombres dénormalisés. En fait, les gens de chez IEEE ont décidé de compliquer la chose. Ils ont décidé que, pour les nombres dénormalisés, bien que la valeur en mémoire soit -127, **l’exposant codé serait -126**, c’est-à-dire le même que pour les plus petits nombres normalisés. Cette exception permet d’assurer une sorte de continuité entre zéro, les nombres dénormalisés et les premiers nombres normalisés. Puisqu’ils ont le même exposant, ceux-ci sont en effet disposés à intervalles réguliers (de pas $2^{126}$).

Dans notre exemple, cela donne $+0b0{,}0001011 ×2^{-126}$, qu’on code ensuite ceci comme un nombre normalisé :

![Schéma : de l’écriture décimale à la représentation en mémoire d’un nombre flottant dénormalisé.](http://progdupeu.pl/media/galleries/10/8905abd1-19be-4217-84e2-11a4dae0c7d3.png)

Vous comprenez maintenant pourquoi le bit implicite est à 0 pour un nombre dénormalisé.

Pour le format 32 bits, l’exposant sera -1022.

On peut trouver plusieurs raisons à l’introduction des nombres dénormalisés.

- Historiquement, l’exposant minimal servait pour représenter zéro, quelle que soit la valeur de la mantisse ; les nombres dénormalisés ont été introduits en 1985 avec la première version de la norme IEEE 754.
- D’ailleurs, si l’on avait choisi des nombres normalisés pour « remplir » cette plage de valeurs, la représentation de zéro n’aurait plus été cohérente avec celle-ci à cause du bit implicite.
- Les nombres dénormalisés permettent de représenter des nombres bien plus petits en valeur absolue. En effet, le plus petit nombre dénormalisé est $0b 0{,}00000000000000000000001 ×2^{-126}$, soit $1 ×2^{-149}$ ; avec des nombres normalisés, ça aurait été $0b 1,00000000000000000000001 ×2^{-127}$.

Cependant, tout cela a un coût. En plus de tout compliquer, les nombres dénormalisés perdent en précision au fur et à mesure qu’ils se rapprochent de zéro : c’est ce que nous allons voir dans la partie suivante.

# Un peu de mathématiques
Dans cette partie, nous allons continuer à approfondir les aspects théoriques. Nous allons étudier les propriétés mathématiques de ces nombres flottants, en particulier le passage du codage en mémoire à la valeur représentée.

### Retrouver la valeur du nombre flottant ###

<div data-alert class="alert-box success">
Pour la suite, vous devrez être à l'aise avec le binaire car je ne détaillerai pas les calculs. Sinon, autant passer cette partie. Il n’est évidemment pas utile de connaître par cœur les formules qu’on obtiendra, l’essentiel est de comprendre le principe.
</div>

Pour la suite, on note :

* $flottant$ la valeur du flottant représenté ;
* $m$ et $e$ le nombre de bits occupés par la mantisse et l'exposant (respectivement) ;
* $mantisse$ la mantisse (plus précisément, sa représentation entière) ;
* $exposant$ l'exposant **non-décalé** (en termes de puissances de 2) ; le décalage de l'exposant est $décalage =  2^{e-1}-1$ , on en déduit les valeurs limites de l'exposant ;
* la valeur minimale de l'exposant non-décalé, réservée aux zéros et nombres dénormalisés, est $exposantMin = 0 - décalage = 1 - 2^{e-1}$ (mais l'exposant **réel** des dénormalisés est $exposantMin+1$) ;
* la valeur maximale de l'exposant non-décalé, réservée aux infinis et NaN, est $exposantMax = (2^e-1) - décalage = 2^{e-1}$.

Pour retrouver la partie significative de la notation scientifique, il suffit de faire $1+\frac{mantisse}{2^m}$ si le nombre est normalisé, ou $0+\frac{mantisse}{2^m}$ s'il est dénormalisé.

* 1 ou 0 représente la partie entière du flottant (c'est-à-dire le bit implicite).
* La fraction qui suit représente la partie décimale (on a $0\le\frac{mantisse}{2^m}<1$ ).

Ensuite, il suffit de multiplier par la puissance de 2 indiquée par l'exposant réel, et d'adapter le signe selon le bit de signe :

* $flottant = \pm\enspace (1+\frac{mantisse}{2^m})\times2^{exposant}$ (normalisé) ;
* $flottant = \pm\enspace (0+\frac{mantisse}{2^m})\times2^{exposantMin+1}$ (dénormalisé).

#### Exemple 1 : Nombre normalisé ####

![Schéma : de la représentation en mémoire à l'écriture décimale d'un nombre flottant normalisé.](http://progdupeu.pl/media/galleries/10/8225a7c5-de24-4f1a-a319-a9292af7359f.png)

$\[\begin{aligned}flottant = - (1 + \frac{\textit{0b} 10001000101100000000000}{2^{23}}) \times2^{11} =  - (1 + \frac{4,478976\times10^6}{2^{23}}) \times2^{11}  =  -3141{,}5\end{aligned}\]$

On retrouve bien -3141,5.

#### Exemple 2 : Nombre dénormalisé ####

![Schéma : de la représentation en mémoire à l'écriture décimale d'un nombre flottant dénormalisé.](http://progdupeu.pl/media/galleries/10/b800a482-453c-4698-b377-3bee7b9ed89f.png)

$\[\begin{aligned}flottant = + (0 + \frac{\textit{0b} 00010110000000000000000}{2^{23}}) \times2^{-127+1}\\ = + (0 + \frac{720896}{2^{23}}) \times2^{-126}  \approx + 1{,}0101905\times10^{-39}\end{aligned}\]$

Là aussi, on retrouve bien le nombre de départ.

### Intervalle entre les nombres en fonction de l'exposant ###

Selon la norme IEEE 754, les nombres consécutifs de même exposant (qu'ils soient normalisés ou pas) sont « placés » à **intervalle régulier**. En effet, pour passer d'un nombre au nombre suivant, on ajoute toujours $\delta = 0{,}00000000000000000000001 \times2^{exposant} = \frac{1}{2^m} \times2^{exposant} = 2^{exposant-m}$.

Cet intervalle double quand on passe d'un exposant à l'exposant supérieur. Quelques valeurs remarquables pour un ```float``` (ne les apprenez pas !) :

* $2^{-126 - 23} = 2^{-149} \approx 1,40 ×10^{-45}$ : écart entre les nombres dénormalisés et les premiers nombres normalisés (et valeur du tout premier nombre dénormalisé) ;
* $2^{0 - 23} \approx 1,19 ×10^{-7}$ : écart entre les nombres normalisés compris entre 1 et 2 ;
* $1$ : écart entre les nombres normalisés d'exposant non-décalé 23 ;
* $2^{127 - 23} \approx 2,03 ×10^{31}$ : écart entre les plus grands nombres normalisés.

### Précision et chiffres significatifs ###

Vous aurez remarqué une colonne « chiffres significatifs » dans le premier tableau. C'est ce dont on va parler ici. Mais qu'est-ce qu'un **chiffre significatif** ? Le nombre de chiffres significatifs d'un nombre, c'est tout simplement le nombre de chiffres utilisés pour écrire ce nombre (dans une base numérique donnée). Par exemple, 43,1337 a 6 chiffres significatifs.

En physique et en chimie, on y voue une attention particulière. En effet, les mesures n'étant jamais exactes, on s'en sert pour **indiquer le degré de *précision* ** de la mesure (qui varie selon les instruments). En conséquence, pour un physicien, 42,1337 est différent de 42,13370 ; le second nombre est plus précis, car il indique quel est le $5^e$ chiffre après la virgule tandis que le premier nombre s'arrête au $4^e$ (le $5^e$ chiffre pourrait être 0, 1, 2, 3, 4, on n’en sait pas plus).

On compte les chiffres significatifs à partir du premier chiffre de gauche différent de 0, ce qui signifie que 3,1416 et 003,1416 sont équivalents (ils ont tous les deux 5 chiffres significatifs).

Vous pouvez maintenant comprendre la colonne du tableau : elle indique le nombre de chiffres significatifs en base 10 que nous permet chaque format :

* le format 32 bits garantit *grosso modo* **7** chiffres significatifs en base 10 ;
* le format 64 bits garantit *grosso modo* **16** chiffres significatifs en base 10.

Maintenant, *contrôle surprise :* combien de chiffres significatifs en base 2 permettent ces formats ? Mais si, vous pouvez tout à fait répondre, réfléchissez un peu. C'est tout simple : la mantisse représentant la partie significative du nombre, un nombre flottant a autant de chiffres significatifs en base 2 que sa mantisse occupe de bits. Hmm hmm. Vous êtes certain ? N'oubliez pas le bit implicite ! Il faut donc ajouter 1 à ce nombre. En vérité, **un nombre normalisé a donc $m+1$ chiffres significatifs en binaire**, soit 23+1=24 pour le format 32 bits, ou 52+1=53 pour le format 64 bits. On appelle souvent le nombre de chiffres significatifs en base 2 la **précision** tout court.

Mais ce n'est pas aussi simple ! Cette « formule » pour la précision n'est valable que pour les nombre normalisés. Voyez-vous pourquoi ?
Rappelez-vous que pour les nombres dénormalisés, le bit implicite, c'est-à-dire la partie entière du nombre, est 0. Comme c'est le premier chiffre, on ne le compte pas dans les chiffres significatifs.

Ah bah alors, pour un nombre dénormalisé, la précision c'est juste le nombre de bits de la mantisse ? Que nenni, jeune padawan. Un court schéma vaut mieux que de longues explications.

![Schéma : précision (nombre de chiffres significatifs en base 2) d'un nombre flottant normalisé ou non.](http://progdupeu.pl/media/galleries/10/5f3c28f0-b09e-495e-a816-58e32b2fc1aa.png)

Comme vous le voyez, **plus un nombre dénormalisé est proche de zéro, moins il est précis.**

# IEEE 754 : Exceptions & arrondis
Après deux chapitres de théorie pure sur le codage en mémoire d'un flottant, il est peut-être temps de changer de sujet, non ? La norme IEEE 754 ne se contente pas de décrire ce codage ; elle définit également des exceptions et des modes d'arrondis. Voyons ça.

### Les exceptions ###


Une **exception** est une sorte de « signal  qui est envoyé dans certains cas, afin de traiter les cas particuliers qui, s'ils étaient ignorés, seraient des erreurs. Cette définition est en fait générale (le terme vous est peut-être familier si vous faites du C++). 

C'est encore flou pour vous ? Ça ne fait rien, vous allez mieux comprendre avec cette liste. IEEE définit cinq exceptions :

* **invalid operation (opération invalide)** : se produit lorsqu'une opération interdite est effectuée ; le résultat du calcul en question sera NaN ;
* **division by zero (division par zéro)** : se produit lorsqu'on tente de diviser un nombre (non nul) par zéro ; le résultat sera ± \infty ;
* **overflow** : se produit lorsque le résultat d'un calcul est trop grand (en valeur absolue) pour être stocké ; on arrondit à ± \infty ;
* **underflow** : se produit lorsque le résultat d'un calcul est trop petit (en valeur absolue) pour être stocké ; on arrondit à zéro ;
* **inexact** : se produit lorsqu'on effectue un autre arrondi pour pouvoir stocker un nombre flottant (parce que le résultat a plus de chiffres significatifs qu'on peut en stocker).

### Les arrondis ###

C'est là que ça devient intéressant (enfin ça l'était déjà avant, c'est une façon de parler, n'est-ce-pas). Les imprécisions s'accumulent au fil des calculs, et au final vous pouvez obtenir quelque chose d'incohérent !

Ces imprécisions se manifestent par exemple lorsqu'on manipule deux nombres dont les exposants sont très éloignés. Par exemple, $4.2e17 + 13.37$ devrait donner $42000000000000001337$ soit $4.2000000000000001337e17$, mais il y a plus de chiffres significatifs qu'on ne peut en stocker ; le nombre sera donc arrondi, et finalement il vaudra $4.2e17$ comme si l'opération n'avait pas eu lieu ! Certains opérateurs entraînent beaucoup d'arrondis, comme l'addition ou la soustraction. Au contraire, d'autres, tels la multiplication ou la division, sont beaucoup plus sûrs. L'exemple précédent devrait vous aider à comprendre pourquoi.

Autre source de problèmes : comme vu précédemment, tous les nombres décimaux ne sont pas représentables de façon finie en binaire, et certains (comme $1.0/10.0 = .1$) sont donc arrondis.

Enfin, et en conséquence de ce qui vient d'être dit :

**Mewtow :**
> Les opérations avec les flottants ne sont pas associatives : l'ordre dans lequel on fait un calcul change le résultat. Par exemple, ```1 - (.2 + .2 + .2 + .2 + .2)``` aura un résultat différent de ```(((((1-.2)-.2)-.2)-.2)-.2)```.

Pas convaincus ? Vérifions ça !

```c
#include <stdio.h>

int main(void)
{
    printf("%g\n%g\n",  (1.0 - .2 - .2 - .2 - .2 - .2),
                       (1.0 - (.2 + .2 + .2 + .2 + .2))  );
    return 0;
}
```

Compilé chez moi, j'obtiens ceci :

```console
5.55112e-017
0
```

Ça parle tout seul.

#### Remarque hors-sujet (mais importante) ####

De façon plus générale, il faut rester vigilant lorsqu'on écrit des expressions impliquant des flottants, car des expressions a priori équivalentes, du point de vue d'un humain, se révèlent en fait différentes en pratique. L'exemple précédent l'illustre bien. D'autres cas parlants sont imaginables.

* Il y a pas mal de cas où ce qui change d'une expression à l'autre est le signe du zéro obtenu. Par exemple, x-y et -(y-x) ne sont pas équivalents car si les deux nombres sont égaux, alors la première expression donne +0.0 mais la deuxième -0.0.
* Il y a aussi des cas où les expressions ne sont pas équivalentes si on considère les valeurs « spéciales » des nombres, à savoir zéro, l'infini ou NaN :
    * ```x - x``` ne vaut pas 0.0 si x vaut l'infini ou NaN ;
    * ```0 * x``` ne vaut pas 0.0 si x vaut -0.0, l'infini ou NaN ;
    * ```x / x``` ne vaut pas 1.0 si x vaut zéro, l'infini ou NaN ;
    * ```x == x``` est faux si x vaut NaN ; :euh:
    * ```x != x``` est vrai si x vaut NaN.

Cette liste est tirée de la norme C99 (ISO/IEC 9899:TC3), que je vous invite à consulter si vous en voulez une plus complète (localisation dans le [draft PDF](http://www.open-std.org/JTC1/SC22/WG14/www/docs/n1256.pdf) de la norme : *Annex F — F.8.2 Expression transformations & F.8.3 Relational operators (p. 464-466)*).

### L'environnement des flottants : <fenv.h> ##

Cet ensemble de paramètres (les exceptions et le mode d'arrondi) forme ce qu'on appelle en informatique (c'est une définition générale) un **environnement**. C'est le cadre dans lequel on travaille.

Cet environnement pour les flottants est accessible avec le header standard (C99) ```<fenv.h>```. Il permet de manipuler les exceptions (les surveiller, en lever, etc.) et les modes d'arrondis (savoir quel est le mode utilisé et en changer). Je ne détaillerai pas son utilisation. Si vous voulez en savoir plus, consultez (par exemple) [cette page Wikipédia](http://en.wikipedia.org/wiki/Fenv.h) ou [cette page du site d'Open Group](http://pubs.opengroup.org/onlinepubs/009604599/basedefs/fenv.h.html).

# Comparer des nombres flottants
### L'infâme traîtrise de l'opérateur == ###

Bon. On a donc vu que l'utilisation des flottants en C est semée d'embûches : on risque des arrondis et des expressions « normalement » équivalentes ne le sont pas. Mais ce n'est pas tout ! Les comparaisons vont aussi vous donner du fil à retordre. En effet, **l'opérateur de comparaison == renvoie vrai si ses deux opérandes sont EXACTEMENT égales**, ou s'il compare un zéro positif et un zéro négatif. Or, avec les problèmes d'arrondis, une différence minuscule peut s'être glissée entre les deux nombres testés. Ainsi, **vous risquez de vous retrouver avec des égalités qui devraient être vraies, mais qui sont fausses** ! Cela peut faire planter lamentablement un programme (boucles infinies, instructions dans un bloc conditionnel jamais exécutées, etc) et la source du problème est difficilement identifiable pour un œil non averti.

Un petit exemple ? ```4.2e17 == 4.2e17 + 13.37``` renverra vrai (d'après l'exemple précédent). Autre exemple :

```c
int main(void) {
   float f=0;
   int i;
   
   for(i=0; i<100; ++i)
      f+= .01;
   
   if(f==1)   printf("f==1\n");
   else       printf("f!=1,  f==%f", f);
   
   return 0;
}
```

La sortie sera : 
```console
f!=1,  f==0.999999.
```

Évidemment, ces exemples sont stupides, mais ils permettent de mieux saisir dans quels cas se pose ce problème.

Les utilisateurs de GCC seront intéressés de savoir qu'il existe une option **-Wfloat-equal** qui déclenche un warning dès que l'on utilise l'opérateur == sur des nombres flottants.

**Vous :**
> Argghh ! mais c'est abominable !

Hé oui, c'est horrible. Vous pouvez encore renoncer à l'informatique et vous mettre au patchwork. Non, revenez ! Il y a un truc !

<div data-alert class="alert-box success">
La suite est fortement inspirée de <a href="http://www.cygnus-software.com/papers/comparingfloats/comparingfloats.htm">cette page Internet</a> (en anglais). Elle est complète et détaillée et je vous invite à la lire, car je n'aborderai pas forcément tout ce qu'elle dit (mais y ajouterai quelques broutilles de mon cru).
</div>

Alors, récapitulons : on cherche à comparer deux nombres à virgule flottante (```float``` ou ```double```) en tenant compte d'une marge d'erreur due aux arrondis ; on va pour cela écrire une fonction qui renverra un booléen (vrai ou faux, 1 ou 0), pour remplacer l'opérateur ==.

### L'écart absolu & l'écart relatif ###

La première méthode consiste tout simplement à mesurer l'écart entre les deux nombres. On parle d'**écart absolu** (par opposition à l'écart relatif que nous verrons par la suite). Si cet écart est inférieur à une certaine valeur (souvent appelée epsilon, ce qui pour un mathématicien signifie « valeur très petite »), alors on considère que les deux nombres sont égaux.

```c
#include <math.h>   // pour la fonction fabs, renvoyant la valeur absolue d'un flottant

#define  EPSILON  1e-8

/* ici pour des doubles, mais on fait la même chose pour des floats */
int doublesAreEqual(double a, double b) {
   return fabs(a-b) <= EPSILON;
/* La fonction fabs renvoie la valeur absolue (c'est-à-dire positive) du nombre
   de type double passé en argument ; ses équivalents (C99) sont fabsf pour les
   float, et fabsl pour les long double (pensez donc à adapter votre code en
   conséquence pour comparer les autres types flottants). */
}
```

Ici, *fabs* nous renvoie l'écart absolu entre a et b. Le reste est facile à comprendre. Simple, non ?

Oui, mais c'est encore loin d'être parfait : en effet, un écart de $1e-8$ (soit $0.00000001$) peut s'avérer judicieux pour comparer des nombres compris entre 0,1 et 1 (par exemple, en fonction de la précision que vous souhaitez), mais trop petit pour des nombres entre 100 et 1000, ou trop grand pour des nombres entre 0,00001 et 0,0001 ; si vous comparez des nombres compris entre 0,00000001 et 0,0000001, vous avez même une marge d'erreur de 100% ! N'employez donc cette méthode que si vous êtes sûr de l'ordre de grandeur des nombres à comparer, et choisissez un *epsilon* adapté.

Pour pallier à ce problème et faire une fonction plus générique, une solution serait de passer l'écart maximal en argument à la fonction et non de se baser sur une constante de préprocesseur ; ainsi, l'utilisateur pourrait fournir un écart adapté à l'ordre de grandeur des nombres qu'il veut comparer. Allons plus loin. On va employer l'**écart relatif**. Celui-ci ramène l'écart absolu dans les proportions des nombres comparés :

```c
#include <math.h>

#define  EPSILON  1e-8

int doublesAreEqual(double a, double b) {
   if(a==b)   return 1;   // si a et b valent zéro  (explications plus bas)
   
   double absError= fabs(a-b);   // écart absolu
   a= fabs(a);   // on ne garde que les valeurs absolues pour la suite …
   b= fabs(b);   // … pour pouvoir calculer le nombre le plus grand en valeur absolue
   
   return  ( absError / (a>b? a:b) )  <=  EPSILON;
}
```

On divise l'écart absolu par le plus grand des deux nombres en valeur absolue (signification du ternaire), pour avoir quelque chose d'adapté à l'ordre de grandeur des deux nombres. La ligne commençant par ```if (a == b)``` vous paraît sans doute bizarre. Elle est là pour gérer le cas où a et b sont égaux à zéro. En effet, sans elle, on aurait une division par zéro qui vaudrait NaN, et la comparaison serait donc toujours fausse. On compare donc les deux nombres pour que la fonction renvoie vrai s'ils sont identiques et égaux à zéro (positif ou négatif).

<div data-alert class="alert-box success">
Remarque : Dans ce tutoriel, j'utilise le C99. Celui-ci autorise de déclarer des variables après des instructions. Si c'était juste pour ce détail, ce serait superflu, mais plus loin on en aura réellement besoin.
</div>

Cependant, il subsiste un problème : dans le cas de deux nombres très proches de zéro, l'écart relatif sera très important (car on divise par un tout petit nombre) alors que ces deux nombres seront très proches ... Pour y remédier, on réintroduit l'écart absolu : la fonction retournerait vrai si l'écart absolu ou l'écart relatif (au moins l'un des deux) est inférieur à une valeur donnée (qu'on passe en argument à la fonction). D'où le code définitif :

```c
#include <math.h>

#define  EPSILON  1e-8

int doublesAreEqual(double a, double b, double maxAbs, double maxRel) {
   if(a==b)   return 1;
   
   double absError= fabs(a-b);
   a= fabs(a);
   b= fabs(b);
   
   return   absError <= maxAbs   ||   ( absError / (a>b? a:b) )  <=  maxRel;
}
```

### La représentation en mémoire convertie en entier ###

Maintenant, vous avez du code à peu près potable et fonctionnel. Toutefois, il existe une autre manière de faire, plus pratique mais un peu plus *hard*. Accrochez-vous, ça va secouer. 

Imaginez qu'au lieu de se baser sur l'écart entre les deux nombres, on cherche à déterminer combien de nombres possibles les séparent ? Ainsi, on aimerait placer une marge d'erreur, non sur la valeur elle-même des nombres flottants, mais sur leur « éloignement », pour pouvoir dire par exemple : « *J'accepte les 5 nombres en dessous et les 5 nombres au dessus de la valeur machin* ». Eh bien, grâce au format de l'IEEE, c'est possible !

<div data-alert class="alert-box">
Ici, on a donc impérativement besoin du format IEEE 754 ! L'astuce présentée est basée dessus. Si jamais ce n'est pas ce format que vous avez chez vous, vous ne pourrez sans doute pas la mettre en œuvre. Toutefois, je vous invite à lire quand même ce qui suit, cela pourra peut-être vous intéresser ; et en tous cas, jetez un œil au code complet (dernière sous-partie), car j’y présente des idées qui pourront vous intéresser même si vous utilisez l'écart absolu/relatif.
</div>

Ce format garantit que « *si deux nombres du même type à virgule flottante sont consécutifs, alors leurs représentations entières le sont aussi (selon le bit de poids fort pour déterminer le signe, et non la règle du complément à 2).* » Que signifie ce charabia ? Eh bien, prenons 2 nombres de type ```float``` codés sur 32 bits selon le format IEEE 754 (évidemment, cela s'applique aussi aux ```double```) :

```console
Valeur du float                       représentation en mémoire
                     binaire                                      hexadécimal    en base 10
+1.9999998           0   0111111 1   1111111 11111111 11111110    3F FF FF FE    1073741822
+1.9999999           0   0111111 1   1111111 11111111 11111111    3F FF FF FF    1073741823
```

Ces 2 nombres sont « consécutifs », il ne peut pas y avoir d'autre nombre du même type dont la valeur serait comprise entre les 2. Or, que constate-t-on ? **Leurs représentations en mémoire, si on les lit comme des nombres entiers**, sont également consécutives ! Pour savoir si les deux nombres à comparer sont « voisins », il suffit donc de comparer leur représentation en mémoire convertie en nombre entier.

<div data-alert class="alert-box success">
Par la suite, je dirais (abusivement, certes) « représentation entière » plutôt que « représentation en mémoire lue comme un entier », c'est quand même plus court.
</div>

Mais comment accéder à cette représentation entière ? Ben, c'est simple, il suffit de faire ```(int) monFloat``` … Surtout pas ! En faisant ça, on convertit le nombre à virgule en nombre entier, et on obtient donc le nombre de départ arrondi à l'unité. Ça n'a rien à voir avec ce que l'on veut. La bonne formule est donc, tenez-vous bien :

```c
*(int*)&monFloat
```

Je vous laisse méditer là-dessus. Ce n'est pas vraiment compliqué, quand on y pense. Quelques explications si vraiment vous bloquez :

[secret]{
Pour comprendre cette expression, il faut en fait la lire de droite à gauche :

* `&monFloat` renvoie l'adresse de la variable de type `float`, donc un pointeur sur `float` ;
* `(int*)` convertit ce pointeur sur `float` en un pointeur sur `int` ; ainsi, l'ordinateur considérera la variable pointée comme un `int` et non plus comme un `float` ;
* et hop ! le tour est joué, il ne nous reste plus qu'à déréférencer ce pointeur avec `*` pour accéder à la variable pointée.
  }

Maintenant, du code avec ce que je viens de vous dire :

```c
#include <stdlib.h>   // pour la fonction abs, renvoyant la valeur absolue d'un entier
#include <stdint.h>   /* header du C99, qui fournit des types entiers de taille fixe :
                         —  int32_t,  int64_t : entier signé de 32 ou 64 bits ;
                         — uint32_t, uint64_t : entier non-signé de 32 ou 64 bits. */

#define  INTREPOFFLOAT(f)   ( *(int32_t*)&(f) )   // représentation entière d'un float (32 bits)
#define  INTREPOFDOUBLE(d)  ( *(int64_t*)&(d) )   // représentation entière d'un double (64 bits)

#define  MAXULPS  5

/* ici pour des floats, mais on fait exactement pareil pour des doubles */
int floatsAreEqual(float a, float b) {
   if(a==b)   return 1;
   
   return abs( INTREPOFFLOAT(a) - INTREPOFFLOAT(b) )  <=  MAXULPS;
/* attention à la fonction abs, qui prend un int en argument ; un int fait 16
   ou 32 bits : il peut donc être trop petit pour contenir les 32 bits de la
   représentation entière d'un float, et sera de toutes façons insuffisant
   pour les 64 bits de celle d'un double. Voyez la fonction labs qui prend un
   long int, ou llabs (C99) qui prend un long long int, ou mieux, écrivez vos
   propres fonctions de valeur absolue, pour 32 et 64 bits (avec les types de
   <stdint.h>) ; ainsi, vous n'aurez plus de problèmes de taille des types
   pouvant varier. Ici, je garde les fonctions standards par souci de clarté. */
}
```

La constante MAXULPS (de ULP, « *Unit of Least Precision* », c'est-à-dire la valeur qui sépare deux flottants consécutifs) nous fournit notre marge d'erreur. Si l'écart entre les représentations entières est inférieur à MAXULPS, alors on considère que les nombres sont égaux.

Ici, la ligne commençant par ```if (a == b)``` est là pour gérer le cas où les deux nombres seraient +0.0 et -0.0. En effet, +0.0 et -0.0 ont des représentations entières très différentes, ce qui fait que la fonction retournerait faux sans ce test préalable.

En outre, remarquez qu'on utilise les types entiers définis dans le header standard ```<stdint.h>``` au lieu des types habituels (```int```, ```long int```, etc). En effet, la taille de ces derniers dépend de l'implémentation et n'est donc pas connue, il serait donc dangereux (non portable) de s'appuyer dessus ; au contraire, la taille de ```int32_t``` et ```int64_t``` est connue et fixe. Ce header a été introduit avec C99, c'est pourquoi je vous ai dit qu'on allait devoir se baser sur cette version du langage C.

Un peu de maths pour vous aider à choisir votre marge d'erreur !

Une variation de $\Delta mantisse$ dans la représentation entière de la mantisse codée sur $m$ bits correspond à une variation de la valeur du flottant donnée par la formule suivante : $\Delta flottant = \frac{\Delta mantisse}{2^m} \times 2^{exposant} = \Delta mantisse \times 2^{exposant-m}$ (où $exposant$ est l'exposant réel). Cette formule provient directement de celle donnant l'intervalle entre les nombres consécutifs en fonction de l'exposant.

Pour un nombre flottant compris entre 1 et 2, une variation d'un ULP correspond donc à une variation de valeur du nombre flottant de $\frac{1}{2^{23}} \approx 1{,}192\times10^{-7}$ pour un ```float``` et $\frac{1}{2^{52}} \approx 2{,}220\times10^{-16}$ pour un ```double```.

Si vous choisissez comme moi une marge de 5 ULP, alors votre marge de valeur (pour un nombre flottant compris entre 1 et 2) sera $\frac{5}{2^{23}} \approx 5{,}960\times10^{-7}$ pour un ```float``` et $\frac{5}{2^{52}} \approx 1{,}110\times10^{-15}$ pour un ```double```.

Mais (hé oui, encore un « mais ») il reste encore un détail à régler, et à ce stade j'aimerais que vous leviez tous la main pour me le dire. Allez, un indice : ça concerne la parenthèse de la phrase en italique de tout à l'heure ... Ben oui, le signe ! Les flottants, selon la norme IEEE 754, sont signés selon le principe du bit de signe et non du complément à 2. Or, les entiers (du moins sur la grande majorité des ordinateurs aujourd'hui) sont stockés… selon la règle du complément à 2.

Un exemple pour bien voir (je ne vous met plus le binaire, vous êtes grands maintenant) :

```console
Valeur du float              représentation en mémoire
                         hexadécimal    en base 10 selon le complément à 2
+4.2038954 e-45          00 00 00 03     3
+2.8025969 e-45          00 00 00 02     2
+1.4012985 e-45          00 00 00 01     1
+0.0000000               00 00 00 00     0
-0.0000000               80 00 00 00    -2147483648
-1.4012985 e-45          80 00 00 01    -2147483647
-2.8025969 e-45          80 00 00 02    -2147483646
-4.2038954 e-45          80 00 00 03    -2147483645
```

Comme vous le voyez, le dernier nombre est inférieur à l'avant-dernier, et pourtant sa représentation entière (en ```signed``` comme en ```unsigned```) est supérieure ! En vérité, cela ne porte pas à conséquence si l'on compare deux nombres négatifs, car on ne s'intéresse qu'à l'écart entre les représentations entières, qui lui ne change pas ; le problème se pose lorsque l'on compare deux nombres de signes opposés.

Heureusement, il existe une solution. Il suffit de convertir les nombres négatifs selon la règle du bit de signe, en nombres négatifs selon la règle du complément à 2. Je vous laisse chercher ; aidez-vous de l'exemple ci-dessus. Trouvé ? Il suffit de garder la valeur telle quelle si le flottant est positif, ou s'il est négatif de soustraire $0x 80 00 00 00$ à la représentation entière puis d'inverser le signe de cette représentation. Cela revient à faire l'opération suivante :

```c
représentation = 0x 8000 0000 - représentation;
```

Similairement, pour un ```double``` de 64 bits, on fera ```représentation = 0x 8000 0000 0000 0000 - représentation;```.

On obtient alors ceci :

```console
Valeur du float              représentation transformée
                         hexadécimal    en base 10 selon le complément à 2
+4.2038954 e-45          00 00 00 03     3
+2.8025969 e-45          00 00 00 02     2
+1.4012985 e-45          00 00 00 01     1
+0.0000000               00 00 00 00     0
-0.0000000               00 00 00 00     0   *    (* = a été transformé)
-1.4012985 e-45          FF FF FF FF    -1   *
-2.8025969 e-45          FF FF FF FE    -2   *
-4.2038954 e-45          FF FF FF FD    -3   *
```

Comme vous le voyez, les représentations entières sont maintenant cohérentes, on peut les comparer sans problème. Et même les deux zéros (positif et négatif) sont égaux !

```c
#include <stdlib.h>
#include <stdint.h>

#define  INTREPOFFLOAT(f)   ( *(int32_t*)&(f) )
#define  INTREPOFDOUBLE(d)  ( *(int64_t*)&(d) )

#define  MAXULPS  5

int floatsAreEqual(float a, float b) {
   int32_t aInt= INTREPOFFLOAT(a);   // représentations entières
   int32_t bInt= INTREPOFFLOAT(b);
   
   if(aInt<0)   aInt= 0x80000000 - aInt;   // ou 0x8000000000000000 pour des doubles
   if(bInt<0)   bInt= 0x80000000 - bInt;
/* NOTE: on teste (aInt<0) et non (a<0). En effet, si a==-0.0 (zéro négatif),
   alors le test (a<0) renverrait faux, et on garderait la représentation de
   -0.0, à savoir 0x80000000. La règle du complément à 2 garde l'avantage du
   bit de signe : si le bit de poids fort est à 1, alors le nombre entier est
   négatif, et réciproquement ; on peut donc utiliser le test sur l'entier et
   non sur le flottant pour savoir s'il faut « transformer » la représentation. */
   
   return abs( aInt - bInt )  <=  MAXULPS;
}
```

Attention à bien utiliser les types signés (```int32_t``` et ```int64_t```) et non les non signés (```uint32_t``` et ```uint64_t```).

Bon, ce n'est pas encore parfait, mais c'est très convenable. Quelques points améliorables :

* les infinis : comme vu précédemment, les infinis sont adjacents aux plus grands nombres en valeur absolue. Notre fonction pourrait par exemple nous dire qu'un nombre positif très très très grand et $+\infty$ sont égaux, alors que ce n'est pas vrai (ne discutez pas, d'un point de vue mathématique c'est faux) ;
* les NaN : de même, certains NaN pourraient être comparés comme égaux à l'infini ou à un nombre extrêmement grand en valeur absolue, voire à un autre NaN. Or, normalement, n'importe quelle comparaison avec un NaN (hormis !=) devrait valoir faux.

Ces détails peuvent être corrigés avec des vérifications supplémentaires. À ce sujet, les [macros de test de nombres flottants (C99)](http://www.man-linux-magique.net/man3/isinf.html) peuvent servir. En résumé (je vous invite à consulter le manuel avec le lien précédent) :

** Le manuel : fpclassify, isfinite, isnormal, isnan, isinf **
> Depuis le C99, le header <math.h> définit les macros *isfinite*, *isnormal*, *isnan* et *isinf* ; elles prennent toutes un nombre flottant en argument (peu importe son type), et renvoient un booléen indiquant respectivement si le nombre est fini, normalisé, NaN ou infini (le retour de *isinf* n'est pas forcément 1 ou 0). La macro *fpclassify* est également définie. On l'utilise comme les autres, et sa valeur de retour indique le type du nombre flottant (FP_ZERO, FP_SUBNORMAL, FP_NORMAL, FP_INFINITE, FP_NAN).

### Code complet ###

Je vous propose finalement un code complet. J'y ai introduit une fonction *cmpFloats* (ou *cmpDoubles*) de mon cru qui permet une comparaison plus générale : en effet, à la manière de *strcmp*, elle renvoie -1 si a > b, 0 si a == b ou 1 si a < b ; elle renvoie par ailleurs -2 si l'un des deux nombres au moins est NaN. Ainsi, il devient plus facile de tester les deux nombres (j'ai de plus écrit des macros simples pour faciliter les comparaisons). En effet, avant, pour tester par exemple a<b (strictement inférieur), il fallait faire ```if (a < b && !floatsAreEqual(a, b))```, ce qui était plus lourd à écrire.

#### En-tête ####

Code disponible [à cette adresse](http://paste.awesom.eu/0f6&ln). Remarquez que j'ai mis des macros en commentaires (correspondant à <= et >=), qui on été remplacées par d'autres. En effet, ces macros ne sont plus valables si cmp… renvoie -2 (qui est le code pour NaN).

<div data-alert class="alert-box success">
Les macros CMP…_GTEQUAL de remplacement sont très bizarres. En fait, c'est une astuce que j'ai trouvé pour éviter quelque chose du type <code>(cmpFloats((a), (b)) ==-1 || cmpFloats((a), (b)) == 0)</code>, ce qui est dangereux car a et b sont potentiellement évalués 2 fois, et non optimisé car on appelle 2 fois la fonction cmp. En fait, les seules macros qui renverront vrai en cas de NaN seront CMP…_NAN et CMP…_UNEQUAL.
</div>

L'utilisation de ces macros est conseillée dans le cas d'un test « simple », c'est-à-dire avec un seul test ; par exemple :

```c
instructions1;
if (CMPFLOATS_GT(a, b))
{
    // a>b
    instructions2;
}
instructions3;
```

En revanche, il vaut mieux éviter de les enchaîner pour traiter différentes possibilités (si a < b, faire machin, si a > b, faire truc...) le ```else``` est aussi à éviter (car il engloberait aussi le cas de NaN, ce qui dans la plupart des cas n'est pas voulu) :

```c
instructions1;
if (CMPFLOATS_GT(a, b))
{
    // a > b
    instructions2;
}
else if (CMPFLOATS_LT(a, b))
{
    // a < b
    /*  /!\  on appelle la fonction cmpFloats 2 fois  */
    instructions2b;
}
else // a == b
{
    instructions2t;   /*  /!\  ce code est aussi exécuté dans le cas de NaN !  */
}
instructions3;
```

Il vaut mieux utiliser un ```switch``` dans ce cas, qui n'appelle la fonction qu'une seule fois tout en permettant un contrôle précis :

```c
instructions1;
switch (cmpFloats(a, b))
{
    case -1: // a > b
        instructions2;
    break;

    case  0: // a == b
        instructions2t;
    break;

    case  1: // a < b
        instructions2b;
    break;

    default: break; // NaN
}
instructions3;
```

Autre exemple pour bien saisir l'utilisation du ```switch``` :

```c
instructions1;
switch (cmpFloats(a, b))
{
    case -1: // a > b
    case  0: // a == b
        instructions2;   // ce code est donc exécuté si a >= b
    break;

    case  1: // a < b
        instructions2b;
    break;

    default: break; // NaN
}
instructions3;
```

#### Fichier source ####

Fichier disponible [à cette adresse](http://paste.awesom.eu/KHF&ln). Ce code est à compiler en C99.

Si vous programmez en C++, pourquoi ne pas surcharger les opérateurs de comparaison ? Cela vous simplifiera la vie (toutefois, vous risquerez alors, à la longue, d'oublier que vous avez fait quelque chose pour comparer tranquillement des flottants, et un jour ça ne marchera plus car vous n'aurez plus inclus votre petit header magique.)

# Mais qu'en dit la norme C ?
Rassurez-vous, si vous êtes fatigués, vous pouvez passer cette partie. Elle se destine aux petits curieux qui voudraient aller plus loin pour savoir plus précisément quelle relation entretient IEEE 754 vis à vis de la norme C, et comment déterminer si le compilateur suit bien les formats IEEE 754 ou pas. Car en C, il y a foule de gourous barbus qui se cramponnent à la norme comme une huître à son rocher, la citent comme un texte sacré, et viennent hurler à l’hérésie au moindre bout de code non « portable ». Et ils ont bien raison.

### IEEE 754 et la norme C ###

La norme C90 était très floue sur ce sujet, et n'imposait ni ne privilégiait aucun format pour les nombres à virgule flottante. Le C99 a changé cela. En effet, la norme C99 (alias ISO/IEC 9899:TC3, téléchargeable [ici](http://www.open-std.org/JTC1/SC22/WG14/www/docs/n1256.pdf) en PDF) introduit le support de la norme IEEE 754.

Voici un extrait le montrant (issu de la liste des changements majeurs depuis le C90) :

**ISO/IEC 9899:TC3 — Foreword (§5, p. xi-xii)**
> This second edition cancels and replaces the first edition, ISO/IEC 9899:1990 […]. Major changes from the previous edition include:
>
> […]
>
> — IEC 60559 (also known as IEC 559 or IEEE arithmetic) support
>
> […]

Quoi ? C'est quoi IEC 60559 ? Encore une nouvelle norme au nom tordu ! Oulala, pas de panique ! IEC 60559, c'est juste un autre nom de IEEE 754. Cette norme est donc **supportée par le langage C depuis sa version C99**. Attention ! Supportée ne veut pas dire imposée. Les compilateurs ne sont pas obligés d'adopter les formats IEEE 754. C'est juste que s'ils le font, ils doivent suivre les règles de support spécifiées par la norme C99. Ce passage le montre clairement :

** ISO/IEC 9899:TC3 — 6.2.6: Representation of types — General (§1, p.37) **
> The representations of all types are unspecified except as stated in this subclause. […]

Cela signifie que la représentation de n'importe quel type (et pas seulement les flottants) est inconnue ; elle reste aux choix du compilateur. Certains compilateurs peuvent supporter plusieurs formats ; dans ce cas, vous devrez spécifier lequel utiliser avec des arguments (sauf si vous voulez garder le format par défaut). GCC, pour sa part, implémente IEEE 754 par défaut, ses utilisateurs peuvent donc dormir sur leurs deux oreilles.

Mais quelles sont les règles de support de IEEE 754 selon le C99 ?  La norme C99 comporte une annexe (l'annexe F) dédiée aux nombres flottants, où se trouve la réponse à cette question. En voici le début :

** ISO/IEC 9899:TC3 — Annex F (normative): IEC 60559 floating-point arithmetic (p.444) **
> F.1 Introduction
>
> This annex specifies C language support for the IEC 60559 floating-point standard. […] An implementation that defines __STDC_IEC_559__ shall conform to the specifications in this annex. […]
>
> F.2 Types
>
> The C floating types match the IEC 60559 formats as follows:
>
>    — The float type matches the IEC 60559 single format.
>
>    — The double type matches the IEC 60559 double format.
>
>    — The long double type matches an IEC 60559 extended format, else a non-IEC 60559 extended format, else the IEC 60559 double format.
>
> Any non-IEC 60559 extended format used for the long double type shall have more precision than IEC 60559 double and at least the range of IEC 60559 double.
>
> Recommended practice
>
> The long double type should match an IEC 60559 extended format.
>
> […]

La deuxième partie dit que le type ```float``` du langage C doit correspondre au format simple précision (32 bits) de IEC 60559 (alias IEEE 754), etc. Il est aussi question du type ```long double```, dont j'ai peu parlé dans ce tutoriel ; sachez qu'en C, son format est moins bien défini, mais qu'il correspond souvent au format de double précision étendue de IEEE 754 (dont je n'ai pas parlé non plus), ou alors au format de double précision tout court (comme un ```double```).

Je ne parlerai pas de la suite de cette annexe, vous pouvez la lire si vous voulez (vous êtes grands). Elle décrit notamment le comportement des opérations sur les flottants.

Enfin, sachez que :

** Taurre **
> un système peut visiblement encoder les nombres flottants suivant le format défini par la norme IEEE 754, sans pour autant remplir toutes les conditions de l'annexe F de la norme C99 ([cf ce sujet](http://bytes.com/topic/c/answers/770825-ieee754-fp)).

Les conditions en questions sont surtout des détails du comportement des calculs. Dans le cadre de ce tutoriel, qui s'est surtout focalisé sur les formats de représentation des flottants, ça ne devrait pas poser trop de problèmes.

Le non-respect partiel de la norme IEEE 754 peut aussi être le fait d'options du compilateur. Par exemple, l'option d'optimisation **-ffast-math** de GCC améliore les performances en accélérant les calculs sur les nombres flottants, mais enfreint certaines règles de IEEE 754.

Je reviens sur l'introduction, elle contient quelque chose d'intéressant. Il est dit que si la macro __STDC_IEC_559__ est définie, alors c'est le format IEEE 754 qui est utilisé. Cela peut vous être utile pour faire des tests ou adapter votre code. Cependant, le contraire n'est pas vrai ! Vous pouvez parfaitement avoir une implémentation qui suit IEEE 754 mais qui ne définit pas cette constante. Cela semble être le cas de GCC sous Windows (portage MinGW par exemple), car GCC laisse cette définition aux headers du système ; or, ceux de Windows ne définissent pas __STDC_IEC_559__, en partie parce qu'il y aurait un risque d'incompatibilité entre GCC et la bibliothèque C de Windows.

### En pratique : savoir si l'implémentation utilise IEEE 754 ###

Puisqu'on ne peut pas compter sur la constante __STDC_IEC_559__ pour nous renseigner, il faut trouver un autre moyen de déterminer si oui ou non on travaille avec IEEE 754. Pour cela, le meilleur moyen reste de se renseigner auprès de votre compilateur favori et/ou de votre plateforme cible. Toutefois, si vous tenez vraiment à faire cette vérification avec du code, je peux vous offrir des pistes.

* **dynamiquement (c'est-à-dire au moment de l'exécution de votre programme)** : Vous pouvez par exemple déclarer un certain nombre de variables de type à virgule flottante, puis vérifier que leur représentation mémoire correspond à celle attendue en se basant sur IEEE 754. Il faudrait effectuer cette série de tests pour les différents types de nombres (zéros, dénormalisés, normalisés, infinis, NaN). Un tel code ne serait pas infaillible (on peut très bien imaginer des formats ressemblant à IEEE 754, qui passeraient avec succès tous les tests) mais il permet d'éliminer certains formats. L'inconvénient est que du code inutile est intégré à l'exécutable, et que l'on perd du temps à chaque exécution du programme lorsqu'on effectue ces vérifications. À éviter en pratique, donc.
  D'un point de vue technique, cela reste cependant un bon exercice. :ange: 

* **statiquement (c'est-à-dire lors de la compilation)** : Pour cela, il faut vous appuyer sur votre ami le préprocesseur. Sans détailler, vous pouvez tester la valeur des macros définies dans le header [<float.h>](http://www.gnu.org/savannah-checkouts/gnu/libc/manual/html_node/Floating-Type-Macros.html) du C99 ; celles-ci caractérisent l'implémentation des nombres flottants : précision, exposants minimum et maximum, valeurs minimales et maximales. Tout cela en 3 variantes pour chacun des 3 types à virgule flottante du C. Cette approche présente l'avantage de ne garder que le code nécessaire lors de la compilation et de ne pas faire cette vérification à l'exécution.Mais avouez que c'est fichtrement moins rigolo.

L'avantage est que le bon fonctionnement du code serait indépendant du compilateur utilisé, facilitant ainsi les échanges de code. Notez toutefois que les propositions ci-dessus vérifient la représentation en mémoire, mais pas les différentes opérations sur les flottants.

Ce cours touche enfin à sa fin ! On sait maintenant comment manier correctement des nombres réels, et surtout ce qui se cache sous le capot. On a vu les difficultés qu’ils causent, et des solutions.

Quelques (res)sources…

* articles de Wikipédia : [virgule flottante](http://fr.wikipedia.org/wiki/Virgule_flottante), [IEEE 754](http://fr.wikipedia.org/wiki/IEEE_754) (n’hésitez pas à aller sur les articles anglais qui sont bien plus complets),
* wikilivre (actuellement en rédaction) : [Arithmétique flottante](http://fr.wikibooks.org/wiki/Arithmétique_flottante),
* page présentant l’astuce pour comparer des flottants : *[Comparing floating point numbers](http://www.cygnus-software.com/papers/comparingfloats/comparingfloats.htm)* par Bruce Dawson **(en)**,
* la norme C99 ! ou plutôt son draft (n1256), disponible [ici](http://www.open-std.org/JTC1/SC22/WG14/www/docs/n1256.pdf) en PDF **(en)**…

… et des liens additionnels :

* page de manuel de *isinf*, *isnan*, etc. : [macros de classification en virgule flottante](http://www.man-linux-magique.net/man3/isinf.html),
* pages du manuel de la lib GNU C concernant les flottants (concepts, constantes fournies par `<float.h>`, exemple pour IEEE 754) : *[floating type macros](http://www.gnu.org/savannah-checkouts/gnu/libc/manual/html_node/Floating-Type-Macros.html)* **(en)**,
* et ce **site très pratique permettant de calculer la représentation en mémoire d’un nombre à virgule et l’inverse, pour les deux formats principaux de IEEE 754 (32 et 64 bits) : *[IEEE-754 Analysis](http://babbage.cs.qc.edu/IEEE-754/)* (en)**.
