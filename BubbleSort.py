def BubbleSort(ls):
    '''
    :param ls:  THE Given list to be sorted
    :return:  the sorted list using bubble algorithm
    '''
    n = len(ls)
    for i in range(n):  # 最坏情况下，一共要遍历n次，才能把所有排序排完
        for j in range(n-i-1):  # 每次需要判断 n-i-1次，因为每外部循环一次，就少一个需要排序的
            if ls[j] < ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls


# time complexity:
# O(n**2)
# space Complexity:
# O(1)
