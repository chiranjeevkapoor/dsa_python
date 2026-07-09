def rotateArray(arr: list, k: int) -> list:
    n = len(arr)
    temp = arr[:k]

    for i in range(k, n):
        arr[i-k] = arr[i]
    
    for i in range(n-k, n):
        arr[i] = temp[i - (n-k)]
    return arr
