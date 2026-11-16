# Linker Nu este un program magic

Deprimant de des (a avut loc la mine din nou chiar înainte de a am scris acest lucru), punctul de vedere mulți programatori au de a trece de la codul sursă la un executabil legat static într-o limbă compilată este:

1. Editează codul sursă
2. Compilează codul sursă în fișiere obiect
3. Ceva magic se întâmplă.
4. Executabil

Pasul 3 este, desigur, pasul de legătură. De ce aş spune aşa ceva? Fac suport tehnic de zeci de ani şi primesc iar şi iar următoarele întrebări:

- Linkerul spune că def este definit de mai multe ori.
- Linkerul spune că ABC este un simbol nerezolvat.
- De ce este executabilul meu atât de mare?

Urmată de "Ce fac acum?" de obicei cu expresiile "pare" și "cumva" amestecate în, și o aură de nedumerire totală. Este "pare" și "cumva" care indică faptul că procesul de legătură este privit ca un proces magic, probabil înțeles doar de către vrăjitori și vrăjitori. Procesul de compilare nu produce astfel de fraze, ceea ce implică faptul că programatorii înțeleg în general cum funcționează compilatorii sau cel puțin ce fac ei.

Un linker este un program foarte prost, pieton, simplu. Tot ce face este să concatenă împreună secţiunile de cod şi date ale fişierelor de obiecte, să conecteze referinţele la simboluri cu definiţiile lor, să scoată simbolurile nerezolvate din bibliotecă şi să scrie un executabil. Asta e. Fără vrăji! Fără magie! Tediu în scris un linker este, de obicei, totul despre decodarea și generarea formatelor de fișiere de obicei ridicol de prea complicate, dar care nu schimbă natura esențială a unui linker.

Să spunem că linkerul spune că def este definit de mai multe ori. Multe limbi de programare, precum C, C++ și D, au atât declarații, cât și definiții. Declarațiile intră în mod normal în fișiere antet, cum ar fi:

```
extern int iii;
```

care generează o referință externă la simbol`iii`. O definiție, pe de altă parte, pune de fapt deoparte stocarea pentru simbol, apare de obicei în fișierul de implementare, și arată astfel:

```
int iii = 3;
```

Câte definiții pot exista pentru fiecare simbol? Ca în film*Muntean*, nu poate fi doar unul. Deci, ce se întâmplă dacă o definiție a iii apare în mai multe fișiere de implementare?

```
// File a.c
int iii = 3;
```

```
// File b.c
double iii(int x) { return 3.7; }
```

Linker se va plânge despre`iii`se multiplică definit.

Nu numai că poate fi unul singur, trebuie să existe unul. Dacă iii apare doar ca o declarație, dar niciodată o definiție, linkerul se va plânge că iii este un simbol nerezolvat.

Pentru a determina de ce un executabil este dimensiunea este, să ia o privire la fișierul hartă pe care linkers genera opțional. Un fișier hartă nu este nimic mai mult decât o listă a tuturor simbolurilor din executabil, împreună cu adresele lor. Acest lucru vă spune ce module au fost conectate din bibliotecă, și dimensiunile fiecărui modul. Acum puteţi vedea de unde vine balonul. Adesea vor exista module de bibliotecă pe care nu aveți nici o idee de ce au fost legate în. Pentru a-l da seama, elimina temporar modulul suspect din bibliotecă, și reconectați. Eroarea nedefinită a simbolului generat va indica cine se referă la acel modul.

Deși nu este întotdeauna evident imediat de ce primiți un anumit mesaj linker, nu există nimic magic despre linkers. Mecanica este simplă; este detaliile pe care trebuie să le dai seama în fiecare caz.

De[Walter Bright](http://creativecommons.org/licenses/by/3.0/us/)
