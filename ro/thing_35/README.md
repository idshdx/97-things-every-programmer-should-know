# Regula de aur a proiectului API

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_35_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_35_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:03)](../audio/thing_35_ro.mp3)

Designul API este greu, în special în mare. Dacă sunteți proiectarea unui API care va avea sute sau mii de utilizatori, trebuie să se gândească la modul în care s-ar putea schimba în viitor și dacă modificările s-ar putea sparge codul client. În afară de asta, trebuie să te gândeşti cum te afectează utilizatorii API. Dacă una dintre clasele tale API foloseşte una din metodele sale interne, trebuie să-ţi aminteşti că un utilizator ar putea să-ţi subclaseze clasa şi să o suprascrie, şi asta ar putea fi dezastruos. Nu ai putea schimba această metodă pentru că unii dintre utilizatorii tăi i-au dat un sens diferit. Viitoarele tale opțiuni de implementare internă sunt la mila utilizatorilor tăi.

Dezvoltatorii API rezolvă această problemă în diferite moduri, dar cel mai simplu mod este de a bloca API. Dacă sunteți de lucru în Java s-ar putea fi tentat să facă cele mai multe dintre clasele și metodele finale. În C#, s-ar putea face clasele și metodele sigilate. Indiferent de limba pe care o utilizați, s-ar putea fi tentat să prezinte API dvs. printr-un singleton sau de a folosi metode de fabrică statică, astfel încât să puteți proteja de la oameni care ar putea suprascrie comportamentul și de a folosi codul în moduri care pot constrânge alegerile mai târziu. Totul pare rezonabil, dar este într-adevăr?

În ultimul deceniu, am realizat treptat că testarea unităţii este o parte extrem de importantă a practicii, dar această lecţie nu a pătruns complet în industrie. Dovezile sunt peste tot în jurul nostru. Luați o clasă arbitrară netestată care utilizează un API terț și încercați să scrieți teste unitare pentru el. De cele mai multe ori, vei avea probleme. Veți găsi că codul folosind API este lipit de ea ca lipici. Nu există nici o modalitate de a imita clasele API astfel încât să puteți simți interacțiunile codului cu ei, sau de aprovizionare valori de returnare pentru testare.

De-a lungul timpului, acest lucru va fi mai bine, dar numai dacă vom începe să vedem testarea ca un caz de utilizare reală atunci când vom proiecta API. Din păcate, este un pic mai implicat decât doar testarea codului nostru. Acolo...**Regula de aur a proiectului API**se încadrează în:*Nu este suficient pentru a scrie teste pentru un API pe care îl dezvoltați; trebuie să scrieți teste unitate pentru cod care utilizează API-ul. Când o faci, înveți personal obstacolele pe care utilizatorii vor trebui să le depășească atunci când încearcă să-și testeze codul independent.*

Nu există nici o modalitate de a face ușor pentru dezvoltatori să testeze codul care utilizează API.`static`,`final`, și`sealed`nu sunt structuri în mod inerent rele. Ele pot fi utile uneori. Dar este important să fie conștienți de problema de testare și, pentru a face acest lucru, trebuie să-l experimenteze tine. Odată ce ați făcut-o, vă puteți apropia ca și cum ați face orice altă provocare de design.

De[Michael Feathers](http://programmer.97things.oreilly.com/wiki/index.php/Michael_Feathers)