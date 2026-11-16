# Scrie funcţii mici folosind exemple

Am dori să scriem codul corect şi să avem dovezi că este corect. Acesta poate ajuta cu ambele probleme să se gândească la "dimensiunea" unei funcții. Nu în sensul valorii de cod care pune în aplicare o funcţie deşi că este interesant 

De exemplu, în jocul de Go există o condiție numită*atari*în care pietrele unui jucător pot fi capturate de adversarul lor: o piatră cu două sau mai multe spații libere adiacente acesteia (numite*Libertăţi*) nu este în Atari. Poate fi dificil să numeri câte libertăţi are o piatră, dar determinarea Atari este uşoară dacă se ştie asta. Am putea începe prin a scrie o funcţie ca asta:

```
boolean atari(int libertyCount)
    libertyCount < 2
```

E mai mare decât pare. O funcție matematică poate fi înțeleasă ca un set, unele subset al produsului cartezian al seturilor care sunt domeniul său (aici,`int`) and rang (here,`boolean`). Dacă acele seturi de valori ar fi de aceeaşi mărime ca în Java atunci ar fi`2L*(Integer.MAX_VALUE+(-1L*Integer.MIN_VALUE)+1L)`sau 8,589,934,592 membri în set`int×boolean`. Jumătate dintre aceștia sunt membri ai subsetului care este funcția noastră, astfel încât să furnizeze dovezi complete că funcția noastră este corectă ar trebui să verifice în jurul valorii de 4.3×10<sup>9</sup>exemple.

Aceasta este esenţa afirmaţiei că testele nu pot dovedi absenţa insectelor. Testele pot demonstra totuşi prezenţa unor caracteristici. Dar totuşi avem această problemă de mărime.

Domeniul problemei ne ajută. Natura lui Go inseamna ca numarul de libertati ale unei pietre nu este nici o int, ci exact unul dintre {1,2,3,4.}. Ca să putem scrie alternativ:

```
LibertyCount = {1,2,3,4} 
boolean atari(LibertyCount libertyCount)
    libertyCount == 1
```

Acest lucru este mult mai tractabil: Funcția calculată este acum un set cu cel mult opt membri. De fapt, patru exemple verificate ar constitui dovezi de certitudine deplină că funcția este corectă. Acesta este unul dintre motivele pentru care este o idee bună de a folosi tipuri strâns legate de domeniul problemă pentru a scrie programe, mai degrabă decât tipuri native. Folosind domenii de tip inspirat poate face de multe ori funcțiile noastre mult mai mici. O modalitate de a afla care ar trebui să fie aceste tipuri este de a găsi exemple pentru a verifica în termeni de domeniu problemă, înainte de a scrie funcția.

de[Keith Braithwaite](http://programmer.97things.oreilly.com/wiki/index.php/Keith_Braithwaite)