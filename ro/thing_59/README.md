# Oportunităţi lipsă de polimorfism

<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">
  <source src="../audio/thing_59_ro.mp3" type="audio/mpeg" />
  Browserul tău nu acceptă elementul audio — <a href="../audio/thing_59_ro.mp3">descarcă fișierul MP3</a>.
</audio>

🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3, 3:53)](../audio/thing_59_ro.mp3)

Polimorfismul este una dintre marile idei fundamentale pentru OO. Cuvântul, luat din greacă, înseamnă multe (*poli*) forme (*morph*). În contextul programării polimorfismului se referă la multe forme ale unei anumite clase de obiecte sau metode. Dar polimorfismul nu este doar despre implementarea alternativă. Folosit cu atenţie, polimorfismul creează mici contexte de execuţie localizate care ne permit să lucrăm fără nevoia de verboză*dacă-atunci-altele*blocuri. Fiind într-un context ne permite să facem ceea ce trebuie în mod direct, în timp ce fiind în afara acelui context ne obligă să-l reconstruim astfel încât să putem face ceea ce trebuie. Cu utilizarea atentă a implementărilor alternative, putem captura context care ne poate ajuta să producem mai puțin cod care este mai ușor de citit. Acest lucru este cel mai bine demonstrat cu un cod, cum ar fi următorul (nerealistic) simplu coș de cumpărături:

```
public class ShoppingCart {
    private ArrayList<Item> cart = new ArrayList<Item>();
    public void add(Item item) { cart.add(item); }
    public Item takeNext() { return cart.remove(0);  }
    public boolean isEmpty() { return cart.isEmpty(); }
}
```

Să spunem că magazinul nostru oferă elemente care pot fi descărcate și elemente care trebuie trimise. Să construim un alt obiect care susţine aceste operaţiuni:

```
public class Shipping {
    public boolean ship(Item item, SurfaceAddress address) { ... }
    public boolean ship(Item item, EMailAddress address) { ... }
}
```

Când un client a terminat checkout trebuie să expediem marfa:

```
while (!cart.isEmpty()) {
    shipping.ship(cart.takeNext(), ???);
}
```

ă*♪?*parametrul nu este un nou operator elvis fantezie, se cere ar trebui să-i mail sau melc-mail elementul? Contextul necesar pentru a răspunde la această întrebare nu mai există. Am putea captura metoda de transport într-un boolean sau enum și apoi utilizați un*dacă-atunci-altele*pentru a completa parametrul lipsă. O altă soluție ar fi crearea a două clase care ambele extinde Postul. Să numim aceste obiecte descărcabileItem și SurfaceItem. Acum să scriem un cod. Voi promova elementul pentru a fi o interfață care susține o singură metodă, navă. Pentru a trimite conţinutul căruciorului, vom suna`item.ship(shipper)`. Clase`DownloadableItem`şi`SurfaceItem`ambele vor implementa nava.

```
public class DownloadableItem implements Item {
    public boolean ship(Shipping shipper) {
        shipper.ship(this, customer.getEmailAddress());
    }
}

public class SurfaceItem implements Item {
    public boolean ship(Shipping shipper) {
        shipper.ship(this, customer.getSurfaceAddress());
    }
}
```

În acest exemplu am delegat responsabilitatea de a lucra cu`Shipping`la fiecare element. Deoarece fiecare element știe cum este cel mai bine expediate, acest aranjament ne permite să obținem mai departe cu ea fără a fi nevoie de un*dacă-atunci-altele*. Codul demonstrează, de asemenea, o utilizare a două modele care joacă de multe ori bine împreună: Comandă și Double Dispatch. Utilizarea eficientă a acestor modele se bazează pe utilizarea atentă a polimorfismului. Atunci când acest lucru se întâmplă, va exista o reducere a numărului de*dacă-atunci-altele*blocuri în codul nostru.

În timp ce există cazuri în care este mult mai practic de utilizat*dacă-atunci-altele*în loc de polimorfism, este mai des cazul că un stil de codare mai polimorf va produce o bază de cod mai mică, mai lizibilă și mai puțin fragilă. Numărul de oportunităţi pierdute este un simplu număr de*dacă-atunci-altele*declarații în codul nostru.

De[Kirk Pepperdine](http://programmer.97things.oreilly.com/wiki/index.php/Kirk_Pepperdine)
