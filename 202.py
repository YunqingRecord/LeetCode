class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans = 0
        n = str(n)
        flag = 0
        while ans != 1:
            ans = 0
            flag += 1
            for num in n:
                ans += int(num) ** 2
            n = str(ans)
            if flag > 6:   # did not know why 6 yet
                return False
        else:
            return True
