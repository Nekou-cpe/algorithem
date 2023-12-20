def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
list_unsort=[5,6,2,1,8,0,4,12]
print(insertion_sort(list_unsort))