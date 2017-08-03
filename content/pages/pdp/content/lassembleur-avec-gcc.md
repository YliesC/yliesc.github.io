Title: L'assembleur avec GCC
Order: 9
Date: 2014-09-27
Slug: lassembleur-avec-gcc
Author: informaticienzero
Display: true

Connaissez-vous les fonctions *inline* ? On les utilise pour optimiser un code, puisque l'appel de la fonction est remplacé par le corps de la fonction elle-même. Pour ceux qui connaissent le C, c'est dans le même principe que les macros. En général, on écrit des fonctions inlines dans le même langage que le reste du code. En général ... car il est possible d'écrire des fonctions en assembleur depuis un code C. A quoi ça peut servir ? Allier la puissance de l'assembleur avec le côté pratique du C.

[TOC]

# La syntaxe AT&T
Avant de commencer, il est important de faire un point sur la syntaxe AT&T. En effet, celle-ci est moins courante que la syntaxe Intel et diffère pas mal. Voici une liste des différences majeures entre les deux syntaxes. Sachez néanmoins que même si vous n'êtes pas familier ou à l'aise avec cette syntaxe, cela ne sera pas gênant pour comprendre la suite.

* **Ordre source / destination** : le premier argument d'une instruction sera toujours l'opérande source et le deuxième l'opérande destination. Ceux qui connaissent la syntaxe Intel savent que l'ordre est inversé : destination puis source.

* **Le nom des registres** : les registres sont précédés par ```%```.
```console
cmp eax, ecx    ; syntaxe Intel
cmp %eax, %ecx    ; syntaxe AT&T
```

* **Opérande immédiate** (c'est à dire une constante ou le résultat d'une expression constante) : une opérande immédiate est toujours précédée par ```$```, ainsi que les variables statiques C. De plus, les valeurs hexadécimales qui commençaient par un ```h``` avec la syntaxe Intel commencent désormais par ```0x```.
```console
mov eax, 1    ; syntaxe Intel
movl $1, %eax     ; syntaxe AT&T

mov ebx, 0ffh    ; syntaxe Intel
movl $0xff, %ebx    ; syntaxe AT&T
```

* **Taille des opérandes** : la taille d'une opérande est connue en regardant la dernière lettre d'un opérande : les suffixes sont ```b``` (byte - 8 bits), ```w``` (word - 16 bits) et ```l``` (double word - 32 bits). Avec la syntaxe Intel, on aurait ajouté ```byte ptr```, ```word ptr``` et ```dword ptr``` devant les opérandes.
```console
mov al, byte ptr foo    ; syntaxe Intel
movb foo, %al    ; syntaxe AT&T
```

* **Opérande mémoire** : la syntaxe Intel utilise les crochets [ et ], la syntaxe AT&T utilise les parenthèses ( et ). Par conséquence, l'accès indirect à la mémoire passe de ```section:[base + index * scale + disp]``` à ```section:disp(base, index, scale)```. Les constantes utilisées pour *disp* et *scale* ne doivent pas être préfixées de ```$```.
```console
sub     eax, [ebx + ecx * 4h - 20h]    ; syntaxe Intel
subl    -0x20(%ebx, %ecx, 0x4), %eax    ; syntaxe AT&T
```

# Assembleur basique
Un bloc de code assembleur se déclare grâce au mot-clef ```__asm__``` et se place entre parenthèse, avec un point-virgule après la parenthèse fermante. Il existe un autre mot-clef, ```asm```, mais celui-ci peut créer des conflits avec certaines options de compilation comme **-ansi**.

> -ansi and the various -std options disable certain keywords. This causes trouble when you want to use GNU C extensions, or a general-purpose header
> file that should be usable by all programs, including ISO C programs. The keywords asm, typeof and inline are not available in programs compiled with 
> -ansi or -std (although inline can be used in a program compiled with -std=c99 or -std=c11).
> *-- Site de GCC*

Chaque instruction se déclare entre guillemets et doit être finie par ```\n\t```. Cela permet de formater correctement les instructions pour les envoyer à **Gas**, l'assembleur de GCC. Voici un exemple basique.

```c
__asm__
(
    "movl %eax, %ebx\n\t"
    "movl $56, %esi\n\t"
    "movb %ah, (%ebx)"
);
```

Cependant, en l'état actuel des choses, ça reste assez limité. En effet, non seulement on ne peut pas interagir avec des variables, mais si en plus on modifie des registres qui étaient utilisés par le programme avant l'appel des routines assembleur, comment le signaler au compilateur ? Heureusement, l'assembleur inline est bien plus puissant que ça.

# L'assembleur étendu
L'assembleur étendu va nous permettre de spécifier des opérandes d'entrées, de sorties et les registres utilisés. On va aussi permettre à GCC de bien comprendre le code pour tenter si possible de l'optimiser. Mais commençons par le commencement, la syntaxe.

```console
__asm__
(
    /* instructions assembleur */
        : opérandes de sortie     /* optionnel */
        : opérandes d'entrée     /* optionnel */
        : liste des registres "pollués"  ou clobber list     /* optionnel */
);
```

Chaque opérande est constituée d'une **contrainte d'opérande** entre guillemets suivi d'une expression en C (variable, calcul, etc) entre parenthèses. Les opérandes sont séparées entre elles par des virgules. Par contre, le **maximum total** d'opérandes est limité à 10, ou plus si la machine le permet (voir les spécifications), mais vous n'aurez que très rarement le cas de dépasser ce nombre. 

Les contraintes d'opérandes sont les suivantes :

* ```"r"``` : dans n'importe quel registre (eax, ebx, etc) ;
* ```"a"``` : spécifiques aux registres eax, ax et al ;
* ```"b"``` : spécifiques aux registres ebx, bx et bl ;
* ```"c"``` : spécifiques aux registres ecx, cx et cl ;
* ```"d"``` : spécifiques aux registres edx, dx et dl ;
* ```"S"``` : pour les registres esi et si ;
* ```"D"``` : pour les registres edi et di ;
* ```"m"``` : lorsque l'opérateur est dans la mémoire ; on peut donc effectuer des opérations directement sur l'adresse mémoire sans avoir à passer par un registre. Cependant, il n'est recommandé d'utiliser cette contrainte que si elle est vraiment nécessaire ou si elle accélère suffisamment le processus (une donnée trop grosse pour rentrer d'un coup dans un registre). Par exemple dans un OS, l'IDT définie par le noyau peut être chargée ainsi :
```c
__asm__ ("lidt %0\n\t" : /* pas de sortie */ : "m"(idt));
```
* ```g``` : pour utiliser n'importe quel registre général, adresse ou entier disponible.

Il en existe également d'autres spécifiques à l'architecture x86 :

* ```"f"``` : pour un registre flottant ;
* ```"t"``` : pour le premier registre flottant ;
* ```"u"``` : pour le second registre flottant ;
* ```"q"``` : registre a, b, c ou d

En plus de ces contraintes, il existe également des **modificateurs de contrainte** :

* ```"="``` : signifie que l'opérande est en écriture seule pour cette instruction, la valeur précédente est éliminée et remplacée par des données de sortie. Ce modificateur est utilisé pour les opérandes de sortie.
* ```"&"``` : signifie que l'opérande sera modifiée avant la fin de la lecture de toutes les opérandes d'entrées par l'instruction en cours. Si l'opérande n'est pas modifiée avant la fin de la lecture, alors le modificateur est ignoré.
* ```"=&"``` : c'est la combinaison des deux précédents.

Le troisième paramètre est quant à lui la liste des registres utilisés dans le code assembleur sans compter les opérandes d'entrée et de sortie. Elle permet d'indiquer à GCC que nous gérons nous-mêmes ces registres. Ainsi, GCC ne vérifiera pas si la valeur chargée dans ces registres est valide, et il ne tentera pas non plus d'y stocker des valeurs tant que nous n'avons pas fini. Par contre, GCC connait les registres utilisés par les opérandes d'entrée et de sortie, il ne faut donc pas les préciser. 

Il est temps de tout récapituler par un exemple. Prenons ce code qui additionne deux variables.

```c
int main(void)
{
    int foo = 10, bar = 15;
    
    __asm__
    (
        "addl %%ebx, %%eax"
            : "=a"(foo)
            : "a"(foo), "b"(bar)
    );
        
    printf("foo += bar = %d\n", foo);
    return 0;
}
```

On demande dans cette exemple de stocker la variable *foo* dans le registre *eax* (```"a"(foo)```), et la variable *bar* dans le registre *ebx* (```"b"(bar)```), puis on demande d'additionner les deux registres et de stocker le résultat dans la variable *foo* (```"=a"(foo)```). On remarque ici que la liste des registres pollués n'est pas précisée puisque les deux registres utilisés sont déjà connus d'avance par GCC, car ils sont utilisés par les opérandes de sortie / d'entrée.

#### Plus d'opérandes, de contraintes et de clobber list ####

Il faut aussi préciser que pour un nombre $x$ d'opérateurs (à la fois d'entrée et de sortie), alors le premier opérande de sortie est numéroté 0, et le dernier opérande d'entrée est numéroté $x - 1$. Cela nous permet de manipuler directement nos variables dans le code assembleur, au contraire du code précédent où nous sommes passés par des registres bien spécifiques. Illustrons ce nouveau concept par un code.

```c
int main(void)
{
    int a = 10, b = 0;
    
    __asm__
    (
        "movl %1, %%eax\n\t"
        "movl %%eax, %0\n\t"
            :"=r"(b)
            :"r"(a)
            :"%eax"
    );
    
    printf("b = %d\n", b);
    return 0;
}
```

Il y a deux opérandes, donc ```"=r"(b)``` est l'opérande 0, représentée par ```%0```, et ```"r"(a)``` l'opérande 1, représentée par ```%1```. Le code charge donc la variable *a* et stocker son contenu dans *eax*, qui est lui même copié dans la variable *b*. Ainsi à la fin de l'instruction, la variable *a* et la variable *b* valent toutes deux 10. Cela nous permet de manipuler plus précisément les opérandes d'entrées et de sorties. On l'utilise dans les cas suivants.

* Dans le cas où on lit une variable pour écrire le résultat dans cette même variable. 
* Dans les cas où il n'est pas nécessaires de séparer les instances d'entrées et de sorties. 

Cette possibilité s'étend également aux contraintes des opérandes. En effet, pour une opérande d'entrée, une contrainte composée d'un chiffre $x$ qui signifie "cette entrée a les mêmes contraintes que la $x^{ème}$ opérande de sortie". Cette technique est utilisée si on veut que l'opérande d'entrée et l'opérande de sortie soient stockées dans le même registre. Prenons un exemple.

```c
int main(void)
{
    int a = 10, b = 25;

    __asm__
    (
        "addl %2, %%eax\n\t"
            : "=a"(a)
            : "0"(a), "b"(b)
    );

    printf("a += b = %d", a);
    return 0;
}
```

Dans ce code, on demande à ce que l'opérande d'entrée 0 ait les mêmes contraintes que la $0^{ème}$ opérande de sortie (soit ```"=a"```). Ainsi, les deux variables seront stockées dans le registre *eax*. Sans cette technique, il aurait fallu préciser que l'opérande d'entrée 0 devait être stockée dans le registre *eax*. 

Je termine cette sous-partie en ajoutant des précisions sur la liste des registres pollués.

* Si l'instruction modifie le registre de condition de code, alors il faut rajouter ```"cc"``` à cette liste.
* Si l'instruction modifie la mémoire de manière imprévisible, il faut ajouter ```"memory"``` à la liste. Si la mémoire modifiée n'est pas listée dans les opérandes d'entrée ou de sortie, il faut alors rajouter le mot-clef ```volatile```.

#### volatile ####

Ce mot-clef est bien connu des programmeurs systèmes. Il permet de définir une variable de façon à ce que celle-ci ne puisse pas être placée dans un registre du processeur, mais en mémoire. Dans le cas de l'assembleur inline, il sert à empêcher les optimisations que pourrait faire GCC. Pour le forcer à respecter ce qu'on a écrit à la lettre on utilise ce mot-clef, ou plutôt sa variante ```__volatile__```, que l'on place juste après ```__asm__```. Il est à noter que s'il n'est pas nécessaire (dans le cas de calculs, ou si le code ne produit aucun effet de bord), il ne sert à rien de le mettre : il est mieux de laisser GCC optimiser le code.

#### goto ####

Sachez également que depuis la version 4.5 de GCC il est possible d'utiliser ```goto``` sur des blocs d'assembleur. La syntaxe pour les utiliser est la suivante :

```c
__asm__ goto
(
    "jmp %l[labelname]"
        : 
        : 
        : "memory"
        : labelname  /* n'importe quel label utilisé */
);
```

Voici un exemple tiré du code source de GNU/Linux (attention les yeux, ça risque de piquer un peu).

```c
// Works for both 32 and 64 bit
#include <stdint.h>
#define cmpxchg( ptr, _old, _new, fail_label ) { \
  volatile uint32_t *__ptr = (volatile uint32_t *)(ptr);   \
  asm goto( "lock; cmpxchg %1,%0 \t\n"           \
    "jnz %l[" #fail_label "] \t\n"               \
    : /* empty */                                \
    : "m" (*__ptr), "r" (_new), "a" (_old)       \
    : "memory", "cc"                             \
    : fail_label );                              \
}
```

#### Variables globales et fonctions ####

Depuis tout à l'heure, nous n'avons vu que le chargement de variables locales à une fonction. Il est pourtant possible de charger des variables globales, et c'est même encore plus facile ! En effet, il suffit d'écrire directement dans le code ceci : ```_ID```, sans même passer par les opérandes d'entrées et de sortie. Exemple.

```c
int b = 25;

int main(void)
{
    int a = 10;

    __asm__
    (
        "addl _b, %%eax\n\t"
            : "=a"(a)
            : "0"(a)
    );

    printf("a += b = %d", a);
    return 0;
}
```

Il est de même pour les appels de fonctions. Voici un exemple appelant la fonction *puts*.

```c
const char * str = "Hello world!";

int main(void)
{
    __asm__
    (
        "movl _str, %eax\n\t"
        "pushl %eax\n\t"
        "call _puts\n\t"
        "add $8, %esp\n\t"
        "leave\n\t"
        "ret\n\t"
    );

    return 0;
}
```

# Exemples
Pour illustrer cette grosse partie théorique, je vais prendre des exemples que j'ai pu voir sur Internet, accompagnés de quelques explications.

#### Mise à zéro de bit ####

```c
__asm__
(   "btsl %1,%0"
       : "=m" (ADDR)
       : "Ir" (pos)
       : "cc"
);
```

Ce code permet de mettre à 1 le bit numéro *pos* de l'adresse ADDR. Si on avait voulu mettre le bit à 0, on aurait utilisé l'instruction *btr*l.

#### strcpy ####

Ce code tiré de la Glibc de Linux est celui de la fonction *strcpy*.

```c
static inline char * strcpy(char * dest, const char * src)
{
    int d0, d1, d2;

    __asm__ __volatile__
    (  
        "1:\tlodsb\n\t"
        "stosb\n\t"
        "testb %%al,%%al\n\t"
        "jne 1b"
            : "=&S" (d0), "=&D" (d1), "=&a" (d2)
            : "0" (src), "1" (dest) 
            : "memory"
    );
    return dest;
}
```

L'adresse de la chaîne source est située dans *esi*, celle de la chaîne de destination dans *edi*. Dès que l'on atteint 0, la copie est terminée. Les contraintes ```"=&S"```, ```"=&D"```, ```"=&a"``` indiquent que les registres *esi*, *edi* and *eax* seront utilisés, donc GCC ne stockera rien dedans. L'instruction *lodsb* charge dans le registre *al* l'octet adressé par *di:si*, si le flag DF vaut 0 après ça, *si* est incrémenté, sinon décrémenté. L'instruction *stosb* stocke le contenu de *a*l dans l'octet pointé par *es:di*, si le flag DF vaut 0 après ça, *di* est incrémenté, sinon décrémenté.

#### Des instructions inaccessibles ? ####

Il est fréquent lors de la création d'un système d'exploitation d'écrire sur divers ports (pour s'adresser au PIC par exemple), ou bien pour activer / désactiver les interruptions. Or il n'existe pas en C de fonction pour se faire. On a donc recours à l'assembleur inline. Dans cette exemple, on utilise des ```#define```, ce qui s'avère pratique quand on appelle plusieurs fois la même instruction.

```c
/* désactive les interruptions */
#define cli __asm__("cli"::)

/* réactive les interruptions */
#define sti __asm__("sti"::)

/* écrit un octet sur un port */
#define outb(port, value) \
	__asm__ __volatile__ ("outb %%al, %%dx" :: "d" (port), "a" (value));

/* lit un octet sur un port */
#define inb(port)(    \
	unsigned char _v;       \
	__asm__ __volatile__ ("inb %%dx, %%al" : "=a" (_v) : "d" (port)); \
        _v;     \
})
```

# Utiliser la syntaxe Intel
Pour ceux qui maitriserait mal la syntaxe AT&T ou qui par gouts personnels préfèrent la syntaxe Intel, il est possible d'utiliser cette dernière. Pour cela, il suffit de rajouter deux lignes dans son code assembleur : ```".intel_syntax noprefix\n\t"``` au début et ```".att_syntax"``` à la fin. Toute instruction écrite entre ces deux lignes sera considérée comme utilisant la syntaxe Intel. Exemple.

```c
int a;

__asm__
(
    ".intel_syntax noprefix\n\t"
    "mov ax, 2\n\t"
    "shl ax, 2\n\t"
    ".att_syntax"
       :"=r"(a)
);
```

Concernant le passage en argument, la méthode est la même que pour la syntaxe AT&T. Exemple avec une variable globale puis un paramètre de fonction (la méthode est identique pour les variables locales).

```c
const char * const str = "Hello world!";

void asm_print(void)
{
    __asm__
    (
        ".intel_syntax noprefix\n\t"
        "mov eax, _str\n\t"
        "push eax\n\t"
        "call _puts\n\t"
        "add esp, 8\n\t"
        "leave\n\t"
        "ret\n\t"
        ".att_syntax"
    );
}

void asm_print_with_args(const char * s)
{
    __asm__
    (
        ".intel_syntax noprefix\n\t"
        "push eax\n\t"
        "mov eax, %0\n\t"
        "call _puts\n\t"
        "add esp, 8\n\t"
        "leave\n\t"
        "ret\n\t"
        ".att_syntax"
            :
            : "r"(s)
    );
}
```

Cet article n'a pas pour but d'être exhaustif, ce qui est impossible, mais plutôt de présenter une introduction à l'assembleur inline avec GCC. Pour continuer votre route, voici le [document original](http://www.ibiblio.org/gferg/ldp/GCC-Inline-Assembly-HOWTO.html) duquel est tiré en grande partie cet article, ainsi qu'une [liste de liens](http://www.ibiblio.org/gferg/ldp/GCC-Inline-Assembly-HOWTO.html#s9).
