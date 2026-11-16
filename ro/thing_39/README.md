# Îmbunătăţirea codului prin eliminarea acestuia

*Mai puțin*e mai mult. Este o maxima destul de banala, dar uneori este adevarat.

Una din îmbunătăţirile aduse bazei noastre de coduri în ultimele săptămâni este să elimini bucăţi din ea.

Ne-am scris software-ul în urma teneturi XP, inclusiv YANGIN (adică, Tu nu o să nevoie de ea). Natura umană fiind ceea ce este, am căzut inevitabil scurt în câteva locuri.

Am observat că produsul a fost de a lua prea mult timp pentru a executa anumite sarcini simple, care ar fi trebuit să fie aproape instantaneu. Acest lucru s - a întâmplat pentru că erau suprasolicitate; erau pline de clopoţei şi fluiere care nu erau necesare, dar atunci păreau o idee bună.

Aşa că am simplificat codul, am îmbunătăţit performanţa produsului şi am redus nivelul entropiei codului global prin eliminarea caracteristicilor ofensatoare din baza de coduri. Din fericire, testele mele de unitate îmi spun că nu am rupt nimic altceva în timpul operațiunii.

O experienţă simplă şi satisfăcătoare.

Deci, de ce a ajuns codul inutil acolo, în primul rând? De ce a simțit un programator nevoia de a scrie cod suplimentar, și cum a trecut revizuirea sau procesul de asociere? Aproape sigur ceva de genul:

- A fost un pic distractiv de lucruri suplimentare, și programatorul a vrut să-l scrie.*(Scrie codul pentru că adaugă valoare, nu pentru că te amuză.)*
- Cineva a crezut că ar putea fi necesar în viitor, așa că a simțit că a fost cel mai bine să-l codeze acum.*Asta nu e YANCI. Dacă nu aveți nevoie de ea chiar acum, nu scrie chiar acum.)*
- Nu părea să fie atât de mare un "extra," așa că a fost mai ușor să-l pună în aplicare mai degrabă decât du-te înapoi la client pentru a vedea dacă a fost într-adevăr necesar.*(Hint: Este întotdeauna nevoie de mai mult timp pentru a scrie și pentru a menține codul suplimentar. Iar clientul este de fapt destul de abordabil. Un pic mai mult de cod bulgări de zăpadă în timp într-o mare bucată de muncă care necesită întreținere.)*
- Programatorul a inventat cerințe suplimentare care nu au fost nici documentate și nici discutate care au justificat funcția suplimentară. Cerinţa era falsă.*(Hint: Programatorii nu stabilesc cerințele sistemului; clientul o face.)*

La ce lucrezi acum? Este totul necesar?

De[Pete Goodliffe](http://programmer.97things.oreilly.com/wiki/index.php/Pete_Goodliffe)
