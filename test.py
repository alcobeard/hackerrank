# def plusMinus(arr):
#     # Write your code here
#     n_p, n_m, n_z = 0, 0, 0
#     for i in arr:
#         if i < 0: n_m += 1
#         if i == 0: n_z += 1
#         if i > 0: n_p += 1
#     print(round((n_p/len(arr), 6)))
#     print(round((n_p/len(arr), 6)))
#     print(round((n_p/len(arr), 6)))

# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)
        
def countingSort(arr):
    # Write your code here
    result = [0] * max((arr) + 1)
    for i in arr:
        result[i] += 1
    
    return result

arr = list(map(int, input().rstrip().split()))
countingSort(arr)

