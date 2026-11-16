# Înainte de a vă reface

La un moment dat, fiecare programator va trebui să refacă codul existent. Dar înainte de a face acest lucru vă rugăm să vă gândiți la următoarele, deoarece acest lucru ar putea salva tu și alții o mare de timp (și durere):

- *Cea mai bună abordare pentru restructurare începe prin inventarierea bazei de coduri existente și a testelor scrise împotriva acestui cod.*Acest lucru vă va ajuta să înțelegeți punctele forte și punctele slabe ale codului așa cum este în prezent, astfel încât să vă puteți asigura că păstrați punctele tari evitând în același timp greșelile. Cu toţii credem că putem face mai bine decât sistemul existent... până când ajungem cu ceva care nu e mai bun decât întruparea anterioară pentru că nu am reuşit să învăţăm din greşelile sistemului existent.

- *Evita tentaţia de a rescrie totul.*Cel mai bine este să refolosim cât mai mult cod posibil. Indiferent cât de urât este codul, a fost deja testat, revizuit, etc. Aruncând vechiul cod  Dacă nu iei asta în considerare, noul cod pe care îl scrii poate ajunge să arate aceleaşi insecte misterioase care au fost fixate în vechiul cod. Acest lucru va pierde o mulțime de timp, efort, și cunoștințe câștigate de-a lungul anilor.

- *Multe schimbări incrementale sunt mai bune decât o schimbare masivă.*Schimbările elementare vă permit să măsurați mai ușor impactul asupra sistemului prin feedback, cum ar fi din teste. Nu e amuzant să vezi o sută de eşecuri după ce faci o schimbare. Acest lucru poate duce la frustrare şi la presiuni care pot duce la rândul lor la decizii greşite. Un cuplu de eșecuri de testare este ușor de a face cu și oferă o abordare mai ușor de gestionat.

- *După fiecare iterație, este important să se asigure că testele existente trec.*Se adaugă noi teste dacă testele existente nu sunt suficiente pentru a acoperi modificările pe care le-ați făcut. Nu aruncaţi testele din codul vechi fără să luaţi în considerare acest lucru. La suprafață, unele dintre aceste teste nu par a fi aplicabile noului proiect, dar ar merita efortul de a săpa adânc în jos în motivele pentru care a fost adăugat acest test special.

- *Preferințele personale și ego-ul nu ar trebui să stea în cale.*Dacă ceva nu e stricat, de ce să-l repari? Că stilul sau structura codului nu corespunde preferinței dumneavoastră personale nu este un motiv valabil pentru restructurare. Crezând că ai putea face o treabă mai bună decât fostul programator nu este un motiv valabil, fie.

- *Noile tehnologii nu sunt suficiente pentru a fi readuse.*Unul dintre cele mai rele motive pentru a refactori este că codul actual este mult în spatele întregii tehnologii cool pe care o avem astăzi, și credem că un nou limbaj sau cadru poate face lucrurile mult mai elegant. Cu excepția cazului în care o analiză cost-beneficiu arată că un nou limbaj sau cadru va duce la îmbunătățiri semnificative în funcționalitate, întreținere sau productivitate, este cel mai bine să-l părăsească așa cum este.

- *Nu uita că oamenii fac greşeli.*Restructurarea nu va garanta întotdeauna faptul că noul cod va fi mai bun decât cel anterior. Am văzut şi am făcut parte din câteva încercări eşuate de restructurare. Nu era frumos, dar era uman.

de[Rajith Attapattu](http://programmer.97things.oreilly.com/wiki/index.php/Rajith_Attapattu)