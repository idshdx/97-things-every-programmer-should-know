# Excepţii de la tehnic

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_21_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_21_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:51)](../audio/thing_21_ro.mp3)

Există practic două motive pentru care lucrurile merg prost la rulare: probleme tehnice care ne împiedică să folosim aplicaţia şi logica de afaceri care ne împiedică să folosim greşit aplicaţia. Majoritatea limbilor moderne, cum ar fi LISP, Java, Smalltalk, și C#, folosesc excepții pentru a semnala ambele situații. Cu toate acestea, cele două situaţii sunt atât de diferite, încât trebuie ţinute cu atenţie separate. Este o sursă potenţială de confuzie să le reprezentăm pe amândouă folosind aceeaşi ierarhie de excepţie, ca să nu mai vorbim de aceeaşi clasă de excepţie.

O problemă tehnică nerezolvabilă poate apărea atunci când există o eroare de programare. De exemplu, dacă încercați să accesați elementul 83 dintr-o gamă de dimensiuni 17, atunci programul este în mod clar off track, și unele excepție ar trebui să conducă. Versiunea subtilă este de asteptare unele cod bibliotecă cu argumente inadecvate, cauzând aceeași situație în interiorul bibliotecii.

Ar fi o greşeală să încerci să rezolvi aceste situaţii pe care le-ai cauzat. În schimb, lăsăm ca excepţia să ajungă la cel mai înalt nivel arhitectural şi să lăsăm un mecanism general de manipulare a excepţiilor să facă tot ce poate pentru a asigura siguranţa sistemului, cum ar fi rularea înapoi a unei tranzacţii, logarea şi alertarea administraţiei şi raportarea înapoi (politicos) către utilizator.

O variantă a acestei situații este atunci când vă aflați în "situația bibliotecii" și un apelant a rupt contractul metodei tale, de exemplu, trecând un argument total bizar sau nu având un obiect dependent înființat în mod corespunzător. Acest lucru este pe o par cu accesarea elementul 83 de la 17: apelantul ar fi trebuit verificat; nu face acest lucru este o eroare programator pe partea client. Răspunsul corect este de a arunca o excepție tehnică.

O situație diferită, dar încă tehnică, este atunci când programul nu poate continua din cauza unei probleme în mediul de execuție, cum ar fi o bază de date care nu răspunde. În această situație trebuie să presupuneți că infrastructura a făcut tot ce a putut pentru a rezolva situația  Chiar dacă cauza este diferită, situația pentru codul de apelare este similară: există puține lucruri pe care le poate face. Aşadar, semnalăm situaţia printr-o excepţie pe care am lăsat-o baltă mecanismului general de manipulare a excepţiei.

Spre deosebire de acestea, avem situația în care nu puteți finaliza apelul pentru un motiv de domeniu-logic. În acest caz am întâlnit o situație care este o excepție, adică, neobișnuită și nedorită, dar nu bizară sau programatic în eroare. De exemplu, dacă încerc să retrag bani dintr-un cont cu fonduri insuficiente. Cu alte cuvinte, acest tip de situație este o parte a contractului, și aruncarea unei excepții este doar o*calea alternativă de întoarcere*care face parte din model și de care clientul trebuie să fie conștient și pregătit să se ocupe. Pentru aceste situații, este oportun să se creeze o excepție specifică sau o ierarhie de excepție separată, astfel încât clientul să se poată ocupa de situație în condiții proprii.

Amestecarea excepțiilor tehnice și a excepțiilor de afaceri în aceeași ierarhie estompează distincția și confundă apelantul cu privire la ceea ce este contractul de metodă, la ce condiții este necesar să se asigure înainte de a suna, și la ce situații ar trebui să se ocupe. Separarea cazurilor oferă claritate și sporește șansele ca excepțiile tehnice să fie tratate printr-un anumit cadru de aplicare, în timp ce excepțiile din domeniul de afaceri sunt de fapt luate în considerare și gestionate prin codul clientului.

De[Dan Bergh Johnsson](http://programmer.97things.oreilly.com/wiki/index.php/Dan_Bergh_Johnsson)