# Să păstrăm clădirea curată

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_42_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_42_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:06)](../audio/thing_42_ro.mp3)

V-ați uitat vreodată la o listă de avertismente compilator durata unui eseu privind codarea proastă și v-ați gândit: "Știți, eu chiar ar trebui să fac ceva despre asta... dar nu am timp acum?" Pe de altă parte, te-ai uitat vreodată la un avertisment singuratic care tocmai a apărut într-o compilație și tocmai a reparat-o?

Când încep un nou proiect de la zero, nu există avertismente, nici dezordine, nici probleme. Dar pe măsură ce baza de cod creşte, dacă nu sunt atent, dezordinea, crucişătura, avertismentele şi problemele pot începe să se adune. Când e mult zgomot, e mult mai greu să găseşti avertismentul că vreau să citesc printre sutele de avertismente de care nu-mi pasă.

Pentru a face avertismentele utile din nou, încerc să folosesc o politică de toleranţă zero pentru avertismentele din clădire. Chiar dacă avertismentul nu este important, mă ocup de el. Dacă nu critic, dar încă relevant, am repara. Dacă compilatorul avertizează cu privire la o posibilă excepție nul-pointer, am repara cauza  În cazul în care documentația încorporată (Javadoc sau similar) se referă la parametrii care au fost eliminați sau renumiți, am curăța documentația.

Dacă e ceva de care chiar nu-mi pasă şi asta nu contează, întreb echipa dacă putem schimba politica noastră de avertizare. De exemplu, mi se pare că documentarea parametrilor și valoarea de returnare a unei metode în multe cazuri nu adaugă nici o valoare, așa că nu ar trebui să fie un avertisment dacă acestea lipsesc. Sau, actualizarea la o nouă versiune a limbajului de programare poate face cod care a fost anterior OK emite acum avertismente. De exemplu, când Java 5 a introdus generice, toate codurile vechi care nu au specificat parametrul generic de tip ar da un avertisment. Acesta este un fel de avertisment pe care nu vreau să-l dau în bară (cel puţin, nu încă). Având un set de avertismente care sunt depasite de realitate nu serveşte nimănui.

Asigurându-mă că clădirea este întotdeauna curată, nu va trebui să decid că un avertisment este irelevant de fiecare dată când îl întâlnesc. Ignorarea lucrurilor este muncă mentală şi trebuie să scap de toată munca mentală inutilă pe care o pot face. Având o clădire curată, de asemenea, face mai ușor pentru altcineva să preia munca mea. Dacă las avertismentele, altcineva va trebui să treacă prin ce e relevant şi ce nu. Sau mai probabil, ignoraţi toate avertismentele, inclusiv cele semnificative.

Avertismentele din clădirea ta sunt utile. Trebuie doar să scapi de zgomot ca să le observi. Nu aştepta o curăţenie mare. Când apare ceva ce nu vrei să vezi, rezolvă imediat. Fixaţi sursa avertismentului, suprimaţi acest avertisment sau fixaţi politicile de avertizare ale instrumentului dumneavoastră. Păstrarea clădirii curate nu este vorba doar despre păstrarea fără erori de compilare sau eșecuri de testare: De asemenea, avertismentele reprezintă o parte importantă și critică a igienei codului.

De[Johannes Brodwall](http://programmer.97things.oreilly.com/wiki/index.php/Johannes_Brodwall)