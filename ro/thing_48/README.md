# Marile date interconectate aparţin unei baze de date

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_48_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_48_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:50)](../audio/thing_48_ro.mp3)

În cazul în care aplicaţia dumneavoastră se va ocupa de un set mare, persistent, interconectat de elemente de date, nu ezitaţi să o stocaţi într-o bază de date relaţională. În trecut RDBMSs folosit pentru a fi scumpe, rare, complexe, și animale nefolositoare. Acest lucru nu mai este cazul. În prezent, sistemele RDBMS sunt ușor de găsit  Unele RDBMS foarte capabile, cum ar fi MySQL și PostgreSQL, sunt disponibile ca software open source, astfel încât costul de cumpărare nu mai este o problemă. Chiar mai bine, așa-numitele sisteme de baze de date integrate pot fi conectate ca biblioteci direct în aplicația dvs., care necesită aproape nici o configurare sau management  Aceste sisteme sunt extrem de eficiente.

Dacă datele aplicației dumneavoastră sunt mai mari decât RAM-ul sistemului, un tabel RDBMS indexat va efectua comenzi de magnitudine mai repede decât tipul de colectare a hărții bibliotecii, care va distruge paginile de memorie virtuale. Ofertele moderne de baze de date pot crește cu ușurință cu nevoile dumneavoastră. Cu grija adecvata, puteti urca o baza de date încorporata la un sistem de baze de date mai mare, atunci cand este necesar. Mai târziu, puteți trece de la o ofertă gratuită, open source la un sistem de proprietate mai bine susținut sau mai puternic.

Odată ce te agăți de SQL, scrierea de aplicații de bază de date-centric este o bucurie. După ce ați stocat datele normalizate în mod corespunzător în baza de date este ușor să extrageți fapte eficient cu o interogare SQL lizibilă; nu este nevoie să scrieți niciun cod complex. În mod similar, o singură comandă SQL poate efectua modificări complexe de date. Pentru modificări one-off, spuneți o schimbare în modul în care vă organizați datele persistente, nici măcar nu trebuie să scrieți codul: Doar porniți interfața SQL directă a bazei de date. Această aceeași interfață vă permite, de asemenea, să experimentați cu întrebări, sidestepting un ciclu regulat de programare a limbajului de operare.

Un alt avantaj al bazei de cod în jurul unui RDBMS implică manipularea relațiilor dintre elementele de date. Puteți descrie constrângerile de consistență asupra datelor într-un mod declarativ, evitând riscul indiciilor atârnatoare pe care le obțineți dacă uitați să actualizați datele într-un caz de margine. De exemplu, puteți specifica că, dacă un utilizator este șters, mesajele trimise de acel utilizator ar trebui eliminate și ele.

De asemenea, puteţi crea legături eficiente între entităţile stocate în baza de date oricând doriţi, prin crearea unui indice. Nu este nevoie să se efectueze refactorii costisitoare și extinse de domenii de clasă. În plus, codificarea în jurul unei baze de date permite mai multe aplicații pentru a accesa datele într-un mod sigur. Acest lucru face mai ușor pentru a actualiza aplicația pentru utilizare concomitentă și, de asemenea, pentru a coda fiecare parte a aplicației folosind cel mai adecvat limbaj și platforma. De exemplu, ai putea scrie back-end XML al unei aplicații web în Java, unele scripturi de audit în Ruby, și o interfață de vizualizare în[Prelucrarea](http://www.processing.org/).

În cele din urmă, țineți minte că RDBMS va transpira greu pentru a optimiza comenzile SQL, permițându-vă să se concentreze pe funcționalitatea aplicației dumneavoastră mai degrabă decât pe tuning algoritmic. Sistemele avansate de baze de date vor profita chiar și de procesoare multicore pe la spatele tău. Şi, pe măsură ce tehnologia se îmbunătăţeşte, la fel va fi şi performanţa aplicaţiei tale.

De[Diomidis Spinellis](http://programmer.97things.oreilly.com/wiki/index.php/Diomidis_Spinellis)