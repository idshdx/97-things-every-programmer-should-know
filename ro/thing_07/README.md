# Feriţi - vă de partea noastră

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_07_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_07_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 2:26)](../audio/thing_07_ro.mp3)

A fost primul meu proiect la companie. Tocmai îmi terminasem diploma şi eram nerăbdător să demonstrez că stau până târziu în fiecare zi trecând prin codul existent. Așa cum am lucrat prin prima mea caracteristică am avut grijă în plus pentru a pune în aplicare tot ce am învățat comentarii, logare, trăgând codul comun în biblioteci, acolo unde este posibil, lucrările. Revizuirea de cod pe care m-am simțit atât de gata pentru a venit ca o trezire nepoliticos 

Cum e posibil? Toate prin reutilizare colegiu a fost reținut ca epitomul de inginerie software de calitate. Toate articolele pe care le-am citit, manualele, profesioniştii care m-au învăţat. A fost totul greşit?

Se pare că am fost lipsește ceva critic.

Context.

Faptul că două părți sălbatice diferite ale sistemului efectua unele logica în același mod însemna mai puțin decât am crezut. Până când am scos acele biblioteci de cod comun, aceste părţi nu erau dependente una de cealaltă. Fiecare ar putea evolua independent. Fiecare şi-ar putea schimba logica în funcţie de nevoile mediului de afaceri în schimbare al sistemului. Aceste patru linii de cod similare au fost accidentale  Asta până am apărut eu.

Bibliotecile de cod comun am creat legat șireturile de fiecare picior unul de altul. Pași de un domeniu de afaceri nu ar putea fi făcute fără a sincroniza mai întâi cu celălalt. Costurile de întreținere în aceste funcții independente utilizate pentru a fi neglijabile, dar biblioteca comună a necesitat o ordine de magnitudine mai mult testare.

Deşi am redus numărul absolut de linii de cod din sistem, am crescut numărul de dependenţe. Contextul acestor dependențe este critic  Când aceste dependenţe nu sunt ţinute sub control, tendioanele lor încurcă preocupările mai mari ale sistemului chiar dacă codul în sine arată foarte bine.

Aceste greşeli sunt insidioase, în miezul lor, par o idee bună. Atunci când sunt aplicate în contextul potrivit, aceste tehnici sunt valoroase. În context greșit, acestea cresc costul mai degrabă decât valoarea. Când intru într-o bază de cod existentă fără să ştiu unde vor fi folosite diferitele părţi, sunt mult mai atent în aceste zile cu privire la ceea ce se împărtăşeşte.

Fereşte-te de partea ta. Verifică-ţi contextul. Numai atunci, continuă.

De[Udi Dahan](http://programmer.97things.oreilly.com/wiki/index.php/Udi_Dahan)