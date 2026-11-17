# Desfăşurarea timpurie şi frecventă

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_20_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_20_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 2:47)](../audio/thing_20_ro.mp3)

Depanarea proceselor de implementare și instalare este adesea amânată până la sfârșitul unui proiect. În unele proiecte scrierea de instrumente de instalare este delegată unui inginer de lansare care preia sarcina ca un "rău necesar." Revizuirile și demonstrațiile se fac dintr-un mediu lucrat manual pentru a se asigura că totul funcționează. Rezultatul este că echipa nu are experienţă în procesul de desfăşurare sau în mediul desfăşurat până când nu va fi prea târziu să facă schimbări.

Procesul de instalare / desfășurare este primul lucru pe care clientul îl vede, iar un proces simplu de instalare / desfășurare este primul pas pentru a avea un mediu de producție fiabil (sau, cel puțin, ușor de depanat). Software-ul implementat este ceea ce clientul va folosi. Neasigurându-vă că implementarea stabilește aplicația corect, veți ridica întrebări cu clientul dumneavoastră înainte de a ajunge să utilizeze software-ul bine.

Pornirea proiectului cu un proces de instalare vă va oferi timp pentru a evolua procesul pe măsură ce treceți prin ciclul de dezvoltare a produsului, precum și șansa de a face modificări la codul de aplicare pentru a face instalarea mai ușoară. Rularea și testarea procesului de instalare pe un mediu curat oferă periodic, de asemenea, o verificare că nu ați făcut ipoteze în codul care se bazează pe mediile de dezvoltare sau de testare.

Punerea în aplicare ultima înseamnă că procesul de desfășurare ar putea fi mai complicat pentru a lucra în jurul ipotezelor din cod. Ceea ce părea o idee grozavă într-un IDE, în cazul în care aveți control deplin asupra unui mediu, s-ar putea face pentru un proces de implementare mult mai complicat. E mai bine să ştii toate compromisurile mai devreme decât mai târziu.

În timp ce "a fi capabil de a implementa" nu pare să aibă o mulțime de valoare de afaceri de timpuriu pe comparativ cu a vedea o aplicație rulează pe laptop-ul unui dezvoltator, adevărul simplu este că până când puteți demonstra aplicarea pe mediul țintă, există o mulțime de lucru de făcut înainte de a putea oferi valoare de afaceri. Dacă raţionamentul pentru amânarea unui proces de desfăşurare este că este trivial, atunci fă-o oricum, deoarece este un cost scăzut. Dacă este prea complicat, sau dacă există prea multe incertitudini, face ceea ce ar face cu codul de aplicare: experiment, evalua, și refactor procesul de implementare pe măsură ce merge.

Procesul de instalare/de desfăşurare este esenţial pentru productivitatea clienţilor dumneavoastră sau a echipei de servicii profesionale, aşa că ar trebui să testaţi şi să refactorizaţi acest proces în timp ce mergeţi. Testăm şi refacem codul sursă pe parcursul unui proiect. Desfășurarea merită nici mai puțin.

De[Steve Berczuk](http://programmer.97things.oreilly.com/wiki/index.php/Steve_Berczuk)
