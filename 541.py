class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ''
        if s == '':
            return s
        while s != '':
            if len(s) <= k:
                ans += s[::-1]
                return ans
            if k <= len(s) <= 2 * k:
                rev = s[k - 1::-1]
                left = s[k:]
                ans += rev + left
                return ans
            elif len(s) > 2 * k:
                rev = s[k - 1::-1]
                left = s[k:2 * k]
                ans += rev + left
                s = s.replace(s[0:2 * k], '')


