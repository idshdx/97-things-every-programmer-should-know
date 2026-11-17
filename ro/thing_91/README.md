# WET diluează blocajele de performanță

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_91_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_91_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 4:31)](../audio/thing_91_ro.mp3)

Importanța principiului DRY (Don't Repeta Yourself) este că codifică ideea că fiecare bucată de cunoștințe într-un sistem ar trebui să aibă o reprezentare singulară. Cu alte cuvinte, cunoștințele ar trebui să fie conținute într-o singură punere în aplicare. Antiteza DRY este WET (Scrie de fiecare dată). Codul nostru este WET atunci când cunoștințele sunt codificate în mai multe implementări diferite. Implicațiile de performanță ale DRY versus WET devin foarte clare atunci când ia în considerare numeroasele lor efecte asupra unui profil de performanță.

Să începem prin a lua în considerare o caracteristică a sistemului nostru, să zicem*X*, care este un blockPU. Să spunem, caracteristică*X*consumă 30% din procesor. Acum, să spunem că caracteristica*X*are zece implementări diferite. În medie, fiecare implementare va consuma 3% din procesor. Deoarece acest nivel de utilizare CPU nu este în valoare de îngrijorătoare dacă suntem în căutarea pentru o victorie rapidă, este probabil că ne-ar lipsi că această caracteristică este blockneck nostru. Cu toate acestea, să spunem că am recunoscut într-un fel caracteristica*X*ca un gât de sticlă. Acum rămânem cu problema găsirii şi reparării fiecărei implementări. Cu WET avem zece implementări diferite pe care trebuie să le găsim și să le reparăm. Cu DRY vom vedea în mod clar utilizarea CPU 30% și ne-ar avea o zecime din codul pentru a repara. Şi am menţionat că nu trebuie să ne petrecem timpul vânând fiecare implementare?

Există un caz de utilizare în cazul în care suntem adesea vinovați de încălcarea DRY: utilizarea noastră de colecții. O tehnică comună de punere în aplicare a unei cereri ar fi aceea de a itera asupra colectării și de a aplica apoi interogarea la rândul său pentru fiecare element:

```
public class UsageExample {
    private ArrayList<Customer> allCustomers = new ArrayList<Customer>();
    // ...
    public ArrayList<Customer> findCustomersThatSpendAtLeast(Money amount) {
        ArrayList<Customer> customersOfInterest = new ArrayList<Customer>();
        for (Customer customer: allCustomers) {
            if (customer.spendsAtLeast(amount))
               customersOfInterest.add(customer);
        }
        return customersOfInterest;
    }
}
```

Prin expunerea acestei colecții brute la clienți, am încălcat încapsularea. Acest lucru nu numai că limitează capacitatea noastră de a refactori, ci obligă utilizatorii codului nostru să încalce DRY prin re-implementarea fiecăreia dintre ele posibil aceeași întrebare. Această situație poate fi ușor evitată prin eliminarea colecțiilor brute expuse din API. În acest exemplu putem introduce un nou tip colectiv specific domeniului numit`CustomerList`Această nouă clasă este mai semantic în conformitate cu domeniul nostru. Va fi un cămin natural pentru toate întrebările noastre.

Având acest nou tip de colectare ne va permite, de asemenea, să vedem cu ușurință dacă aceste întrebări sunt un blocaj de performanță. Prin includerea întrebărilor în clasă eliminăm necesitatea de a expune alegerile de reprezentare, cum ar fi`ArrayList`Pentru clienţii noştri. Acest lucru ne dă libertatea de a modifica aceste implementări fără teama de încălcarea contractelor de client:

```
public class CustomerList {
    private ArrayList<Customer> customers = new ArrayList<Customer>();
    private SortedList<Customer> customersSortedBySpendingLevel = new SortedList<Customer>();
    // ...
    public CustomerList findCustomersThatSpendAtLeast(Money amount) {
        return new CustomerList(customersSortedBySpendingLevel.elementsLargerThan(amount));
    }
}

public class UsageExample {
    public static void main(String[] args) {
        CustomerList customers = new CustomerList();
        // ...
        CustomerList customersOfInterest = customers.findCustomersThatSpendAtLeast(someMinimalAmount);
        // ...
    }
}
```   

În acest exemplu, aderarea la DRY ne-a permis să introducem un sistem alternativ de indexare cu SortedList care să se axeze pe nivelul de cheltuieli al clienților noștri. Mai important decât detaliile specifice ale acestui exemplu particular, în urma DRY ne-a ajutat să găsim și să reparăm un blocaj al performanței care ar fi fost mai dificil de găsit dacă codul ar fi fost WET.

De[Kirk Pepperdine](http://programmer.97things.oreilly.com/wiki/index.php/Kirk_Pepperdine)