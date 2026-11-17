# Principiul responsabilității unice

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_76_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_76_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:37)](../audio/thing_76_ro.mp3)

Unul dintre principiile cele mai fundamentale de proiectare bună este:

> Adună acele lucruri care se schimbă din acelaşi motiv şi separă acele lucruri care se schimbă din diferite motive.

Acest principiu este adesea cunoscut sub numele de*Principiul responsabilității unice*sau SRP. Pe scurt, se spune că un subsistem, un modul, o clasă sau chiar o funcție nu ar trebui să aibă mai multe motive să se schimbe. Exemplul clasic este o clasă care are metode care se ocupă cu regulile de afaceri, rapoarte și baze de date:

```
public class Employee {
  public Money calculatePay() ...
  public String reportHours() ...
  public void save() ...
}
```

Unii programatori ar putea crede că reunirea acestor trei funcţii în aceeaşi clasă este perfect adecvată. La urma urmei, clasele ar trebui să fie colecții de funcții care funcționează pe variabile comune. Cu toate acestea, problema este că cele trei funcții se schimbă din motive complet diferite. ă`calculatePay`funcția se va schimba ori de câte ori normele de afaceri pentru calcularea schimbării salariilor. ă`reportHours`Funcția se va schimba ori de câte ori cineva vrea un format diferit pentru raport. Funcția de salvare se va schimba ori de câte ori DBA schimbă schema bazei de date. Aceste trei motive pentru a schimba combina pentru a face`Employee`Foarte volatil. Se va schimba din oricare dintre aceste motive. Mai important, orice clase care depind de`Employee`vor fi afectate de aceste schimbări.

Designul bun al sistemului înseamnă că separăm sistemul în componente care pot fi utilizate independent. Desfășurarea independentă înseamnă că, dacă schimbăm o componentă, nu trebuie să redistribuim niciuna dintre celelalte componente. Cu toate acestea, dacă`Employee`este puternic utilizat de multe alte clase din alte componente, atunci fiecare schimbare a Angajatului este de natură să determine redistribuirea celorlalte componente; prin urmare, negarea unui beneficiu major al designului componentelor (sau SOA dacă preferați numele mai la modă).

```
public class Employee {
  public Money calculatePay() ...
}

public class EmployeeReporter {
  public String reportHours(Employee e) ...
}

public class EmployeeRepository {
  public void save(Employee e) ...
}
```

Simpla partiție arătată mai sus rezolvă problemele. Fiecare dintre aceste clase poate fi plasată într-o componentă proprie. Sau, mai degrabă, toate clasele de raportare pot intra în componenta de raportare. Toate clasele legate de baza de date pot intra în componenta depozitului. Și toate regulile de afaceri pot intra în componenta regulii de afaceri.

Cititorul inteligent va vedea că există încă dependențe în soluția de mai sus. Asta`Employee`este încă dependentă de celelalte clase. Deci, dacă`Employee`este modificat, celelalte clase vor trebui probabil recompilate și redistribuite. Astfel,`Employee`nu pot fi modificate și apoi utilizate independent. Cu toate acestea, celelalte clase pot fi modificate și utilizate independent. Nici o modificare a unuia dintre ele nu îi poate obliga pe ceilalţi să fie recompilaţi sau redistribuiţi. Chiar`Employee`ar putea fi utilizate independent printr-o utilizare atentă a*Principiul inversării dependenței*(DPI), dar asta e un subiect pentru o[carte diferită](http://www.amazon.com/dp/0135974445/).

Aplicarea atentă a SRP, separarea lucrurilor care se schimbă din diferite motive, este una dintre cheile pentru crearea de modele care au o structură de componente care poate fi implementată independent.

de[Unchiul Bob](http://programmer.97things.oreilly.com/wiki/index.php/Uncle_Bob)
