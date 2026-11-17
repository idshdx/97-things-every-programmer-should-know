# Încapsularea comportamentului, nu doar stat

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_32_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_32_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:23)](../audio/thing_32_ro.mp3)

În teoria sistemelor, izolarea este una dintre cele mai utile construcţii atunci când se ocupă cu structuri de sistem mari şi complexe. În industria de software valoarea de izolare sau încapsulare este bine înțeles. Containere este susținută de construirea limbajului de programare, cum ar fi subrutine și funcții, module și pachete, clase și așa mai departe.

Modulele și pachetele abordează nevoile la scară mai mare pentru încapsulare, în timp ce clasele, subrutinele și funcțiile abordează aspectele mai bine înrădăcinate ale problemei. De-a lungul anilor am descoperit că clasele par a fi unul dintre cele mai grele construcţii de încapsulare pentru dezvoltatori pentru a obţine dreptul. Nu este neobişnuit să găseşti o clasă cu o singură metodă principală de 3000 de linii, sau o clasă cu numai*set*şi*Ia*metode pentru atributele sale primitive. Aceste exemple demonstrează că dezvoltatorii implicați nu au înțeles pe deplin gândirea orientată spre obiecte, nereușind să profite de puterea obiectelor ca construcții de modelare. Pentru dezvoltatorii familiarizați cu termenii Pojo (Plain Old Java Object) și POCO (Plain Old C# Object sau Plain Old CLR Object), aceasta a fost intenția de a merge înapoi la elementele de bază ale OO ca o paradigmă de modelare 

Un obiect încapsulază atât starea cât şi comportamentul, unde comportamentul este definit de starea actuală. Gândeşte-te la un obiect de uşă. Are patru state: închis, deschis, închis, deschis, deschis. Acesta oferă două operațiuni: deschis și aproape. În funcție de stat, operațiunile deschise și strânse se vor comporta diferit. Această proprietate inerentă a unui obiect face ca procesul de proiectare să fie conceptual simplu. Se reduce la două sarcini simple: alocarea și delegarea responsabilității diferitelor obiecte, inclusiv protocoalele de interacțiune inter-obiect.

Modul în care funcționează în practică este ilustrat cel mai bine cu un exemplu. Să spunem că avem trei clase: Client, ordine, și articol. Un obiect al clientului este posesorul natural al limitei de credit și al normelor de validare a creditului. Un obiect Order ştie despre clientul său asociat, iar operaţiunea addItem deleagă verificarea reală a creditului prin apelare`customer.validateCredit(item.price())`. În cazul în care condiţia post-metodă eşuează, o excepţie poate fi aruncată şi achiziţia anulată.

Dezvoltatorii mai puțin experimentați orientate la obiecte ar putea decide să încheie toate regulile de afaceri într-un obiect foarte des menționat ca`OrderManager`sau`OrderService`În aceste desene,`Order`,`Customer`, și`Item`sunt tratate ca puțin mai mult decât tipuri de înregistrări. Toate logica este factorată din clase și legat împreună într-o mare, metodă procedurală cu o mulțime de interior*dacă-atunci-altele*constructii. Aceste metode sunt ușor de rupt și sunt aproape imposibil de menținut. Motivul? Încapsularea este ruptă.

Deci, în cele din urmă, nu rupe încapsularea, și de a folosi puterea limbajului de programare pentru a-l menține.

De[Einar Landre](http://programmer.97things.oreilly.com/wiki/index.php/Einar_Landre)