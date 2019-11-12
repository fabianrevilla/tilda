/* Headerfil med funktioner som används i
   i en dubbellänkad lista i en hashtabell
*/
#ifndef LISTA_H
#define LISTA_H
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct nod {
    char key[512];
    char value[512];
    struct nod * next;
    struct nod * prev;
};
typedef struct nod Nod;

Nod * createnod(char key[512], char value[512]);

void insertnod(Nod ** padr, Nod * tobeadded);

void printnod(Nod * p);

void printlist(Nod * p);

Nod * search(Nod * p, char key[512]);

void removenod(Nod ** padr, Nod * toberemoved);

void clrlist(Nod**padr,Nod * p);

#endif