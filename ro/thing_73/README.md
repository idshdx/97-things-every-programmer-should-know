# Rezistă tentaţiei modelului Singleton

Modelul Singleton rezolvă multe dintre problemele tale. Ştii că ai nevoie doar de un singur caz. Aveți o garanție că acest caz este inițializat înainte de a fi utilizat. Acesta păstrează design-ul simplu de a avea un punct de acces global. Totul e bine. Ce nu-ţi place la modelul ăsta clasic?

Destul de mult, se pare. Tentant ei pot fi, dar experiența arată că majoritatea singletonilor într-adevăr face mai mult rău decât bine. Ele împiedică testabilitatea și menținerea pericolelor. Din păcate, această înţelepciune suplimentară nu este atât de răspândită pe cât ar trebui şi singletonii continuă să fie irezistibili pentru mulţi programatori. Dar merită să ne împotrivim:

- Este adesea imaginată cerinţa unei singure instalări. În multe cazuri, este pur speculație că nu vor fi necesare cazuri suplimentare în viitor. La un moment dat, difuzarea unor astfel de proprietăţi speculative în cadrul proiectului unei aplicaţii va provoca durere. Cerinţele se vor schimba. Un design bun acceptă asta. Singletons nu.

- Singletonii cauzează dependențe implicite între unitățile de cod independente conceptual. Acest lucru este problematic atât pentru că sunt ascunse și pentru că introduc cuplarea inutilă între unități. Acest miros de cod devine înţepător atunci când încercați să scrieți teste de unitate, care depind de cuplare liber și capacitatea de a înlocui selectiv o punere în aplicare mișto pentru unul real. Singletonii previn astfel de batjocură.

- Singletonii poartă, de asemenea, starea implicită persistentă, ceea ce împiedică din nou testarea unității. Testarea unității depinde de faptul că testele sunt independente unele de altele, astfel încât testele pot fi efectuate în orice ordine, iar programul poate fi setat într-un stat cunoscut înainte de efectuarea fiecărei încercări a fiecărei unități. Odată ce ați introdus singletons cu stare mutabilă, acest lucru poate fi greu de realizat. În plus, o astfel de stare persistentă accesibilă la nivel mondial îngreunează motivarea codului, în special într-un mediu cu mai multe fire.

- Multi-fire introduce capcane suplimentare la modelul Singleton. Deoarece blocarea directă a accesului nu este foarte eficientă, așa-numitul model de blocare dublu-verificat (DCLP) a câștigat popularitate. Din păcate, aceasta poate fi o altă formă de atracţie fatală. Se pare că în multe limbi DCLP nu este sigur și, chiar și în cazul în care este, există încă oportunități de a obține în mod subtil greșit.

Curățarea singletonilor poate prezenta o provocare finală:

- Nu există nici un sprijin pentru uciderea explicită a singletonilor, care poate fi o problemă serioasă în unele contexte. De exemplu, într-o arhitectură plug-in unde un plug-in poate fi descărcat în siguranță numai după ce toate obiectele sale au fost curățate.

- Nu există nici o ordine de curățare implicită de singletons la ieșirea programului. Acest lucru poate fi problematic pentru aplicații care conțin singletons cu interdependențe. Când închideţi astfel de aplicaţii, un singurton poate avea acces la altul care a fost deja distrus.

- Unele dintre aceste deficiențe pot fi depășite prin introducerea unor mecanisme suplimentare. Cu toate acestea, acest lucru se datorează costului complexității suplimentare a codului care ar fi putut fi evitată prin alegerea unui model alternativ.

Prin urmare, restricţionaţi utilizarea modelului Singleton la clasele care cu adevărat nu trebuie să fie instanţiate mai mult de o dată. Nu folosi punctul de acces global al lui Singleton din codul arbitrar. În schimb, accesul direct la singleton ar trebui să fie de la doar câteva locuri bine definite, de unde poate fi trecut prin interfaţa sa la alt cod. Acest alt cod este inconștient, și astfel nu depinde de dacă un singleton sau orice alt tip de clasă implementează interfața. Acest lucru rupe dependențele care au împiedicat testarea unității și îmbunătățește menținerea. Deci, data viitoare când te gândești la implementarea sau accesarea unui Singleton, sperăm că va pauză, și cred că din nou.

de[Sam Saariste](http://programmer.97things.oreilly.com/wiki/index.php/Sam_Saariste)