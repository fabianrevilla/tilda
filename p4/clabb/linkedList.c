#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct nod
{
    char name[30];
    int tel;
    struct nod * next;
    struct nod * prev;
};

typedef struct nod Nod;

void insertnod(Nod ** padr, Nod * tobeadded)
{

    //if *padr==NULL
        
    Nod * current;
    current=*padr;
                //Låter currentpekaren peka på den första noden i listan
    while(current->next != NULL) //Stegar currentpekaren till sista noden i listan
        current= current->next;
    
    current->next=tobeadded;    //Låten sista noden i listan peka på den nya noden
    tobeadded->next=NULL;       //Den nya noden pekar på NULL
}

//Skapar noder
int main()
{
    Nod * p1=malloc(sizeof(Nod));
    p1->tel=13;
    p1->next=NULL;
    
    Nod * p2=malloc(sizeof(Nod));
    p2->tel=44;
    p2->next=NULL;
    Nod * root=malloc(sizeof(Nod));//Rootpekare
    root=p1; //P1 blir root
    insertnod(&root,p2);

}









