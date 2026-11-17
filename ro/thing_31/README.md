# Nu atinge acel cod!

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_31_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_31_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 2:45)](../audio/thing_31_ro.mp3)

La un moment dat ni s-a întâmplat tuturor. Codul dvs. a fost rulat pe serverul de montare pentru testarea sistemului și managerul de testare scrie înapoi că ea a lovit o problemă. Prima ta reacţie este: "Repede, lasă-mă să repar asta."

În sens mai larg, totuși, ceea ce este greșit este că ca un dezvoltator crezi că ar trebui să aibă acces la serverul de așteptare.

În majoritatea mediilor de dezvoltare bazate pe web arhitectura poate fi împărţită astfel:

- Dezvoltarea locală și testarea unității pe mașina dezvoltatorului
- Server de dezvoltare în cazul în care se efectuează testarea automată sau manuală a integrării
- Server de stocare în cazul în care echipa QA și utilizatorii fac testarea de acceptare
- Server de producție

Da, există alte servere și servicii stropite acolo, cum ar fi controlul codului sursă și ticketing, dar ai prins ideea. Folosind acest model, un dezvoltator  Cea mai mare dezvoltare se face pe mașina locală a unui dezvoltator folosind amestecul lor preferat de IDE-uri, mașini virtuale, și o cantitate adecvată de magie neagră stropit peste ea pentru noroc.

După ce a fost verificat în SCC, fie automat sau manual, acesta ar trebui să fie rulat pe serverul de dezvoltare în cazul în care acesta poate fi testat și optimizat, dacă este necesar, pentru a vă asigura că totul funcționează împreună. Din acest moment însă, dezvoltatorul este un spectator al procesului.

Managerul de pregătire trebuie să împacheteze și să ruleze codul pe serverul de pregătire pentru echipa QA. La fel ca dezvoltatorii nu ar trebui să aibă acces la nimic dincolo de serverul de dezvoltare, echipa QA și utilizatorii nu au nevoie să atingă nimic pe serverul de dezvoltare. Dacă este gata pentru testare de acceptare, taie o versiune și rola, nu cere utilizatorului să "Uită-te la ceva foarte rapid" pe serverul de dezvoltare. Amintiți-vă, dacă nu sunteți codificarea proiectului de unul singur, alte persoane au cod acolo și acestea nu pot fi gata pentru utilizator să-l vadă. Managerul de lansare este singura persoană care ar trebui să aibă acces la ambele.

În nici un caz, în nici un caz, în cazul în care un dezvoltator au acces la un server de producție. Dacă există o problemă, personalul de sprijin ar trebui fie să-l repara sau să ceară să-l reparați. După aceea
Verificat în SCC vor rula un plasture de acolo. Unele dintre cele mai mari dezastre de programare am fost o parte din au avut loc pentru că cineva**tuse*\*Eu...**tuse**a încălcat ultima regulă. Dacă e stricată, producţia nu e locul potrivit să o repari.

de[Cal Evans](http://programmer.97things.oreilly.com/wiki/index.php/Cal_Evans)