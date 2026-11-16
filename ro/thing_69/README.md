# Pune mouse-ul jos și pas departe de tastatură

Te-ai concentrat ore în şir pe o problemă şi nu există nici o soluţie. Aşa că te ridici să-ţi dezmorţeşti picioarele, sau să loveşti automatele, şi când te întorci, răspunsul devine evident.

Ţi se pare cunoscut acest scenariu? Te-ai întrebat vreodată de ce se întâmplă? Trucul este că, în timp ce sunteți de codificare, partea logică a creierului este activă și partea creativă este închisă. Nu-ţi poate prezenta nimic până când partea logică nu ia o pauză.

Iată un exemplu din viaţa reală: curăţam un cod de moştenire şi am dat peste o metodă "interesantă." Acesta a fost proiectat pentru a verifica dacă un șir conținea un timp valabil folosind formatul*hh:mm:ss xx*, unde*hh*reprezintă ora;*mm*reprezintă minute;*ss*reprezintă secunde; și*xx*este fie*AM*sau*PM*.

Metoda a folosit următorul cod pentru a converti două caractere (reprezentând ora) într-un număr, și a verifica dacă a fost în intervalul adecvat:

```
try {
    Integer.parseInt(time.substring(0, 2));
} catch (Exception x) {
    return false;
}

if (Integer.parseInt(time.substring(0, 2)) > 12) {
    return false;
}
```

Acelaşi cod a apărut de două ori mai mult, cu modificările corespunzătoare la caracterul offset şi limita superioară, pentru a testa minute şi secunde. Metoda sa încheiat cu aceste linii pentru a verifica pentru AM și PM:

```
if (!time.substring(9, 11).equals("AM") &
    !time.substring(9, 11).equals("PM")) {
    return false;
}
```

Dacă nici una dintre aceste serii de comparaţii nu a eşuat, întorcându-se fals, metoda a revenit la adevăr.

În cazul în care codul anterior pare Wordy și dificil de urmat, nu vă faceți griji. Şi eu am crezut la fel, ceea ce înseamnă că am găsit ceva care merită curăţat. Am readus-o şi am scris câteva teste, doar ca să mă asigur că încă funcţionează.

Când am terminat, m - am simţit mulţumit de rezultate. Noua versiune a fost ușor de citit, jumătate din dimensiunea, și mai precis, deoarece codul original testat doar limita superioară pentru ore, minute și secunde.

În timp ce mă pregăteam de muncă a doua zi, mi-a venit o idee: De ce nu validați șir folosind o expresie regulată? După câteva minute de dactilografiere, am avut o implementare de lucru într-o singură linie de cod. Aici este:

```
public static boolean validateTime(String time) {
    return time.matches("(0[1-9]|1[0-2]):[0-5][0-9]:[0-5][0-9] ([AP]M)");
}
```

Ideea acestei poveşti nu este că am înlocuit în cele din urmă peste treizeci de linii de cod cu doar una. Ideea e că până am scăpat de computer, am crezut că prima mea încercare a fost cea mai bună soluţie la problemă.

Data viitoare când mai ai o problemă urâtă, fă-ţi o favoare. Odată ce ați înțeles într-adevăr problema du-te face ceva care implică partea creativă a creierului tău schița problema, asculta unele muzică, sau doar să ia o plimbare afară. Uneori, cel mai bun lucru pe care îl puteți face pentru a rezolva o problemă este de a pune mouse-ul jos și pas departe de tastatură.

De[BurkHufnagel](http://programmer.97things.oreilly.com/wiki/index.php/BurkHufnagel)