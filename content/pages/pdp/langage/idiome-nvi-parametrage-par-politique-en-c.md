Title: Idiome NVI & Paramétrage par politique en C++
Order: 9
Date: 2015-01-23
Tags: idiome, nvi, c++, tutoriel
Slug: idiome-nvi-parametrage-par-politique-en-c
Author: Höd
Display: true

### Introduction & Motivations

Cet article, sur le C++, vise à présenter d'une part l'idiome NVI, pour « Non Virtual Interface », et d'autre part, une technique de conception développée par Andreï Alexandrescu, notamment présentée dans son livre Modern C++ Design, à savoir le paramétrage pas politique.   
Le choix de présenter au sein du même article un idiome et une méthode plus générale d'architecture logicielle est motivé par le fait que la combinaison des deux permet de produire du code robuste, plus spécifiquement destiné à être réutilisé (notamment dans le cadre d'un framework ou d'une bibliothèque).    

Dans un premier temps nous aborderons l'idiome NVI, ses applications et sa mise en place. Ensuite, nous verrons ce qu'est le paramétrage par politique et la manière d'identifier des comportements transversaux au sein d'un ensemble de classes.
Enfin, nous mettrons en application la combinaison des deux techniques afin de produire du code tirant bénéfice de ces deux techniques.

Dans la suite de l'article on se placera dans une situation générale où l'on écrit du code dit « service », pour un client qui écrira du code dit « client ».

[TOC]

### L'idiome NVI
#### Violation du SRP

Une façon classique de considérer une interface est la suivante :
```cpp
class InterfaceService
{
public :
    virtual void service(); // Eventuellement virtuel pur
};
```

Une classe concrète pourra ou devra (selon ce que propose l'interface) réimplémenter le service de la sorte :
```cpp
class MonService : public InterfaceService
{
public : 
    virtual void service() { // Implémentation de mon service }
};
```

Cette approche très utilisée en Java notamment propose un désavantage de taille. En effet, en procédant de la sorte, nous donnons deux responsabilités à la classe concrète MonService :

- L'implémentation du service
- La réalisation du service

Ceci est donc une violation du « Single responsibility principle » qui veut que chaque objet ne se voit accorder qu'une unique responsabilité (et que cette responsabilité doit être complètement encapsulée par cette classe).

Aidons-nous de ce petit exemple de code client pour mieux comprendre :
```cpp
class A
{
public :
    void operator()(InterfaceService& _serveur)
    {
        _serveur.service();
    }
};

int main(void)
{
    A a;
    MonService s;
    
    a(s);

    return 0;
}
```

On voit très clairement que le code client s'adresse directement à MonService malgré le fait qu'il manipule InterfaceService. Enfin, le service est réalisé par MonService, ce qui semble légitime.    
La mauvaise distribution des responsabilités au sein d'une architecture est source de rigidité et va donc à l'encontre de la ré-utilisabilité et augmente la maintenance par une complexification du code.

#### Programmation par contrat

L'idiome NVI permet de distribuer ces responsabilités par la définition d'un contrat entre l'Interface et la classe concrète : l'Interface se charge de la vérification des invariants et préconditions sur le service et en contrepartie, la classe concrète se charge d'implémenter le service concret.

Voici l'implémentation de l'idiome :
```cpp
class InterfaceService
{
public :
    void service(); // Notez la non-virtualité

private : // Notez le private
    virtual void _service(); // Eventuellement virtuel pur
};

InterfaceService::service()
{
    // Préconditions & invariants
    // ...

    _service();

    // Postconditions & invariants
    // ...
}
```

Contrairement à la première approche, ici c'est bien InterfaceService::service qui sera appelé par le code client et qui lui même appellera l'implémentation du service (soit celle qu'il propose par défaut, soit celle redéfinie par la classe concrète MonService).   


#### Inversion de contrôle

On a ici une vraie séparation des responsabilités en plus d'une factorisation du code appréciable : les préconditions et postconditions sont réalisées à un unique endroit : dans l'interface, c'est à dire dans le code service.   
Au delà du respect du SRP, cela permet également de centraliser en un endroit les préconditions relatives au contrat d'appel entre le code client et le code service : après tout, le never trust user inputs s'applique également avec un client. Qui nous garantit que si le client écrit une classe héritant de InterfaceService, il pensera à vérifier les invariants nécessaires au bon fonctionnement de la classe ?

En fait, le NVI permet une inversion de contrôle, caractéristique d'un framework : c'est le code service qui va appeler le code client et non l'inverse comme c'est le cas avec une simple bibliothèque. La différence est qu'ici, cette inversion de contrôle a une granularité très fine puisqu'elle est à l'échelle d'une classe, là où elle est généralement à l'échelle du flux d'exécution pour un framework. Cette inversion de contrôle permet de mieux faire face à la hantise du designer : le Fragile Base Class problem.    

Ce qui permet de réaliser cette inversion de contrôle est non seulement l'appel à l'implémentation du service par l'interface mais aussi et surtout l'encapsulation de l'implémentation du service dont la visibilité est privée dans l'interface, ce qui fait qu'elle sera impossible à appeler depuis la classe concrète du fait de sa virtualité.
On s'assure alors que le code client n’appellera jamais le code service.

Dans de très rares occasions, cela peut cependant être utile de procéder de la sorte. Pour cela, il est toujours possible de définir la méthode _service avec une visibilité en protégée, ce qui permettra au code client d'appeler l'implémentation par défaut :

```cpp
class InterfaceService // Évidemment on ne devrait avoir d'un seul service, ceci est juste pour l'exemple !
{
public :
    void service();

protected :
    virtual void _service();

private :
    virtual void _service2();
};

class MonService : public InterfaceService
{ 
    virtual void _service()
    {
        InterfaceService::_service(); // OK
    }

    virtual void _service2()
    {
        InterfaceService::_service2(); // ERROR
    }
};
```

#### Ce qu'il faut retenir

NVI aide à localiser les invariants à un unique endroit permettant de prévenir ou sécuriser le code client quand à la consistance de ces invariants. L'inversion de contrôle permet de respecter le Single Responsability Principle et de mieux maîtriser le problème du Fragile Base Class.   

Pour la mise en place, citons Herb Sutter, dans son article Virtuality :

- Prefer to make interfaces nonvirtual, using Template Method design pattern.
- Prefer to make virtual functions private.
- Only if derived classes need to invoke the base implementation of a virtual function, make the virtual function protected.
- A base class destructor should be either public and virtual, or protected and nonvirtual.

#### Un mot sur Patron de Méthode

Il est important d'insister sur le fait que NVI n'est pas la même chose que le patron de conception Patron de Méthode. En effet, la ressemblance est très forte sur le plan technique puisque ce patron de conception s'articule autour d'une interface définie ou redéfinie par les besoins concrets au niveau de sous-classes.

La principale différence provient des motivations : l'objectif d'un patron de conception Patron de Méthode est de proposer un découpage logique d'un algorithme ou d'un service en méthodes dont l'implémentation de certaines sera reléguée à des sous-classes concrètes, permettant de modifier l'algorithme selon diverses considérations sans pour autant risquer de changer la structure générale de l'algorithme.

### Paramétrage par politiques
#### Présentation

Le paramétrage par politique est une technique de programmation développée et démocratisée par Andrei Alexandrescu dans son livre Modern C++ Design: Generic Programming and Design Patterns Applied et dans la bibliothèque Loki dédiée à la méta-programmation en C++.    

Concrètement, il s'agit de profiter de l'héritage multiple et de la méta-programmation pour permettre de séparer les différents comportements d'une classe ou de plusieurs classes et de créer sur mesure des comportements en combinant plusieurs politiques.

#### Identification des politiques

La clef d'un paramétrage par politique efficace réside dans l'analyse des différents comportements d'une classe ou d'un ensemble de classes. Imaginons que nous ayons à créer une bibliothèque de gestion de graphes. Un graphe peut être représenté sous différentes formes : matrice d'adjacence, matrice d'incidence , ou liste de successeurs. Chaque représentation à ses avantages et ses inconvénients en fonction des applications. On pourrait aisément créer 3 classes différentes mais cela ne serait pas très pertinent. On pourrait simplement templater la classe de graphe mais chaque type donné n'a pas la même API. De plus, imaginons qu'un graphe puisse être partagé entre plusieurs thread ou non selon les applications.    
Sans paramétrage par politique, il faudrait un nombre de classes égales au nombre de facteurs de comportement multiplié par le nombre de modes par facteur. Cela apporterait évidemment du code redondant et une maintenabilité moindre puisque dans le cas d'un paramétrage par politique le but est d'isoler complètement un comportement. Pour modifier l'intégralité du modèle multithread d'une application, la modification d'une seule classe de politique est nécessaire.

Chaque facteur est représenté par une classe abstraite permettant de définir l'API commune à tous les modes et qui pourra être utilisée par les classes paramétrées avec ce facteur. Les classes concrètes implémentent chacun des modes de la politique.    
Enfin, la classe de services qui doit être paramétrée par politique va être templatée avec chacune des politique et en hériter de manière publique ou privée selon les besoins.

Le mot clef pour distinguer les comportements d'une classe est l'orthogonalité. En effet, les politiques doivent être totalement orthogonale et de fait, être indépendantes. On perd tout l'intérêt, en terme de maintenabilité et de simplicité dans le cas où une politique dépend d'une autre.    
Dans le cas de notre graphe, la représentation des données et son accès sont indépendants de la politique de multithread. C'est à la classe concrète de graphe d'utiliser ces deux politiques pour rendre ses services indépendamment des modes de politique choisis.

#### Mise en place

La mise en place est aisée. Dans un premier temps, il suffit de définir des classes de politiques. Nous choisissons de créer une hiérarchie de classes pour chaque facteur.    
Dans l'exemple évoqué à la section précédente, nous avons d'une part la politique relative au contexte parallèle et la politique relative à la représentation (et l'utilisation) des données du graphe.

```cpp
class ThreadingModel 
{
protected :
    virtual void Lock() = 0;
};

class MultiThread : public ThreadingModel
{
protected :
    virtual void Lock()
    {
        m.lock();
    }
    
    std::mutex m;
};

class MonoThread : public ThreadingModel
{
protected :
    virtual void Lock() { }
};

// ... Autres modeles ...
```

On définit la classe principale de graphe et on la paramétrise à l'instanciation selon les besoins :
```cpp
template <class Rep = AdjacenceMatrix, class ThreadModel = MonoThread>
class Graph : public Rep, protected ThreadModel
{
public :
    bool IsConnected() const
    {
        ThreadModel::Lock();
        return Rep::IsConnected();
    }
};

using GraphInciMT = Graph<IncidenceMatrix, MultiThread>;
using GraphAdjMT = Graph<AdjacenceMatrix, MultiThread>;

// Exemples
Graph a; // Adjacence, MonoThread
GraphInciMT b; // Incidence, MultiThread
GraphAdjMT c; // Adjacence, MultiThread
```
La classe Graph fait appelle à l'aveugle à sa politique de thread ainsi qu'à sa politique de représentation. La bonne écriture d'une politique est guidée par l'API de la classe abstraite en haut de la hiérarchie mais aucune vérification de type n'est effectuée par la classe Graph. Ainsi, un client pourrait écrire sa propre politique qui ne serait pas basée sur une des classes abstraites du code service.

La partie définissant les alias n'est pas du simple sucre syntaxique puisqu'il contribue également à la maintenabilité de l'application. L'utilisateur final utilise des types en dur, sans template, ce qui permet, si le besoin s'en fait sentir, de ne changer le template qu'à un unique endroit.

### Combiner les deux techniques

En observant attentivement l'exemple utilisant le paramétrage par politique, on se rend compte que le but de chaque politique est d'apporter un ensemble de services aux classes. On peut donc structurer nos hiérarchies de politiques en utilisant l'idiome NVI, leurs apportant tous les avantages cités précédemment.

```cpp
class ThreadingModel 
{
protected :
    void Lock() 
    {
        Logger << std::this_thread << " : acquisition du lock." << std::endl;
        _Lock();
    }

private : 
    virtual void _Lock() = 0;
};

class MultiThread : public ThreadingModel
{
private :
    virtual void _Lock()
    {
        m.lock();
    }
    
    std::mutex m;
};

class MonoThread : public ThreadingModel
{
private :
    virtual void Lock() = default
};

// ... Autres modeles ...
```

Le reste ne change. Cependant, cela présente le désavantage de briser un des intérêts du NVI qui était de localiser les vérification des préconditions et des invariants à un seul endroit.  
En effet, l'utilisateur peut très bien écrire une classe de politique possédant l'interface requise par la classe paramétrée, sans respecter les invariants intrinsèques au service offert par la politique.

#### Limitation du type de politique

Nous pouvons cependant forcer l'héritage de la classe de politique depuis la classe base de la hiérarchie par l'utilisation d'une assertion statique. Aucun overhead en runtime n'est à prévoir puisque l'assertion est statique.

```cpp
template <class Rep = AdjacenceMatrix, class ThreadModel = MonoThread>
class Graph : public Rep, protected ThreadModel
{
public :

    Graph()
    {
        static_assert(std::is_base_of<ThreadModel, ThreadingModel>::value, "ThreadModel must inherit from ThreadingModel class");
    }
    
    // ...
};
```

Le choix de la vérification basée sur l'interface ou celle plus stricte, basée sur l'interface et le type de la politique dépend du degré de liberté que vous souhaitez accorder à l'utilisateur. 

### Une alternative

Comme il m'a été fait remarqué, à la relecture de cet article, l'utilisation de classes virtuelles et de template a un effet certain sur les performances en plus de n'avoir qu'un avantage : l'utilisation de politiques dynamiques.

Il a alors été proposé une alternative intéressante, qui permet en outre, de n'effectuer la vérification que sur demande explicite :

```cpp
template <typename Policy> class AssertChecker : protected Policy {
protected:
    void service(int i) { 
        assert(i > 42);
        Policy::service(i);
    }
};

class Policy1 { void service(int i); };
class Policy2 { void service(int i); };

template <typename Policy>
class Concret : protected Policy { .... };

Concret<Policy1> c1; // Sans vérification de contrat
Concret<AssertChecker<Policy1>> c1bis; // Avec vérification de contrat
```


### Allez plus loin : politique de base à la construction logicielle

Il peut parfois être intéressant, pour des questions de commodité, d'avoir une politique par défaut qui puisse être modifiée dans l'ensemble du logiciel lors de la compilation.    
L'exemple le plus classique est celui de la politique du modèle de thread utilisée. En fonction de la machine sur laquelle va tourner le programme (ou des programmes utilisant la bibliothèque s'il s'agit d'une bibliothèque), on peut vouloir par défaut l'utilisation d'un unique thread et se passer de l'overhead généré par la protection des accès concurrents, ou alors au contraire utiliser l'ensemble de cœurs disponibles, choisir le mode de parallélisme (thread standards ou OpenMP par exemple, voire MPI), etc.

Évidemment, on veut toujours pouvoir redéfinir localement la politique pour des raisons diverses et variées (dans notre exemple, l'utilisateur peut juger que localement il n'est pas nécessaire d'utiliser un modèle parallèle car il y aurait un overhead trop important sur une instance donnée).

Pour se faire on peut envisager la définition d'une constante via le préprocesseur et la définition d'un alias permettant d'avoir un vrai type à passer en paramètre comme politique :

```cpp
#ifndef DEFAULT_THREADING_MODEL
#define DEFAULT_THREADING_MODEL MultiThread

#ifndef DEFAULT_GRAPH_DATA
#define DEFAULT_GRAPH_DATA AdjacenceMatrix

using DefThreadingPolicy = DEFAULT_THREADING_MODEL;
using DefGraphDataPolicy = DEFAULT_GRAPH_DATA;

template <class Rep = DefGraphDataPolicy, class ThreadModel = DefThreadingPolicy>
class Graph : public Rep, protected ThreadModel
{ }

```

Cela n'empêche en rien d'utiliser des alias spécialisant les templates comme vu précédemment.

Il suffit ainsi de redéfinir le constante souhaitée au moment de la compilation :
```
g++ -DDEFAULT_THREADING_MODEL=MonoThread ...
```

## Conclusion

Comme n'importe quel patron de conception et autre technique de conception, l'utilisation du NVI ou du paramétrage par politique ne doit pas être systématique mais faire l'objet d'une motivation réelle vis à vis d'une situation où elle est pertinente.   
Ces situations n'ont pas été décrites en détail puisqu'il est impossible d'en dresser une liste exhaustive : l'important est d'identifier les situations où leur utilisation est bénéfique ou résout un problème donné.

L'utilisation stricto sensu des deux techniques combinées présente le désavantage d'un surcoût naturel lié à l'utilisation de méthodes virtuelles avec des templates ce qui peut être rebutant. Cette utilisation n'est intéressante que dans le cas où l'on veut absolument maintenir la consistance d'une hiérarchie de classes de politique. Dans les autres cas, il est certainement plus intéressant d'utiliser l'alternative proposée.    

J'espère que cet article vous aura donné les grandes lignes permettant de justifier l'utilisation du NVI et du paramétrage par politique, ainsi que quelques idées pour combiner les deux et faciliter la vie aux utilisateurs de votre code.
