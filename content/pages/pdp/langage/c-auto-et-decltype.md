Title: C++, auto et decltype
Order: 9
Date: 2015-09-14
Tags: c, decltype, tutoriel
Slug: c-auto-et-decltype
Authors: informaticienzero

La détection de type par le compilateur est une fonctionnalité intéressante qui nous permet d'éviter de la redondance dans le code. Plusieurs langages modernes intègrent cette fonctionnalité. Or, avant 2011, la seule déduction de type qui existait en C++ était celle des templates. Mais avec C++11 sont apparus deux nouveaux mots-clefs : `auto` et `decltype`. Durant ce tutoriel, nous allons voir ce qu'ils peuvent nous apporter, les règles de détection de type qu'ils emploient, les points auxquels faire attention afin que ces deux mots-clefs n'ait plus de secret !

**Information** : Premièrement, les codes montrés en exemple sont inspirés de ceux écrits par Scott Meyers dans son livre [Effective Modern C++](http://shop.oreilly.com/product/0636920033707.do), comme autorisé par l'auteur, tout comme certaines explications.   

Deuxièmement, pour pouvoir tester les codes mis en exemple, il faut au minimum un compilateur supportant C++11. Pour les exemples illustrant C++14, là encore, il faut un compilateur bien à jour. Dans mon cas, il s'agit de GCC 5.1.0 sous Archlinux. À noter également que bien que facultatif pour la compréhension de ce tutoriel, boost est nécessaire pour tester la partie où l'on affichera le type d'un objet.

# Les règles de déduction des templates
Avant d'aller plus loin, il est important de comprendre comment les templates fonctionnent, puique `auto` va utiliser quasiment les mêmes règles. Pour cela, nous allons utiliser une bête fonction comme celle-là.

```c++
template <typename T>
void foo(ParamType param);
```

Non seulement il faut déduire le type de T, mais également ParamType, qui n'est pas forcément le même. On peut en effet y trouver `const` ou une référence par exemple. Ainsi, dans le code suivant, si T est de type `int`, ParamType est de type `const int &`.

```c++
template <typename T>
void foo(const T & param);

int x = 0;
foo(x);
```

Dans ce cas, c'est tout à fait normal que, donnant un `int` en argument, T soit déduit comme `int`. Cependant, T ne dépend pas que de ce qu'on passe en argument à la fonction, mais aussi de la forme de ParamType. Il existe trois cas possibles.

* ParamType est un pointeur ou une référence.
* ParamType est une référence universelle.
* ParamType n'est ni un pointeur ni une référence.

[[attention]]
| La notion de référence universelle est trop longue pour être expliquée ici, surtout que Scott Meyers a écrit un [article](https://isocpp.org/blog/2012/11/universal-references-in-c11-scott-meyers) dessus. Tout ce qu'il y a à savoir pour lire la suite du tutoriel est qu'une référence universelle peut se comporter comme une rvalue-reference `T&&` ou comme une lvalue-reference `T&` ; elles se rencontrent dans deux cas.
|
| ```c++
| template <typename T>
| void foo(T && param);
| 
| auto && y = x;
| ```

# Pointeur ou référence #

C'est la situation la plus facile à comprendre, puisque les règles sont simples : si l'argument fourni lors de l'appel de *foo* est une référence ou un pointeur, on ignore la dite référence ou le dit pointeur. Examinons un exemple tout simple.

```c++
template <typename T>
void foo(T & param);

int x = 0; // x est de type int
foo(x); // T est de type int et ParamType est de type int&

const int y = x; // y est de type const int
foo(y); // T est de type const int, ParamType est de type const int&

const int & z = x; // z est de type const int&, soit une référence sur un const int
foo(z); // T est de type const int, ParamType est de type const int&
```

Comme dit précédemment, on remarque bien que la référence est supprimé. Par contre, `const` est conservé et c'est bien normal : quand on passe un objet `const` à une fonction prennant une référence comme paramètre, on s'attend bien à ce que l'objet reste `const` et ne soit pas modifiable, d'où ParamType qui sera de type `const T &`. 

Le même comportement est observable avec des pointeurs (bien qu'un bon programmeur C++ n'utilise que le moins possible les pointeurs nus).

```c++
template <typename T>
void foo(T * param);

int x = 0; // x est de type int
foo(&x); // T est de type int, ParamType est de type int*

const int * ptr = &x; // ptr est de type const int*, soit un pointeur sur un const int
foo(ptr); // T est de type const int, ParamType est de type const int*
```

Les déductions du compilateur changent un petit peu dans le cas où ParamType est de type `const T &` (ou `const T *`). En effet, dans ce cas, puisque ParamType est déjà de type `const`, alors T n'a plus besoin d'être déduit comme `const` lui aussi, même si l'argument donné est `const`. Pas clair ? Voyons ça avec du code.
```c++
template <typename T>
void foo(const T & param);

int x = 0; // x est de type int
f(x); // T est de type int et ParamType est de type const int&, tout est normal

const int y = x; // y est de type const int
f(y); // ParamType est déjà const, donc T sera de type, non pas const int, mais simplement int et ParamType sera de type const int&

const int & z = x; // z est de type const int &, soit une référence sur un const int
f(z); // ParamType est déjà const, donc T sera simplement int et ParamType sera de type const int&. On note que les règles sur les références vues juste avant s'appliquent encore ici.
```

Quand on y réfléchit, c'est normal. Si ParamType est déjà `const`, il est superflu et redondant de dire que T l'est aussi. Jusque là, tout est logique et la déduction de type fonctionne exactement comme ce à quoi on s'attend.

# Références universelles #

Là, les choses se complexifient un peu. En effet, le comportement n'est pas le même en fonction de si l'on passe en argument une lvalue ou une rvalue.

* Dans le cas d'une lvalue, T et ParamType sont déduits comme étant des lvalue-references. C'est le seul cas dans les règles de déduction des templates que T conserve sa référence. L'autre point surprenant est que bien que ParamType soit déclaré comme une rvalue (`T && param`), le compilateur en déduit que c'est une lvalue-reference.
* Dans le cas d'une rvalue, les règles vues dans la section pointeurs / références s'appliquent.

```c++
template <typename T>
void foo(T && param);

int x = 0; // x est une lvalue de type int
foo(x); // x étant une lvalue, T et ParamType sont déduits comme int&

const int y = x; // y est une lvalue de type const int
foo(y); // y étant une lvalue, T et ParamType sont déduits comme const int&

const int & z = x; //z est une lvalue de type const int&
foo(z); // z étant une lvalue, T et ParamType sont déduits comme const int&

foo(0); // 0 est une rvalue, donc T est déduit comme int et ParamType comme int&&
```

La chose importante à retenir est que les règles ne sont pas les mêmes si l'on a affaire à une lvalue ou à une rvalue. Dans le premier cas, les règles que nous venons de voir s'appliquent ; dans le second cas, les règles *classiques*, celles vues pour les pointeurs et les références, s'appliquent. Le pourquoi exact de ces comportements est néanmoins trop complexes pour être examiné ici ; des recherches sur Internet peuvent néanmoins être menées par ceux désireux de comprendre les raisons.

# Passage par recopie #

Quand le prototype de notre fonction ne comporte ni pointeur ni référence, alors c'est qu'on à affaire à un passage par copie.

```c++
template <typename T>
void foo(T param);
```

Si l'expression passée en argument contient référence ou pointeur, ceux-ci sont ignorés. Classique. Par contre, et c'est là qu'est la différence, si l'expression contient `const` (ou plus rarement `volatile`), ceux-ci sont ignorés également. La raison est toute simple : puisque on recopie les arguments donnés à la fonction, on ne manipule plus l'objet original mais un nouvel objet totalement indépendant du premier ; le fait que l'original ne soit pas modifiable ne veut pas dire que sa copie ne peut pas l'être non plus.

```c++
int x = 0; // x est de type int
foo(x); // T et ParamType sont de type int

const int y = x; // y est de type const int
foo(y); // T et ParamType sont de type int

const int & z = x; // z est de type const int&
foo(z); // T et ParamType sont de type int
```

# Les tableaux C #

Bien qu'un bon programmeur C++ moderne utilise `std::array` à la place des tableaux C, le monde n'est pas parfait et il y aura des cas où l'on devra traiter avec cet héritage du C. Et il y a aussi les curieux qui veulent connaître ces petits détails. Alors soit, explorons. Les tableaux C ne constituent pas un quatrième cas mais rentrent dans les précédents, comme nous allons le voir.

Tout d'abord, il est important de savoir qu'il est impossible de passer un tableau par recopie. En effet, les règles héritées du C impliquent que dans quasiment toutes les situations, un tableau est converti en un pointeur constant sur son premier élément. Les deux fonctions suivantes sont donc strictement **identiques**.

```c++
void foo(int * param);
void foo(int param[]);
```

Dans le cas d'une fonction par recopie, si on lui donne un tableau, le compilateur interprètera ça comme un pointeur.

```c++
template <typename T>
void foo(T param);

const char string[] = "Zeste de Savoir"; // string est de type const char[15]
foo(string); // conversion en pointeur, T sera déduit comme un const char*
```

Par contre, et là ça devient plus amusant, on peut déclarer une fonction prenant une référence sur un tableau. Comme la logique le veut, on va suivre les règles établies dans le cas 1 et surprise ! le type déduit pour T est celui du tableau ! 

```c++
template <typename T>
void foo(T & param);

const char string[] = "Zeste de Savoir"; // string est de type const char[15]
foo(string); // suivant les règles, T sera de type const char[15] lui aussi
```

Sur de nombreux forums, on trouve le code suivant qui permet de connaître, à la compilation, la taille d'un tableau C. Maintenant, après avoir lu jusqu'ici, vous êtes en mesure de comprendre et d'expliquer le comment de ce code.

```c++
template <typename T, std::size_t N>
inline constexpr std::size_t array_size(T (&)[N]) noexcept
{
    return N;
}
```

Désormais, les régles qu'utilise le compilateur n'ont plus de secret pour nous. Enfin presque. Il reste sans doute des cas exotiques et particuliers qui ne sont pas nécessaires pour bien comprendre l'article. Ceux qui le souhaitent peuvent continuer leurs recherches sur le sujet. Pour les autres, passons maintenant à `auto`.

# Les règles de fonctionnement de auto
Les règles de déduction de `auto` sont les mêmes que celles des templates ... sauf une petite exception. Mais commençons simple et voyons de comportements tout à fait normaux auxquels on s'attend.

```c++
// Cas classiques
auto x = 0; // 27 est de type int, donc x aussi

const auto y = x; // x est de type int, donc y sera de type const int

const auto & z = x; // x est de type int, donc z sera de type const int&

// Références unverselles
auto && universal_x = x; // x est une lvalue de type int, donc universal_x est de type int&

auto && universal_y = y; // y est une lvalue de type const int, donc universal_y est de type const int&

auto && universal_right = 27; // 27 est une rvalue de type int, donc universal_right est de type int&&

// Tableaux
const char site[] = "Zeste de Savoir";

auto pointer = site; // pointer est de type const char*

auto & array = site; // array est de type char (&)[15]
```

Jusque là, rien de surprenant, les règles appliquées sont bien les mêmes que pour les templates. La seule différence qui existe entre les règles de déduction appliquées aux templates et celles appliquées à `auto` viennent de la nouvelle façon d'initialiser une variable, introduite avec C++11. En effet, en plus des syntaxes "classiques", on retrouve deux nouvelles formes.

```c++
int x1 = 27;
int x2(27);
int x3 = {27};
int x4 {27};
```

Or, en remplaçant `int` par `auto`, si l'on obtient bien le type `int` pour les deux premières formes, on obtient un `std::initializer_list<int>` dans les deux dernières formes, contenant 27 comme unique élément ! Et pour vous convaincre que les règles de `auto` et des templates sont bien différentes dans ce cas, examinez le code suivant.

```c++
template <typename T>
void foo(T param)
{

}

template <typename T>
void bar(std::initializer_list<T> list)
{

}

int main()
{
    auto x = {1, 2, 3}; // x est bien un std::initializer_list<int> contenant 1, 2 et 3
    foo({1, 2, 3}); // erreur: no matching function for call to ‘foo(<brace-enclosed initializer list>)’
    bar({1, 2, 3}); // ici tout va bien
    return 0;
}
```

Alors que pour `auto` tout va bien, si l'on tente de faire de même avec `foo`, alors le compilateur nous envoie boûler. Pour qu'il accepte le code, il faut le même prototype que la fonction `bar`, soit `std::initializer_list<T>`. Voilà tout pour C++11

Mais avec C++14, l'histoire change encore un peu. En effet, avec cette nouvelle révision de la norme, il est possible d'écrire des fonctions dont le type devra être déduit (ou dit vulgairement, retournant `auto`) ; de même, on peut utiliser `auto` dans les paramètres des lambdas. Sauf que là, l'utilisation du mot-clef `auto` n'entraîne pas l'utilisation des règles de déduction de `auto` mais ... des templates ! Exemples ?

```c++
auto create_initialisation_list()
{
    return {1, 2, 3}; // erreur: returning initializer list
}

int main()
{
    std::vector<int> v;
    auto reset = [&v](const auto & new_value) { v = new_value; };

    reset({1, 2, 3}); // erreur: no match for call to ‘(main()::<lambda(const auto:1&)>) (<brace-enclosed initializer list>)’
    // note: template argument deduction/substitution failed : couldn't deduce template parameter ‘auto:1’

    return 0;
}
```

Compliqué hein ? En vérité, si l'on excepte ces quelques cas particuliers, `auto` et les templates suivent les mêmes règles. Voici un petit résumé pour aider à bien mémoriser toutes ces informations.

* `auto` et les templates ont les mêmes règles de déductions sauf en présence de crochets {}, auquel cas `auto` déduit qu'il est en présence de `std::initializer_list` alors que les templates non.
* En C++14, s'il est le type de retour d'une fonction ou le type d'un argument de lambdas, alors `auto` utilise les mêmes règles de déduction que les temples (notamment sur les `std::initializer_list`).

# Mais qu'est-ce que decltype ?
Peut-être vous-êtes vous posés la même question que moi la première fois que vous avez vu `decltype`. Le mot-clef en lui même est très simple : il renvoie le type exact d'une expression ou d'un identificateur qu'on lui donne. Exemples ?

```c++
int a = 0; // decltype(a) est int

const int b = 0; // decltype(b) est const int

class A;
A instance_de_A; // decltype(instance_de_A) est A;

const A & instance_2_de_A = instance_de_A;
// decltype(instance_2_de_A) est const A&

double foo(const std::string & value); 
// decltype(foo) est double(const std::string&)

decltype(if (0 == 0)) est bool
```

Ces quelques exemples, s'ils illustrent comment `decltype` fonctionne, sont assez inutiles, avouons-le. La principale utilisation de `decltype` en C++11 est dans le cas où une fonction template retourne une valeur qui dépend de ses paramètres.

```c++
template<typename LHS, typename RHS>
auto add(LHS lhs, RHS rhs) -> decltype(lhs + rhs)
{
    return lhs + rhs;
}

auto i = add(1, 1);   // int
auto j = add(1, 1.0); // double
```

**Attention**, l'utilisation de `auto` ici ne veut pas dire que ce sont les règles vues précédemment pour auto qui s'appliquent, mais plutôt que l'on utilise la syntaxe de déduction avec `decltype`. En effet, avec `decltype`, on peut utiliser des paramètres de la fonction pour déterminer le résultat, ce qui ne serait pas possible si on devait écrire le type de retour de la fonction à la place de `auto`.

Mais il faut admettre que c'est un peu long à écrire et même redondant, comme le montre le code ci-dessous (tiré d'un [article](http://scottmeyers.blogspot.fr/2013/07/when-decltype-meets-auto.html) de Scott Meyers, où l'on répète deux fois la même chose.

```c++
template <typename Container, typename Index>
auto grab(ContainerType && container, IndexType && index) -> 
    decltype(std::forward<ContainerType>(container)[std::forward<IndexType>(index)])
    // Déjà que le contenu de decltype est long ...
{
    authenticateUser();
    return std::forward<ContainerType>(container)[std::forward<IndexType>(index)];
    // ... mais en plus on doit réécrire la même chose ici !
}
```

L'idéal serait de faire pour les fonctions ce qui est possible dès C++11 avec les lambdas : ne pas avoir à expliciter le type de retour. 

```c++
[](int rhs, int lhs) -> int { return rhs + lhs; }; // ok
[](int rhs, int lhs)        { return rhs + lhs; }; // ok 
```

Eh bien, avec C++14, c'est possible, en utilisant `auto`. Maintenant, un code comme celui-ci est parfaitement valide.

```c++
template<typename LHS, typename RHS>
auto add(LHS lhs, RHS rhs)
{
    return lhs + rhs;
}
```

Mais du coup, est-ce que `decltype` est devenu inutile en C++14 ? Eh bien non. Si l'on se souvient bien de la partie précédente, on sait que `auto` ne conserve pas la référence ou le pointeur de ce qu'il évalue. Et si l'on reprend le code de Scott Meyers vu précédemment, ça peut poser un grave problème. Par exemple, si l'opérateur `[]` appliqué à un `std::vector<int>` renvoie bien un `int`, ce même opérateur appliqué à un `std::vector<bool>` renvoie un `bool&`. Si on n'utilise que `auto`, on perdra la référence. On ne peut pas non plus utiliser `decltype` avant le début de la fonction, puisque on ne sera pas encore dans sa portée et on ne pourra donc pas utiliser ses paramètres pour la déduction de type.

Et comme dit le proverbe, "l'union fait la force" ; la réponse est d'utiliser en même temps `decltype` et `auto`.

```c++
template <typename Container, typename Index>
auto grab(ContainerType && container, IndexType && index) -> decltype(auto)
    // Le type de retour est déjà beaucoup moins long et n'est plus redondant
{
    authenticateUser();
    return std::forward<ContainerType>(container)[std::forward<IndexType>(index)];
}
```

Tout est logique : `auto` indique que le type doit être déduit et `decltype` précise que les règles de déduction seront les siennes et non celles de `auto`. Et comme nous sommes des fainéants par nature, nous disposons d'un moyen d'écrire ça encore plus simplement.

```c++
template <typename Container, typename Index>
decltype(auto) grab(ContainerType && container, IndexType && index)
// Voilà qui est parfait !
{
    authenticateUser();
    return std::forward<ContainerType>(container)[std::forward<IndexType>(index)];
}
```

Et le meilleur dans tout ça, c'est que cette syntaxe peut s'utiliser autre part que dans les retours de fonction ; en fait, elle se place partout où `auto` peut être utilisé pour une déduction de type, mais reprend le même comportement que `decltype`.

```c++
// Fini ça ...
decltype(longAndComplexInitializingExpression) var = longAndComplexInitializingExpression;

// ... place à la concision !
decltype(auto) var = longAndComplexInitializingExpression;
```

# Petite particularité de decltype #

Comme rien n'est parfait en ce bas-monde, il y aura parfois des moments où `decltype` vous surprendra en vous donnant un type auquel vous ne vous attendiez pas. S'il retourne bien le type d'un identificateur qu'on lui donne, pour des expressions lvalues un peu plus compliquées, `decltype` déduit qu'elle est une lvalue-reference ; autrement dit, si une expression un peu complexe est de type `T`, `decltype` la déduira comme étant de type `T&`. 

```c++
int x = 0;

decltype(x); // est bien de type int

decltype((x)); // (x) est une expression lvalue, donc le type déduit est int&
```

Le danger se présente avec C++14 et l'utilisation conjointe de `decltype` et `auto`. Ainsi, si vous aviez l'habitude d'entourer de parenthèses le retour d'une fonction, vous allez avoir quelques surprises.

```c++
decltype(auto) foo()
{
    int x = 0;

    ...

    return x; // decltype(x) est un int, pas de problème
}

decltype(auto) bar()
{
    int x = 0;

    ...

    return (x); // decltype((x)) est un int&, une référence sur une variable locale !
}
```

La leçon ? Rester prudent lorsqu'on utilise `decltype` et `auto` ensembles pour éviter les mauvaises surprises.

# Connaître et afficher le type exact
Bien que connaître et comprendre les règles des templates, de `auto` et de `decltype` puisse grandement nous aider à savoir quel type est déduit, il se peut que l'on ait besoin d'afficher le type d'une expression ou d'un identificateur. La meilleure solution est celle fournie par Boost avec l'en-tête `<boost/type_index.hpp>`. Bien qu'il faille Boost d'installé, cet en-tête ne nécessite pas d'être compilé pour être utilisé. Et comme un code vaut mille mots, voici une petite illustration compilée avec GCC 5.1.0 sous Archlinux.

```c++
#include <boost/type_index.hpp>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

template <typename T>
void foo(const T & param)
{
    using boost::typeindex::type_id_with_cvr;

    std::cout << "T = " << type_id_with_cvr<T>().pretty_name() << std::endl;
    std::cout << "param = " << type_id_with_cvr<decltype(param)>().pretty_name() << std::endl;
    std::cout << std::endl;
}

int main()
{
    foo(3.1415926);
    foo("Hello with C-string");

    auto ptr = std::make_unique<int>(42);
    foo(ptr);

    const std::string str("Hello with C++ std::string");
    foo(str);

    const std::vector<float> v;
    foo(v);

    auto lambda = []() -> int { return 42; };
    foo(lambda);

    
    return 0;
}
```
```
T = double
param = double const&

T = char [20]
param = char const (&) [20]

T = std::unique_ptr<int, std::default_delete<int> >
param = std::unique_ptr<int, std::default_delete<int> > const&

T = std::string
param = std::string const&

T = std::vector<float, std::allocator<float> >
param = std::vector<float, std::allocator<float> > const&

T = main::{lambda()#1}
param = main::{lambda()#1} const&
```

N'hésitez pas à jeter un œil à la [documentation](http://www.boost.org/doc/libs/1_58_0/doc/html/boost_typeindex.html) pour en apprendre plus sur cet outil précieux.

# Quand les utiliser ? 

Tu ne sais pas penser de ces nouveautés et tu es tout perdu ? Pour t'aider, voici des avis de différents programmeurs, récoltés sur Internet.

> Principalement pour les types moches et à rallonge, avec plein de templates dedans. De temps à autre je tente du AAA, mais sans trop me forcer à l'utiliser.
>
> *[AAA]: Almost Always Auto
Source: [Luthaf](https://zestedesavoir.com/forums/sujet/3216/c-auto-et-decltype/#p57958)

> * `auto` : je l'utilise quand le type est très long, souvent avec la ST(L) et ses noms template à rallonge en retour de fonction. Mais quand je sais ce que je vais manipuler bien sûr (des itérateurs, conteneurs, etc.). Je l'utilise aussi pour des types numériques qui peuvent varier dans le temps (passer de float à double par exemple), ça permet de gagner pas mal de temps !
>
> * `decltype` : je l'utilise moins que le précédent mais lorsque je m'en sers c'est souvent avec auto (pas decltype(auto)), pour bien montrer que le type d'une variable doit absolument être le même que celui d'une autre.
>
Source: [zeFresk](https://openclassrooms.com/forum/sujet/c-auto-decltype-et-deduction-de-types#message-88695630)

> Sinon, je mets `auto` quand la variable est initialisée avec une autre variable ou avec un retour de fonction. Dans les autres cas, j'appelle directement le constructeur `T x{...};` et non pas `auto x = T{...}`.
> Aussi dans les boucles sur intervalle (sauf si l'IDE décide de ne pas reconnaître le type... -_-).
>
> Je ne le mets pas quand je veux une interface. À la place, je mets le type de l'interface.
> 
> Je ne l'utilise pas quand il y a `std::reference_wrapper`, sinon il faut mettre machin.get() partout. Je trouve ça regrettable en fait, j'espère que la proposition de surcharge de l'opérateur . va être accepté (pas du tout suivit le truc).
> (D'ailleurs, je remplace souvent reference_wrapper par à un proxy rien que pour cette raison...)
>
> `decltype` quand j'ai besoin de construire une variable du même type. Généralement, dans un alias (`using Truc = decltype(machin)`).
>
Source: [jo_link_noir](https://openclassrooms.com/forum/sujet/c-auto-decltype-et-deduction-de-types#message-88695917)

> Salut ! Mon avis :
>
> * `auto` : souvent pour les types qui peuvent changer (`float`, `double` notamment), presque toujours pour les variables initialisées par un retour de fonction (`make_shared`, `make_unique`, `begin` pour ne donner que des exemples de la SL) ;
>
> * `decltype` : dans des arguments de fonction qui ont deux fois le même type (exemple : `maFonction(UnTypeComplique::iterator first, decltype(first) last))`, rarement en d'autres circonstances
>
> * `decltype(auto)` : je n'ai jamais rencontré un cas de figure ou j'ai eu à l'utiliser, et je préfère l'éviter car je le trouve peu explicite, car il faut aller voir quels qualificateurs (`const`, `volatile`, référence) marquent la "variable source", ce qui est peu lisible. Je préfère dans ce cas réécrire `auto const&` par exemple.
>
Source: [mehdidou99](https://openclassrooms.com/forum/sujet/c-auto-decltype-et-deduction-de-types#message-88695943)

> Les `auto`, c'est bien, mangez-en.
Source: [gbdivers](https://openclassrooms.com/forum/sujet/c-auto-decltype-et-deduction-de-types#message-88696449)

> Personnellement, je suis dans la même optique que **@jo_link_noir**, j'utilise `auto` quand je crée un élément qui est dépendant d'un autre. Pour `decltype`, j'ajouterai une autre petite utilisation que pour la création d'un alias : une dépendance de type mais où la première utilisation ne nous donne pas l'info. Cas typique :
>
> ```c++
>std::vector<bidule> v;
> 
>//...
> 
>for(decltype(v)::size_type i = 0; i < v.size(); ++i){
>
>}
>```
> Après, dans ce cas, on aura effectivement envie de définir le type avant avec un using.
>
Source: [Ksass`Peuk](https://openclassrooms.com/forum/sujet/c-auto-decltype-et-deduction-de-types#message-88701634)

> - Use `auto` if a reference type **would never be correct**.
> - Use `decltype(auto)` only if a reference type could be correct.
Source:[Scott Meyers](http://www.aristeia.com/TalkNotes/C++TypeDeductionandWhyYouCareCppCon2014.pdf)

- Un peu de [StackOverflow](http://stackoverflow.com/questions/21369131/when-should-i-use-decltypex-instead-of-auto-to-declare-the-type-of-a-variable).
- Encore [un peu plus](http://stackoverflow.com/questions/24109737/what-are-some-uses-of-decltypeauto).
- Et du [cplusplus.com](http://www.cplusplus.com/forum/general/188645/) aussi.

J'espère que, par la lecture de ce tutoriel, vous en savez désormais plus sur le fonctionnement des templates, de `auto` et de `decltype`. Ce sont des fonctionnalités vraiment intéressantes qui font du C++ un langage frais et moderne (propos absolument subjectif). Libre à vous désormais de les adopter !