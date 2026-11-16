# Pune totul sub control versiune

Pune totul în toate proiectele sub control versiune. Resursele de care aveți nevoie sunt acolo: instrumente gratuite, cum ar fi Subversiune, Git, Mercurial și CVS; spațiu pe disc abundent; servere ieftine și puternice; rețele omniprezente; și chiar servicii de găzduire de proiecte. După ce ați instalat software-ul de control versiune tot ce aveți nevoie pentru a pune munca în depozitul său este de a emite comanda corespunzătoare într-un director curat care conține codul. Și există doar două noi operațiuni de bază pentru a învăța: tu*comite*codul se modifică în depozit și vă actualizați versiunea de lucru a proiectului cu versiunea depozitului.

Odată ce proiectul dvs. este sub control versiune puteți urmări în mod evident istoria sa, a se vedea cine a scris ce cod, și se referă la un fișier sau versiune de proiect printr-un identificator unic. Mai important, puteți face modificări de cod îndrăzneț fără frică  Puteți (și ar trebui) eticheta un software de eliberare cu un nume simbolic, astfel încât să puteți revizui cu ușurință în viitor versiunea exactă a software-ului pe care clientul dumneavoastră îl rulează. Puteți crea ramuri de dezvoltare paralelă: Cele mai multe proiecte au o ramură de dezvoltare activă și una sau mai multe ramuri de întreținere pentru versiunile lansate care sunt susținute activ.

Un sistem de control al versiunii minimizează frecarea între dezvoltatori. Când programatorii lucrează pe piese software independente, acestea sunt integrate aproape prin magie. Când calcă pe degetele de la picioare ale celuilalt, sistemul le permite să rezolve conflictele. Cu o anumită configurare suplimentară, sistemul poate notifica toți dezvoltatorii pentru fiecare schimbare comisă, stabilind o înțelegere comună a progresului proiectului.

Când îţi faci proiectul, nu fi zgârcit: loc*toate*activele proiectului aflate sub controlul versiunii. În afară de codul sursă, include documentația, instrumente, script-uri construi, cazuri de testare, lucrări de artă, și chiar biblioteci. Cu proiectul complet ascuns în depozit (în mod regulat susţinut) deteriorarea pierderii discului sau a datelor este minimizată. Înființarea pentru dezvoltare pe o mașină nouă implică pur și simplu verificarea proiectului din depozit. Acest lucru simplifică distribuirea, construirea și testarea codului pe diferite platforme: Pe fiecare mașină o singură comandă de actualizare va asigura că software-ul este versiunea curentă.

Odată ce ați văzut frumusețea de a lucra cu un sistem de control versiune, urmând câteva reguli va face tu și echipa ta chiar mai eficient:

- Comite fiecare schimbare logică într-o operațiune separată. Faptul de a face multe schimbări împreună într-un singur angajament va face dificilă dezmembrarea lor în viitor. Acest lucru este deosebit de important atunci când faceți refactoruri la nivel de proiect sau schimbări de stil, care pot ascunde cu ușurință alte modificări.
- Însoțiți fiecare angajament cu un mesaj explicativ. Cel puţin descrie succint ce ai schimbat, dar dacă vrei să înregistrezi raţionamentul schimbării acesta este cel mai bun loc pentru a-l stoca.
- În cele din urmă, evitați comiterea unui cod care va sparge construirea unui proiect, altfel veți deveni nepopulari cu alți dezvoltatori ai proiectului.

Viaţa sub un sistem de control al versiunii este prea bună pentru a o distruge cu paşi uşor de evitat.

De[Diomidis Spinellis](http://programmer.97things.oreilly.com/wiki/index.php/Diomidis_Spinellis)