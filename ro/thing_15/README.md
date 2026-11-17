# Codificare cu motiv

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_15_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_15_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 4:12)](../audio/thing_15_ro.mp3)

Încercarea de a raţiona despre corectitudinea software-ului de mână duce la o dovadă formală care este mai mult decât codul şi este mai probabil să conţină erori decât codul. Instrumentele automate sunt de preferat, dar nu întotdeauna posibile. Ceea ce urmează descrie o cale de mijloc: raționamentul semi-formal despre corectitudine.

Abordarea de bază este de a împărți tot codul în cauză în secţiuni scurte de la o singură linie, cum ar fi un apel funcţional, la blocuri de mai puţin de zece linii şi argumentând despre corectitudinea lor. Argumentele trebuie să fie suficient de puternice pentru a-l convinge pe avocatul diavolului de programator.

Trebuie aleasă o secţiune astfel încât la fiecare criteriu final de evaluare să fie aleasă o secţiune*stadiul programului*(și anume, contorul de program și valorile tuturor obiectelor "viu") satisface o proprietate ușor de descris, și că funcționalitatea acestei secțiuni (transformare de stat) este ușor de descris ca o singură sarcină  Astfel de proprietăți ale obiectivului generalizează concepte precum*Precondiție*şi*Postcondiție*pentru funcții și*invariant*pentru bucle și clase (în ceea ce privește cazurile lor). Faptul că secţiunile trebuie să fie cât mai independente unele de altele simplifică raţionamentul şi este indispensabil atunci când aceste secţiuni urmează să fie modificate.

Multe dintre practicile de codificare bine cunoscute (deși poate mai puțin bine urmate) și considerate "bune" facilitează raționamentul. Prin urmare, doar dacă intenţionezi să te gândeşti la codul tău, începi deja să te gândeşti la un stil şi o structură mai bune. Nesurprinzător, cele mai multe dintre aceste practici pot fi verificate prin analizatoare de coduri statice:

- Evitați utilizarea declarațiilor goto, deoarece acestea fac secțiuni îndepărtate foarte interdependente.
- Evitați utilizarea variabilelor modificate globale, deoarece acestea fac toate secțiunile care le folosesc dependente.
- Fiecare variabilă ar trebui să aibă cel mai mic domeniu de aplicare posibil. De exemplu, un obiect local poate fi declarat chiar înainte de prima utilizare.
- Face obiecte*imutabil*dacă este cazul.
- Face codul lizibil prin utilizarea distanței, atât orizontală cât și verticală. De exemplu, alinierea structurilor aferente și utilizarea unei linii goale pentru a separa două secțiuni.
- Face codul auto-documentare prin alegerea descriptive (dar relativ scurte) nume pentru obiecte, tipuri, funcții, etc.
- Dacă aveți nevoie de o secțiune cuib, face o funcție.
- Asigurați-vă funcțiile scurt și concentrat pe o singură sarcină. Vechea*Limita de 24 de linii*Încă se aplică. Deși dimensiunea ecranului și rezoluția s-au schimbat, nimic nu s-a schimbat în cunoașterea umană din anii 1960.
- Funcţiile ar trebui să aibă puţini parametri (patru este o bună limită superioară). Acest lucru nu limitează datele comunicate funcțiilor: Gruparea parametrilor asociați într-un singur obiect beneficiază de*Invariante obiect*și salvează raționamentul, cum ar fi coerența și coerența lor.
- Mai general, fiecare unitate de cod, de la un bloc la o bibliotecă, ar trebui să aibă o*interfață îngustă*. Mai puțină comunicare reduce raționamentul necesar. Aceasta înseamnă că*geters*că statul intern de returnare sunt o datorie  În schimb, cereți obiectul să lucreze cu informațiile pe care le are deja. Cu alte cuvinte,*încapsulare*este tot *interfețe înguste*.
- Pentru a păstra clasa*invariante*, utilizarea*Seturi*trebuie descurajat, aşa cum*Seturi*tind să permită invarianților care guvernează starea unui obiect să fie rupt.

Pe lângă faptul că te gândeşti la corectitudinea ei, faptul de a te certa cu privire la codul tău îţi dă o înţelegere. Comunicaţi informaţiile pe care le câştigaţi în beneficiul tuturor.

De[Yechiel Kimchi](http://programmer.97things.oreilly.com/wiki/index.php/Yechiel_Kimchi)
