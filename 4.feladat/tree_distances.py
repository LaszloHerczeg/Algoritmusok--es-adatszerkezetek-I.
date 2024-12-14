# https://cses.fi/problemset/task/1132/

from collections import defaultdict, deque

def build_tree(edges):
    """
    Létrehoz egy szomszédsági listát a fa reprezentálására
    """

    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    return tree

def bfs(tree, start):
    """
    Végrehajt egy szélességi bejárást, visszaadva a legtávolabbi csomópontot és a bejárt csúcsoktól vett távolságot
    """
    queue = deque([(start, -1, 0)])  # aktuális csomópont, szülő, távolság
    farthest_node = start
    max_distance = 0

    distances = [-1] * (len(tree) + 1)
    distances[start] = 0

    while queue:
        node, parent, distance = queue.popleft()
        for neighbor in tree[node]:
            if neighbor != parent:  # Ne menjünk vissza a szülő csomópontra
                distances[neighbor] = distance + 1
                queue.append((neighbor, node, distance + 1))
                if distance + 1 > max_distance:
                    max_distance = distance + 1
                    farthest_node = neighbor

    return farthest_node, distances

def find_max_distances(n, edges):
    """
    Meghatározza minden csomópontra a maximális távolságot.
    """
    if n == 1: return [0]

    tree = build_tree(edges)

    # 1. Találjuk meg a fa egyik átmérőjének egyik végpontját
    farthest_node, _ = bfs(tree, 1)

    # 2. Végezünk egy BFS-t innen az átmérő másik végpontjának megtalálásához
    other_end, distances_from_first = bfs(tree, farthest_node)

    # 3. Végezünk egy BFS-t az átmérő másik végpontjából
    _, distances_from_second = bfs(tree, other_end)

    # 4. Minden csomópontra a két távolság maximumát vesszük
    max_distances = [max(distances_from_first[i], distances_from_second[i]) for i in range(1, n + 1)]

    return max_distances


if __name__ == "__main__":
    n = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

    result = find_max_distances(n, edges)

    for item in result:
        print(item, end = " ")
