#include "lista.h"

Nod * createnod(char key[512], char value[512])
{
    Nod * ny = malloc(sizeof(Nod));
    strcpy(ny->key,key);
    strcpy(ny->value,value);
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
    if(p == NULL)//ifall noden är tom
    {
        printf("p = %s\n","NULL");
    }
    else if(p->prev==NULL && p->next==NULL)//ifall noden är ensam i listan
    {
    printf("key = %s\n",p->key); //key
    printf("value = %s\n",p->value);   //value
    printf("p->prev->value = %s\n","NULL");
    printf("p->prev->key = %s\n","NULL");
    printf("p->next->value = %s\n","NULL");
    printf("p->next->key = %s\n","NULL");
    printf("\n");
    }
    else if(p->prev==NULL)//ifall noden är först i listan
    {
    printf("key = %s\n",p->key);       //nyckel
    printf("value = %s\n",p->value);   //värde
    printf("p->prev->value = %s\n","NULL");
    printf("p->prev->key = %s\n","NULL");
    printf("p->next->value = %s\n",p->next->value);
    printf("p->next->key = %s\n",p->next->key);
    printf("\n");
    }
    else if(p->next==NULL)//ifall noden är sist i listan
    {
    printf("key = %s\n",p->key);       //nyckel
    printf("value = %s\n",p->value);   //värde
    printf("p->prev->value = %s\n",p->prev->value);
    printf("p->prev->key = %s\n",p->prev->key);
    printf("p->next->value = %s\n","NULL");
    printf("p->next->key = %s\n","NULL");
    printf("\n");
    }

    else//övriga fall
    {
    printf("key = %s\n",p->key);       //nyckel
    printf("value = %s\n",p->value);   //värde
    printf("p->prev->value = %s\n",p->prev->value);
    printf("p->prev->key = %s\n",p->prev->key);
    printf("p->next->value = %s\n",p->next->value);
    printf("p->next->key = %s\n",p->next->key);
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

Nod * search(Nod * p, char key[512])
{
    Nod * current=p;//den nuvarande noden pekar på den försa noden i listan
    if(p==NULL)//Ifall listan är tom
    {
        //printf("Listan är tom\n");
        return NULL;
    }
    int cmp = strcmp(key,current->key);
    while(cmp != 0)//så länge som det nuvarande värdet inte är det värdet som söks går loopen
    {
        if(current->next == NULL)//ifall sista noden är nådd utan matchning
        {
            return NULL;//returnera NULL
        }
        current=current->next;
        cmp = strcmp(key,current->key);
    }
    return current;
    
}

void removenod(Nod ** padr, Nod * toberemoved)
{
    Nod * current=search(*padr,toberemoved->value);//letar efter det givna värdet i listan och returnerar noden
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




