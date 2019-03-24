# Time Complexity:O(n**2)
# Space Complexity:O(1)


def InsertionSort(ls):
    '''

    :param ls:  the list to be sorted
    :return:  the sorted list
    '''
    n = len(ls)
    for i in range(1, n):  # 为什么是 1开始，因为从已经排好的序列末尾开始向前比较。后面会出现i-1
        j = i
        target = ls[i]  # 每次要插入的数值， 需要额外空间的地方
        while j > 0 and target > ls[j-1]:  # 对已经排好的序列，从后往前逐渐比较
            ls[j] = ls[j-1]  # 如果已经排序的最后一位比目标值更小，那么让位出来，重复此过程
            j = j-1  # 位次往前轮, 如果下次也这样，那么继续腾位置，改变的只有一个值。
        ls[j] = target
    return ls


m = InsertionSort([1, 3, 2, 4, 5, 9, 4])

print(m)