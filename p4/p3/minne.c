#include <stdlib.h>
#include <stdio.h>
#include <string.h>

long foo(void * a) {
    long offset = 4196518;
    long adr = (long) a;
    return adr - offset;
}

int main(int argc, char * argv[]) {
    int a = 1;
    char tkn = 't';
    int v[] = {1, 3, 5};

    int * vdyn = malloc(sizeof(int) * 2);
    vdyn[0] = 7;
    vdyn[1] = 4;

    char * staticstr = "Hej";

    char * sv = malloc(sizeof(char) * 11);
    strcpy(sv, staticstr);    // kopierar sträng se frl-anteckningar

    printf("variabel        adress            värde\n");
    printf("---------------------------------------\n");
    printf("a               %ld      %d\n"      ,(long) &a        , a);
    printf("tkn             %ld      %c\n"      ,(long) &tkn      , tkn);
    printf("v[0]            %ld      %d \n"     ,(long) v         , *v);
    printf("v[1]            %ld      %d \n"     ,(long) (v + 1)     , *(v + 1));
    printf("v[2]            %ld      %d \n"     ,(long) (v + 2)     , *(v + 2));
    printf("vdyn[0]         %ld      %d \n"     ,(long) vdyn     , *vdyn);
    printf("vdyn[1]         %ld      %d \n"     ,(long) (vdyn+1)     , *(vdyn+1));
    printf("foo             %ld      \n"        ,(long) &foo);
    printf("staticstr       %ld      %s\n"      ,(long) &staticstr        , staticstr);
    printf("sv              %ld      %s\n"      ,(long) &sv        , sv);
    printf("\n");
}


