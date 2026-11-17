# Prevenirea erorilor

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_66_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_66_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 4:03)](../audio/thing_66_ro.mp3)

Mesajele de eroare sunt cele mai critice interacţiuni dintre utilizator şi restul sistemului. Acestea se întâmplă atunci când comunicarea dintre utilizator și sistem este aproape punctul de rupere.

Este ușor să te gândești la o eroare ca fiind cauzată de o intrare greșită de la utilizator. Dar oamenii fac greşeli în moduri previzibile şi sistematice. Deci este posibil să "depanați" comunicarea dintre utilizator și restul sistemului la fel cum ați face-o și între alte componente ale sistemului.

De exemplu, spuneți că doriți ca utilizatorul să introducă o dată într-un interval permis. În loc să lăsați utilizatorul să introducă orice dată, este mai bine să oferiți un dispozitiv, cum ar fi o listă sau un calendar care să arate doar datele permise. Acest lucru elimină orice șansă a utilizatorului de a intra o dată în afara intervalului.

Formatarea erorilor este o altă problemă comună. De exemplu, în cazul în care un utilizator este prezentat cu un câmp de text Data și intră într-o dată fără echivoc, cum ar fi "29 iulie 2012" este nerezonabil să-l respingem pur și simplu pentru că nu este într-un format preferat (cum ar fi "ZZ/LL/AAAAAA"). Este şi mai rău să respingem "29 / 07 / 2012" deoarece conţine spaţii suplimentare 

Această eroare apare pentru că este mai ușor să respingeți data decât parse cele trei sau patru formate cele mai frecvente date. Aceste tipuri de erori minore duc la frustrarea utilizatorilor, ceea ce la rândul său duce la erori suplimentare ca utilizatorul pierde concentrarea. În schimb, respectă preferinţa utilizatorilor de a introduce informaţii, nu date.

Un alt mod de a evita erorile de formatare este acela de a oferi indicii de exemplu, cu o etichetă în interiorul câmpului care să indice formatul dorit ("ZZ/LL/AAAAA"). Un alt tac ar putea fi de a împărți câmpul în trei cutii text de două, două, și patru caractere.

Indiciile sunt diferite de instrucţiuni: indiciile tind să fie indicii; instrucţiunile sunt verboase. Semnele apar la punctul de interacţiune; instrucţiunile apar înaintea punctului de interacţiune. Tacurile oferă context; instrucțiuni dictează utilizarea.

În general, instrucțiunile sunt ineficiente în prevenirea erorilor. Utilizatorii tind să presupună că interfețele vor funcționa în conformitate cu experiența lor anterioară ("Cu siguranță toată lumea știe ce înseamnă "29 iulie 2012"?"). Aşa că instrucţiunile nu se citesc. Îndepărtează utilizatorii de erori.

Un alt mod de a evita erorile este de a oferi implicit. De exemplu, utilizatorii introduc de obicei valori care corespund*Astăzi*,*mâine*,*Ziua mea*,*termenul meu limită*, sau*data la care am intrat ultima dată când am folosit acest formular*. În funcție de context, unul dintre acestea este probabil să fie o alegere bună ca un implicit inteligent.

Oricare ar fi cauza, sistemele ar trebui să fie tolerante la erori. Puteți face acest lucru prin furnizarea de mai multe niveluri de*Anulează*pentru toate acțiunile și în special acțiunile care au potențialul de a distruge sau modifica datele utilizatorilor.

Logging și analiză*Anulează*acțiunile pot evidenția, de asemenea, unde interfața atrage utilizatorii în erori inconștiente, cum ar fi click persistent pe butonul "greșit." Aceste erori sunt adesea cauzate de indicii înșelătoare sau secvențe de interacțiune pe care le puteți reproiecta pentru a preveni erori suplimentare.

Indiferent de abordarea pe care o luați, cele mai multe erori sunt sistematice  Înțelegerea modului în care utilizatorii gândesc, interpretează informații, iau decizii, și datele de intrare vă vor ajuta să depanați interacțiunile dintre software-ul dvs. și utilizatori.

de[Giles Colborne](http://programmer.97things.oreilly.com/wiki/index.php/Giles_Colborne)