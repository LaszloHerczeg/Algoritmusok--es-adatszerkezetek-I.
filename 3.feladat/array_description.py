# https://cses.fi/problemset/task/1746/

def array_description(n:int, m:int, array:list):
    """
    n: a tömb mérete
    m: az értékek felső határa
    array: a tömb
    Visszaadja azon tömbök számát, amelyek megfelelnek a következő leírásnak:
    Tudjuk, hogy van egy tömb, amely n darab egész számot tartalmaz 1 és m között, 
    és bármely két szomszédos elem abszolút különbsége legfeljebb 1 lehet.
    Egy leírást kapunk a tömbről, ahol néhány érték ismeretlen lehet.
    """
    
    # létrehozom a kétdimenziós tömböt, ahol l[i][j] azt jelöli, hogy i helyen hányféleképpen lehet j érték: 
    l = [[0] * (m + 2) for _ in range(n)]

    # végigiterálok a tömb értékein:
    for i in range(n):
        # ha a tömb első eleme 0, akkor 1-től m-ig bármilyen szám előfordulhat ott:
        if i == 0:
            if array[i] == 0:
                for _ in range(1, m + 1):
                    l[i][_] = 1
            # ha a tömb első emele nem 0, akkor csak az adott szám lehet ott, egyféleképpen: 
            else:
                l[i][array[i]] = 1
        # Az első utáni elemeket vizsgálom:
        else:
            # Ha az elem 0, akkor az azt megelőző helyen lévő lehetőségek határozzák meg az értékeket:
            if array[i] == 0:
                for sub_i in range(1, m + 1):
                    l[i][sub_i] = (l[i - 1][sub_i - 1] + l[i - 1][sub_i] + l[i - 1][sub_i + 1]) % 1000000007
            # Ha az érték nem 0, akkor a feltételek miatt az előző helyen lévő, 
            # (érték - 1) + érték + (érték + 1) lehetőségek száma adja a megoldást:
            else:
                l[i][array[i]] = (l[i - 1][array[i] - 1] + l[i - 1][array[i]] + l[i - 1][array[i] + 1]) % 1000000007
    
    # összegzem az utolsó elemnél a lehetőségek számát:
    output = 0
    for value in range(1, m + 1):
        output = (output + l[n - 1][value]) % 1000000007
    
    return output % 1000000007

if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    array = list(map(int, input().split(" ")))
    print(array_description(n, m, array))
