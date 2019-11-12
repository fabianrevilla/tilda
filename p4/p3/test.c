#include "lista.h"

int main()
{
    Nod * root = NULL;
    
    Nod * ny = malloc(sizeof(Nod));
    ny->tel = 1122;
    ny->next = NULL;
    
    Nod * nytt = malloc(sizeof(Nod));
    nytt->tel = 4283798;
    nytt->next = NULL;
    
    Nod * nytti = malloc(sizeof(Nod));
    nytti->tel = 927;
    nytti->next = NULL;
    
    insertnod(&root, ny);
    insertnod(&root, nytt);
    insertnod(&root, nytti);
    
    Nod*f=search(root,4283798);
    printf("tel = %d\n",f->tel);
}
