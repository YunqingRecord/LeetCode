class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n == 2:
            return True
        while n > 2:
            n /= 2
            if n == 2:
                return True
        else:
            if n<2:
                return False


# bin function
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and bin(n).count('1') == 1