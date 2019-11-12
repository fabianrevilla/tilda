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
extern const int HASHVEKSIZE;

//  Läser artister från filename och lägger dem i artistarray
//  Returnerar antalet inlästa artister
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
    Artist * artister = malloc(sizeof(Artist) * HASHVEKSIZE);
    //skapar en hashtabell
    Nod ** artist_hashtable = malloc(sizeof(Nod) * HASHVEKSIZE);
    
    init(artist_hashtable);
    // calloc är ett alternativ till malloc som initierar vektorn till noll
    //   Artist * artister = calloc(1000000, sizeof(Artist));
    
    int antalartister = readartists("sang-artist-data.txt", artister);
    
    int i = 0;
    for (i = 0; i < antalartister; i += 1)
    {
        //lägger in låtarna i hashvektorn, med artistnamn som key & låttitel som value
        put(artist_hashtable,artister[i].artistname,artister[i].songtitle);
        //skriver ut artistnamn & låttitel
        printf("artist: %s\n  songtitle: %s\n",artister[i].artistname, artister[i].songtitle);
    }
    char * song = get(artist_hashtable,"Don Omar");
    printf("song->key = %s\n",song);
    free(artister);
    return 0;
}
