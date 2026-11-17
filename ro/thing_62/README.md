# Numai codul spune adevărul

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_62_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_62_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:13)](../audio/thing_62_ro.mp3)

Semantica supremă a unui program este dată de codul de funcționare. Dacă acest lucru este doar în formă binară, va fi o lectură dificilă! Cu toate acestea, codul sursă ar trebui să fie disponibil dacă este programul dvs., orice dezvoltare tipică de software comercial, un proiect open source, sau cod într-un limbaj interpretat dinamic. Privind la codul sursă, sensul programului ar trebui să fie evident. Pentru a ști ce face un program, sursa este în cele din urmă tot ce puteți fi sigur de a privi la. Chiar și cele mai exacte cerințe documentul nu spune întregul adevăr: Nu conține povestea detaliată a ceea ce programul face de fapt, doar intențiile la nivel înalt ale analistului cerințelor. Un document de proiectare poate captura un proiect planificat, dar va lipsi detaliile necesare ale punerii în aplicare. Aceste documente s-ar putea să nu fie sincronizate cu implementarea curentă... sau s-ar putea să fi fost pierdute. Sau nu a scris în primul rând. Codul sursă poate fi singurul lucru rămas.

Cu acest lucru în minte, întrebați-vă cât de clar este codul vă spune sau orice alt programator ce face?

Ai putea spune, "Oh, comentariile mele îţi vor spune tot ce trebuie să ştii." Dar ţine minte că comentariile nu rulează codul. Ele pot fi la fel de greșite ca și alte forme de documentare. A existat o tradiţie spunând că comentariile sunt un lucru bun necondiţionat, deci fără îndoială unii programatori scriu din ce în ce mai multe comentarii, chiar repetând şi explicând trivia deja evidentă în cod. Acesta este un mod greșit de a clarifica codul. Dacă codul tău are nevoie de comentarii, ia în considerare refactoring-l astfel încât să nu. Comentariile lungi pot dezordona spaţiul ecranului şi pot fi chiar ascunse automat de IDE. Dacă aveți nevoie pentru a explica o schimbare, face acest lucru în versiunea sistem de control check-in mesaj și nu în cod.

Ce poţi face ca codul tău să spună adevărul cât mai clar posibil? Străduieşte-te pentru nume bune. Structurați codul în ceea ce privește funcționalitatea coezivă, care ușurează, de asemenea, numirea. Decuplează codul pentru a atinge ortogonia. Scrieți teste automate care explică comportamentul dorit și verificați interfețele. Refactor fără milă când înveţi să codifici o soluţie mai simplă şi mai bună. Face codul cât mai simplu posibil pentru a citi și înțelege.

Tratați codul ca orice altă compoziție, cum ar fi un poem, un eseu, un blog public, sau un e-mail important. Craft ceea ce exprima cu atenție, astfel încât să facă ceea ce ar trebui și comunică cât mai direct posibil ceea ce face, astfel încât încă comunică intenția ta atunci când nu mai sunt în jurul valorii de. Amintiți-vă că codul util este folosit mult mai mult decât a fost vreodată destinat. Programatorii de întreţinere vă vor mulţumi. Și, dacă sunteți programator de întreținere și codul la care lucrați nu spune adevărul cu ușurință, aplicați orientările de mai sus într-un mod proactiv. Stabileşte-ţi o minte sănătoasă în cod şi păstrează-ţi sănătatea mintală.

de[Peter Sommerlad](http://programmer.97things.oreilly.com/wiki/index.php/Peter_Sommerlad)