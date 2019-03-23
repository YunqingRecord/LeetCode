# Time Complexity:O(n**2)
# Space Complexity:O(1)


def InsertionSort(ls):
    '''

    :param ls: the list to be sorted
    :return:  the sorted list by insertion algo.
    '''
    n = len(ls)
    for i in range(1, n):
        j = i
        target = ls[i]  # The value to be inserted
        while j > 0 and target > ls[j-1]:
            ls[j] = ls[j-1]
            j = j-1
            ls[j] = target
    return ls


m = InsertionSort([1, 2, 3, 4])

print(m)




