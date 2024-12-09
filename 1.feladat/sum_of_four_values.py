# https://cses.fi/problemset/task/1642/

# Input felvétele:
n, x = map(int, input().split(" "))
array = list(map(int, input().split(" ")))



def sum_of_four_values(n:int, x:int, array:list):
    """
    Paraméterek:
    -n: a kapott tömb mérete
    -x: a megcélzott összeg
    -array: a kapott tömb
    A funkció megkeresi, azt a 4 külöböző pozícióban található egész számot a tömbben, amelyeknek az összege x-szel egyenlő és visszaadja ezeknek a pozícióját. A pozíciók jelölése 1-gyel kezdődik a tömbben.
    Ha nincs ilyen négy szám a tömbben, visszaadja az "IMPOSSIBLE" stringet.
    """

    # Létrehozok egy új tömböt, amelyben az eredeti tömb elemeit párosítom az indexekkel és rendezem őket:
    sorted_array = [(array[i], i + 1) for i in range(n)]
    sorted_array.sort()

    # Végigiterálok a tömb elemein:
    # Először kiválasztom a 4 keresett elemből az elsőt:
    for i in range(n - 3):
        
        target = x - sorted_array[i][0]
        # Kiválasztom a 2. elemet:
        for sub_i in range(i + 1, n - 2):
            sub_target = target - sorted_array[sub_i][0]
            # Kiválasztom a 3. és a 4. elemet:
            left = sub_i + 1
            right = n - 1
            while left < right:
                # Ha az összeg egyenlő a megcélzott értékkel, akkor visszaadom az egészek pozícióját:
                if sorted_array[left][0] + sorted_array[right][0] == sub_target:
                    return (sorted_array[i][1], sorted_array[sub_i][1], sorted_array[left][1], sorted_array[right][1])
                # Ha a kapott érték túl alacsony, akkor a 3. elem indexét növelem:
                elif sorted_array[left][0] + sorted_array[right][0] < sub_target:
                    left += 1
                # Ha a kapott összeg túl nagy, a 4. elem indexét csökkentem:
                else:
                    right -= 1
    # Ha az iteráció végbement és a funkció nem adott értéket, akkor nincsenek olyan számok, amiknek az összege megfelelő lenne:
    return "IMPOSSIBLE"


if __name__ == "__main__":
    solution = sum_of_four_values(n, x, array)
    if solution == "IMPOSSIBLE":
        print(solution)
    else:
        for item in solution:
            print(item, end= " ")
