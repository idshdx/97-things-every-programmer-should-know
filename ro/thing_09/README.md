# Verificați codul înainte de a căuta să dea vina pe alții

Dezvoltatorii  Este atât de improbabil că, măcar o dată, compilatorul trebuie să fie cel stricat.

Cu toate acestea, în realitate, este foarte (foarte) neobișnuit că codul este rupt de un bug în compilator, interpret, OS, server de aplicații, baze de date, manager de memorie, sau orice altă piesă de software de sistem. Da, aceste insecte există, dar sunt mult mai puţin comune decât ne-ar plăcea să credem.

Am avut o dată o problemă reală cu un bug compilator optimizarea departe o variabilă buclă, dar mi-am imaginat compilatorul meu sau OS a avut un bug de multe ori. Mi-am irosit o mulțime de timp, timp de sprijin, și timp de management în acest proces doar pentru a simți un pic prost de fiecare dată sa dovedit a fi greșeala mea, după toate.

Presupunând că instrumentele sunt utilizate pe scară largă, mature și utilizate în diferite stive tehnologice, nu există niciun motiv să ne îndoim de calitate. Desigur, în cazul în care instrumentul este o lansare timpurie, sau utilizate de doar câțiva oameni din întreaga lume, sau o bucată de rareori descărcate, versiunea 0.1, Open Source Software, poate exista un motiv bun pentru a suspecta software-ul. (Egal, o versiune alfa de software comercial ar putea fi suspect.)

Având în vedere cât de rare sunt bug-uri compilator, sunteți mult mai bine punerea timpul și energia în găsirea erorii în codul dvs. decât dovedirea compilatorului este greșit. Toate recomandările obişnuite de depanare se aplică, aşa că izolaţi problema, scoateţi apelurile, înconjuraţi-o cu teste; verificaţi convenţiile de apelare, bibliotecile comune şi numerele de versiune; explicaţi-o altcuiva; uitaţi-vă la corupţia stivă şi la neconcordanţele de tip variabil; încercaţi codul de pe diferite maşini şi diferite configuraţii de construcţie, cum ar fi depanarea şi eliberarea.

Îţi pui la îndoială propriile ipoteze şi presupunerile altora. Unelte de la diferiți furnizori ar putea avea ipoteze diferite construite în ele 
Când altcineva raportează o problemă pe care nu o poţi copia, du-te şi vezi ce face. Poate că fac ceva la care nu te-ai gândit sau fac ceva diferit.

Ca regulă personală, dacă am un microfon pe care nu-l pot fixa, şi încep să cred că e compilatorul, atunci e timpul să căutăm corupţia. Acest lucru este valabil mai ales dacă adăugarea de coduri de urmărire face ca problema să se mişte.

Problemele multiple sunt o altă sursă de bug-uri pentru a transforma parul gri și induce tipetele la mașină. Toate recomandările pentru a favoriza codul simplu sunt multiplicate atunci când un sistem este multi-filtrat. Depanarea și încercările de unitate nu pot fi invocate pentru a găsi astfel de bug-uri cu orice consistență, astfel încât simplitatea de proiectare este primordială.

Înainte de a da vina pe compilator, amintiți-vă sfatul lui Sherlock Holmes: "Odată ce eliminați imposibilul, orice rămâne, oricât de improbabil ar fi, trebuie să fie adevărul," și preferați-l lui Dirk Gently, "Odată ce eliminați improbabilul, orice rămâne, indiferent cât de imposibil, trebuie să fie adevărul."

De[Allan Kelly](http://programmer.97things.oreilly.com/wiki/index.php/Allan_Kelly)
