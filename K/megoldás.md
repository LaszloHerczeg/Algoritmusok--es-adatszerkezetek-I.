# Kollikviumi feladat - SPOJ / OKTV
## AGGRCOW - Aggressive cows
[A feladat linkje](https://www.spoj.com/problems/AGGRCOW/)

### Stratégia:
Létrehozunk egy segédfüggvényt, ami megállapítja, hogy x minimális távolságra lehetséges-e a rendezés, majd a lehetséges távolságokon bináris kereséssel végigiterálunk.

1. Definiáljuk a segédfüggvényt.
Végigiterálunk az istállók pozícióján. Ha az adott pozíció és az azt megelező közötti távolság legalább akkora, mint x, akkor az adott pozícióra elhelyezünk egy tehenet. Ha az iteráció folyamán minden tehenet elhelyeztünk, akkor a függvény True-t ad d vissza, tehát adott x minimális távolsággal elhelyezhetők a tehenek az istállókban.
<br> `def agressive_cows(x):`
<br> `cowsplaced = 1`
<br> `for i in range(1,n):`		
<br> `if positions[i] - positions[i - 1] >= x:`	
<br> `cowsplaced += 1`
<br> `if cowsplaced == c:`
<br> `return True`
<br> `return False`


2. Az istállók pozícióját egy listában eltároljuk és növekvő sorrendbe rendezzük.
<br> `	for i in range(n):`
<br> `positions.append(int(input().strip()))`
<br> `positions.sort()`

3. A segédfüggvény segítségével bináris kereséssel végigiterálunk a lehetséges távolságok halmazán.
<br >A minimális távolság lehet 0:
<br> `left = 0`
<br> A maximális távolság az első és az utolsó állás közötti távolság + 1:
<br> `right = positions[n-1] - positions[0] + 1`
<br> A ciklus addig fut, amíg a tartomány nem szűkül egy lehetséges értékre:
<br> `while right - 1 > left:`
<br> Meghatározza a középső értéket (próbált minimális távolság):
<br> `mid = (left + right) // 2`
<br> Ha lehetséges ennyi távolsággal elhelyezni a teheneket, a left értékét növeli:
<br> `if agressive_cows(mid):`
<br> `left = mid`
<br> Ha nem lehetséges, a right értékét csökkenti:
<br> `else:`
<br> `right = mid`

4. Visszaadjuk a kapott eredményt.
<br> `print(left)`
