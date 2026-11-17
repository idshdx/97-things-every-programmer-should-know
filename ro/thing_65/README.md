# Preferi tipuri specifice domeniului la tipuri primitive

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_65_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_65_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 2:57)](../audio/thing_65_ro.mp3)

Pe 23 septembrie 1999 s-a pierdut 327,6 milioane de dolari pe Marte, când a intrat pe orbita planetei Marte, din cauza unei erori software pe Pământ. Eroarea a fost mai târziu numit*mix-up metric*. Software-ul stație de sol a fost de lucru în lire sterline în timp ce nava spațială a așteptat newtoni, conducând stația de la sol pentru a subestima puterea propulsoarelor navei spațiale cu un factor de 4.45.

Acesta este unul dintre numeroasele exemple de eșecuri ale software-ului care ar fi putut fi prevenite dacă s-ar fi aplicat tastarea mai puternică și mai specifică domeniului. Acesta este, de asemenea, un exemplu de motivație în spatele mai multor caracteristici în limba Ada, unul dintre obiectivele principale de proiectare a fost de a implementa software-ul integrat de siguranță critic. Ada are tastarea puternica cu verificarea statica atat pentru tipurile primitive cat si pentru tipurile definite de utilizator:

```
type Velocity_In_Knots is new Float range 0.0 .. 500.00;

type Distance_In_Nautical_Miles is new Float range 0.0 .. 3000.00;

Velocity: Velocity_In_Knots;

Distance: Distance_In_Nautical_Miles;

Some_Number: Float;

Some_Number:= Distance + Velocity; -- Will be caught by the compiler as a type error.
```

Dezvoltatorii din domenii mai puțin exigente ar putea beneficia, de asemenea, de aplicarea unui dactilograf mai specific domeniului, în cazul în care ar putea continua altfel să utilizeze tipurile de date primitive oferite de limba și bibliotecile sale, cum ar fi siruri de caractere și flotoare. În Java, C++, Python și alte limbi moderne, tipul de date abstracte este cunoscut sub numele de clasă. Utilizarea unor clase precum:`Velocity_In_Knots`şi`Distance_In_Nautical_Miles`adaugă o mulțime de valoare în ceea ce privește calitatea codului:

- Codul devine mai lizibil pe măsură ce exprimă concepte ale unui domeniu, nu doar Float sau String.
- Codul devine mai testabil pe măsură ce codul încapsulază comportamentul care este uşor de testat.
- Codul facilitează reutilizarea între aplicații și sisteme.

Abordarea este valabilă și pentru utilizatorii de limbi cu tastaturi statice și dinamice. Singura diferenta este ca dezvoltatorii care folosesc limbaje tiptate static primesc ajutor de la compilator in timp ce cei care imbratiseaza limbaje tastate dinamic se pot baza mai mult pe testele lor unitare. Stilul de verificare poate fi diferit, dar motivația și stilul de exprimare nu este.

Morala este de a începe explorarea de tipuri specifice domeniului în scopul dezvoltării de software de calitate.

De[Einar Landre](http://programmer.97things.oreilly.com/wiki/index.php/Einar_Landre)
