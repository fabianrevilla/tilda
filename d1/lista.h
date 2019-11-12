#ifndef LISTA_H
#define LISTA_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct nod {
    char name[30];
    int tel;
    struct nod * next;
    struct nod * prev;
};
typedef struct nod Nod;

Nod * createnod(char name[30], int tel)
{
    Nod * ny = malloc(sizeof(Nod));
    strcpy(ny->name,name);
    ny->tel=tel;
    ny->prev=NULL;
    ny->next=NULL;
    return ny;
    
}
void insertnod(Nod ** padr, Nod * tobeadded)
{
    if(*padr==NULL)//Ifall listan är tom
    {
        *padr=tobeadded;//dubbelpekaren pekar på nodpekaren som pekar på noden som ska läggas till
        tobeadded->next=NULL;
        tobeadded->prev=NULL;
    }
    else
    {

    Nod * current=*padr;//startvärde för loopen,aktuella noden är första noden i listan
    while(current->next != NULL)
    {
        current=current->next;//stegar vidare i listan
    }
    current->next=tobeadded;//låter den sista noden i listan peka på den nya noden
    tobeadded->prev=current;//låter den nya noden peka tillbaks på den gamla sista noden
    tobeadded->next=NULL;
}

}


void printnod(Nod * p)
{
    if(p->prev==NULL && p->next==NULL)//ifall noden är ensam i listan
    {
    printf("Name = %s\n",p->name); //namn
    printf("Tel = %d\n",p->tel);   //telefonnummer
    printf("p->prev->tel = %s\n","NULL");
    printf("p->prev->name = %s\n","NULL");
    printf("p->next->tel = %s\n","NULL");
    printf("p->next->name = %s\n","NULL");
    printf("\n");
    }
    else if(p->prev==NULL)//ifall noden är först i listan
    {
    printf("Name = %s\n",p->name); //namn
    printf("Tel = %d\n",p->tel);   //telefonnummer
    printf("p->prev->tel = %s\n","NULL");
    printf("p->prev->name = %s\n","NULL");
    printf("p->next->tel = %d\n",p->next->tel);
    printf("p->next->name = %s\n",p->next->name);
    printf("\n");
    }
    else if(p->next==NULL)//ifall noden är sist i listan
    {
    printf("Name = %s\n",p->name); //namn
    printf("Tel = %d\n",p->tel);   //telefonnummer
    printf("p->prev->tel = %d\n",p->prev->tel);
    printf("p->prev->name = %s\n",p->prev->name);
    printf("p->next->tel = %s\n","NULL");
    printf("p->next->name = %s\n","NULL");
    printf("\n");
    }

    else//övriga fall
    {
    printf("Name = %s\n",p->name); //namn
    printf("Tel = %d\n",p->tel);   //telefonnummer
    printf("p->prev->tel = %d\n",p->prev->tel);
    printf("p->prev->name = %s\n",p->prev->name);
    printf("p->next->tel = %d\n",p->next->tel);
    printf("p->next->name = %s\n",p->next->name);
    printf("\n");
    }
}

void printlist(Nod * p)
{
    if(p==NULL)
{
	printf("Listan är tom\n");
}
else
{
    Nod * current=p;
    while(current != NULL)//så länge den nuvarande nodpekaren inte är NULL
    {
        printnod(current);
        current=current->next;
    }
}
}

Nod * search(Nod * p, int tel)
{
    Nod * current=p;//den nuvarande noden pekar på den försa noden i listan
    while(current->tel != tel)//så länge som det nuvarande värdet inte är det värdet som söks går loopen
    {
        current=current->next;
    }
    return current;
    
}

void removenod(Nod ** padr, Nod * toberemoved)
{
    Nod * current=search(*padr,toberemoved->tel);//letar efter det givna telefonnummret i listan och returnerar noden
    if(current->prev==NULL && current->next==NULL)//enda noden i listan
	{
	*padr=NULL;//p=NULL;	
	}
    else if(current->prev==NULL)//ifall den noden som ska tas bort är först i listan
    { 
        *padr=current->next;
	current->next->prev=NULL;
	current->next=NULL;
    }
    
    else if(current->next==NULL)//ifall den noden som ska tas bort är sist i listan
    {
        current->prev->next=NULL;//näst sista noden i listan blir nya sista noden 
        current->prev=NULL;	
    }
    
    else{
    current->prev->next=current->next;
    current->next->prev=current->prev;
    current->next=NULL;
    current->prev=NULL;	
    }
free(toberemoved);
}

void clrlist(Nod**padr,Nod * p)
{
    Nod * current=p;
    Nod * temp;
    while(current != NULL)//så länge den nuvarande noden inte är NULL
    {
        temp=current;
        current=current->next;
	removenod(padr,temp);	
    }
}

#endif
