
# 机理：每次遍历都把更大数值通过与相邻数值交换，让其逐渐靠后，排到末尾。
# 这样， 就可以逐渐把需要的数值逐渐交换到前面来，实现排序。
# Key: 从后往前排

# time complexity:
# O(n**2)
# space Complexity:
# O(1)


def BubbleSort(ls):
    '''
    :param ls:  THE Given list to be sorted
    :return:  the sorted list using bubble algorithm
    '''
    n = len(ls)
    for i in range(n-1):  # 最坏情况下，一共要遍历n-1次，才能把所有排序排完
        for j in range(n-i-1):  # 每次需要判断 n-i-1次，因为每外部循环一次，就少一个需要排序的
            if ls[j] < ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j] # 只能交换，不能赋值，因为不能改变原有的数据
    return ls


ls1 = [1, 2, 3, 4]
print(BubbleSort(ls1))


