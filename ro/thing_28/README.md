# Nu vă fixaţi programul în poziţia corectă

Am scris o dată un test C++, în care am sugerat satiric următoarea strategie pentru manipularea excepției:

> Prin dint de abundenta`try...catch`construiește în întreaga noastră bază de cod, suntem uneori în măsură să împiedice aplicațiile noastre de avort. Ne gândim la starea care a rezultat ca "cuie cadavrul în poziție verticală."

În ciuda levităţii mele, rezumam o lecţie pe care am primit-o la genunchiul lui Dame Bitter Experience.

A fost o clasă de aplicații de bază în propria noastră bibliotecă C++ de casă. De-a lungul anilor, a suferit loviturile degetelor multor programatori: Nimeni nu avea mâinile curate. Acesta conținea cod pentru a se ocupa cu toate excepțiile scăpate de la orice altceva. Luând conducerea noastră de la Yossarian în Catch-22, am decis, sau mai degrabă simțit (*decis*implică mai mult decât a intrat în construcția acestui monstru) că un exemplu al acestei clase ar trebui să trăiască pentru totdeauna sau mor în încercarea.

În acest scop, am interconectat mai multe persoane care se ocupă cu excepţia. Ne-am amestecat în modul structurat de manipulare a excepției Windows cu tipul nativ (amintiți`__try...__except`în C++? Nici eu. Când lucrurile au apărut pe neaşteptate, am încercat să-i sunăm din nou, apăsând mai tare parametrii. Privind înapoi, îmi place să cred că atunci când scrie un interior`try...catch`Un fel de conştient s-a strecurat asupra mea, în cadrul clauzei de captură, un fel de conştientizare care mi-a spus că aş fi luat din greşeală un drum alunecos de pe autostrada bunelor practici pe banda aromată dar insalubră a nebuniei. Totuşi, aceasta este probabil o înţelepciune retrospectivă.

Inutil să spun, de fiecare dată când ceva mergea prost în aplicații bazate pe această clasă, au dispărut ca victimele mafiei la docuri, lăsând în urmă nici o urmă utilă de bule pentru a indica ce naiba s-a întâmplat, în ciuda rutinelor de dumping care se presupune că au fost numite pentru a înregistra dezastrul. În cele din urmă, am trecut în revistă ce am făcut şi am simţit ruşine. Am înlocuit toată mizeria cu un mecanism de raportare minim şi robust. Dar au fost multe accidente pe linie.

Nu te-aş deranja cu asta pentru că cu siguranţă nimeni altcineva nu ar putea fi atât de prost ca noi, dar pentru un argument online pe care l-am avut recent cu un tip al cărui titlu academic de slujbă a declarat că ar trebui să ştie mai bine. Discutam codul Java într-o tranzacţie la distanţă. În cazul în care codul nu a reușit, el a susținut, ar trebui să prindă și să blocheze excepția*in situ*. ("Și apoi face*Ce*Am întrebat. "Gătit pentru cină?")

El a citat regula designerilor UI: NU LĂSAŢI NICIODATĂ UTILIZATORUL SĂ VEZI UN RAPORT DE EXCEPŢIE, mai degrabă ca şi cum acest lucru ar rezolva problema, ceea ce cu ea fiind în capace şi totul. Mă întreb dacă el a fost responsabil pentru codul într-unul dintre acele ATM-uri cu ecran albastru ale căror fotografii decora blogurile fleebler, și a fost permanent traumatizat.
Oricum, dacă ar trebui să te întâlneşti cu el, să dai din cap şi să zâmbeşti şi să nu iei în seamă, în timp ce te îndrepţi spre uşă.

De[Verity Stob](http://programmer.97things.oreilly.com/wiki/index.php/Verity_Stob)