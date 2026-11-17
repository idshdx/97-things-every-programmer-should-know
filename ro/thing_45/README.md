# Cunoaşteţi IDE - ul

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_45_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_45_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:05)](../audio/thing_45_ro.mp3)

În anii 1980, mediile noastre de programare nu erau mai bune decât editorii de text glorificaţi... dacă eram norocoşi. Sublinierea sintaxei, pe care o considerăm de la sine înţelesă în zilele noastre, era un lux care cu siguranţă nu era disponibil tuturor. Imprimante frumoase pentru a forma codul nostru frumos au fost, de obicei, instrumente externe care au trebuit să fie difuzate pentru a corecta distanța noastră. Depanatorii au fost, de asemenea, programe separate rula pentru a trece prin codul nostru, dar cu o mulțime de criptic tastetrokes.

În timpul anilor 1990 companiile au început să recunoască veniturile potenţiale pe care le-ar putea obţine din dotarea programatorilor cu instrumente mai bune şi mai utile. Mediul integrat de dezvoltare (IDE) a combinat caracteristicile de editare anterioare cu un compilator, depanator, destul de imprimantă și alte instrumente. În acest timp, meniurile și mouse-ul au devenit, de asemenea, populare, ceea ce a însemnat că dezvoltatorii nu mai au nevoie pentru a învăța combinații cheie criptice pentru a utiliza editorii lor. Ei ar putea selecta pur și simplu comanda lor din meniu.

În secolul XXI, IDE-urile au devenit un loc atât de comun încât sunt date gratuit de către companiile care doresc să câștige cota de piață în alte domenii. IDE-ul modern este echipat cu o gamă uimitoare de caracteristici. Preferatul meu este refactorarea automată, în special*Metoda de extracție*, unde pot selecta și converti o bucată de cod într-o metodă. Instrumentul de refacere va ridica toți parametrii care trebuie să fie trecut în metoda, ceea ce face extrem de ușor de modificat codul. IDE mea va detecta chiar și alte bucăți de cod care ar putea fi, de asemenea, înlocuite cu această metodă și mă întreabă dacă aș dori să le înlocuiască prea.

O altă caracteristică uimitoare a IDE moderne este capacitatea de a aplica reguli stil în cadrul unei companii. De exemplu, în Java, unii programatori au început să facă toţi parametrii finali (care, în opinia mea, este o pierdere de timp). Cu toate acestea, din moment ce au o astfel de regulă stil, tot ce ar trebui să fac pentru a urmări este stabilit în IDE mea: aș primi un avertisment pentru orice parametru non-final. Normele de stil pot fi, de asemenea, utilizate pentru a găsi bug-uri probabile, cum ar fi compararea obiectelor autoboxed pentru egalitatea de referință, de exemplu, folosind`==`pe valori primitive care sunt autoboxate în obiecte de referință.

Din păcate, ID-urile moderne nu ne cer să investim efort pentru a învăţa cum să le folosim. Când am programat pentru prima dată C pe Unix, a trebuit să petrec ceva timp învăţând cum funcţionează editorul Vi, datorită curbei sale abrupte de învăţare. Acest timp petrecut în avans a fost răsplătit cu generozitate de-a lungul anilor. Sunt chiar tastarea proiectul acestui articol cu*vi*. IDE-urile moderne au o curbă de învățare foarte graduală, care poate avea efectul că niciodată nu vom progresa dincolo de utilizarea cea mai de bază a instrumentului.

Primul meu pas în învățarea unui IDE este de a memora comenzi rapide tastatură. Din moment ce degetele mele sunt pe tastatură când scriu codul meu, apăsând*Ctrl+ Shift+I*pentru a inlinia o variabilă salvează ruperea fluxului, în timp ce trecerea pentru a naviga un meniu cu mouse-ul meu întrerupe fluxul. Aceste întreruperi duc la schimbări inutile de context, făcându-mă mult mai puțin productiv dacă încerc să fac totul leneș. Aceeaşi regulă se aplică şi abilităţilor de tastatură: Învaţă să atingi tipul, nu vei regreta timpul investit în avans.

În cele din urmă, ca programatori avem timp dovedit Unix instrumente de streaming care ne pot ajuta să manipuleze codul nostru. De exemplu, în cazul în care în timpul unei revizuiri a codului, am observat că programatorii au numit o mulțime de clase la fel, am putut găsi aceste foarte ușor folosind instrumentele*Caută*,*sed*,*sortează*,*uniq*, și*grep*, așa:

```
find . -name "*.java" | sed 's/.*\///' | sort | uniq -c | grep -v "^ *1 " | sort -r
```

Ne asteptam ca un instalator sa vina la noi acasa sa poata folosi lanterna. Să petrecem puţin timp pentru a studia cum să devenim mai eficienţi cu IDE-ul nostru.

de[Heinz Kabutz](http://programmer.97things.oreilly.com/wiki/index.php/Heinz_Kabutz)