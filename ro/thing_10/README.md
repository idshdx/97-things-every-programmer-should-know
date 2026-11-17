# Alegeţi - vă uneltele cu grijă

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_10_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_10_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:49)](../audio/thing_10_ro.mp3)

Aplicațiile moderne sunt foarte rar construite de la zero. Acestea sunt asamblate cu ajutorul instrumentelor existente 

- Aplicaţiile cresc în mărime, complexitate şi sofisticare, în timp ce timpul disponibil pentru a le dezvolta creşte mai scurt. Aceasta utilizează mai bine timpul și inteligența dezvoltatorilor dacă se pot concentra pe scrierea mai multor coduri de afaceri-domeniu și pe mai puține coduri de infrastructură.

- Componentele și cadrele utilizate pe scară largă sunt susceptibile de a avea mai puține microfoane decât cele dezvoltate intern.

- Există o mulțime de software de înaltă calitate disponibile pe internet gratuit, ceea ce înseamnă costuri de dezvoltare mai mici și o probabilitate mai mare de a găsi dezvoltatori cu interesul și expertiza necesare.

- Productia si intretinerea software-ului este o munca intensa, deci cumpararea poate fi mai ieftina decat constructia.

Cu toate acestea, alegerea mixului potrivit de instrumente pentru aplicația dumneavoastră poate fi o afacere complicată care necesită un gând. De fapt, când faci o alegere, sunt câteva lucruri pe care ar trebui să le ţii minte:

- Diferitele instrumente se pot baza pe ipoteze diferite cu privire la contextul lor  O astfel de neconcordanță duce la hacks și workarounds care va face codul mai complex decât este necesar.

- Diferite instrumente au diferite cicluri de viață, și modernizarea unul dintre ele poate deveni o sarcină extrem de dificilă și consumatoare de timp, deoarece noile funcționalități, modificări de proiectare, sau chiar soluții bug-uri pot provoca incompatibilități cu celelalte instrumente. Cu cât numărul de instrumente este mai mare, cu atât problema poate deveni mai gravă.

- Unele instrumente necesită destul de un pic de configurare, adesea prin intermediul unuia sau mai multor fișiere XML, care pot crește de sub control foarte repede. Aplicația poate ajunge să arate ca și cum totul a fost scris în XML plus câteva linii ciudate de cod în unele limbaj de programare. Complexitatea configurațională va îngreuna menținerea și extinderea aplicației.

- Vânzătorul de blocare-in apare atunci când codul care depinde foarte mult de produse specifice vânzătorului sfârșește prin a fi constrâns de ei pe mai multe capete de acuzare: întreținere, performanțe, capacitatea de a evolua, preț, etc.

- Dacă intenționați să utilizați software-ul gratuit, ați putea descoperi că nu este atât de gratuit, după toate. S-ar putea să fie nevoie să cumpăraţi suport comercial, care nu va fi neapărat ieftin.

- Termenii de acordare a licențelor contează, chiar și pentru software-ul gratuit. De exemplu, în unele companii nu este acceptabil să se utilizeze software-ul licenţiat în condiţiile de licenţă GNU datorită naturii sale virale, adică software-ul dezvoltat cu acesta trebuie distribuit împreună cu codul său sursă.

Strategia mea personală de atenuare a acestor probleme este de a începe de mici, folosind doar instrumentele care sunt absolut necesare. De obicei, accentul inițial se pune pe eliminarea nevoii de a se angaja în programarea infrastructurii la nivel scăzut (și probleme), de exemplu, prin utilizarea unor aparate de mijloc în loc să utilizeze prize brute pentru aplicații distribuite. Și apoi adăugați mai mult, dacă este necesar. De asemenea, am tendința de a izola instrumentele externe de la obiectele mele de domeniu de afaceri prin intermediul interfețelor și stratificare, astfel încât să pot schimba instrumentul dacă trebuie să cu doar o cantitate mică de durere. Un efect secundar pozitiv al acestei abordări este că, în general, sfârşesc cu o aplicaţie mai mică care utilizează mai puţine instrumente externe decât prognoza iniţială.

De[Giovanni Asproni](http://programmer.97things.oreilly.com/wiki/index.php/Giovanni_Asproni)