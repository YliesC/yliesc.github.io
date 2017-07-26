Title: Liaisons en C++
Order: 9
Date: 2014-09-27
Tags: liaisons, c++, tutoriel
Slug: liaisons-en-c
Author: Höd
Display: true

# Article
### Introduction

L'objectif de cet article est de présenter les différents types de liaisons en C++. Pour cela, nous introduirons la notion de liaisons et donnerons quelques exemples des mécanismes de liaisons proposés par le C++ et, à titre d'information supplémentaire, comment émuler des mécanismes absents du C++.    
Nous présenterons enfin une technique dite du _Tag Dispatching_, que l'on pourrait traduire par « Liaison par Tag » permettant la sélection de méthodes en _compile time_.    
Cependant, même si l'ensemble des exemples et techniques sont réalisés en C++, le lecteur trouvera des informations plus générales et pourra tout aussi bien adapter le code à son langage favori, en faisant attention aux caractéristiques propres de ce langage.

A noter que cet article ne se veut pas exhaustif sur les différents types de liaisons qui peuvent exister mais essaye simplement de renseigner sur les notions basiques gravitant autour du concept de liaison, d'où l'appellation d'« usuelles » pour les liaisons traitées ici. Pour de plus amples détails, la lecture de la thèse de Coplien est un bon point de départ.

### Notion de liaison

La liaison est la capacité d'un langage à sélectionner l'implémentation d'une méthode polymorphique qui est appelée. On distingue plusieurs types de liaisons, en fonction des caractéristiques du langage mais également du contexte d'appel de la méthode ou fonction considérée. 

La liaison, _dispatch_ en anglais ne doit pas être confondu avec le _binding_, malgré que dans beaucoup d'articles ou de livres le terme de _binding_ remplace et / ou aggrège celui de _dispatch_ et que la traduction française de liaison soit plus proche de la traduction de _binding_. Le _binding_ est en effet la capacité à associer à un appel le nom d'une méthode, tandis que le _dispatch_ sélectionne l'implémentation d'une méthode parmi plusieurs proposant le même nom. Le _dispatch_ intervient donc après le _binding_ et un _binding_ peut être statique là où le dispatch sera dynamique. L'inverse est évidemment impossible puisqu'avant de choisir une implémentation d'une méthode il faut évidemment en choisir son nom. 

Cependant, selon le langage ainsi que la communauté et les habitudes de chacun, le terme _dispatch_ peut être ou non confondu avec le terme _binding_, l'un désignant le concept général de sélection de la méthode à appeler et le second l'implémentation des mécanismes. Une réponse confrontant les divers avis se trouve [ici](http://progdupeu.pl/forums/sujet/126/article-liaisons-en-c#p2123).

#### Liaison statique ou dynamique

Dans un premier temps, on peut caractériser la liaison selon que toute l'information nécessaire à l'appel puisse être déduite en _compile time_ - on parlera alors de liaison statique - ou qu'il faille un contexte donné en _run time_.    
Il y a un liaison dynamique lorsque la sélection d'une méthode à utiliser dépend d'un type qui ne sera connu qu'à l'exécution, comme celui du paramètre d'une méthode par exemple.    
Le C++ propose ces deux types de liaisons, la liaison statique étant le comportement par défaut et la liaison dynamique étant obtenue grâce à l'utilisation du mot clef ```virtual```.

Exemple de static dispatch :
```c++
struct Foo
{
    void f() const { cout << "Foo::f()" << endl ; }
} ;

struct Bar
{
    void f() const { cout << "Bar::f()" << endl ; }
} ;

int main()
{
    Foo a ;
    Bar b ;

    a.f() ;
    b.f() ;

    return 0;
}
```

Il est évident ici que le compilateur peut extraire de manière certaine du contexte, la méthode à appeler. L'ensemble des types utilisés par le programme principal est connu à l'avance. 

Nous avons donc pour sortie :
```
Foo::f
Bar::f
```

Exemple de liaison dynamique :
```c++
struct Base
{
    virtual void f() const = 0;
    virtual ~Base() {}
};

struct Foo : public Base
{
    void f() const { cout << "Foo::f()" << endl ; }
};

struct Bar : public Base
{
    void f() const { cout << "Bar::f()" << endl ; }
};

void dispatch(const Base& base)
{
    base.f();
}

int main()
{
    Foo a;
    Bar b;

    dispatch(a);
    dispatch(b) ;

    return 0;
}
```

Remarquez le type du paramètre de la fonction ```dispatch``` : il s'agit d'un objet polymorphique de type ```Base```. Comment savoir quelle méthode membre ```f``` appeler avant l'appel explicite à la fonction ```dispatch``` ? La liaison est donc faite en fonction du contexte d'exécution.

La sortie est la suivante :
```
Foo::f
Bar::f
```

#### Liaison simple ou multiple

On peut également caractériser davantage la liaison dynamique, en fonction de sa capacité à s'appliquer au regard du nombre d'objets polymorphiques qu'une méthode prend en paramètre.    
Si le langage est capable de correctement choisir l'implémentation d'une fonction appelée contenant un seul objet polymorphique, on parle de liaison simple ou _Single Dispatch_, s'il peut en traiter deux, on parle de _Double Dispatch_ et pour un nombre quelconque de _Multiple Dispatch_ de manière générale.

Le C++ ne permet, nativement, que le _Single Dispatch_ mais nous verrons qu'il est possible d'émuler du _Double Dispatch_ assez facilement.

Avant de donner quelques exemples, rappeler que lorsque l'on appelle une méthode depuis une instance de classe, il y a TOUJOURS un paramètre : l'instance de la classe qui appelle la méthode. L'écriture courante utilisant un point (ou autre selon les langages) pour séparer visuellement l'instance appelante des autres paramètres n'est que du sucre syntaxique permettant une plus grande lisibilité. Il faut donc en tenir compte lorsque l'on parle de liaison puisque dans le cas du _Single Dispatch_, le seul paramètre prit en compte est l'instance appelante.    
Nous avons donc déjà rencontré un exemple de _Single Dispatch_ : l'exemple de la liaison dynamique donné à la section précédente. 

Voici un exemple qui montre le comportement limité de la liaison en C++ . Considérons les classes suivantes :
```c++
struct Vehicle 
{
    virtual void print() const { cout << "Je suis juste un vehicule ! :'(" << endl; };
};

struct Plane : public Vehicle 
{
    void print() const { cout << "Je suis un avion ! :)" << endl; }
};

struct Parking
{
    virtual void park(const Vehicle& v) const { cout << "Bienvenue au garage !" << endl; v.print(); };
    virtual void park(const Plane& p) const { cout <<  "Pas assez de place pour garer un avion !" << endl; p.print();};
};

struct WideParking : public Parking
{
    void park(const Vehicle& v) const { cout << "Bienvenue au garage extra-large !" << endl; v.print(); };
    void park(const Plane& p) const { cout <<  "Il y a toute la place qu'il faut pour un avion !" << endl; p.print();};
};
```

Et voici quelques fonctions ```main``` accompagnées de leur sortie :
```c++
int main()
{
    Vehicle v;
    Plane pl;
    Parking p;
    WideParking wp;
    
    p.park(v);
    wp.park(v);
    
    p.park(pl);
    wp.park(pl);

    return 0;
}
```

Et la sortie associée :
```
Bienvenue au garage !
Je suis juste un vehicule ! :'(
Bienvenue au garage extra-large !
Je suis juste un vehicule ! :'(

Pas assez de place pour garer un avion !
Je suis un avion ! :)
Il y a toute la place qu'il faut pour un avion !
Je suis un avion ! :)
```

Ici, aucun soucis, nous avons bien le comportement désiré. En effet, tous les types sont bien caractérisés et peuvent être déduit en _compile time_,

Un autre essai en utilisant un pointeur sur vehicule en lieu et place de notre instance d'avion caractérisée :
```c++
int main()
{
    Plane pl;
    Vehicle& plr = pl;
    
    Parking p;
    WideParking wp;
    
    p.park(plr);
    wp.park(plr);

    return 0;
}
```

Ce qui nous donne :
```
Bienvenue au garage !
Je suis un avion ! :)
Bienvenue au garage extra-large !
Je suis un avion ! :)
```

Il s'agit toujours du comportement attendu et pourtant cette fois il y a eu liaison dynamique. En effet, on ne pouvait déterminer qu'en _run time_ que l'objet passé aux parkings était un avion et non pas un simple véhicule. Par ailleurs, si l'on avait retiré la virtualité à la méthode ```print```, nous n'aurions évidemment pas eu le message indiquant qu'il s'agit d'un avion.

Un dernier exemple au comportement attendu avant de montrer les limites du _Single Dispatch_ :
```c++
int main()
{
    Vehicle v;
    Plane pl;

    WideParking wp;
    Parking& wpr = wp;

    wpr.park(v);
    wpr.park(pl);

    return 0;
}
```

Avec pour sortie :

```
Bienvenue au garage extra-large !
Je suis juste un vehicule ! :'(
Il y a toute la place qu'il faut pour un avion !
Je suis un avion ! :)
```

Cette fois, c'est un pointeur sur ```Parking``` qui pointe sur un objet ```WideParking```. Les types des véhicules sont pleinement caractérisés. On pourrait alors croire qu'il y a eu une liaison statique alors qu'en réalité la liaison c'est effectuée en _run time_. En effet, l'instance de l'objet est un paramètre de la méthode ```park```. Ainsi, pour appeler la bonne méthode ```park```, il a fallu attendre l'appel effectif pour que le contexte permette de savoir qu'il s'agissait bien d'un ```WideParking``` !

Pour vous convaincre que l'instance est bien un paramètre, voici le cas pathologique :
```c++
int main()
{
    Plane pl;
    Vehicle& plr = pl;
    
    WideParking wp;
    Parking& wpr = wp;
    
    wp.park(pl);
    wp.park(plr);
    
    wpr.park(pl);
    wpr.park(plr);

    return 0;
}
```

Et nous obtenons ainsi :
```
Il y a toute la place qu'il faut pour un avion !
Je suis un avion ! :)
Bienvenue au garage extra-large !
Je suis un avion ! :)

Il y a toute la place qu'il faut pour un avion !
Je suis un avion ! :)
Bienvenue au garage extra-large !
Je suis un avion ! :)

```

Les 3 premiers appels ont été traités dans les exemples précédents. Le dernier ne donne cependant pas le résultat correct ! En effet, nous aurions aimé avoir :
```
Il y a toute la place qu'il faut pour un avion !
Je suis un avion ! :)
```

Le _Single Dispatch_ fait que la résolution ne permet pas de trouver la bonne implémentation entre ```WideParking::park(const Vehicle&) const``` et ```WideParking::(const Plane&) const``` ainsi, c'est la première qui est appelée puisque c'est le type légitime de ```plr```. On voit bien que le premier argument traité pour le dispatching est l'instance de l'objet qui appelle la méthode, puisqu'on appelle bien une méthode de l'objet ```WideParking``` et non pas ```Parking```.

D'où provient cette limitation en nombre qui peut sembler surprenante ?    
La raison est assez simple et n'est pourtant pas liée directement au C++. Le mécanisme de résolution des appels virtuels se fait au travers d'une structure de données appelée la _vtable_ qui ne permet pas directement de faire de la liaison multiple. La _vtable_ se charge de stocker dans un tableau interne et invisible au programmeur, des pointeurs vers les instances de classes allouées. Typiquement, une _vtable_ sera créée pour chaque classe.    
Là où le bat blesse, c'est que l'implémentation de la _vtable_ est dépendante du compilateur, de même que les mécanismes nécessaires à son bon fonctionnement (notamment l'ajout de code dans le constructeur des objets, pointeurs internes à l'instance). Pire encore, le standard ne spécifie pas l'usage d'une _vtable_ pour la liaison dynamique et donc, en théorie, il serait possible d'utiliser des alternatives. Cependant, le standard guide suffisemment pour que l'approche _vtable_ soit celle retenue par tous les compilateurs.

Pour information, diverses autres solutions existent, notamment des arbres binaires de recherche ou des tables de hashages. L'avantage de la _vtable_ est sa simplicité d'implémentation et ses performances plutôt bonnes. 

Notons que sous gcc, l'option ```-fdump-class-hierarchy``` permet d'afficher la vtable.

##### Double Dispatch en C++ : patron de conception Visiteur

Le besoin de liaison double est un besoin relativement courant en développement logiciel et c'est donc tout naturellement qu'un patron de conception visant à résoudre le problème a vu le jour. Connu sous le nom de Visiteur, il permet de simuler une liaison double lorsque le nombre de classes est relativement restreint (sinon le surcoût en terme de code et donc de maintenabilité devient problématique).

Si techniquement il permet la simulation de la liaison double dynamique, les problèmes rencontrés qui amènent à se tourner vers cette solution relèvent plutôt de la séparation entre algorithme et structure de données.

Le principe est d'avoir une méthode publique pour chaque objet devant être visité, prenant un objet Visiteur devant effectuer un traitement en utilisant des données internes à l'objet visité. Cette méthode publique va appeler la méthode effectuer ce traitement sur l'instance du Visiteur, tout en lui donnant une réference sur lui même.

Concrètement, admettons que nous ayons ces quelques classes :

```c++
class A;

class B : public A {};
class C : public A {};
```

Pour chaque objet dérivant de A, nous devons créer une méthode acceptant un Visisteur :

```c++
 void B::acceptVisit(Visitor *visitor) {
   visitor->visitB(this) ;
 }

 void C::acceptVisit(Visitor *visitor) {
   visitor->visitC(this) ;
 }
```

Enfin, nous devons créer notre visiteur et chacune de ses méthodes pour visiter nos objets.

```c++
void Visitor::visitB(B * object) {
    // Le traitement de l'objet de type B en utilisant une instance pleinement caractérisée
  }
```
 On comprendra donc pourquoi le visiteur n'est une solution efficace et élégante qu'en présente d'un nombre restreint de classes.

La littérature sur les patrons de conception étant vaste et très bien fournie, je me contenterai ici de ce strict minimum pour parler du _tag_ _dispatching_, beaucoup moins représenté.

### Tag Dispatching
#### Présentation & Mise en place
Le _Tag Dispatching_ est une technique de métaprogrammation permettant de choisir en _compile time_ un algorithme ou plus généralement une fonction polymorphique en fonction des besoins. Cette technique est donc souvent couplée aux classes de politique ou _Type Traits_.

Concrètement, il s'agit de surcharger une fonction en rajoutant un paramètre invisible pour l'utilisateur : le tag. Seule la version sans tag est laissée publique et c'est cette version qui va appeler la version correcte au travers du tag correspondant. Un tag est une structure de donnée vide, qui porte généralement l'information utile grâce à son ou ses templates.

Imaginons une politique de gestion du parallélisme constituée de deux classes : ```MonoThread``` et ```MultiThread```. Dans le premier cas, aucun mécanisme de vérification d'accès concurrent ne sera fourni, tandis que la seconde fourni toute l'interface nécessaire au parallélisme.

J'ai un algorithme qui dépend d'une heuristique, qui pourra être changée à la volée en fonction du contexte. Cependant, si je peux paralléliser le traitement de mon heuristique avec d'autres étapes de mon algorithme, l'algorithme et l'heuristique vont accéder à des données en commun et il est donc important de s'assurer que l'heuristique est _thread-safe_ (elle a le niveau de granularité le plus fin, c'est donc à elle d'assurer ce rôle).    
Cependant, il existe des cas où l'on ne veut pas exécuter en parallèle l'heuristique (parce que les accès concurrents feraient perdre trop de temps pour un gain non significatif, parce que la machine cible ne sera capable de gérer le multithread correctement, etc).

Le _Tag Dispatching_ va nous permettre d'appeler la bonne version de l'algorithme selon la politique de l'heuristique.

Voici les politiques :
```c++
struct MonoThread
{
    void Lock()
    {
        cout << "Rien à locker, je suis en monothread !" << endl;
    }
    
    void Unlock()
    {
        cout << "Rien à unlocker !" << endl;
    }
};

class MultiThread
{
public :
    void Lock()
    {
        m.lock();
        cout << "Je lock le scope, des accès concurrents sont possibles. " << endl;
    }
    
    void Unlock()
    {
        cout << "On delock le scope !" << endl;
        m.unlock();
    }
    
protected :
    std::mutex m;
};
```

Et voici l'heuristique. Il faut bien comprendre que l'heuristique ne fait pas forcément ses traitements en parallèle. Le _lock_ effectué s'assure juste l'exclusivité sur l'accès des données partagées (non représentées ici).
```c++
template <class ThreadPolicy = MonoThread>
struct Heuristic : protected ThreadPolicy
{
    void operator()()
    {
        ThreadPolicy::Lock();
        cout << "On lance l'heuristique !" << endl;
        ThreadPolicy::Unlock();
    };
};
```

Enfin, voici les tags et l'algorithme : 
```c++
template <bool> struct isMultiThread {};
using multi_tag = isMultiThread<true>;
using mono_tag = isMultiThread<false>;
```

Tout d'abord, nous définissons le tag général : l'information utile est portée par le template booléen. Soit nous sommes en _multithread_, soit nous sommes en _monothread_ et ainsi nous spécialisons les tags. A noter que dans un cas plus complexe, il est possible de laisser un cas par défaut.

```c++
class Algo
{
public :
    template <class T>
    void operator()(Heuristic<T>& h)
    {
        cout << "On lance l'algorithme !" << endl;
        cout << "Quelques étapes d'initiatialisation" << endl;
        operator()(h, isMultiThread<is_same<T, MultiThread>::value>());
    }
    
protected :
    template <class T>
    void operator()(Heuristic<T>& h, const multi_tag&)
    {
        cout << "Chouette, mon heuristique est protégée, je peux la lancer en parallèle" << endl;
        thread t(ref(h));
        cout << "Quelques opérations en parallèle de mon heuristique." << endl;
        t.join();
    }
    
    template <class T>
    void operator()(Heuristic<T>& h, const mono_tag&)
    {
        cout << "Mince, mon heuristique n'est pas parallèle." << endl;
        h();
    }
};
```

Seule la version sans tag de l'opérateur ```()``` est laissée publique. Les templates étant résolus à la compilation, lorsque le compilateur arrive sur la ligne ```operator()(h, isMultiThread<is_same<T, MultiThread>::value>());```, il va remplacer l'appel par le résultat du _type trait_ de la bibliothèque standard ```is_same``` qui renvoie la valeur vrai si les types des deux templates spécifiés sont les même et faux autrement.

Ainsi, si la politique *T* de l'heuristique est ```MultiThread```, cette ligne sera équivalente à ```operator()(h, multi_tag)``` qui correspond au prototype de l'appel parallèle puisque ```multi_tag``` est un alias sur ```isMultiThread<true>```. Dans le cas contraire, c'est l'appel séquentiel qui sera engagé.

Avec le main suivant :
```c++
int main()
{
    Heuristic<MultiThread> heur_mt;
    Algo algo;
    
    algo(heur_mt);
    
    return 0;
}
```

Nous obtenons la sortie suivante :
```c++
On lance l'algorithme !
Quelques étapes d'initiatialisation
Chouette, mon heuristique est protégée, je peux la lancer en parallèle
Quelques opérations en parallèle de mon heuristique.
Je lock le scope, des accès concurrents sont possibles. 
On lance l'heuristique !
On delock le scope !
```

Et si l'on change la politique de l'heuristique pour MonoThread :
```c++
On lance l'algorithme !
Quelques étapes d'initiatialisation
Mince, mon heuristique n'est pas parallèle.
Rien à locker, je suis en monothread !
On lance l'heuristique !
Rien à unlocker !
```

Précisions tout de même que cette implémentation n'est pas _exception_ _safe_ mais laissée en l'état pour des raisons pédagogiques.

#### Coût

Le coût du _Tag Dispatching_ est très faible puisqu'il ne représente qu'un temps de compilation plus élevé et l'appel d'une fonction supplémentaire. En terme de place mémoire, le compilateur optimise normalement les tags qui disparaitront, étant vides et non utilisés en _run time_.

### Conclusion

Au cours de cet article nous avons pu aborder une bonne partie des mécanismes de liaisons, qu'ils soient statiques ou dynamiques, simples ou multiples. Nous avons également donné des pistes pour émuler une liaison dynamique double en C++ avec le patron de conception Visiteur, et d'une technique de programmation générique permettant la sélection de fonction en compile time, à savoir le _Tag Dispatching_.

Pour conclure, notons qu'il existe diverses méthodes pour implémenter de manière plus élégante que le Visiteur la liaison dynamique mais nous laissons cela en référence pour le lecteur qui voudrait aller plus loin. Est également présent dans les références, un article sur des structures de données liées aux liaisons dynamiques.

### Références

+ [Open Multi-Methods for C++](http://www.stroustrup.com/multimethods.pdf), P. Pirkelbauer Y. Solodkyy B. Stroustrup
+ [Evaluation of Control Structures for Dynamic Dispatching](http://hal.inria.fr/inria-00072218/PDF/RR-4370.pdf), O. Zendra K.Driesen
+ [Multi-Paradigm Design](http://www.netobjectives.com/files/CoplienThesis.pdf), de James O. Coplien
