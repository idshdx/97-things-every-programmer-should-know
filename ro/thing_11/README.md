# Codul în limba domeniului

Imaginează-ţi două baze de coduri. Într-unul dai peste:

```
if (portfolioIdsByTraderId.get(trader.getId())
  .containsKey(portfolio.getId())) {...}
```
  
Te scarpini pe cap, întrebându-te pentru ce ar putea fi acest cod. Pare să fie obtinerea unui ID de la un obiect comerciant, folosind faptul că pentru a obține o hartă dintr-o, bine, harta-of-maps aparent, și apoi a vedea dacă un alt ID de la un obiect de portofoliu există în harta interioară. Te mai scarpini la cap. Cauţi declaraţia de portofoliuIdsByTraderId şi descoperi asta:

```
Map<int, Map<int, int>> portfolioIdsByTraderId;
```

Treptat vă daţi seama că ar putea avea legătură cu accesul unui comerciant la un anumit portofoliu. Şi, desigur, veţi găsi acelaşi fragment de căutare sau mai probabil un fragment de cod similar-dar-subtly-diferit-diferit de ori de câte ori ceva îi pasă dacă un comerciant are acces la un anumit portofoliu.

În cealaltă bază de coduri dai peste asta:

```
if (trader.canView(portfolio)) {...}
```

Fără zgârieturi la cap. Nu trebuie să ştii cum ştie un comerciant. Poate că există una din hărţile astea ascunse undeva înăuntru. Dar asta e treaba comerciantului, nu a ta.

În care dintre aceste baze de coduri ai prefera să lucrezi?

A fost odată ca niciodată când aveam doar structuri de date de bază: biți și biți și caractere (de fapt doar octeți, dar ne prefăceam că sunt litere și punctuație). Decimals au fost un pic dificil pentru că numerele noastre de bază 10 nu funcționează foarte bine în binar, așa că am avut mai multe dimensiuni de tipuri de puncte plutitoare. Apoi au venit array-uri și siruri de caractere (de fapt doar diferite array-uri). Apoi am avut stive și cozi și hashes și liste legate și sări peste liste și o mulțime de alte structuri de date interesante*care nu există în lumea reală*"Science Computer" a fost despre a cheltui o mulțime de efort cartografiind lumea reală în structurile noastre restrictive de date. Adevăratul guru îşi aminteşte cum au făcut-o.

Apoi avem tipuri definite de utilizator! OK, acest lucru nu este o veste, dar nu schimba jocul într-un fel. Dacă domeniul dumneavoastră conţine concepte precum comercianţii şi portofoliile, le puteţi modela cu tipuri numite, să zicem, Comerciant şi Portofoliu. Dar, mai important decât aceasta, puteți modela*relaţiile dintre ele*utilizarea termenilor de domeniu prea.

Daca nu codezi folosind termeni de domeniu creezi un tacit (citeste: secret) intelegand ca*Asta*int aici inseamna modalitatea de identificare a unui comerciant, in timp ce*că*int acolo inseamna modul de identificare a unui portofoliu. (Cel mai bun pentru a nu le amesteca!) Și dacă reprezentați un concept de business ("Unor comercianți nu li se permite să vadă unele portofolii e ilegal") cu un fragment algoritmic, spune o relație de existență într-o hartă de chei, nu sunteți de a face tipi de audit și de conformitate orice favoruri.

Următorul programator de-a lungul s-ar putea să nu fie în pe secretul, așa că de ce nu-l explicit? Folosind o cheie ca o privire la o altă cheie care efectuează o verificare a existenței nu este teribil de evident. Cum este cineva ar trebui să intuiți că este în cazul în care normele de afaceri prevenirea conflictelor de interese sunt puse în aplicare?

A face concepte de domeniu explicite în codul dumneavoastră înseamnă că alți programatori pot aduna*intenţie*a codului mult mai ușor decât prin încercarea de a adapta un algoritm în ceea ce înțeleg despre un domeniu. Aceasta înseamnă, de asemenea, că, atunci când modelul de domeniu evoluează  Împreună cu o bună încapsulare, şansele sunt bune ca regula să existe într-un singur loc, şi că o poţi schimba fără ca vreunul din codurile dependente să fie mai înţelept.

Programatorul care vine câteva luni mai târziu să lucreze la cod vă va mulţumi. Programatorul care vine câteva luni mai târziu s-ar putea să fii tu.

De[Dan North](http://programmer.97things.oreilly.com/wiki/index.php/Dan_North)