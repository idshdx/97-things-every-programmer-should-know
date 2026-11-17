# Mesajul duce la o mai bună scalabilitate în sistemele paralele

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_57_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_57_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:12)](../audio/thing_57_ro.mp3)

Programatorii sunt învățați încă de la început de studiu lor de calcul care con și în special paralelism, un subset special de con  Există un accent invariabil mare pe fire, semafore, monitoare, și cât de greu este de a obține acces concomitent la variabile pentru a fi de siguranță.

Este adevărat, există multe probleme dificile şi ele pot fi foarte greu de rezolvat. Dar care este rădăcina problemei? Memorie comună. Aproape toate problemele de convailizare pe care oamenii merg mai departe și mai departe despre se referă la utilizarea memoriei mobile comune: condițiile de rasă, impas, blocaj, etc. Răspunsul pare evident: fie să renunţi la bani fie să împarţi memoria!

Excluderea monedei nu este cu siguranţă o opţiune. Calculatoarele au din ce în ce mai multe nuclee aproape trimestrial, astfel încât valorificarea paralelismului adevărat devine din ce în ce mai importantă. Nu ne mai putem baza pe creșterea vitezei ceasului procesorului pentru a îmbunătăți performanța aplicației. Doar prin exploatarea paralelismului se va îmbunătăți performanța aplicațiilor. Evident, neîmbunătățirea performanței este o opțiune, dar este puțin probabil să fie acceptabilă pentru utilizatori.

Deci, putem eschew memorie comună? Categoric.

În loc să folosim fire și memorie comună ca model de programare, putem folosi procesele și mesajele care trec. Proces aici înseamnă doar un stat independent protejat cu codul de executare, nu neapărat un proces de sistem de operare. Limbi precum Erlang (şi occam înaintea lui) au arătat că procesele sunt un mecanism de succes pentru programarea sistemelor simultane şi paralele. Astfel de sisteme nu au toate tensiunile de sincronizare pe care le au memorie comună, sisteme cu mai multe fire. Mai mult decât atât, există un model formal 

Putem merge mai departe și introduce sisteme de flux de date ca un mod de calcul. Într-un sistem de flux de date nu există un flux de control programat în mod explicit. În schimb, un grafic direcţionat al operatorilor, conectat prin căi de date, este configurat şi apoi furnizat în sistem. Evaluarea este controlată de disponibilitatea datelor din cadrul sistemului. Cu siguranţă nu sunt probleme de sincronizare.

Acestea fiind spuse, limbi precum C, C++, Java, Python și Groovy sunt principalele limbi ale dezvoltării sistemelor și toate acestea sunt prezentate programatorilor ca limbi pentru dezvoltarea memoriei partajate, sisteme cu mai multe fire. Deci, ce se poate face? Răspunsul este de a utiliza 

Toate în toate, nu programare cu memorie comună, dar în schimb folosind mesaje care trec, este probabil să fie cel mai de succes mod de implementare a sistemelor care exploatează paralelismul care este acum endemic în hardware-ul computerului. Bizar probabil, deşi procesele preced fire ca unitate de convalescenţă, viitorul pare să fie în utilizarea firelor pentru implementarea proceselor.

De[Russel Winder](http://programmer.97things.oreilly.com/wiki/index.php/Russel_Winder)