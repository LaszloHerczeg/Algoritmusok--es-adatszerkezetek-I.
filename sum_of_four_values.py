# https://cses.fi/problemset/task/1642/

n, x = map(int, input().split(" "))
array = list(map(int, input().split(" ")))



def sum_of_four_values(n:int, x:int, array:list):
    sorted_array = [(array[i], i + 1) for i in range(n)]
    sorted_array.sort()
    for i in range(n - 3):
        target = x - sorted_array[i][0]
        for sub_i in range(i + 1, n - 2):
            sub_target = target - sorted_array[sub_i][0]           
            left = sub_i + 1
            right = n - 1
            while left < right:
                if sorted_array[left][0] + sorted_array[right][0] == sub_target:
                    return (sorted_array[i][1], sorted_array[sub_i][1], sorted_array[left][1], sorted_array[right][1])
                elif sorted_array[left][0] + sorted_array[right][0] < sub_target:
                    left += 1
                else:
                    right -= 1
        
    return "IMPOSSIBLE"


if __name__ == "__main__":
    solution = sum_of_four_values(n, x, array)
    if solution == "IMPOSSIBLE":
        print(solution)
    else:
        for item in solution:
            print(item, end= " ")