# Gândirea în state

Oamenii din lumea reală au o relaţie ciudată cu statul. Azi dimineaţă am trecut pe la magazinul local să mă pregătesc pentru o altă zi de transformare a cofeinei în cod. Din moment ce felul meu preferat de a face asta e să beau latte, şi nu am găsit lapte, l-am întrebat pe funcţionar.

"Ne pare rău, suntem super-duper, mega-out de lapte."

Pentru un programator, e o declaraţie ciudată. Ori nu mai ai lapte, ori nu. Nu există nici o scară atunci când vine vorba de a fi din lapte. Poate încerca să-mi spună că nu mai au lapte o săptămână, dar rezultatul a fost aceeaşi zi de espresso pentru mine.

În majoritatea situaţiilor reale, atitudinea relaxată a oamenilor faţă de stat nu este o problemă. Din păcate, totuși, mulți programatori sunt destul de vagi în ceea ce privește și statul și aceasta este o problemă.

Luați în considerare un simplu webshop care acceptă doar carduri de credit și nu face facturi clienților, cu un`Order`clasă care conține această metodă:

```
 public boolean isComplete() {
     return isPaid() && hasShipped();
 }
```
 
Rezonabil, nu? Ei bine, chiar dacă expresia este bine extrasă într-o metodă în loc de copiat 'n' trecut peste tot, expresia nu ar trebui să existe deloc. Faptul că scoate în evidenţă o problemă. De ce? Pentru că un ordin nu poate fi expediat înainte de a fi plătit. Prin urmare,`hasShipped`Nu poate fi adevărat dacă nu`isPaid`este adevărat, ceea ce face parte din expresia redundantă. S-ar putea dori încă`isComplete`pentru claritate în cod, dar apoi ar trebui să arate așa:

```
 public boolean isComplete() {
     return hasShipped();
 }
```

În munca mea, văd atât cecuri lipsă cât şi cecuri redundante tot timpul. Acest exemplu este mic, dar atunci când adăugați anulare și rambursare, va deveni mai complex și necesitatea unei bune manipulări de stat crește. În acest caz, un ordin poate fi doar într-una din cele trei stări distincte:

- *În curs:*Se pot adăuga sau elimina elemente. Nu pot naviga.
- *Plătit:*Nu se poate adăuga sau elimina elemente. Poate fi expediat.
- *Expediere:*Gata. Fără alte modificări acceptate.

Aceste state sunt importante și trebuie să verificați că sunteți în starea așteptată înainte de a face operațiuni, și că vă mutați doar într-un stat legal de unde vă aflați. Pe scurt, va trebui sa iti protejezi obiectele cu atentie, in locurile potrivite.

Dar cum începi să gândeşti în state? Extragerea expresiilor la metode semnificative este un început foarte bun, dar este doar un început. Fundaţia este de a înţelege maşinile statului. Ştiu că poate ai amintiri urâte de la cursul CS, dar lasă-le în urmă. Mașinile de stat nu sunt deosebit de greu. Vizualizați-le pentru a le face simplu de înțeles și ușor de vorbit despre. Test-drive codul pentru a desluşi stările şi tranziţiile valide şi invalide şi pentru a le păstra corecte. Studiază modelul statului. Când vă simțiți confortabil, citiți pe Design by Contract. Vă ajută să asiguraţi o stare validă prin validarea datelor primite şi a obiectului însuşi la intrarea şi ieşirea fiecărei metode publice.

Dacă starea ta e incorectă, există o eroare şi rişti să distrugi datele dacă nu abandonezi. Dacă găsiți controalele de stat pentru a fi zgomot, învățați cum să utilizați un instrument, generarea de cod, țesut, sau aspecte pentru a le ascunde. Indiferent de care abordare alegeţi, gândirea în state va face codul dvs. mai simplu şi mai robust.

De[Niclas Nilsson](http://programmer.97things.oreilly.com/wiki/index.php/Niclas_Nilsson)