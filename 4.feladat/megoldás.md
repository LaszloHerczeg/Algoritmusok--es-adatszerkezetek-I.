# 4.feladat - Fák, gráfok
## Tree Distances I.
[A feladat linkje](https://cses.fi/problemset/task/1132/)

### Stratégia
Szélességi bejárást hajtok végre a gyökérpontból, ezzel meghatározom a fa egyik végpontját, majd ebből a végpontból ismételten végrehatok egy szélességi bejárást, ami közben elraktározom az első végponttól vett távolságokat és aminek köszönhetően megtalálom a 2. végpontot. A 2. végpontból ismét végrehajtok egy szélességi bejárást és elraktározom a tőle vett távolságokat. Visszaadom minden csúcsra a végpontoktól vett távolságok maximumát.

1. Egy alapesetet kezelek. Ha inputként egy csúcsot kapunk, akkor a visszaadott érték 0:
<br> `if n == 1: return [0]`


2. Létrehozok egy szomszédsági listát, amit eltárolok. Végigiterálok az inputként kapott éleken és felveszem az értéket a megfelelő listába:
<br> `def build_tree(edges):`
<br> `tree = defaultdict(list)`
<br> `for a, b in edges:`
<br> `tree[a].append(b)`
<br> `tree[b].append(a)`
<br> `return tree`
<br> `tree = build_tree(edges)`

3.  Egy queue segítségével hajtom végre a szélességi bejárást, amiben mindig az aktuális csúcsot, azt a csúcsot, ahonnan érkeztem és a kezdponttól vett távolságot.
<br> `queue = deque([(start, -1, 0)])  # aktuális csomópont, szülő, távolság`
<br> `farthest_node = start`
<br> `max_distance = 0`

4. Felveszek egy segédtömböt, amiben elraktározom a csúcsok kezdőponttól vett távolságát:
<br> `distances = [-1] * (len(tree) + 1)`
<br> `distances[start] = 0`

5. Elkezdem a bejárást. A queue-ból eltávolítom az aktuális csúcs információit és végigiterálok a csúcs szomszédjain a szomszédsági listából. 
<br> `while queue:`
<br> `node, parent, distance = queue.popleft()`
<br> Azokat a szomszédokat járom be, amelyeken még nem voltam:
<br> `for neighbor in tree[node]:`
<br> `if neighbor != parent:`
<br> A távolsághoz hozzáadok egyet a segédtömbben:
<br> ` distances[neighbor] = distance + 1`
<br> Hozzáadom az új csúcsot a queue-ba, hiszen a következő lépésekben azt is fogom vizsgálni:
<br> `queue.append((neighbor, node, distance + 1))`
<br> Ha a kapott távolság nagyobb, mint az eddig talált legnagyobb távolság, akkor beállítom ezt a csúcsot, mint eddig talált legtávolabbi csúcs és visszaadom a megfelelő értékeket:
<br> `max_distance = distance + 1`
<br> `farthest_node = neighbor`

6. Az első bejárást a gyökérpontból végzem el, ezzel megtalálom az első végpontot:
<br> `farthest_node, _ = bfs(tree, 1)`

7. A második bejárást az első végpontból végzem el, ezzel megtalálom a 2. végpontot és eltárolom a csúcsok első végponttól vett távolságait:
<br> `other_end, distances_from_first = bfs(tree, farthest_node)`

8. A harmadik bejárást a második végpontból végzem el és eltárolom a csúcsok tőle vett távolságait:
<br> `_, distances_from_second = bfs(tree, other_end)`

9. Veszem a csúcsok végpontoktól vett távolságainak a maximumát és visszaadom azt:
<br> `max_distances = [max(distances_from_first[i], distances_from_second[i]) for i in range(1, n + 1)]`
<br> `return max_distances`

10. Standard outputon megjelenítem az értékeket:
<br> `for item in result:`
<br> `print(item, end = " ")`