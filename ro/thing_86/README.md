# Două greşeli pot face dreptate (şi sunt greu de reparat)

Codul nu minte niciodată, dar se poate contrazice. Unele contradicții duc la acele momente "Cum ar putea funcționa?"

În[interviu](http://www.netjeff.com/humor/item.cgi?file=ApolloComputer), principalul designer al software-ului Apollo 11 Lunar Module, Allan Klumpp, a dezvăluit că software-ul care controlează motoarele conținea un bug care ar fi trebuit să facă lander instabil. Cu toate acestea, un alt bug compensat pentru primul și software-ul a fost utilizat atât pentru Apollo 11 și 12 Lună aterizări înainte fie a fost găsită sau reparată.

Gândiţi - vă la o funcţie care returnează statutul de finalizare. Imaginați-vă că se întoarce fals atunci când ar trebui să se întoarcă adevărat. Acum imaginaţi-vă că funcţia de chemare neglijează verificarea valorii de întoarcere. Totul merge bine până într-o zi cineva observă cecul lipsă şi îl introduce.

Sau ia în considerare o aplicație care stochează starea ca un document XML. Imaginați-vă că unul dintre nodurile în scris incorect ca`TimeToLive`în loc de`TimeToDie`, aşa cum spune documentaţia. Totul pare în regulă în timp ce codul scriitorului şi codul cititorului conţin aceeaşi eroare. Dar repara unul, sau adăugați o nouă aplicație lectură același document, și simetria este rupt, precum și codul.

Când două defecte ale codului creează o singură eroare vizibilă, abordarea metodică a defectelor de fixare se poate descompune singură. Dezvoltatorul primeşte un raport de eroare, găseşte defectul, îl repară şi retestează. Cu toate acestea, vina raportată încă apare, deoarece un al doilea defect este la locul de muncă. Deci, primul fix este eliminat, codul inspectat până la al doilea defect de bază este găsit, și un fix aplicat pentru asta. Dar primul defect a revenit, defectul raportat este încă văzut, și astfel a doua fix este laminate înapoi. Procesul se repetă, dar acum dezvoltatorul a respins două posibile soluţii şi încearcă să facă o treime care nu va funcţiona niciodată.

Interacțiunea dintre două defecte de cod care apar ca o singură eroare vizibilă nu numai că face dificilă rezolvarea problemei, dar duce dezvoltatorii pe alei oarbe, doar pentru a afla că au încercat răspunsurile corecte timpuriu.

Acest lucru nu se întâmplă doar în cod: Problema există şi în documentele scrise. Şi se poate răspândi, viral, dintr-un loc în altul. O eroare în cod compensează o eroare în descrierea scrisă.

Se poate răspândi și la oameni: Utilizatorii află că atunci când aplicația spune stânga înseamnă dreapta, așa că își ajustează comportamentul în consecință. Ei chiar îl transmit noilor utilizatori: "Amintiţi-vă când aplicaţiile spun că faceţi clic pe butonul din stânga înseamnă cu adevărat butonul din dreapta." Fix bug-ul și dintr-o dată utilizatorii au nevoie de recalificare.

Greşelile simple pot fi uşor de reperat şi uşor de reparat. Problemele cu cauze multiple, care necesită schimbări multiple, sunt mai greu de rezolvat. În parte, deoarece problemele uşoare sunt atât de uşor de rezolvat încât oamenii tind să le repare relativ repede şi să stocheze problemele mai dificile pentru o dată ulterioară.

Nu există sfaturi simple pentru a da cu privire la modul de a aborda defectele care decurg din defectele de simpatie. Este nevoie de conştientizarea posibilităţii, de un cap limpede şi de disponibilitatea de a analiza toate posibilităţile.

De[Allan Kelly](http://programmer.97things.oreilly.com/wiki/index.php/Allan_Kelly)