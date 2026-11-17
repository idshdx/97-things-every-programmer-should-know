# Test în timp ce dormi (și peste weekend-uri)

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_82_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_82_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:56)](../audio/thing_82_ro.mp3)

Relaxează-te. Nu mă refer la centrele de dezvoltare offshore, ore suplimentare în weekend-uri, sau la tura de noapte. Doresc să vă atrag atenţia asupra puterii de calcul pe care o avem la dispoziţie. Mai exact, cât de mult nu suntem valorificarea pentru a face viața noastră ca programatori un pic mai ușor. În mod constant îţi este greu să obţii suficientă putere de calcul în timpul zilei de lucru? Dacă da, ce fac serverele de testare în afara orelor normale de lucru? De cele mai multe ori nu, serverele de testare sunt de mers pe jos peste noapte și peste week-end. Poţi folosi asta în avantajul tău.

- *Ai fost vinovat de a comite o schimbare fără a rula toate testele?*Unul dintre principalele motive pentru care programatorii nu execută suitele de testare înainte de a comite un cod este durata de timp pe care o pot lua. Când termenele limită se apropie și împinge vine la împingere, oamenii începe natural de tăiere colțuri. O modalitate de a aborda acest lucru este de a rupe în jos suita de test mare în două sau mai multe profiluri. Un profil de încercare mai mic, obligatoriu, care este rapid pentru a rula, va ajuta la asigurarea faptului că testele sunt efectuate înainte de fiecare comitere. Toate profilurile de încercare (inclusiv profilul obligatoriu 

- *Ai avut destule ocazii să testezi stabilitatea produsului?*Testele mai lungi sunt vitale pentru identificarea scurgerilor de memorie şi a altor probleme de stabilitate. Ele sunt rareori difuzate în timpul zilei, deoarece va lega timp și resurse. Ai putea automatiza un test pentru a fi difuzate în timpul nopții, și un pic mai mult peste week-end. De la 6:00 pm Vineri la 6:00 am lunea următoare există 60 de ore în valoare de timp de testare potențial.

- *Primești timp de calitate pe mediul de testare Performance?*Am văzut echipe certându-se între ele pentru a obține timp pe mediul de testare a performanțelor. În cele mai multe cazuri, nici o echipă nu obține suficient timp de calitate în timpul zilei, în timp ce mediul este practic inactiv după ore. Serverele și rețeaua nu sunt la fel de ocupat în timpul nopții sau peste weekend. Este un moment ideal pentru a rula unele teste de performanță de calitate.

- *Sunt prea multe permutări pentru a testa manual?*În multe cazuri, produsul dumneavoastră este vizat pentru a rula pe o varietate de platforme. De exemplu, atât 32 biți cât și 64 biți, pe Linux, Solaris și Windows, sau pur și simplu pe versiuni diferite ale aceluiași sistem de operare. Pentru a înrăutăţi lucrurile, multe aplicaţii moderne se expun la o multitudine de mecanisme şi protocoale de transport (HTTP, AMQP, SOAP, CORBA etc.). Testarea manuală a tuturor acestor permutări este foarte consumatoare de timp și cel mai probabil făcută aproape de o eliberare din cauza presiunii resurselor. Din păcate, poate fi prea târziu în ciclu pentru a prinde anumite insecte urâte.

Testele automate efectuate în timpul nopții sau în weekenduri se vor asigura că toate aceste permutări sunt testate mai des. Cu un pic de gândire și unele cunoștințe de scripting, puteți programa câteva*cron*locuri de muncă pentru a începe unele teste pe timp de noapte și de-a lungul weekend-ului. Există, de asemenea, multe instrumente de testare acolo care ar putea ajuta. Unele organizaţii au chiar şi reţele de servere care oferă servere în diferite departamente şi echipe pentru a se asigura că resursele sunt utilizate eficient. Dacă acest lucru este disponibil în organizația dumneavoastră, puteți trimite teste pentru a fi efectuate pe timp de noapte sau pe parcursul weekend-urilor.

de[Rajith Attapattu](http://programmer.97things.oreilly.com/wiki/index.php/Rajith_Attapattu)