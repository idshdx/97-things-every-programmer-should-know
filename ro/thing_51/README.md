# Învaţă să spui "Bună, lume"

Paul Lee, nume de utilizator Leep, mai cunoscut sub numele de Hoppy, avea reputaţia de expert local în probleme de programare. Aveam nevoie de ajutor. M-am dus la biroul lui Hoppy şi l-am întrebat, poate să se uite la un cod pentru mine?

Sigur, a spus Hoppy, trage un scaun. Am avut grijă să nu răstoarne cutii goale cola stivuite într-o piramidă în spatele lui.

Ce cod?

Într-un dosar, am spus.

Deci, să aruncăm o privire la această funcție. Hoppy a dat deoparte o copie a K&R şi şi-a alunecat tastatura în faţa mea.

Unde e IDE? Se pare că Hoppy nu a avut IDE rulează, doar un editor pe care nu am putut opera. A luat înapoi tastatura. Câteva lovituri de tastatură mai târziu și am avut fișierul deschis  M-a chemat la blocul condiţional despre care voiam să întreb.

Ce ar face această clauză de fapt dacă`x`E negativ? Am întrebat. Cu siguranţă e greşit.

Am încercat toată dimineaţa să găsesc o cale de a forţa.`x`să fie negativ, dar funcția mare în fișierul mare a fost parte a unui proiect mare, și ciclul de recompilare*atunci*Rularea experimentele mele a fost mă poartă în jos. N-ar putea un expert ca Hoppy să-mi spună răspunsul?

Hoppy a recunoscut că nu era sigur. Spre surprinderea mea, el nu a ajuns pentru K&R. În schimb, el a copiat blocul de cod într-un nou editor tampon, re-indentat, înfășurat într-o funcție. Un scurt timp mai târziu, el ar codat o funcție principală care buclat pentru totdeauna, motivând utilizatorul pentru valorile de intrare, trecerea lor la funcția, imprimarea rezultatului. El a salvat tampon ca un nou fișier, tryit.c. Toate astea le-aş fi putut face pentru mine, deşi poate nu atât de repede. Dar următorul său pas a fost minunat de simplu și, la momentul respectiv, destul de străin de modul meu de lucru:

```
$ cc tryit.c && ./a.out
```

Uite! Programul său real, conceput cu câteva minute mai devreme, era acum în funcţiune. Am încercat câteva valori şi am confirmat suspiciunile mele (aşa că am avut dreptate în legătură cu ceva!) şi apoi a verificat secţiunea relevantă a K&R. I-am mulţumit lui Hoppy şi am plecat, având din nou grijă să nu-i deranjez piramida cola.

Înapoi la biroul meu, am închis IDE mea. M-am obişnuit atât de mult să lucrez la un proiect mare într-un produs mare încât am început să cred că asta ar trebui să fac. Un computer cu scop general poate face şi el mici sarcini. Am deschis un editor de text şi am început să scriu.

```
#include <stdio.h>

int main()
{
    printf("Hello, World\n");
    return 0;
}
```

De[Thomas Guest](http://programmer.97things.oreilly.com/wiki/index.php/Thomas_Guest)