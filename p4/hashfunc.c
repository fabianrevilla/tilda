#include "hashfunc.h"
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

//Konstanter
const int HASHVEKSIZE = 1048576;
//Funktioner
uint32_t tilpro_hash(const char * s)
{
    uint32_t hash = 0;
    size_t i = 0;
    while (s[i] != '\0')
    {
        hash += s[i++];
        hash += hash << 10;
        hash ^= hash >> 6;
    }
    hash += hash << 3;
    hash ^= hash >> 11;
    hash += hash << 13;
    
    hash = hash & ( HASHVEKSIZE - 1 );
    return 17;
}

void put(Nod ** hashtable, char * key, char * value)
{
    //Skapar en ny nod
    Nod * new_node = createnod(key,value);
    //Beräknar hashindex
    int hash= tilpro_hash(key);
    //Går till det givna indexet i arrayen
    Nod * p = hashtable[hash];
    Nod * searched = search(p,key);
    //ifall nyckeln inte finns i listan på det givna indexet i arrayen
    if(searched==NULL)
    {
    //lägg till noden i listan
        insertnod(&p,new_node);
        hashtable[hash] = p;//lägger till listan i arrayen
    }
    //ifall nyckeln redan finns
    else
    {
    //skriver över värdet
        strcpy(searched->value,value);
    }
}

char * get(Nod ** hashtable, char * key)
{
    //Beräknar hashindex
    int hash= tilpro_hash(key);
    //Går till det givna indexet i arrayen
    Nod * p = hashtable[hash];
    Nod * searched = search(p,key);
    //ifall key inte finns i listan
    if(searched==NULL)
        {
            return NULL;
        }
    //ifall nyckeln redan finns
    else
        {
            //Returnerar värdet associerat med key
            return searched->value;
        }
}

void init(Nod ** hashtable)
{
    //Sätter alla index till NULL
    memset(hashtable,'\0',HASHVEKSIZE);
}


//MAIN
int main()
{
    //Skapar en hashtabell
    Nod ** myhashvek = malloc(sizeof(Nod *) * HASHVEKSIZE);
    
    //Initierar hashvektorn
    init(myhashvek);
    
    //Testar att lägga till noder i i hashtabellen
    put(myhashvek,"Adam","123321");
    char * s = get(myhashvek,"Adam");
    printf("Adam -> value = %s, expecting 123321\n", s);
    
    //Testar att skriva över Adam:s värde
    put(myhashvek,"Adam","123321");
    put(myhashvek,"Adam","7");
    char * s2 = get(myhashvek,"Adam");
    printf("Adam -> value = %s, expecting 7\n", s2);
    
    //Testar att krockhanteringen funkar
    put(myhashvek,"Adam","123321");
    put(myhashvek,"Eva","7");
    char * s3 = get(myhashvek,"Adam");
    char * s4 = get(myhashvek,"Eva");
    printf("Adam -> value = %s, expecting 123321\n", s3);
    printf("Eva -> value = %s, expecting 7\n", s4);
    //Kollar att listan har lagrats korrekt i arrayen
    printlist(myhashvek[17]);
}




