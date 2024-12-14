# 3.feladat - Dinamikus programozás
## Array description
[A feladat linkje](https://cses.fi/problemset/task/1746/)
### Stratégia
Egy két dimenziós tömbben eltárolom, hogy mely szám hányféleképpen fordulhat elő az eredeti listában az őt megelőző értékek alapján, majd az utolsó szám előrfordulási lehetőségeinek összegét adom vissza.

1. Létrehozom a kétdimenziós tömböt, ahol l[i][j] azt jelöli, hogy i helyen hányféleképpen lehet j érték:
<br> `l = [[0] * (m + 2) for _ in range(n)]`

2. Ezek után végigiterálok az inputként kapott tömb értékein:
<br> `for i in range(n):`

3. Ha a tömb első eleme 0, akkor 1-től m-ig bármilyen szám egyféleképpen előfordulhat ott:
<br> `if i == 0:`
<br> `if array[i] == 0:`
<br> `for _ in range(1, m + 1):`
<br> `l[i][_] = 1`

4. Ha a tömb első emele nem 0, akkor csak az adott szám lehet ott, egyféleképpen:
<br> `else:`
<br> `l[i][array[i]] = 1`

5. Az ezt követő elemeket vizsgálom:
<br> `else:`

6. Ha az elem 0, akkor végigiterálok az m lehetséges értéken a következő módon:
<br> ` if array[i] == 0:`
<br> `for j in range(1, m + 1):`
<br> `l[i][j] = (l[i - 1][j - 1] + l[i - 1][j] + l[i - 1][j + 1]) % 1000000007`

7. Ha az érték nem 0, akkor a feltételek miatt az előző helyen lévő, (érték - 1) + érték + (érték + 1) lehetőségek száma adja a megoldást:
<br> `else:`
<br> `l[i][array[i]] = (l[i - 1][array[i] - 1] + l[i - 1][array[i]] + l[i - 1][array[i] + 1]) % 1000000007`

8. Összegzem az utolsó elemnél a lehetőségek számát és visszaadom azt:
<br> `output = 0`
<br> `for value in range(1, m + 1):`
<br> `output = (output + l[n - 1][value]) % 1000000007`
<br> `return output % 1000000007`