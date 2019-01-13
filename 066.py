class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ss = ''
        ans = []
        for num in digits:
            ss += str(num)
        num = str(int(ss)+1)
        for n in num:
            ans.append(int(n))
        return ans
