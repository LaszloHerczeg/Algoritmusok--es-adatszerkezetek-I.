import sys
sys.setrecursionlimit(200000)

def increasing_array(array:list, index = 1, moves = 0):
    """
    Rekurzív módon meghatározza a minimális lépések számát ahhoz, hogy a tömb növekvővé váljon.
    arr (list): A tömb elemei
    index (int): Az aktuális index a tömbben
    moves (int): Az eddig végrehajtott lépések száma

    Returns:
        int: A minimális lépések száma
    """
    # Báziseset: Ha elértük a tömb végét, visszatérünk az összesített lépésekkel
    if index == len(array):
        return moves

    # Ha az aktuális elem kisebb, mint az előző, növeljük a szükséges értékre
    if array[index] < array[index - 1]:
        moves += array[index - 1] - array[index]
        array[index] = array[index - 1]  # Az aktuális elem értékét módosítjuk

    # Következő elem feldolgozása
    return increasing_array(array, index + 1, moves)

# Bemenet
if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    # Eredmény kiírása
    print(increasing_array(array))
