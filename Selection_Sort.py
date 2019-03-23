
# Time Complexity： O（n**2）
# Space Comlpexity O(1)
# 实现过程：每次遍历时，找到整个数组中尚未排序的数值中最大值的坐标，
# （上述过程体现在外部循环是i时，内部循环从i+1开始）然后赋给maxindex
# 至此，在每一次遍历之中已经找到了最大值的索引，并存在了maxindex里面。
# 接下来，通过索引把最大值的数值与现在值为现在遍历的轮次数（也就是i）交换，
# 意思是把最大值安排到第i个位置上，这样就实现了每次遍历都把目前最大的值给第i位的功能
# 由于只需要排n-1次，剩下那个就自动排在了应该的位置，所以最多只需要遍历 n-1 次


def Selection_Sort(ls):
    '''
    :param ls:  The list to be sorted from start to end
    :return: the sorted list
    '''
    n = len(ls)
    for i in range(n-1):
        maxindex = i
        for j in range(i+1, n):
            if ls[j] > ls[maxindex]:
                maxindex = j
        if maxindex != i:
            ls[i], ls[maxindex] = ls[maxindex], ls[i]
    return ls


m = Selection_Sort([1, 2, 3, 4])
print(m)

