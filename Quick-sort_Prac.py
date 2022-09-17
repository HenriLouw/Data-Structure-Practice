my_arr = [5, 8, 3, 1, 19, 20, 4]


def QuickSort(arr):

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return QuickSort(items_lower) + [pivot] + QuickSort(items_greater)


#                  3, 1 ,  {4}  ,5,8,19,20  [1ST ITERATION RETURN]
print(QuickSort(my_arr))