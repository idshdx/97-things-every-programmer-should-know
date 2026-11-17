# Automatizează standardul de codificare

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_04_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_04_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:33)](../audio/thing_04_ro.mp3)

Probabil ai fost şi tu acolo. La începutul unui proiect, toată lumea are multe intenţii bune. Foarte des, multe dintre aceste rezoluţii sunt scrise în documente. Cele despre cod ajung în standardul de codificare al proiectului. În timpul reuniunii de lansare, dezvoltatorul principal trece prin document și, în cel mai bun caz, toată lumea este de acord că vor încerca să le urmeze. Odată ce proiectul începe, însă, aceste bune intenţii sunt abandonate, pe rând. Când proiectul este livrat în cele din urmă codul arată ca o mizerie, și nimeni nu pare să știe cum a ajuns să fie în acest fel.

Când au mers lucrurile prost? Probabil deja la întâlnirea de început. Unii dintre membrii proiectului nu au fost atenţi. Alţii n-au înţeles ideea. Mai rău, unii nu au fost de acord și au fost deja de planificare rebeliunea lor standard de codificare. În cele din urmă, unii au înţeles şi au fost de acord, dar când presiunea din proiect a crescut prea mult, au trebuit să renunţe la ceva. Codul bine formatat nu vă câştigă puncte cu un client care vrea mai multă funcţionalitate. În plus, respectarea unui standard de codificare poate fi o sarcină destul de plictisitoare dacă nu este automată. Încearcă să identifici o clasă murdară cu mâna pentru a afla singur.

Dar dacă este o astfel de problemă, de ce este că vrem să avem un standard de codificare în primul rând? Un motiv pentru a forma codul într-un mod uniform este ca nimeni să nu poată "propria" o bucată de cod doar prin formatarea acestuia în felul său privat. S-ar putea dori să prevină dezvoltatorii folosind anumite anti-patterne, pentru a evita unele bug-uri comune. În total, un standard de codificare ar trebui să faciliteze lucrul în proiect și să mențină viteza de dezvoltare de la început până la sfârșit. Apoi, rezultă că toată lumea ar trebui să fie de acord cu privire la standardul de codificare prea 

Există o mulțime de instrumente care pot fi folosite pentru a produce rapoarte de calitate cod și pentru a documenta și menține standardul de codificare, dar care nu este întreaga soluție. Aceasta ar trebui să fie automatizată și aplicată acolo unde este posibil. Iată câteva exemple:

- Asigurați-vă că formatul de cod face parte din procesul de construire, astfel încât toată lumea îl rulează automat de fiecare dată când compila codul.
- Utilizați instrumente de analiză a codului static pentru a scana codul pentru anti-patterne nedorite. Dacă sunt găsite, spargeţi clădirea.
- Învățați să configurați aceste instrumente astfel încât să puteți scana pentru propriile dvs. anti-modele specifice proiectului.
- Nu numai că măsurați acoperirea încercării, dar verificați și rezultatele automat. Din nou, rupeți clădirea dacă acoperirea testului este prea scăzută.

Încearcă să faci asta pentru tot ce consideri important. Nu vei putea automatiza tot ce-ţi pasă cu adevărat. În ceea ce priveşte lucrurile pe care nu le puteţi fixa automat, consideraţi-le un set de orientări suplimentare la standardul de codificare care este automatizat, dar acceptaţi că dvs. şi colegii dvs. nu le puteţi urmări ca cu sârguinţă.

În cele din urmă, standardul de codificare ar trebui să fie mai degrabă dinamic decât static. Pe măsură ce proiectul evoluează, nevoile proiectului se schimbă, și ceea ce poate părea inteligent la început, nu este neapărat inteligent câteva luni mai târziu.

De[Filip van Laenen](http://programmer.97things.oreilly.com/wiki/index.php/Filip_van_Laenen)