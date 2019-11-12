#include "hashfunc.h"
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

struct artist {
    char artistid[20];
    char artistname[400];
    char songtitle[300];
    double length;
    int year;
};
typedef struct artist Artist;

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
    return hash;
}

void put(Nod ** hashtable, char * key, char * value)
{

    //Beräknar hashindex
    int hash= tilpro_hash(key);
    //Går till det givna indexet i arrayen
    Nod * p = hashtable[hash];
    Nod * searched = search(p,key);
    //ifall nyckeln inte finns i listan på det givna indexet i arrayen
    if(searched==NULL)
    {
        //Skapar en ny nod
        Nod * new_node = createnod(key,value);
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
//  Läser artister från filename och lägger dem i artistarray
//  returnerar antalet inlästa artister
int readartists(char * filename, Artist * artistarray) {
    char linebuffer[425];
    
    FILE * fil = fopen(filename, "r");
    
    int currentartist = 0;
    
    while (fgets (linebuffer, 425, fil) != NULL) {
        
        Artist * artist = artistarray + currentartist;
        
        int i = 0;
        int j = 0;
        // kolumner är TAB-separerade
        while (linebuffer[i] != '\t')
        i++;
        
        strncpy(artist -> artistid, linebuffer, j);
        
        i += 1;
        j = i;
        while (linebuffer[i] != '\t')
        i++;
        
        strncpy(artist -> artistname, linebuffer + j, i - j);
        
        i += 1;
        j = i;
        while (linebuffer[i] != '\t')
        i++;
        
        strncpy(artist -> songtitle, linebuffer + j, i - j);
        
        i += 1;
        // atof - array to float
        artist -> length = atof(linebuffer + i);
        
        while (linebuffer[i] != '\t')
        i++;
        
        i += 1;
        // atoi - array to integer
        artist -> year = atoi(linebuffer + i);
        
        currentartist += 1;
    }
    return currentartist;
}

int main() {
    Artist * artister = malloc(sizeof(Artist) * 1000000);
    //skapar en hashtabell
    Nod ** artist_hashtable = malloc(sizeof(Nod) * HASHVEKSIZE);
    
    // calloc är ett alternativ till malloc som initierar vektorn till noll
    //   Artist * artister = calloc(1000000, sizeof(Artist));
    
    int antalartister = readartists("sang-artist-data.txt", artister);
    
    int i = 0;
    for (i = 0; i < antalartister; i += 1)
    {
        //lägger in låtarna i hashvektorn, med artistnamn som key & låttitel som value
        put(artist_hashtable,artister[i].artistname,artister[i].songtitle);
        //skriver ut artistnamn & låttitel
        //printf("artist: %s\n  songtitle: %s\n",artister[i].artistname, artister[i].songtitle);
    }
    char * song = get(artist_hashtable,"Don Omar");
    printf("song->key = %s\n",song);
    free(artister);
    return 0;
}
