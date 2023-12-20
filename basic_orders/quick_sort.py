def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr.pop()
    left = []
    right = []
    for item in arr:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)
list_unsort=[5,6,2,1,8,0,4,12]
print(quick_sort(list_unsort))