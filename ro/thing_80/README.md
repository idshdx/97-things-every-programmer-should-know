# Test pentru comportamentul necesar, nu comportament incidental

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_80_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_80_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:41)](../audio/thing_80_ro.mp3)

O capcană comună în testare este de a presupune că exact ceea ce face o implementare este exact ceea ce doriți să testați pentru. La prima vedere pare mai mult o virtute decât o capcană. Însă, altfel spus, problema devine mai evidentă: O capcană comună în testare este de a hardwire teste la specificul unei implementări, în cazul în care aceste caracteristici sunt accidentale și nu au nici un efect asupra funcționalității dorite.

Atunci când testele sunt hardwired la punerea în aplicare accidentale, modificări la punerea în aplicare care sunt de fapt compatibile cu comportamentul necesar pot provoca teste pentru a eșua, ceea ce duce la rezultate fals pozitive. Programatorii răspund de obicei fie prin rescrierea testului, fie prin rescrierea codului. Presupunând că un fals pozitiv este de fapt un adevărat pozitiv este adesea o consecinţă a fricii, a incertitudinii sau a îndoielii. Acesta are efectul de a ridica statutul de comportament accidental la comportamentul necesar. În rescrierea unui test, programatorii fie refocalizează testul pe comportamentul necesar (bun), fie pur și simplu îl hardwire la noua implementare (nu este bine). Testele trebuie să fie suficient de precise, dar trebuie, de asemenea, să fie exacte.

De exemplu, într-o comparație în trei, cum ar fi C`strcmp`sau Java`String.compareTo`, cerințele privind rezultatul sunt că este negativ dacă partea stângă este mai mică decât cea dreaptă, pozitivă dacă partea stângă este mai mare decât cea dreaptă și zero dacă sunt considerate egale. Acest stil de comparație este utilizat în multe API, inclusiv comparatorul pentru C`qsort`funcţie şi`compareTo`în Java`Comparable`Interfață. Deși valorile specifice`-1`şi`+1`sunt utilizate în mod obișnuit în implementări pentru a semnifica*sub*şi*mai mare decât*, respectiv, programatorii presupun adesea în mod greșit că aceste valori reprezintă cerința reală și, prin urmare, scriu teste care stabilesc această ipoteză în public.

O problemă similară apare odată cu încercările care susţin spaţierea, formularea precisă şi alte aspecte ale formatării textuale şi ale prezentării accidentale. Dacă nu scrieți, de exemplu, un generator XML care oferă formatare configurabilă, distanța nu ar trebui să fie semnificativă pentru rezultat. De asemenea, plasarea butoanelor și etichetelor pe controalele UI reduce opțiunea de modificare și rafinare a acestor incidente în viitor. Schimbări minore în ceea ce privește punerea în aplicare și schimbările neimportante în formatare devin brusc întrerupătoare de construcție.

Testele supraspecificate sunt adesea o problemă cu abordările Whitebox pentru testarea unității. Testele Whitebox folosesc structura codului pentru a determina cazurile de testare necesare. Modul tipic de eroare de testare Whitebox este că testele ajung să afirme că codul face ceea ce face codul. Pur și simplu reafirmând ceea ce este deja evident din cod nu adaugă nicio valoare și duce la un fals sentiment de progres și securitate.

Pentru a fi eficiente, testele trebuie să precizeze obligații contractuale mai degrabă decât implementarea papagalilor. Ei au nevoie pentru a lua o vedere Blackbox a unităților supuse testului, schițarea contractelor de interfață în formă executabilă. Prin urmare, alinierea comportamentului testat cu comportamentul necesar.

De[Kevlin Henney](http://programmer.97things.oreilly.com/wiki/index.php/Kevlin_Henney)