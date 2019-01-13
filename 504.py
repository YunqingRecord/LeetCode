class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        bit = []
        ans = ''
        if num == 0:
            return '0'
        while num > 0:
            if num == 0:
                bit = bit[::-1]
                break
            num, b = divmod(num, 7)
            bit.append(b)
        else:
            if num < 0:
                num = abs(num)
                while num >= 0:
                    if num == 0:
                        bit.append('-')
                        bit = bit[::-1]
                        break
                    num, b = divmod(num, 7)
                    bit.append(b)
        for b in bit:
            ans += str(b)
        return ans


