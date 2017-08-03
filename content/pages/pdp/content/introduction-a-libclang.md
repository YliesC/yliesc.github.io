Title: Introduction à libclang
Order: 9
Date: 2014-09-27
Slug: introduction-a-libclang
Author: Davidbrcz
Display: true

## Introduction ##
Un adage populaire veut que tout programmeur soit le plus fainéant possible. Et la manipulation de code source déjà écrit (dans un but de refactorisation par exemple) est une tache pénible qui doit revenir à l'ordinateur.

Le but de cet article est de présenter libclang, une interface à clang qui va nous aider dans cette tache. Le but final de l'article est d’écrire un petit outil pour créer automatiquement des fichiers squelettes à partir des headers.

[TOC]

## Clang-LLVM : Kezako ? ##

Clang est un compilateur (au même titre que g++ ou ICC) qui via divers frontend supporte le C, C++ et l'Objective C.

Initié par Apple en 2005, il a été rendu open-source en 2007. Pour rappel, le travail essentiel d'un compilateur est de transformer un fichier texte en une représentation intermédiaire facilement manipulable. On peut visualiser cette représentation intermédiaire sous forme d'arbre abstrait de syntaxe (ou AST en anglais, pour *Abstract syntax tree*)

La gestion de cette représentation est confiée à LLVM (historiquement pour *Low Level Virtual Machine*) qui se chargera de l'optimiser et de la retraduire en langage machine adapté à la cible (x86 ou ARM, Linux ou Windows, 32 ou 64 bits...)

On peut résumer ceci par le schéma suivant : 
![schema](../../../progdupeupl//galleries/54/c10b26e4-7af9-457d-bac1-2a34fd6a31d3.png)

Par ailleurs, clang fournit [plusieurs interfaces](http://clang.llvm.org/docs/Tooling.html) pour manipuler l'arbre résultant de la phase.

 - La première est Libclang à proprement parler. C'est une interface stable de haut niveau écrite en C.
 - Ensuite vient Clang Plugins, interface dédiée à la création de plugins intégrés dans clang qui seront appelés lors de la compilation.
 - Enfin, vient libtooling une interface en C++ qui vise à faciliter l’écriture d'outils standalone.

On va choisir la dernière, car elle correspond bien à ce qu'on souhaite faire.

## AST ##
### Exemple basique  ###
Pour illustrer la notion d'AST, il est plus simple de partir sur des exemples simples d'expressions arithmétiques .

L’idée directrice est de construire un arbre,où chaque nœud va correspondre à un élément de l'expression (un nombre, un opérateur) et dont les fils (si applicable) sont ce sur quoi le nœud va agir. Il représente la structure du programme 

Exemple sur l'expression 2+3*5.
![exemple_expression](../../../progdupeupl//galleries/54/e059e91c-5dc6-43d3-9eb6-fc083c827303.png)

C'est sous  cette représentation qu'on peut facilement travailler l'expression.
### Exemple sur des codes sources ###
NB : Je ne vais pas détailler ici comment se passe le processus de création des AST, juste utiliser le résultat. Si vous voulez en savoir plus, vous pouvez toujours regarder des cours de compilation.  

On peut étendre les AST pour représenter des codes sources en généralisant les noeuds. 
Par exemple, un noeud pourra symboliser une boucle *while*. Un de ses fils symbolisera la condition à remplir et l'autre le corps de la boucle.

Avec le code source suivant, 

```c++
int foo(int x)
{
        return 2*x;
}


int main(int argc,char* argv[])
{
    int i=0;
    while(foo(i)<10)
    {
        ++i;
    }
}
```

clang génère l'AST suivant :

```text
FunctionDecl 0x2add210 </home/david/libclang/src/test.cpp:1:1, line:4:1> foo 'int (int)'
|-ParmVarDecl 0x2add150 <line:1:9, col:13> x 'int'
`-CompoundStmt 0x2add360 <line:2:1, line:4:1>
  `-ReturnStmt 0x2add340 <line:3:9, col:18>
    `-BinaryOperator 0x2add318 <col:16, col:18> 'int' '*'
      |-IntegerLiteral 0x2add2b8 <col:16> 'int' 2
      `-ImplicitCastExpr 0x2add300 <col:18> 'int' <LValueToRValue>
        `-DeclRefExpr 0x2add2d8 <col:18> 'int' lvalue ParmVar 0x2add150 'x' 'int'

FunctionDecl 0x2b089d0 </home/david/libclang/src/test.cpp:7:1, line:14:1> main 'int (int, char **)'
|-ParmVarDecl 0x2add390 <line:7:10, col:14> argc 'int'
|-ParmVarDecl 0x2b08900 <col:19, col:30> argv 'char **'
`-CompoundStmt 0x2b08d30 <line:8:1, line:14:1>
  |-DeclStmt 0x2b08b08 <line:9:5, col:12>
  | `-VarDecl 0x2b08a90 <col:5, col:11> i 'int'
  |   `-IntegerLiteral 0x2b08ae8 <col:11> 'int' 0
  `-WhileStmt 0x2b08d08 <line:10:5, line:13:5>
    |-<<<NULL>>>
    |-BinaryOperator 0x2b08c78 <line:10:11, col:18> '_Bool' '<'
    | |-CallExpr 0x2b08c10 <col:11, col:16> 'int'
    | | |-ImplicitCastExpr 0x2b08bf8 <col:11> 'int (*)(int)' <FunctionToPointerDecay>
    | | | `-DeclRefExpr 0x2b08ba0 <col:11> 'int (int)' lvalue Function 0x2add210 'foo' 'int (int)'
    | | `-ImplicitCastExpr 0x2b08c40 <col:15> 'int' <LValueToRValue>
    | |   `-DeclRefExpr 0x2b08b78 <col:15> 'int' lvalue Var 0x2b08a90 'i' 'int'
    | `-IntegerLiteral 0x2b08c58 <col:18> 'int' 10
    `-CompoundStmt 0x2b08ce8 <line:11:5, line:13:5>
      `-UnaryOperator 0x2b08cc8 <line:12:9, col:11> 'int' lvalue prefix '++'
        `-DeclRefExpr 0x2b08ca0 <col:11> 'int' lvalue Var 0x2b08a90 'i' 'int'
```
Le premier élément de chaque ligne correspond au type (au sens classe du C++) du nœud. La mise en page permet de visualiser les relations parent-enfant entre les différents nœuds. On retrouve aussi l'adresse de l'objet en mémoire, sa position dans le fichier source et si ceci a du sens, des informations sur son type dans le code source en fin de ligne.

A noter que pour chaque élément de plus haut niveau (déclaration d'une fonction, d'une classe, d'une variable globale), clang va générer un AST. Donc dans le code précédant, il y a en réalité 2 AST. Un pour *foo* et un autre pour *main*.

## Examen des AST ##
Chaque nœud d'un AST est une instance d'une classe dérivée soit de *Decl* soit de *Stmt*.

 - *Decl* (pour Déclaration), représente une déclaration au sens général. Il existe des sous classes pour la déclaration de fonction, de classe ou de paramètre dune fonction. Je vous laisse admirer [l'arbre d’héritage](http://clang.llvm.org/doxygen/classclang_1_1Decl.html) de la classe *Decl* pour vous faire une idée.
 - *Stmt* (pour *Statement*), représente différents types d'expression et de structure de contrôle associée. Là encore, il existe des sous classes pour tout. Du *for* au *try-catch*, tout y passe. De la même manière , [l'arbre d’héritage](http://clang.llvm.org/doxygen/classclang_1_1Stmt.html) résume bien la chose.


Plusieurs remarques sont à faire : 

 -  Les commentaires ne sont bien sur pas présents dans l'AST. En effet, ils sont la pour le programmeur, pas pour le compilateur. 
 -  De la même façon, toutes les macros ont été évaluées, il n'y en a donc plus aucune trace dans l'AST. 
 -  Enfin, en C++11 les variables déclarées avec un type auto ont vu leur type inféré.

## Parcours AST ##
Maintenant qu'on dispose d'un AST, il faut le parcourir.

### Visiteur de l'AST ###
La méthode classique est d'utiliser le pattern visiteur. Pour ce faire, on va donc déclarer une classe *ExampleVisitor*
qui va dériver de la classe template *RecursiveASTVisitor* en utilisant le [CRTP](https://en.wikipedia.org/wiki/Curiously_recurring_template_pattern).


```c++
class ExampleVisitor : public RecursiveASTVisitor<ExampleVisitor> {
private:
    ASTContext *astContext;

public:
    explicit ExampleVisitor(CompilerInstance *CI,StringRef file)
      : astContext(&(CI->getASTContext())) 
    {
    }
   
   virtual bool VisitTypeDecl(Decl  *d) {
        return true;
    }
};
```
De cette façon, on dispose de fonctions telles que `VisitVarDecl `ou `VisitTypeDecl `qui seront appelées respectivement 
lors de la déclaration dune fonction ou lors de la déclaration d'un nouveau type. Plus généralement, pour une classe de *TypeNoeud*, on dispose de la fonction `VisitNodeType(NodeType *)`Ces fonctions doivent renvoyer **true** si le parsing doit continuer ou **false** si au contraire il doit s’arrêter.

Notre classe dispose aussi d'un attribut *ASTContext* qui sert à stocker des informations connexes a l'AST. Il ne sera pas utilisé ici, mais peut servir à beaucoup de choses, dont récupérer le gestionnaire de source pour extraire du code ou savoir si une fonction est *noexcept* en C++11.

### Consommateur d'AST ###
On va ensuite définir une classe *ExampleASTConsumer* qui va dériver de *ASTConsumer* et qui sera chargée 
de construire notre visiteur et d'appeler dessus la fonction membre `TraverseDecl`, qui réalisera un parcours de l'AST.

On peut à ce niveau choisir si on veut un parcours de l'AST une fois que toute la [*translation unit* ](https://en.wikipedia.org/wiki/Translation_unit_%28programming%29)a été parsée (`HandleTranslationUnit`), ou si au contraire on veut le faire à chaque déclaration de premier rang (`HandleTopLevelDecl `).

Toujours dans l'objectif de faire un expander de header, on va choisir de le faire une fois toute la *translation unit* parsée. En effet, de cette façon, on va pouvoir savoir si des fonctions déclarées dans le header disposent d'une définition dans le fichier, puisque tout le fichier aura déjà été parsé.

```c++
class ExampleASTConsumer : public ASTConsumer {
private:
    ExampleVisitor *visitor; 
public:
    explicit ExampleASTConsumer(CompilerInstance *CI,StringRef file)
        : visitor(new ExampleVisitor(CI,file)) 
    { }

    virtual void HandleTranslationUnit(ASTContext &Context) {
       // de cette façon, on applique le visiteur sur l'ensemble de la translation unit
        visitor->TraverseDecl(Context.getTranslationUnitDecl());
    }
};
```

Si on avait utilisé la seconde méthode (celle sur les déclarations de plus haut niveau), le code aurait été le suivant

```c++
    virtual bool HandleTopLevelDecl(DeclGroupRef DR) {
        for (DeclGroupRef::iterator b = DR.begin(), e = DR.end();
             b != e; ++b)
            Visitor.TraverseDecl(*b);
        return true;
    }
```
Avec ce code, pour chaque déclaration de plus haut niveau, on va parcourir chacune des déclarations contenues dans le groupe de déclaration *DR*. Ceci peut paraitre étrange (une déclaration de plus haut niveau qui en contient plusieurs), mais il suffit de  penser à la déclaration de variable globale dans le style `int g1,g2;` pour se convaincre que ceci a du sens.

### Point d'entré ###
Quand on écrit un outil basé sur libtooling, le point d'entré le plus courant se fait via *FrontendAction*. Cette classe permet l’exécution  d'actions définies par l'utilisateur au moment de la compilation. On va créer une classe *ExampleFrontendAction* qui par commodité dérivera de *ASTFrontendAction*. En effet, cette dernière classe se charge d’exécuter l'action voulue. La seule charge qui nous incombe est la création d'un consommateur d'AST  dans la fonction `CreateASTConsumer`. Cette dernière dispose de 2 paramètres. Le premier est le contexte de l'AST et le second une chaine de caractère représentant le fichier actuel. C'est grâce à cette dernière qu'on va pouvoir modifier le fichier source.

```c++
class ExampleFrontendAction : public ASTFrontendAction {
public:
  virtual ASTConsumer *CreateASTConsumer(CompilerInstance &CI, StringRef file) {
    return new ExampleASTConsumer(&CI,file);
};
```
### Main ###
Dans le main, il ne reste plus qu'à créer les objets pour parser la ligne de commande, créer l'outil et le lancer.
Le parsage des options de la ligne de commande offert par libclang peut sembler être trop pour un projet de cette taille mais permet en réalité une grande souplesse à moindre coût.  

En effet, on peut passer à notre outil tous les flags nécessaires de la même manière que si on compilait le code qu'on souhaite analyser. Ceci est très utile si on veut par exemple activer le C++11 (-std=c++11) ou indiquer qu'il faut aussi chercher des header dans tel répertoire (classique option -I/path)


```c++
int main(int argc, const char **argv) {

  CommonOptionsParser op(argc, argv);       
  ClangTool Tool(op.getCompilations(), op.getSourcePathList());

  int result = Tool.run(newFrontendActionFactory<ExampleFrontendAction>());

  return result;
}
```


Compilation : 
Sous Fedora, il faut installer les paquets de développement de llvm et clang ainsi que llvm-static et on compile avec 

``` clang++ -std=c++11 `llvm-config --cxxflags --ldflags` Example.cpp -o app 
-lclangFrontend -lclangSerialization -lclangDriver -lclangTooling -lclangParse -lclangSema 
-lclangAnalysis -lclangRewriteFrontend -lclangRewriteCore -lclangEdit -lclangAST -lclangLex 
-lclangBasic -lclang -lllvm `llvm-config --libs asmparser bitreader support mc option` -lLLVM-3.3```

Utilisation : 

`./app test.cpp -- -std=c++11`

On dispose maintenant d'un programme qui ne fait strictement rien. Mais ceci va très bien tôt changer.

## Écriture d'un expander de header ##
### Contexte ###
Le C++ dispose d'un système de *header*/fichier source. Les *headers* contiennent les déclarations des fonctions et classes,
les fichiers sources les implémentations. De cette façon, quand on a besoin dans un autre fichier d'utiliser certaines choses,
il suffit d'inclure le *header* pour que le compilateur sache ce qu'il en retourne.

Cependant, ce système impose une certaine redondance. Une fois le *header* écrit, il faut ré-écrire quasiment tout.
Prenons l'exemple du fichier suivant
```c++
//A.h
struct A 
{
	int foo(double d,int x=5);
	void bar();
};
```
il faut être capable de créer le fichier suivant 

```c++
//A.cpp
int A::foo(double d,int x)
{
}

void A::bar()
{
}
```
C'est clairement un travail d'ordinateur

### Analyse ###
Avant de s'attaquer au cœur du programme, il faut dans premier temps récupérer  le nom de classe qu'on souhaite développer.
Pour ce faire, pm va passer par le système d'option *CommonOptionsParser*. Rien de plus simple, il suffit d'utiliser la classe template 
 `cl::opt`. La paramétrisation template permet de récupérer des options de n'importe quelle nature (`std::string`, entier, booléen, ...). Son utilisation est simple : on précise le nom de l'option, sa visibilité par défaut dans l'aide et sa description. Puis on construit comme avant notre objet *CommonOptionsParser *. Après, si l'option a été passée, on peut récupérer sa valeur simplement via l’opérateur de conversion implicite vers son paramètre template.

```c++
 cl::opt<std::string> optClassToExpand("cl-exp", cl:: NotHidden,cl::desc("Class to Expand"));
 CommonOptionsParser op(argc, argv);    
  std::string classToExpand=optClassToExpand;
```

Le passage du nom de la classe à étendre à la classe *ExampleVisitor* va se faire via une variable globale pour des raisons de simplicité.

### Écriture du visiteur ###
Étant donné qu'on souhaite générer le code de fonctions membres, il parait logique de s’intéresser aux déclarations de nouveaux types. La fonctions appelée dans ce cas est *CXXRecordDecl*. Le paramètre qu'elle reçoit est un pointeur de type *CXXRecordDecl*. Il faut alors vérifier que le nom de classe correspond bien à  celui de la classe à développer. On utilise pour cela  la fonction `getNameAsString`. 

On va pouvoir ensuite itérer sur les fonctions membres de la classe avec avec `method_begin` et `method_end`.

Pour implémenter une fonction, elle doit remplir 3 conditions :


    1. Ne pas déjà avoir une implémentation, soit directement dans le header soit dans le fichier source.
    2. Être fournie par le programmeur et non par le compilateur. Ceci concerne les fonctions automatiquement générée par le compilateur mais aussi en C++11 les fonctions marquées comme *delete* (qui ont une existence dans l'AST !) ou celles marquées comme *default*.
    3. Ne pas être pure 

Le type *CXXMethodDecl *,qui est le type sous-jacent aux itérateurs fournis par `method_begin`, dispose respectivement des fonctions `hasBody`, `isUserProvided` et `isPure`

Comme expliqué plus haut, le premier point ne marche que parce qu'on gère la *translation unit* qu'une fois que celle ci a été entièrement parsée.

Dans tous les cas, une fonction doit avoir un type de retour *sauf* si c'est un constructeur, destructeur, ou un opérateur de conversion, au quel cas il n'y a aucun type de retour.  Ces fonctions un peu spéciales sont représentées par les types *CXXConstructorDecl*, *CXXDestructorDecl* et *CXXConversionDecl* qui dérivent de *CXXMethodDecl*.


Il est donc nécessaire de tester si l'itérateur courant n'est pas de ce type. Pour ce faire, on dispose d'un [RTTI ](http://en.wikipedia.org/wiki/RTTI) propre à clang via de la fonction template `isa<T>(Arg)` qui va renvoyer vrai si  Arg est du type T. On dispose aussi d'un analogue au `dynamic_cast` avec `dyn_cast`. 

On peut donc récupérer et ajouter le cas échéant le type de retour avec `getResultType` qu'il faut ensuite convertir en string avec `getAsString`.

Le nom de la fonction s'obtient avec `getNameAsString` et on peut itérer à travers les paramètres via `param_begin` et `param_end`, récupérer type et nom de ces derniers avec `getOriginalType().getAsString()` et `getNameAsString`

Il ne reste plus qu'a rajouter le **const** en fin de définition si la fonction est constante, chose qu'on sait via `isConst`

Au final, le code de la fonction ressemble à ceci :


```c++
virtual bool VisitCXXRecordDecl(CXXRecordDecl *dd) {

  if(dd->getNameAsString()!=classToExpand)
    return true;

  const std::string base=dd->getNameAsString()+"::";      
  for(auto fct = dd->method_begin();fct!=dd->method_end();++fct)
  {
    if(!fct->hasBody() && fct->isUserProvided() && !fct->isPure())
    {
      std::string r2;

      if( !(isa<CXXConstructorDecl>(*fct) || 
            isa<CXXDestructorDecl>(*fct) || 
            isa<CXXConversionDecl>(*fct) )
        )
      { 
        r2+=fct->getResultType().getAsString()+" ";
      }

      r2+=base + fct->getNameAsString()+"(";
      for(auto param = fct->param_begin();param!=fct->param_end();++param)
      {
        r2+=(*param)->getOriginalType().getAsString()+" "+(*param)->getNameAsString();
        r2+=",";
      }

      if(fct->param_size()>0)
        r2.pop_back();

      r2+=std::string(")") +(fct->isConst() ? " const " : "") + "\n{\n}\n";
      off<<r2<<std::endl;
    }
  }

  return true;
}
```


### Utilisation ###
L'utilisation est assez simple. Une fois compilé, le programme s'utilise de la façon suivante : 
```batch
./app test.cpp -cl-exp=C -- -std=c++11
```
avec *test.cpp* qui contient : 

```c++
#include "header.hpp"
```
et *header.hpp* :
```c++
   struct A{};
      class C
      {
      public :
        C();
        ~C();	
        void a();
        void a(int);

        //nope, deleted
        C& operator=(const C&) = delete;

        //nope, default
        C(const C&c)=default;

        operator A();
  
        void Z(std::string s="foobar");
  
        //member
        static const int x;

        //nope, has a body
        const double fct1(double chose = 5.){return 5.;}

        //yes, not pure
        virtual const A fct3(const float& truc=5.) const;

        //nope, pure
        virtual const A fct2(const float& truc) const =0;

        void foo() const;	

        //template, so no
        template <class T> void bar();
	}; //-- C 
```

on arrive au fichier final suivant :

```c++
#include "header.hpp"

C::C()
{
}

C::~C()
{
}

void C::a()
{
}

void C::a(int )
{
}

C::operator A()
{
}

void C::Z(std::string s)
{
}

const struct A C::fct3(const float & truc) const 
{
}

void C::foo() const 
{
}
```
Ce qui est déjà un très bon résultat vu la simplicité du coeur du code, qui tient sur moins de 50 lignes !

## Conclusion ##
J'espère que cet article vous aura convaincu de la puissance de libclang et de ses interfaces pour manipuler du code source et qu'il va vous encourager à écrire vos propre outils.

Il existe de nombreuse améliorations possibles à notre petit programme:

 - Gérer les classes imbriquées et les namespaces et avoir le choix su la manière d’écrire le code.
- Rajouter la possibilité de placer des commentaires pour rappeler les valeurs par défaut, la virtualité des fonctions, ...
 - Ajouter une définition des membres **static**.
- Gérer les fonctions templates.
- Améliorer le résultat des types de retour (std::string devient std::basic_stream<char>) .

Pour information, l'ensemble du projet (contenant une partie des améliorations sus-citées) est disponible sur [Github](https://github.com/Davidbrcz/header-expander)

Merci à lmghs, antoine1023, MicroJoe et les autres que j'oublie pour les relectures et conseils.
