# Uneltele Unix sunt prietenii tăi

Dacă în drum spre exil pe o insulă pustie ar trebui să aleg între un IDE şi unix, aş alege uneltele Unix fără să mă gândesc. Iată motivele pentru care ar trebui să devii expert cu instrumentele Unix.

În primul rând, ID-urile vizează limbi specifice, în timp ce instrumentele Unix pot lucra cu orice apare în formă textuală. În mediul de dezvoltare de astăzi, unde noile limbi şi note apar în fiecare an, învăţarea de a lucra în stilul Unix este o investiţie care va da roade de nenumărate ori.

În plus, în timp ce IDE oferă doar comenzile concepute de dezvoltatorii lor, cu instrumente Unix puteți efectua orice sarcină vă puteți imagina. Gândiți-vă la ei ca (pre-Bionic clasic) Blocuri Lego: Îţi creezi propriile comenzi prin combinarea uneltelor Unix mici, dar versatil. De exemplu, urmatoarea secventa este o implementare bazata pe text a analizei semnaturii lui Cunningham 

```
for i in *.java; do 
    echo -n "$i: "
    sed 's/[^"{};]//g' $i | tr -d '\n'
    echo
done
```

În plus, fiecare operațiune IDE pe care o înveți este specifică acestei sarcini date; de exemplu, adăugarea unui nou pas în configurarea bug-ului unui proiect. Prin contrast, ascuţirea abilităţilor de instrument Unix te face mai eficient la orice sarcină. Ca un exemplu, am folosit instrumentul sed folosit în secvenţa de comandă anterioară pentru a transforma construcţia unui proiect pentru a compara mai multe arhitecturi de procesor.

Unix instrumente au fost dezvoltate într-o epocă în care un computer multiutilizator a avut 128kB de RAM. Ingeniozitatea care a intrat în designul lor înseamnă că în zilele noastre ei pot gestiona seturi de date uriașe extrem de eficient. Cele mai multe instrumente funcţionează ca filtrele, procesând doar o singură linie la momentul respectiv, ceea ce înseamnă că nu există limită superioară în cantitatea de date pe care le pot manipula. Doriți să căutați numărul de editări stocate în jumătate de terabyte engleză Wikipedia groapa de gunoi? O simplă invocare a

```
grep '<revision>' | wc –l 
```

îţi va da răspunsul fără să transpire. Dacă găsiți o secvență de comandă în general utilă, o puteți împacheta cu ușurință într-un script shell, folosind niște construcții unice de programare puternice, cum ar fi conductele de date în bucle și condiționale. Chiar mai impresionant, Unix comandă executarea ca conducte, la fel ca cel precedent, va distribui în mod natural sarcina lor printre numeroasele unități de prelucrare ale CPU multicore moderne.

Micul-este-frumos proveniență și implementarea open source a instrumentelor Unix le face disponibile omniprezent, chiar și pe platforme de resurse, cum ar fi meu set-top player media sau router DSL. Este puțin probabil ca astfel de dispozitive să ofere o interfață grafică puternică, dar ele includ adesea aplicația BusyBox, care oferă cele mai utilizate instrumente. Și dacă sunteți în curs de dezvoltare pe Windows, mediul Cygwin vă oferă toate instrumente imaginabile Unix, atât ca executabile și în formă de cod sursă.

În cele din urmă, în cazul în care nici unul dintre instrumentele disponibile se potrivesc nevoilor dumneavoastră, este foarte ușor să se extindă lumea instrumentelor Unix. Scrie doar un program (în orice limbă vă place) care joacă după câteva reguli simple: Programul dumneavoastră ar trebui să efectueze doar o singură sarcină; ar trebui să citească datele ca linii de text de la intrarea standard; și ar trebui să afișeze rezultatele sale neadorate de antete și alte zgomote pe ieșirea standard. Parametrii care afectează funcționarea instrumentului sunt specificați în linia de comandă. Urmează aceste reguli şi "a ta este Pământul şi tot ce este în el."

De[Diomidis Spinellis](http://programmer.97things.oreilly.com/wiki/index.php/Diomidis_Spinellis)