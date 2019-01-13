class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bi = str(bin(num).replace('0b', ''))
        ans = ''
        for b in bi:
            if b == '1':
                ans += '0'
            else:
                ans += '1'
        return int(ans, 2)

