# Verbose Logging va tulbura somnul

Când întâlnesc un sistem care a fost deja în dezvoltare sau producție pentru o vreme, primul semn de probleme reale este întotdeauna un jurnal murdar. Ştii despre ce vorbesc. Atunci când faceţi clic pe un singur link pe un flux normal pe o pagină web duce la un potop de mesaje în singurul jurnal pe care sistemul oferă. Prea mult lemn poate fi la fel de inutil ca nici unul.

Dacă sistemele tale sunt ca ale mele, atunci când treaba ta se face treaba altcuiva este doar la început. După ce sistemul a fost dezvoltat, sperăm că va trăi o viață lungă și prosperă servind clienții. Dacă ai noroc. Cum vei şti dacă ceva nu merge bine când sistemul este în producţie şi cum te vei descurca cu el?

Poate cineva îţi monitorizează sistemul, sau poate îl vei monitoriza singur. Oricum, jurnalele vor face probabil parte din monitorizare. Dacă apare ceva şi trebuie să te trezeşti pentru a face faţă, vrei să te asiguri că există un motiv bun pentru asta. Dacă sistemul meu moare, vreau să ştiu. Dar dacă e doar un sughiţ, prefer să mă bucur de somnul de frumuseţe.

Pentru multe sisteme, primul indiciu că ceva nu este în regulă este că un jurnal este scris pe un jurnal. În mare parte, acesta va fi jurnalul de eroare. Aşa că fă-ţi o favoare: Asigurați-vă că din prima zi că dacă ceva este conectat în jurnalul de eroare, sunteți dispus să aibă pe cineva apel și te trezesc în mijlocul nopții despre asta. Dacă puteți simula sarcina pe sistemul dumneavoastră în timpul testării sistemului, uitați-vă la un jurnal de eroare fără zgomot este, de asemenea, un bun prim indiciu că sistemul dumneavoastră este destul de robust. Sau un avertisment devreme dacă nu este.

Sistemele distribuite adaugă un alt nivel de complexitate. Trebuie să decizi cum să faci faţă unei dependenţe externe. Dacă sistemul dumneavoastră este foarte distribuit, acesta poate fi un eveniment frecvent. Asigurați-vă că politica de exploatare forestieră ia în considerare acest lucru.

În general, cel mai bun indiciu că totul este în regulă este că mesajele la o prioritate mai mică ticăie de-a lungul fericit. Vreau un mesaj INFO pentru fiecare eveniment important.

Un jurnal aglomerat este un indiciu că sistemul va fi greu de controlat odată ce ajunge la producţie. Dacă nu te aştepţi să apară ceva în jurnalul de eroare, va fi mult mai uşor să ştii ce să faci când apare ceva.

De[Johannes Brodwall](http://programmer.97things.oreilly.com/wiki/index.php/Johannes_Brodwall)