class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n)[:1:-1]
        return int(n + '0'*(32-len(n)), 2)

    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = bin(n)[2:].zfill(32)
        ans = ans[::-1]
        return int(ans, 2)