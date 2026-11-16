# Nu te repeta.

Dintre toate principiile de programare, Nu te repeta (DRY) este, probabil, unul dintre cele mai fundamentale. Principiul a fost formulat de Andy Hunt și Dave Thomas în*Programatorul Pragmatic*, și subliniază multe alte bine-cunoscute software dezvoltare cele mai bune practici și modele de proiectare. Dezvoltatorul care invata sa recunoasca duplicarea si intelege cum sa o elimine prin practica corespunzatoare si abstractie corespunzatoare, poate produce un cod mult mai curat decat cel care infecteaza continuu aplicatia cu repetitie inutila.

Duplicarea este deşeuri.
---

Fiecare linie de cod care intră într-o aplicație trebuie menținută, și este o sursă potențială de bug-uri viitoare. Duplicarea umflă fără rost baza de coduri, rezultând mai multe oportunități pentru bug-uri și adăugarea de complexitate accidentală la sistem. Bloat care se suprapune adaugă la sistem, de asemenea, face mai dificil pentru dezvoltatorii care lucrează cu sistemul pentru a înțelege pe deplin întregul sistem, sau pentru a fi siguri că modificările făcute într-o locație nu trebuie, de asemenea, să fie făcute în alte locuri care duplicat logica la care lucrează. DRY cere ca "fiecare bucată de cunoaştere să aibă o singură reprezentare, fără ambiguitate şi autoritate într-un sistem."

Repetarea în proces necesită automatizare
---

Multe procese de dezvoltare software sunt repetitive și ușor automatizate. Principiul DRY se aplică în aceste contexte, precum și în codul sursă al cererii. Testarea manuală este lentă, predispusă la erori și dificil de repetat, astfel încât să se utilizeze suite automate de testare, dacă este posibil. Integrarea software-ului poate fi consumatoare de timp și predispuse la erori dacă este făcut manual, astfel încât un proces de construire ar trebui să fie rulat cât mai frecvent posibil, ideal cu fiecare check-in. Oriunde există procese manuale dureroase care pot fi automatizate, acestea ar trebui să fie automatizate și standardizate. Scopul este de a asigura există doar o singură cale de a îndeplini sarcina, și este cât mai dureros posibil.

Repetarea în logică necesită abstractizare
---

Repetiţia în logică poate lua multe forme. Copiere-și-pastă*dacă-atunci*sau*cutie de comutare*Logica este printre cele mai usor de detectat si corect. Multe modele de proiectare au scopul explicit de a reduce sau elimina suprapunerea logicii în cadrul unei aplicații. Dacă un obiect necesită de obicei mai multe lucruri să se întâmple înainte de a putea fi folosit, acest lucru poate fi realizat cu o Fabrica abstractă sau o metodă de fabrică. Dacă un obiect are multe variante posibile în comportamentul său, aceste comportamente pot fi injectate folosind modelul de strategie mai degrabă decât mare*dacă-atunci*Structuri. De fapt, formularea modelelor de proiectare în sine este o încercare de reducere a duplicării eforturilor necesare pentru rezolvarea problemelor comune și discutarea unor astfel de soluții. În plus, DRY poate fi aplicat structurilor, cum ar fi schema de baze de date, ceea ce duce la normalizare.

O chestiune de principiu
---

Alte principii software sunt, de asemenea, legate de DRY. Principiul "Odată și o singură dată," care se aplică doar comportamentului funcțional al codului, poate fi considerat un subset de DRY. Principiul deschis/închis, care prevede că "entitățile software ar trebui să fie deschise pentru extindere, dar închise pentru modificare," funcționează în practică numai atunci când DRY este urmat. De asemenea, bine-cunoscutul principiu al responsabilității unice impune ca o clasă să aibă "un singur motiv de schimbare," se bazează pe DRY.

Atunci când este urmat în ceea ce privește structura, logica, procesul și funcția, principiul DRY oferă orientări fundamentale dezvoltatorilor de software și ajută la crearea de aplicații mai simple, mai durabile, de calitate superioară. În timp ce există scenarii în care repetiția poate fi necesară pentru a îndeplini performanța sau alte cerințe (de exemplu, denormalizarea datelor într-o bază de date), aceasta ar trebui utilizată doar în cazul în care abordează direct o problemă reală, mai degrabă decât imaginară.

De[Steve Smith](http://programmer.97things.oreilly.com/wiki/index.php/Steve_Smith)