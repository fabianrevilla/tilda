#include "lista.h"

int main()
{

//Skapar en nodpekare p ska peka på första noden i listan
Nod * p = NULL;

//Skapar noder
Nod * ny1=createnod("Danne",15314234);
Nod * ny2=createnod("Ogge",123764);
Nod * ny3=createnod("Roffe",9584385);
Nod * ny4=createnod("Davve",5488734);

//Lägger till noder i listan
insertnod(&p,ny1);
insertnod(&p,ny2);
insertnod(&p,ny3);
insertnod(&p,ny4);

//Tar bort noder ur listan
removenod(&p,ny1);
removenod(&p,ny2);
removenod(&p,ny3);
removenod(&p,ny4);

//Skriver ut listan
printlist(p);

//Rensar listan & frigör allokerat minne
clrlist(&p,p);

}


