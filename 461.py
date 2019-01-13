class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = str(bin(x).replace('0b', ''))
        by = str(bin(y).replace('0b', ''))
        num = max(len(bx), len(by))
        num1 = num - len(bx)
        num2 = num - len(by)
        final = 0
        for i in range(num1):
            bx = '0' + bx
        for j in range(num2):
            by = '0' + by
        for m in range(num):
            if bx[m] != by[m]:
                final += 1
        return final

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        m = bin(x ^ y)
        m = m.count('1')
        return m


