# Testdriven utveckling
## Vecka 24

<!-- TOC -->
* [Testdriven utveckling](#testdriven-utveckling)
  * [Vecka 24](#vecka-24)
    * [Status uppgifter](#status-uppgifter)
    * [Mina svar](#mina-svar-)
      * [<ins>Läsa of förstå kod</ins> ✅](#insläsa-of-förstå-kodins-)
      * [<ins>Öva på TDD</ins> ✅](#insöva-på-tddins-)
      * [<ins>Söka efter användare</ins> 🟡](#inssöka-efter-användareins-)
      * [<ins>Multiplikationstabellen</ins> ✅](#insmultiplikationstabellenins-)
      * [<ins>Balansera listor</ins> ✅](#insbalansera-listorins-)
<!-- TOC -->


### Status uppgifter

| Uppgift                     | Status| 🟠🟡🟢  |
|-----------------------------|-------|----------|
| 1 Läsa och förstå kod       | 100%  | 🟢       |
| 2 Öva på TDD                | 100%  | 🟢       |
| 3 Söka efter användare      | 40%   | 🟡       |
| 4 Multiplikationstabellen   | 100%  | 🟢       |
| 5 Balansera Listor          | 100%  | 🟢       |


### Mina svar 
#### <ins>Läsa of förstå kod</ins> ✅

**Vilka ekvivalensklasser har uttrycken?**

1a. <br> x > 100

Svar: Minst 2st. True = 101 och uppåt / False = 100 och nedåt.

1b. <br> y == 42

Svar: Minst 2st. True = 42 / False = Under eller över 42

1c. <br> len(text) >= 5

Svar: Minst 2st. True = 5 och uppåt / False = 4 och nedåt. 

1d. <br> z == True

Svar: Minst 2st. True = z / False != z.

1e. <br> 8 < v < 16

Svar: 5st. 1 under 8 / 8 / v / 16 / 1 över 16.

1f. <br> w == 32 or w == 64 or w == 128

Svar: Minst 4. 32, 64, 128 och minst en siffra utöver det.

1g. <br> if x < 5: … elif x < 10: … elif x < 15: … else … 

Svar: 4st. 1 mindre än 5 / 1 mellan 5 - 9 / 1 mellan 10 - 14 / 1 över 15.


---
#### <ins>Öva på TDD</ins> ✅


1a. <br>Hittat på testdata i test_temperatur.

1b. <br>parametern degree har 2 ekvivalensklasser. None eller grader Fahrenheit.

1c. <br>Som en amerikansk badgäst,
vill jag kunna omvandla temperaturen i vattnet från grader Celsius till grader Fahrenheit,
så att jag vet hur varmt det är i vattnet.

2a.

Krav:
    Funktionen skall räkna varje serie tecken som separeras med mellanslag.
    
AK:
    1. Strängen "Detta är en serie tecken" == 5.
    2. Strängen "D3.*a /r också en seri3 t3c-3n." == 6.


2b. <br>"test_count_words"

2c. <br>Check!

3a.

Krav: <br><br>
    Syfte: Beräkna medianen vid ojämnt antal element. Beräkna medelvärdet på de två mittersta talen när det är ett jämnt antal element.


AK: <br><br>
    1. Listan ska vara sorterad i stigande ordning när beräkning görs.
    2. Om funktionen anropas med en tom lista; returnera 'None'
    3. Om funktionen anropas med en lista med ett ojämnt antal numeriska element; returnera medianen av listan.
    4. Om funktionen anropas med en lista med ett jämnt antal numeriska element; returnera medelvärdet på summan av talen.

3b. <br><br>test_median

3c. <br><br> Done.


4a. <br><br>
    Två st. True och False.

4b. <br>
Krav: <br><br> En funktion som kontrollerar att en inmatad lista är sorterad i stigande ordning.

AK: <br><br> Funktionen ska returnera True om listan numbers är sorterad i stigande ordning. Annars False.

4c. test_sort_numbers.py

___

#### <ins>Söka efter användare</ins> 🟡

Krav: <br><br>
    Låt användare söka i 'master-listan' och visa förslag baserat på innehållet i listan
    vart eftersom användaren skriver in tecken i ett sökfält.

AK: <br><br>
    Funktionen ska ta två parametrar: input är det användaren skriver, master_list är en lista med alternativ som kan hittas.
    Förslagen skall dyka upp direkt under tiden användaren fyller i tecken.


---

#### <ins>Multiplikationstabellen</ins> ✅

Krav: <br><br>
    Skapa en funktion som tar två parametrar. En parameter som talar om vilken multiplikationstabell
    som ska användas och en parameter som talar om hur många steg som ska multipliceras.
        

AK: <br><br>
    * Exemplet ifrån veckouppgiften ska fungera.  
    * När någon av parametrarna är 0 så ska 0 returneras. Testa en parameter i taget.  
    * Det ska fungera att mata in negativa värden i första parametern med matematiskt korrekt resultat.  


---


#### <ins>Balansera listor</ins> ✅

Krav:
    Två listor behöver balanseras genom att flytta element från den längre listan till den kortare.
    Listorna ska ha så jämna antal element som möjligt.

AK:
    När en lista har minst 2 element mer än den andra listan så ska balansering ske. Annars görs ingenting.
    Returnera listorna när jobbet är klart.


---




