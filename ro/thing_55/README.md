# Usor de folosit corect si greu de folosit corect

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_55_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_55_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:25)](../audio/thing_55_ro.mp3)

Una dintre cele mai frecvente sarcini în dezvoltarea software-ului este specificațiile de interfață. Interfețele au loc la cel mai înalt nivel de abstractizare (interfețele utilizatorului), la cele mai mici (interfețele funcționale) și la nivelurile dintre (interfețele de clasă, interfețele bibliotecii etc.). Indiferent dacă lucrați cu utilizatorii finali pentru a specifica modul în care aceștia vor interacționa cu un sistem, colaborați cu dezvoltatorii pentru a specifica un API sau declara funcții private unei clase, proiectarea interfeței este o parte importantă a jobului dumneavoastră. Dacă o faci bine, interfețele tale vor fi o plăcere de a utiliza și va stimula productivitatea altora. Dacă o faci prost, interfețele tale vor fi o sursă de frustrare și erori.

Interfețele bune sunt:

- **Ușor de utilizat corect.**Oamenii care folosesc o interfaţă bine proiectată folosesc aproape întotdeauna interfaţa corect, pentru că aceasta este calea rezistenţei minime. Într-un GUI, ei aproape întotdeauna faceți clic pe pictograma dreapta, buton, sau meniu de intrare, pentru că este evident și lucru ușor de făcut. Într-un API, ei aproape întotdeauna trec parametrii corect cu valorile corecte, pentru că asta e ceea ce este cel mai natural. Cu interfețe care sunt ușor de utilizat corect,*Lucrurile funcţionează.*
- **Greu de utilizat incorect.**Interfețele bune anticipa greșelile pe care oamenii le-ar putea face și le face dificil  Un GUI ar putea dezactiva sau elimina comenzile care nu au nici un sens în contextul actual, de exemplu, sau un API ar putea elimina problemele de argument-ordonare, permițând parametrii să fie trecut în orice ordine.

O modalitate bună de a proiecta interfețele care sunt ușor de utilizat corect este de a le exercita înainte de a exista. Mock up a GUI  Scrie apeluri către un API înainte ca funcţiile să fie declarate. Mergi prin cazuri de utilizare comune și specifică modul în care*Vreau*interfața să se comporte. Ce faci?*Vreau*pentru a putea face clic pe? Ce faci?*Vreau*Pentru a putea trece? Ușor de utilizat interfețele par naturale, pentru că te lasă să faci ceea ce vrei să faci. Sunteți mai probabil să vină cu astfel de interfețe dacă le dezvoltați din punctul de vedere al unui utilizator. (Această perspectivă este unul dintre punctele forte ale primei programări de testare.)

A face interfețe greu de utilizat incorect necesită două lucruri. În primul rând, trebuie să anticipați erorile pe care utilizatorii le-ar putea face și să găsiți modalități de a le preveni. În al doilea rând, trebuie să observaţi modul în care o interfaţă este folosit greşit în timpul degajării timpurii şi de a modifica interfaţa da, modificaţi interfaţa! Cel mai bun mod de a preveni utilizarea incorectă este de a face imposibilă o astfel de utilizare. Dacă utilizatorii doresc să anuleze o acțiune irevocabilă, încercați să faceți acțiunea relocabilă. În cazul în care acestea păstrează trecerea valorii greșite la un API, faceți tot posibilul pentru a modifica API pentru a lua valorile pe care utilizatorii doresc să treacă.

Mai presus de toate, amintiţi-vă că există interfeţe pentru confortul utilizatorilor lor, nu pentru implementatorii lor.

De[Scott Meyers](http://programmer.97things.oreilly.com/wiki/index.php/Scott_Meyers)