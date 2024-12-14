# 2.feladat - Rekurzió
## Increasing Array
[A feladat linkje](https://cses.fi/problemset/task/1094/)

### Stratégia
Az algoritmus elemenként végigjárja a tömböt és ha a vizsgált elem kisebb, mint az őt megelőző, akkor addig növeli az értékét, amíg az egyenlő lesz vele. Minden egyes növelés 1 lépésnek számít, az algoritmus a lépések számával tér vissza.

1. Rekurzív algoritmus, így felvesszük a bázisesetet. Ha elértük a tömb végét, akkor visszatérünk a lépések számával.
<br> `if index == len(array):`
<br> `return moves`

2. Ha az aktuális elem kisebb, mint az öt megelőző elem, akkor az elemet egyelőre változtatjuk az öt megelőzővel és a lépések számát megnöveljük a két érték különbségével:
<br> `if array[index] < array[index - 1]:`
<br> `moves += array[index - 1] - array[index]`
<br> `array[index] = array[index - 1]`

3. Az algoritmus rekurzívan meghívja saját magát az eggyel magasabb indexű elemre:
<br> `return increasing_array(array, index + 1, moves)`