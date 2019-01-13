class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        S = ''
        for a in s:
            S = a + S
        return S
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

