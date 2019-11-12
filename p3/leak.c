#include <stdlib.h>

struct nod {
    char name[30];
    int tel;
    struct nod * next;
    struct nod * prev;
};
typedef struct nod Nod;

int main() {
    Nod * p =  malloc(sizeof(Nod));
    p -> next =  malloc(sizeof(Nod));
    p -> next -> prev = p;
    free(p);
}
