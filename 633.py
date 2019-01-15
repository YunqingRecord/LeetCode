import math


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        high = int(math.sqrt(c))
        low = 0
        while low <= high:
            sum = low * low + high * high
            if sum == c:
                return True
            elif sum > c:
                high -= 1
            else:
                low += 1
        return False


'''
直接遍历会超时，所以从两端开始
'''
