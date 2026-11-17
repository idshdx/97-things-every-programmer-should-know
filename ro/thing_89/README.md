# Utilizați algoritmul și structura de date corespunzătoare

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_89_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_89_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:53)](../audio/thing_89_ro.mp3)

> O bancă mare cu multe filiale s - a plâns că noile calculatoare cumpărate pentru casieri erau prea lente. Acest lucru a fost în timp înainte ca toată lumea să utilizeze sistemul bancar electronic și ATM-urile nu au fost la fel de răspândite ca acum. Oamenii vizitau banca mult mai des, iar computerele lente îi făceau pe oameni să stea la coadă. În consecință, banca a amenințat să rupă contractul cu vânzătorul.

> Vânzătorul a trimis un specialist în analize de performanţă şi tuning pentru a determina cauza întârzierilor. Curând a găsit un program specific care rulează pe terminal consumând aproape toată capacitatea procesorului. Folosind un instrument de profilare, el a mărit în programul și el a putut vedea funcția care a fost vinovat. Codul sursă se citește:

> ```
> pentru (i=0, i<strlen(s); ++i) {
> dacă (... s[i) ...) ...
> }
> ```

> Și sir s a fost, în medie, mii de caractere lungi. Codul (scris de bancă) a fost schimbat rapid, iar castorii băncii au trăit fericiţi până la adânci bătrâneţi....

N-ar fi trebuit ca programatorul să facă mai bine decât să folosească codul care a escaladat în mod inutil patrulatic?
Fiecare apel la strlen a traversat fiecare dintre multele mii de caractere din șir pentru a găsi caracterul său nul de încheiere. Cu toate acestea, coarda nu s-a schimbat niciodată. Prin determinarea lungimii sale în avans, programatorul ar fi putut salva mii de apeluri la strlen (și milioane de execuții bucle):

```
n=strlen(s);
for (i=0; i<n; ++i) {
  if (... s[i] ...) ...
}
```

Toată lumea știe zicala "mai întâi face să funcționeze, apoi face să funcționeze rapid" pentru a evita capcanele de micro-optimizare. Dar exemplul de mai sus aproape te-ar face să crezi că programatorul l-a urmat pe machiavelian adagio "mai întâi fă-l să funcţioneze încet."

Această neatenţie e ceva ce poţi întâlni de mai multe ori. Și nu este doar un lucru "nu reinventa roata." Uneori programatorii încep să tasteze fără să gândească şi dintr-o dată au inventat un fel de bulă. S-ar putea chiar să se laude cu asta.

Cealaltă parte a alegerii algoritmului corect este alegerea structurii datelor. Acesta poate face o mare diferență: Folosind o listă legată pentru o colecție de un milion de elemente pe care doriți să le căutați prin 

Programatorii nu ar trebui să reinventeze roata și ar trebui să utilizeze bibliotecile existente, dacă este posibil. Dar pentru a putea evita probleme precum cele ale băncii, acestea ar trebui, de asemenea, să fie educate cu privire la algoritmii și la modul în care acestea cresc. Este doar bomboane ochi în editorii de text moderne care le face la fel de lent ca programele de școală veche ca WordStar în anii 1980? Mulţi spun că reutilizarea programelor este esenţială. Cu toate acestea, mai presus de toate, programatorii ar trebui să știe când, ce și cum să reutilizeze. Pentru a fi capabili să facă acest lucru, ei ar trebui să cunoască domeniul problemei și algoritmii și structurile de date.

Un programator bun ar trebui să ştie şi când să folosească un algoritm abominabil. De exemplu, dacă domeniul problemă dictează nu poate fi mai mult de cinci elemente (cum ar fi numărul de zaruri într-un joc Yahtzee), știi că*întotdeauna*trebuie să sorteze cel mult cinci lucruri. În acest caz, un fel de bule ar putea fi de fapt cel mai eficient mod de a sorta elementele. Fiecare câine are ziua lui.

Deci, citiți niște cărți bune și asigurați-vă că le înțelegeți. Şi dacă chiar citeşti Donald Knuth's*arta programării calculatoarelor*Ei bine, s-ar putea fi chiar norocos: Găsiţi o greşeală de autor şi de a câştiga unul dintre Don Knuth lui hexazecimal ($2.56) cecuri.

De[JC van Winkel](http://programmer.97things.oreilly.com/wiki/index.php/JC_van_Winkel)
