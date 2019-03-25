# 快速排序


def QuickSort1(ls):
    '''

    :param ls:  the arrayt to be sorted
    :return:  the sorted list by using iteration
    '''
    if len(ls) == 1:
        return ls
    small = []
    big = []
    try:
        base = ls.pop(0)
    except:
        return ls
    for num in ls:
        if num <= base:
            small.append(num)
        else:
            big.append(num)
    return QuickSort1(small)+[base]+QuickSort1(big)


def QuickSort2(ls):
    '''
    : The Classic quick sort algorithm
    :param ls: the list to be sorted
    :return:  the result
    '''
    def partition(ls, left, right):
        '''
        :param ls:  the array to be divided
        :param left:the start point from left
        :param right:the start point from right
        :return: the partition base
        '''
        base = left
        while left < right:  # 目标是从小排到大
            while left < right and ls[right] >= ls[base]:  # 如果大于base，那么判断通过，判断下一个
                right -= 1   # 相当于pass，在不通过的时候right停下，存着
            while left < right and ls[left] <= ls[base]:   # 如果小于base， 那么判断通过，判断下一个
                left += 1   # 相当于pass，不通过的时候left停下，存着
            ls[right], ls[left] = ls[left], ls[right]   # 把不通过的字符相互交换位置
        ls[base], ls[left] = ls[left], ls[base]   # 交换base与处理之后的left的位置，这个left相当于小于base的子序列的数，是最后一个
        return left

    def quick(ls, left, right):
        if left > right:
            return ls
        mid = partition(ls, left, right)
        quick(ls, left, mid-1)
        quick(ls, mid+1, right)
    n = len(ls)
    quick(ls, 0, n-1)
    return ls


m = [2, 1, 4, 3, 5]

x = QuickSort2(ls=m)
print(x)

