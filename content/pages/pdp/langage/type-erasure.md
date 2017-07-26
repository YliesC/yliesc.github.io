% Type Erasure
% Freedom
% 28/03/2015

Title: Type Erasure
Order: 9
Date: 2015-03-28
Tags: type, erasure, tutoriel
Slug: type-erasure
Authors: Freedom

# Introduction

Le C++ ne permet pas de stocker des objets hétérogènes dans un même conteneur, ce qui peut être nécessaire dans certaines situations.

Cette problématique est souvent celle utilisée pour introduire le polymorphisme d'inclusion, cependant la problématique est plus générale et peut exister sans qu'il soit possible d'utiliser directement ce polymorphisme.

# Typage
### Définition

Un des objectifs du typage du C++ est d'associer à une zone définie et continue de la mémoire une sémantique, c'est-à-dire ce qu'on peut faire avec cet espace mémoire. On appelle un tel espace *un objet* et la sémantique *le type de l'objet*. La sémantique est essentiellement[^10] déterminée par les fonctions que l'on peut appliquer à un tel objet, un type peut donc se définir par l'ensemble des fonctions qui lui sont associées.

Notons ici que le type de l'objet ne dépend que de l'objet, il n'est pas à confondre avec le type d'une expression qui va associer une sémantique à une expression et peut être de deux natures *statique* ou *dynamique*. Illustrons ceci :
```c++
struct B {};
struct D : B {};

B* p = new D();
```
Ici l'objet occupe la zone entre les adresses `p` et `p+sizeof(D)`, et son type est `D`, le type statique de l'expression `*p` est `B` alors que son type dynamique est `D`. 

### Relation d'ordre

On peut définir un ordre entre les types en fonction des opérations qu'ils supportent. Concrètement :
```c++
struct G {};
struct H {};

void foo(G&);
void foo(H&);

void bar(G&);
```
On peut noter $H < G$, qui signifie que toutes les expressions valables avec une expression de type statique `H` le seront avec une expression de type statique `G`. 

[^10]: Pas uniquement, l'organisation des données au sein de la zone mémoire et le nom du type en font aussi partie.

# Polymorphismes
### Plusieurs polymorphismes

On va parler ici de deux polymorphismes du C++, celui paramétrique et celui d'inclusion. Outre les différences syntaxiques[^20], ils diffèrent par la résolution de l'appel :  

 - Le polymorphisme paramétrique est résolu à la compilation, ce qui permet de profiter du typage et du compilateur pour s'assurer des opérations effectuées ;
 - Le polymorphisme d'inclusion est résolu à l’exécution[^21], on perd l'avantage du typage, mais cela peut être nécessaire lorsque le type d'un objet sera déterminé à l’exécution, c'est-à-dire lorsque l'on a déjà perdu l'avantage du typage.

Concrètement, le polymorphisme intervient dans cette situation :
```c++
foo(expr);
```
Le polymorphisme paramétrique va conserver le type statique de `expr` lors de la réalisation des opérations de `foo`, dans le cas du polymorphisme d'inclusion[^22] ce sera le type dynamique de `expr` qui sera utilisé.

### Polymorphisme paramétrique

La syntaxe typique du polymorphisme paramétrique est :
```c++
template<class T>
void foo(T& t)
{ /*stuff on t*/ }
```
L'ensemble des fonctions qui vont être appelées sur `t` définissent un type virtuel `C` et chaque argument template `T` valide respecte $C<T$. Ce type `C` représente un concept qui doit être respecté lors de l'appel.

### Polymorphisme d'inclusion

Dans le cas du polymorphisme d'inclusion, la syntaxe est :
```c++
struct B {
  virtual void foo()
  { /*stuff*/ }

  virtual ~B() {}
};

struct D : B {
  void foo()
  { /*other stuff*/ }
};
```
On a directement la relation $B<D$, c'est le point commun entre les deux polymorphismes : chaque classe fille propose l'interface de la classe mère comme chaque argument template respecte un concept[^23].

[^20]: Importantes pour écrire du code, mais n'influencent pas fondamentalement le choix entre l'un et l'autre.
[^21]: Le C++ ne fera cette résolution qu'en fonction d'un objet, le langage ne dispose pas de multi-méthode (il existe des techniques pour effectuer du multi-dispatch en C++, mais ce n'est pas notre sujet).
[^22]: La syntaxe d'appel est alors `expr.foo()`.
[^23]: A l'heure actuelle le C++ ne propose aucun outil pour exprimer concrètement un concept, c'est cependant en projet pour une future version du langage.

# Problématique
### Approche du problème

La problématique intervient lorsque l'on ne peut plus conserver le type de l'objet grâce au polymorphisme paramétrique, il s'agit typiquement des situations où le type de l'objet créé est déterminé à l’exécution, par exemple :
```c++
struct G {
  void foo()
  { std::cout << "G" << std::endl; }
};
struct H {
  void foo()
  { std::cout << "H" << std::endl; }
};

std::vector</*?*/> vec;
int i; std::cin >> i;
switch(i) {
  case 1 :
    vec.push_back(G());
    break;
  case 2 :
    vec.push_back(H());
    break;
}
vec[0].foo();
```
`G` et `H` représentent deux types distincts, que mettre à la place de `/*?*/` ?

Les opérations que l'on effectue sur `vec[0]`, ici l'appel à la fonction membre `foo`, définissent à nouveau un type `C` qui respecte $C<G$ et $C<H$, cependant on ne peut pas profiter du polymorphisme paramétrique, le C++ nous demande sur quel type travaille le conteneur `std::vector`.

### Première solution

Il va donc s'agir de rendre réel ce type virtuel `C`, une première solution nous est proposée par le polymorphisme d'inclusion grâce au point commun existant entre les deux polymorphismes mis en évidence dans la partie précédente. Concrètement il s'agit de mettre en place une classe de base et d'adapter la syntaxe pour manipuler des pointeurs[^30] :
```c++
struct C {
  virtual void foo() =0;
  virtual ~C(){}
};

struct G : C {
  void foo()
  { std::cout << "G" << std::endl; }
};
struct H : C {
  void foo()
  { std::cout << "H" << std::endl; }
};

std::vector<std::unique_ptr<C>> vec;
int i; std::cin >> i;
switch(i) {
  case 1 :
    vec.push_back(std::make_unique<G>());
    break;
  case 2 :
    vec.push_back(std::make_unique<H>());
    break;
}
vec[0]->foo();
```
On a ici appliqué un *type erasure* : on a créé un *type plus faible* que le type des objets que l'on manipule et *convenant à l'utilisation* que l'on fait de ces objets.

Cette première solution est fonctionnelle mais présente un défaut, en effet dans le cas du polymorphisme paramétrique, l'existence du concept est orthogonale à l'existence de types le respectant, alors que dans le cas du polymorphisme d'inclusion, la classe de base est nécessaire pour réaliser les classes dérivées. Ainsi l'utilisation directe du polymorphisme d'inclusion pour la réalisation d'un *type erasure* a un défaut : elle est intrusive, c'est-à-dire que l'on a introduit des modifications dans des éléments existants, ici `G` et `H`. Si l'on a ce besoin et que les types existent déjà, on se retrouve face à un mur : on ne peut pas ajouter une classe de base à des types qui existent déjà.

### Seconde solution

Une seconde solution vient répondre à ce problème, avant d'en présenter une implémentation, donnons un exemple concret présent dans la bibliothèque standard. En C++ il existe plusieurs expressions supportant la syntaxe `fun()`, par exemple :
```c++
void foo()
{ std::cout << "foo" << std::endl; }

struct F { 
  void operator()() const 
  { std::cout << "bar" << std::endl; }
};
F bar;

auto goo = []()
{ std::cout << "goo" << std::endl; };

foo();
bar();
goo();
```
Ici les types de `foo`, `bar` et `goo` sont différents, n'ont pas de type de base commun et il nous est impossible d'en rajouter un. Ainsi dans la situation suivante :
```c++
std::vector</*?*/> vec;
int i; std::cin >> i;
switch(i) {
  case 1 :
    vec.push_back(foo);
    break;
  case 2 :
    vec.push_back(bar);
    break;
  case 3 :
    vec.push_back(goo);
    break;
}
vec[0]();
```
Que mettre à la place de `/*?*/` ?

La bibliothèque standard nous propose ici le type `std::function<void()>`, il est plus faible que les types de `foo`, `bar` et `goo` et convient pour réaliser l'opération `vec[0]()` : on a un *type erasure* sans avoir introduit de classe de base commune aux types de nos trois objets.

De manière concrète, si vous exécutez ce code, il va attendre une entrée[^31] et selon celle-ci l'expression `vec[0]` de type `std::function<void()>&` va correspondre à l'objet `foo`, `bar` ou `goo` : on n'a plus accès aux types de ces objets, par contre le type `std::function<void()>` nous permet de faire `vec[0]()` grâce à sa fonction membre `operator()` en ayant le comportement attendu, c'est-à-dire un appel à `foo()`, `bar()` ou `goo()` selon l'entrée utilisateur saisie.

[^30]: Il est nécessaire de manipuler des pointeurs ou des références pour profiter du polymorphisme d'inclusion en C++.  
[^31]: La gestion des entrées est faite de manière très sommaire ici, aucune vérification de la saisie n'est faite pour vérifier qu'un nombre entier entre 1 et 3 est bien présent. Une gestion rigoureuse complexifierait inutilement les exemples.

# Implémentation
### Adaptateur (*Wrapper*)[^30] générique

Nous allons implémenter une classe qui fait exactement la même chose que `std::function<void()>`, nommons là `function`. Dans la partie précédente nous avons une implémentation dans le cas où l'on peut ajouter une classe de base à nos types. Si l'on arrive à créer une classe pour chacun des types `foo`, `bar` et `goo` qui supporte la syntaxe `fun()`, c'est-à-dire qui a un `operator()`, et peut contenir respectivement `foo`, `bar` ou `goo`, alors on pourra introduire notre classe de base. Une telle classe correspond à un adaptateur, pour `foo` il ressemblerait à :
```c++
struct foo_class {
  template<class F3, class =std::enable_if_t<!std::is_same<foo_class,std::decay_t<F3>>::value>>
  foo_class(F3&& fun3)
    : fun2(std::forward<F3>(fun3))
  { }

  void operator()()
  { fun2(); }

private:
  /*foo_type*/ fun2;
};
```
La syntaxe utilisée pour le constructeur est celle du *perfect forwarding* selon ce qui est passé au constructeur, un temporaire ou non, l'argument template `F3` sera `/*foo_type*/` ou `/*foo_type*/&`[^31] où `/*foo_type*/` est le type de `foo`. `enable_if_t` permet de désactiver[^32] le constructeur si l'argument template `F3` est déduit à `foo_class` ou `foo_class&` ce qui permet d'assurer que ces appels soient pris en charge par les constructeurs par copie et déplacement.

Les classes pour `bar` ou `goo` seront similaires, le C++ a un outil pour factoriser des codes qui se ressemblent : les template de classe. Nommons ce template `function_impl` :
```c++
template<class F2>
struct function_impl {
  template<class F3, class =std::enable_if_t<!std::is_same<function_impl,std::decay_t<F3>>::value>>
  function_impl(F3&& fun3)
    : fun2(std::forward<F3>(fun3))
  { }

  void operator()()
  { fun2(); }

private:
  F2 fun2;
};
```

### Polymorphisme d'inclusion

On peut alors introduire une classe de base, nommée `function_base`[^33], comme dans notre première implémentation :
```c++
struct function_base {
  virtual void operator()() =0;

  virtual ~function_base() { }
};

template<class F2>
struct function_impl : function_base {
  template<class F3, class =std::enable_if_t<!std::is_same<function_impl,std::decay_t<F3>>::value>>
  function_impl(F3&& fun3)
    : fun2(std::forward<F3>(fun3))
  { }

  void operator()()
  { fun2(); }

private:
  F2 fun2;
};
```

On peut alors utiliser notre système comme dans la première partie :
```c++
std::vector<std::unique_ptr<function_base>> vec;
int i; std::cin >> i;
switch(i) {
  case 1 :
    vec.push_back(std::make_unique<function_impl<decltype(&foo)>>(foo));
    break;
  case 2 :
    vec.push_back(std::make_unique<function_impl<decltype(bar)>>(bar));
    break;
  case 3 :
    vec.push_back(std::make_unique<function_impl<decltype(goo)>>(goo));
    break;
}
(*vec[0])();
```

### Second adaptateur

C'est fonctionnel, mais on n'est pas encore à ce que propose `std::function<void()>` : utilisation moins flexible à cause du besoin de déréférencer et excès de verbosité lors de l'insertion. Pour améliorer les choses l'on va réaliser un adaptateur sur ce `std::unique_ptr` et profiter d'un constructeur template pour éviter la répétition avec le `decltype` :
```c++
struct function {
  template<class F1, class =std::enable_if_t<!std::is_same<function,std::decay_t<F1>>::value>>
  function(F1&& fun1)
    : func(std::make_unique<function_impl<std::decay_t<F1>>>(std::forward<F1>(fun1)))
  { }

  void operator()() const
  { (*func)(); }

private:
  std::unique_ptr<function_base> func;
};
```
On a cette fois quelque chose de fonctionnel proche de ce que propose `std::function<void()>` :
```c++
std::vector<function> vec;
int i; std::cin >> i;
switch(i) {
  case 1 :
    vec.push_back(foo);
    break;
  case 2 :
    vec.push_back(bar);
    break;
  case 3 :
    vec.push_back(goo);
    break;
}
vec[0]();
```

[^30]: Il s'agit d'un patron de conception (*design pattern*).
[^31]: Ou une version `const` et/ou `volatile` de ces types.
[^32]: `enable_if_t` est un alias sur `enable_if<B>::type` qui n'existe pas si la condition `B` est fausse et dans ce cas le constructeur n'existe pas non plus.
[^33]: Je ne la nomme pas `function` par anticipation sur la suite.

# Améliorations
### Factorisation de `enable_if`

On peut encore améliorer notre implémentation, le premier point est de factoriser les deux lignes suivantes :
```c++
class =std::enable_if_t<!std::is_same<function_impl,std::decay_t<F3>>::value>
class =std::enable_if_t<!std::is_same<function,std::decay_t<F1>>::value>>
```
On va réaliser un nouvel alias, nommé `dispatch_ctor` :
```c++
template<class C, class T>
using dispatch_ctor =std::enable_if_t<!std::is_same<C,std::decay_t<T>>::value>;
```
Ce qui conduit à réécrire notre implémentation sous la forme :
```c++
template<class F2>
struct function_impl : function_base {
  template<class F3, class =dispatch_ctor<function_impl,F3>>
  function_impl(F3&& fun3)
    : fun2(std::forward<F3>(fun3))
  { }

  void operator()()
  { fun2(); }

private:
  F2 fun2;
};

struct function {
  template<class F1, class =dispatch_ctor<function,F1>>
  function(F1&& fun1)
    : func(std::make_unique<function_impl<std::decay_t<F1>>>(std::forward<F1>(fun1)))
  { }

  void operator()() const
  { (*func)(); }

private:
  std::unique_ptr<function_base> func;
};
```

### Sémantique de copie

En l'état `function` n'est pas copiable, or lorsque l'on est certain que les types que l'on veut affaiblir sont copiables, il est pertinent de vouloir que le *type erasure* le soit aussi. Pour permettre la copie, il faut disposer d'une fonction `clone` dans le premier adaptateur qui va effectuer la copie[^50] :
```c++
struct function_base {
  virtual std::unique_ptr<function_base> clone() const =0;

  virtual void operator()() =0;

  virtual ~function_base() { }
};

template<class F2>
struct function_impl : function_base {
  template<class F3, class =dispatch_ctor<function_impl,F3>>
  function_impl(F3&& fun3)
	: fun2(std::forward<F3>(fun3))
  { }

  std::unique_ptr<function_base> clone() const
  { return std::make_unique<function_impl>(fun2); }

  void operator()()
  { fun2(); }

private:
  F2 fun2;
};

struct function {
  template<class F1, class =dispatch_ctor<function,F1>>
  function(F1&& fun1)
	: func(std::make_unique<function_impl<std::decay_t<F1>>>(std::forward<F1>(fun1)))
  { }

  function(function const & rhs)
	: func(rhs.func->clone())
  { }
  function& operator=(function const & rhs) {
	func=rhs.func->clone();
	return *this;
  }

  function(function&&) =default;
  function& operator=(function&&) =default;

  void operator()() const
  { (*func)(); }

private:
  std::unique_ptr<function_base> func;
};
```

### Adaptateurs

L'utilisation que l'on a fait jusqu'ici de ce pattern est assez naïve, on adapte peu de chose puisque l'interface que l'on propose est la même que celle du type adapté. Pour s'en apercevoir, il suffit de remarquer que d'un côté la nomenclature utilisée aux lignes *4*, *19* et *44* n'est pas primordiale tant qu'elle est cohérente sur ces trois lignes, et que seul celle à la ligne *43* a de l'importance et définit l'interface.

Par exemple on pourrait avoir une fonction libre à la place d'une fonction membre :
```c++
friend void apply(function const & lhs)
{ (*lhs.func)(); }
```
Qui s'utiliserait ainsi : `apply(vec[0]);`[^51].

De l'autre côté de l'adaptateur il y a le comportement, à nouveau dans notre situation il se limite à la ligne *20* mais il pourrait être aussi complexe qu'on le veut et pourrait varier selon le type. En effet la spécialisation template permet de changer l'implémentation de l'adaptateur selon le type, cependant cette spécialisation est intrusive, il faut donc la réserver aux types que l'on connait lors de la création de notre *type erasure*, typiquement les types fondamentaux[^52]

Par exemple `std::function<void(A&)>` permet de stocker un pointeur de fonction membre de `A` ne prenant pas de paramètre et ne retournant rien, disons une fonction nommé `hoo`. La syntaxe `(&hoo)(a)`, où `A a`, n'est pas supportée, mais le comportement que l'on pourrait attendre est celui de `(a.*(&A::hoo))();`. En spécialisant l'adaptateur qui correspond à notre `function_impl` pour le type `void (A::*)()` on peut avoir une utilisation de cette syntaxe dans ce cas particulier. Ce qui permet de faire :
```c++
std::function<void(A&)> f(&A::hoo);
A a;
f(a);
```

[^50]: Il s'agit de la construction idiomatique lorsque l'on veut copier des éléments d'une hiérarchie polymorphe.
[^51]: Ce qui n'a aucun intérêt dans cette situation, mais peut en avoir d'en d'autre.
[^52]: Dans les autres situations, l'utilisateur devra mettre en place son propre adaptateur.

# Conclusion

Vous avez maintenant tout les éléments pour répondre aux divers problématiques qui demandent d'avoir des collections hétérogènes.

N'oubliez cependant pas de consulter les documentations des bibliothèques que vous utilisez pour vérifier que le *type erasure* dont vous avez besoin n'existe pas déjà.

Merci à *lmghs*, *saroupille* et *Maëlan* pour leurs conseils.
