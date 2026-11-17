# Ia avantajul instrumentelor de analiză cod

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_79_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_79_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:29)](../audio/thing_79_ro.mp3)

Valoarea testelor este ceva ce este introdus în dezvoltatorii de software din etapele incipiente ale călătoriei lor de programare. În ultimii ani, creșterea testării unitare, a dezvoltării bazate pe teste și a metodelor agile a cunoscut un val de interes în a face din plin testele pe parcursul tuturor fazelor ciclului de dezvoltare. Cu toate acestea, testarea este doar unul dintre multele instrumente pe care le puteți folosi pentru a îmbunătăți calitatea codului.

În trecut, când C era încă un fenomen nou, timpul procesorului şi stocarea de orice fel erau la un nivel premium. Primii compilatori C au fost atenți la acest lucru și au redus astfel numărul de treceri prin codul pe care l-au făcut prin eliminarea unor analize semantice. Acest lucru a însemnat că compilatorul a verificat doar un subset mic de bug-uri care ar putea fi detectate la momentul compilării. Pentru a compensa, Stephen Johnson a scris un instrument numit*scame*Cu toate acestea, instrumentele de analiză statică au dobândit reputaţia de a da un număr mare de avertismente şi avertismente false pozitive despre convenţiile stilistice care nu sunt întotdeauna necesare pentru a le urma.

Peisajul actual al limbilor, compilatorilor și instrumentelor de analiză statică este foarte diferit. Memoria și timpul procesorului sunt acum relativ ieftine, astfel încât compilatorii își pot permite să verifice pentru mai multe erori. Aproape fiecare limbă se mândrește cu cel puțin un instrument care verifică încălcări ale ghidurilor de stil, gotchas comune, și, uneori, erori viclene care pot fi dificil de prins, cum ar fi potențialele dereferințe pointer nul. Instrumente mai sofisticate, cum ar fi Atelă pentru C sau Pylint pentru Python, sunt configurabile, ceea ce înseamnă că puteți alege care erori și avertizează instrumentul emite cu un fișier de configurare, prin comutatoare linie de comandă, sau în IDE. Atelă vă va permite chiar să adnotați codul dvs. în comentarii pentru a da indicii mai bune despre modul în care funcționează programul.

În cazul în care toate celelalte eșuează, și te găsești în căutarea pentru bug-uri simple sau încălcări ale standardelor care nu sunt capturate de compilator, IDE, sau instrumente scame, atunci puteți rula întotdeauna propriul checker static. Acest lucru nu este la fel de dificil cum ar putea suna. Majoritatea limbilor, în special cele marcate*dinamic*, expune lor sintetic abstract și instrumente compilator ca parte a bibliotecii standard. Merită să cunoașteți colțurile prăfuite ale bibliotecilor standard care sunt folosite de echipa de dezvoltare a limbii pe care o utilizați, deoarece acestea conțin adesea pietre ascunse care sunt utile pentru analiza statică și testarea dinamică. De exemplu, biblioteca standard Python conține un demontor care vă spune bytecode folosit pentru a genera un cod compilat sau obiect de cod. Sună ca un instrument obscur pentru scriitorii compilatorilor din echipa Python-dev, dar este surprinzător de util în situaţiile de zi cu zi. Un lucru această bibliotecă poate dezasambla este ultima ta urmă stiva, oferindu-vă feedback cu privire la exact care instrucțiuni octecod aruncat ultima excepție neprinsă.

Deci, nu lăsa testarea să fie sfârșitul de asigurare a calității dumneavoastră 

De[Sarah Mount](http://programmer.97things.oreilly.com/wiki/index.php/Sarah_Mount)