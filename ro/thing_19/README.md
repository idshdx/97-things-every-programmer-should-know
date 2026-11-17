# Convenie Nu este o -ilitate

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_19_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_19_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:27)](../audio/thing_19_ro.mp3)

S-au spus multe despre importanţa şi provocările conceperii de bune API. E greu să îndrepţi lucrurile de prima dată şi e şi mai greu să te schimbi mai târziu. Ca şi cum ai creşte copii. Majoritatea programatorilor experimentaţi au învăţat că un bun API urmează un nivel consistent de abstractizare, prezintă consistenţă şi simetrie şi formează vocabularul pentru un limbaj expresiv. Din păcate, faptul de a fi conştient de principiile directoare nu se traduce automat în comportamentul adecvat. Să mănânci dulciuri îţi face rău.

În loc să predic de sus, vreau să aleg o anumită strategie API, una pe care o întâlnesc de nenumărate ori: argumentul convenienţei. Acesta începe de obicei cu una dintre următoarele "vizore:"

- Nu vreau ca alte clase să trebuiască să dea două telefoane separate pentru a face asta.
- De ce ar trebui să fac o altă metodă dacă este aproape la fel ca această metodă? Voi adăuga doar un comutator simplu.
- A se vedea, este foarte ușor: Dacă al doilea parametru de șir se termină cu ".txt," metoda presupune automat că primul parametru este un nume de fișier, așa că nu am nevoie de două metode.

Deși bine intenționate, astfel de argumente sunt predispuse să reducă lizibilitatea codului folosind API. O metodă de invocare ca

```
parser.processNodes(text, false);
```

este practic lipsit de sens fără a cunoaște implementarea sau cel puțin consultarea documentației. Această metodă a fost probabil conceput pentru confortul de implementator, spre deosebire de confortul apelantului  Nu e nimic în neregulă cu confortul dacă este destinat să fie antidotul la plictiseală, clincuri, sau jenă. Totuşi, dacă ne gândim mai atent la acest lucru, antidotul pentru aceste simptome este eficienţa, consistenţa şi eleganţa, nu neapărat comoditatea. API ar trebui să ascundă complexitatea de bază, astfel încât să ne putem aștepta în mod realist design API bun pentru a necesita un efort. O singură metodă mare ar putea fi cu siguranță mai convenabil de a scrie decât un set bine gândit-out de operațiuni, dar ar fi mai ușor de utilizat?

Metafora API ca limbă ne poate ghida spre decizii de proiectare mai bune în aceste situații. Un API ar trebui să ofere un limbaj expresiv, care oferă următorul strat de mai sus suficient vocabular pentru a pune și răspunde la întrebări utile. Acest lucru nu înseamnă că ar trebui să ofere exact o metodă, sau verb, pentru fiecare întrebare care ar putea fi în valoare de a cere. Un vocabular divers ne permite să exprimăm subtilități în sens. De exemplu, preferăm să spunem alerga în loc de mers (adevărat), chiar dacă ar putea fi privit ca în esență aceeași operațiune, doar executat la viteze diferite. Un vocabular API coerent și bine gândit face expresiv și ușor de înțeles codul în următorul strat în sus. Mai important, un vocabular composabil permite altor programatori să utilizeze API în moduri în care este posibil să nu fi anticipat  Data viitoare când eşti tentat să legi câteva lucruri într-o singură metodă API, aminteşte-ţi că limba engleză nu are un singur cuvânt pentru`MakeUpYourRoomBeQuietAndDoYourHomeWork`, chiar dacă ar părea într-adevăr convenabil pentru o astfel de operațiune solicitată frecvent.

De[Gregor Hohpe](http://programmer.97things.oreilly.com/wiki/index.php/Gregor_Hohpe)