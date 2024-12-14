# 1. feladat - Keresés, rendezés, mohó stratégia
## Sum of four values
[A feladat linkje](https://cses.fi/problemset/task/1642/)

### Stratégia
1. A számokat növekvő sorrendbe rendezem úgy, hogy mindegyikhez hozzárendelem az eredeti pozícióját a tömbben, mivel outputként az eredeti pozíciót kell visszaadni:
<br> `sorted_array = [(array[i], i + 1) for i in range(n)]`
<br> `sorted_array.sort()`

2. Ezután a különböző számokon végigiterálok az alábbiak szerint, ezzel keresem a megfelelő értéket.

3. Rögzítem az első értéket, a i-edik indexű elemnek (0 <= i <= n-4) és csökkentem a célösszeg értékét vele:
<br> `for i in range(n - 3):`
<br> `target = x - sorted_array[i][0]`

4. Kiválasztom a második értéket, a j-edik indexű elemnek (i+1 <= j <= n-3) és csökkentem a célösszeg értékét vele:
<br> `for j in range(i + 1, n - 2):`
<br> `j = target - sorted_array[j][0]`

5. Kiválasztom a 3. számot, a j+1-edik indexű elemnek:
<br> `left = j + 1`

6. Kiválasztom a 4. számot, mint n-1-edik indexű elem:
<br> `right = n - 1`

7. Ez után a 3. és a 4. szám összegét összehasonlítom a csökkentett célösszeggel. Ha az összeg alacsonyabb, mint a célérték, akkor a 3. választott szám a listában az eggyel nagyobb indexű lesz, ha az összeg túl nagy, akkor a 4. választott szám a listában az eggyel alacsonyabb indexű lesz. Ezt addig ismétlem, amíg az összeg meg nem egyezik a célösszeggel vagy amíg el nem fogynak a lista elemei. Ha az összeg megegyezik, visszaadom a sorszámokat. Ellenkező esetben a második számértékként az eggyel magasabb indexű számkot választom és ismétlem a lépéseket az 5. lépéstől.
<br> ` while left < right:`
<br> `elif sorted_array[left][0] + sorted_array[right][0] < sub_target:`
<br> `left += 1`
<br> `else:`
<br> `right -= 1`

8. Ha j-n végigiterálok n-3-ig és nem kapok értéket, akkor i-t megnövelem 1-gyel és folytatom a 2. lépéstől.

9. Ha az algoritmus visszaad egy értéket, akkor az egy optimális megoldás és visszaadom az indexeket. Ha az algoritmus visszaadott érték nélkül megáll, akkor nincs megfelelő eredmény.
<br> `if sorted_array[left][0] + sorted_array[right][0] == sub_target:`
<br> `return (sorted_array[i][1], sorted_array[j][1], sorted_array[left][1], sorted_array[right][1])`
<br> ` return "IMPOSSIBLE"`




