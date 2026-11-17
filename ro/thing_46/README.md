# Cunoaşteţi - vă limitele

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_46_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_46_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 2:09)](../audio/thing_46_ro.mp3)

> *"Omul trebuie să-şi cunoască limitele." Dirty Harry*

Resursele tale sunt limitate. Ai doar atât de mult timp și bani pentru a face munca ta, inclusiv timpul și banii necesari pentru a menține cunoștințele, abilitățile și instrumentele la zi. Poţi munci din greu, atât de repede, atât de deştept şi atât de mult. Uneltele tale sunt atât de puternice. Masinile tinta sunt atat de puternice. Deci trebuie să respecţi limitele resurselor tale.

Cum să respecte aceste limite? Cunoaşte-te pe tine, cunoaşte-ţi oamenii, cunoaşte-ţi bugetele, şi cunoaşte-ţi lucrurile. În special, în calitate de inginer de software, cunoașteți complexitatea spațiului și a timpului structurilor de date și algoritmilor, precum și caracteristicile arhitecturii și performanței sistemelor dumneavoastră. Treaba ta este de a crea o căsătorie optimă de software și sisteme.

Complexitatea spaţiului şi timpului este dată ca funcţie*O [f(n) ]*care pentru n egal cu dimensiunea de intrare este spațiul asimptotic sau timpul necesar ca n crește la infinit. Clase importante de complexitate pentru*f(n)*include*ln (n)*,*n*,*n ln (n)*,*n<sup>e</sup>*, și*e<sup>n</sup>*. După cum graficul acestor funcții arată în mod clar, ca*n*devine mai mare*O [ln(n) ]*Este mult mai mic decât*O (n)*şi*O [în ln (n) ]*, care sunt atât de mult mai mici decât*O (n)<sup>e</sup>)*şi*O (e)<sup>n</sup>)*. După cum spune Sean Parent, pentru a realiza n toate clasele de complexitate se ridică la aproape-constant, aproape-linear, sau aproape-infinit.

![](http://programmer.97things.oreilly.com/wiki/images/c/c0/Clearly.jpeg)

|              | access time      |   capacity |
- - - - - -: ------------:
| register     |  < 1 ns          |        64b |
| cache line   |                  |        64B |
| L1 cache     |  1 ns            | 64 KB      |
| L2 cache     |  4 ns            | 8 MB       |
| RAM          | 20 ns            | 32 GB      |
| disk         | 10 ms            | 10 TB      |
| LAN          | 20 ms            | > 1 PB     |
| internet     | 100 ms           | > 1 ZB     |

Analiza complexității este în ceea ce privește o mașină abstractă, dar software-ul rulează pe mașini reale. Sistemele informatice moderne sunt organizate ca ierarhii ale mașinilor fizice și virtuale, inclusiv timpii de funcționare a limbajului, sisteme de operare, procesoare, memorie cache, memorie cu acces aleatoriu, unități de disc și rețele. Primul tabel arată limitele privind timpul de acces aleatoriu și capacitatea de stocare pentru un server de rețea tipic.

Rețineți că capacitatea și viteza variază în funcție de mai multe ordine de magnitudine. Caching și lookfore sunt utilizate puternic la fiecare nivel al sistemelor noastre pentru a ascunde această variație, dar acestea funcționează doar atunci când accesul este previzibil. Când Cache ratează frecvent, sistemul va bate. De exemplu, pentru a inspecta aleatoriu fiecare octet pe un hard disk ar putea dura 32 de ani. Chiar și pentru a inspecta aleatoriu fiecare octet în RAM ar putea dura 11 minute. Accesul aleatoriu nu este previzibil. Ce este? Aceasta depinde de sistem, dar re-accesarea articolelor utilizate recent și accesarea secvențială a articolelor sunt de obicei un câștig.

Algoritmile şi structurile de date variază în funcţie de eficienţa utilizării cachelor. De exemplu:
- Căutarea liniară face o bună utilizare a Lookfore, dar necesită*O (n)*comparaţii.
- Căutarea binară a unui array sortate necesită numai*O [log (n) ]*comparaţii.
- Căutarea unui copac van Emde Boas este*O [log (n) ]*si cache-evident.


|Elements | Search time (ns)|       |         |
Traducerea şi adaptarea:
|         | **liniară** | **binar** |	**vEB** |
| 8       | 50         | 90         | 40      |
| 64      | 180        | 150        | 70      |
| 512     | 1200       | 230        | 100     |
| 4096    | 17000      | 320        | 160     |


Cum să alegi? În ultima analiză, măsurând. Al doilea tabel arată timpul necesar pentru a căuta array-uri de 64-biți numere întregi prin intermediul acestor trei metode. Pe calculatorul meu:
- Căutarea liniară este competitivă pentru array-uri mici, dar pierde exponențial pentru array-uri mai mari.
- Van Emde Boas câștigă mâinile în jos, datorită modelului de acces previzibil.

> *"Îţi plăteşti banii şi alegi."[Punch](http://www.nytimes.com/1988/02/28/magazine/on-language-you-pays-yer-money.html?pagewanted=all)*

De[Greg Colvin](http://programmer.97things.oreilly.com/wiki/index.php/Greg_Colvin)
