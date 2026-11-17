# Testați exact și concret

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_81_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_81_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 4:18)](../audio/thing_81_ro.mp3)

Este important să se testeze pentru comportamentul dorit, esențial al unei unități de cod, mai degrabă decât să se testeze pentru comportamentul accidental al implementării sale specifice. Dar acest lucru nu trebuie luat sau confundat ca o scuză pentru teste vagi. Testele trebuie să fie atât de exacte*şi*Exact.

Ceva de un încercat, testat, și testarea rutine clasice de sortare oferă un exemplu ilustrativ. Punerea în aplicare a unui algoritm de sortare nu este neapărat o sarcină zilnică pentru un programator, dar sortarea este o idee atât de familiară încât majoritatea oamenilor cred că știu ce să se aștepte de la el. Cu toate acestea, această familiaritate ocazională poate face mai greu de văzut dincolo de anumite ipoteze.

Când programatorii sunt întrebați "Pentru ce să testați?" cel mai frecvent răspuns este "Rezultatul sortării este o secvență sortate de elemente." Deşi acest lucru este adevărat, nu este întregul adevăr. Atunci când se solicită o condiție mai precisă, mulți programatori adaugă că secvența rezultată ar trebui să fie aceeași cu cea originală. Deși corect, acest lucru nu este încă suficient. De exemplu, având în vedere următoarea secvență:

```
3 1 4 1 5 9
```

Secvența de mai jos satisface o postcondiție de sortare în ordine nedescendentă și având aceeași lungime ca și secvența originală:

```
3 3 3 3 3 3
```

Deşi satisface specificaţiile, cu siguranţă nu este ceea ce a însemnat! Acest exemplu se bazează pe o eroare luată din codul real de producție (din fericire prins înainte de a fi lansat), în cazul în care o simplă alunecare a unei lovituri de tastatură sau o pierdere de moment a motivului a condus la un mecanism elaborat pentru popularea întregului rezultat cu primul element al matricei date.

Întreaga postcondiție este că rezultatul este sortate și că deține o permutare a valorilor originale. Acest lucru limitează în mod corespunzător comportamentul necesar. Că lungimea rezultatului este aceeași ca lungimea de intrare iese în spălare și nu are nevoie de odihnă.

Chiar şi afirmarea condiţiei post- descrise nu este suficientă pentru a vă oferi un test bun. Un test bun ar trebui să fie lizibil. Ar trebui să fie ușor de înțeles și suficient de simplu încât să puteți vedea cu ușurință că este corect (sau nu). Cu excepția cazului în care aveți deja cod situat în jurul valorii de pentru verificarea faptului că o secvență este sortate și că o secvență conține o permutare a valorilor în alta, este destul de probabil ca codul de testare va fi mai complex decât codul sub test. După cum a observat Tony Hoare:

> Există două moduri de a construi un design software: O modalitate este de a face atât de simplu că există*Evident.*nu există deficienţe, iar cealaltă este să complicăm lucrurile atât de mult încât să nu existe deficienţe evidente.

Folosirea unor exemple concrete elimină această complexitate accidentală și oportunitatea unui accident. De exemplu, având în vedere următoarea secvență:

```
3 1 4 1 5 9
```

Rezultatul sortării este următorul:

```
1 1 3 4 5 9
```

Nici un alt răspuns nu e bun. Nu accepta înlocuitori.

Exemple concrete ajută la ilustrarea comportamentului general într-un mod accesibil și lipsit de ambiguitate. Rezultatul adăugării unui element la o colecție goală nu este pur și simplu faptul că nu este gol: Este că colecția are acum un singur element. Și că elementul unic deținut este elementul adăugat. Două sau mai multe elemente s-ar califica ca nu gol. Şi ar fi greşit. Un singur element de o valoare diferită ar fi, de asemenea, greșit. Rezultatul adăugării unui rând la o masă nu este doar faptul că masa este cu un rând mai mare. Aceasta presupune, de asemenea, că cheia rândului poate fi utilizată pentru a recupera rândul adăugat. Şi aşa mai departe.

Pentru a specifica comportamentul, testele nu ar trebui să fie pur şi simplu exacte: Acestea trebuie să fie, de asemenea, precise.

De[Kevlin Henney](http://programmer.97things.oreilly.com/wiki/index.php/Kevlin_Henney)