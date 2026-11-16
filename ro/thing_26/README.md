# Nu ignora această eroare!

> *Intr-o seara mergeam pe strada sa ma intalnesc cu niste prieteni intr-un bar. N-am mai băut o bere de ceva vreme şi abia aşteptam să-i văd din nou. În grabă, nu mă uitam pe unde merg. M-am împiedicat de marginea unei borduri şi am ajuns pe faţa mea. Mă ajută să nu fiu atent.*

> *M-a durut piciorul, dar mă grăbeam să-mi întâlnesc prietenii. Aşa că m-am ridicat şi am continuat. Pe măsură ce mergeam mai departe, durerea se înrăutăţea. Deşi l-am respins iniţial ca şoc, mi-am dat seama rapid că ceva nu e în regulă.*

> *Dar m-am grăbit la bar, indiferent. Eram în agonie când am ajuns. N-am avut o noapte grozavă în oraş, pentru că eram foarte distras. Dimineaţa m-am dus la doctor şi am aflat că mi-am fracturat osul. Dacă m-aş fi oprit când am simţit durerea, aş fi prevenit multe daune în plus pe care le-am cauzat mergând pe ea. Probabil cea mai rea dimineaţă după viaţa mea.*

Prea mulţi programatori scriu un cod ca noaptea mea dezastruoasă.

*Eroare, ce eroare? Nu va fi grav. Sincer. O pot ignora.*Aceasta nu este o strategie câștigătoare pentru cod solid. De fapt, e doar lene. Nu e genul potrivit. Indiferent cât de puțin probabil credeți că o eroare este în codul dvs., ar trebui să verificați întotdeauna pentru ea, și să se ocupe întotdeauna. De fiecare dată. Nu economiseşti timp dacă nu: Tu stochezi potenţiale probleme pentru viitor.

Raportăm erori în codul nostru în mai multe moduri, inclusiv:

- **Coduri de returnare**poate fi folosit ca valoarea rezultată a unei funcții pentru a însemna "nu a funcționat." Codurile de returnare a erorilor sunt mult prea ușor de ignorat. Nu vei vedea nimic în cod pentru a sublinia problema. Într-adevăr, a devenit o practică standard să ignori valorile de întoarcere ale unor funcţii standard C. Cât de des verifici valoarea returnării de pe printf?

- **erno**este o aberație C curios, o variabilă globală separată setat pentru a semnala eroare. Este ușor de ignorat, greu de utilizat, și duce la tot felul de probleme urâte  Unele platforme te izolează de durere aici; altele nu.

- **Excepții**sunt un mod mai structurat de semnalizare și de manipulare a erorilor, susținut de limbaj. Şi nu le poţi ignora. Sau poţi? Am văzut multe coduri ca asta:

```
try {
    // ...do something...
}
catch (...) {} // ignore errors
```

Graţia salvatoare a acestei construcţii îngrozitoare este că scoate în evidenţă faptul că faci ceva dubios din punct de vedere moral.

Dacă ignori o greşeală, închizi ochii şi te prefaci că nu s-a întâmplat nimic, îţi asumi mari riscuri. La fel cum piciorul meu a ajuns într-o stare mai rea decât dacă nu m-aş mai plimba pe el imediat, aratându-mă pe el indiferent de ce ar putea duce la eşecuri foarte complexe. Rezolvă problemele cât mai repede posibil. Păstrează un cont scurt.

Negestionarea erorilor duce la:

- **Codul Brittle.**Cod care e plin de gândaci excitanţi şi greu de găsit.
- **Cod nesigur.**Crackers exploateaza adesea manipularea slaba a erorilor pentru a sparge sistemele software.
- **Structură slabă.**Dacă există erori din codul tău care sunt plictisitoare pentru a face față continuu, probabil că ai o interfață slabă. Exprimă-l astfel încât erorile sunt mai puțin intruzive și manipularea lor este mai puțin oneroasă.

Așa cum ar trebui să verificați toate erorile potențiale din codul dumneavoastră, aveți nevoie pentru a expune toate condițiile potențial eronate în interfețele dumneavoastră. Nu le ascunde, pretinzând că serviciile tale vor funcţiona întotdeauna.

De ce nu verificăm erorile? Există o serie de scuze comune. Cu care dintre acestea eşti de acord? Cum le-ai contracara pe toate?

- Eroare de manipulare dezordine până fluxul de cod, ceea ce face mai greu de citit, și mai greu de reperat fluxul "normal" de execuție.
- E muncă suplimentară şi am un termen limită.
- Știu că acest apel funcție va*Niciodată.*returnaţi o eroare (printf funcţionează întotdeauna, malloc întotdeauna întoarce memorie nouă 
- Este doar un program de jucărie, și nu trebuie să fie scris la un nivel de producție demn.

De[Pete Goodliffe](http://programmer.97things.oreilly.com/wiki/index.php/Pete_Goodliffe)
