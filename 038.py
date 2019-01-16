class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        pre = '1'
        if n == 1:
            return pre

        cur = pre[0]
        temp = ''
        count = 0
        ans = ''
        for i in range(1, n):
            for j in range(len(pre)):
                if cur == pre[j]:
                    count += 1
                else:
                    temp += str(count) + cur
                    cur = pre[j]
                    count = 1
            temp += str(count) + cur
            ans = temp
            pre = temp
            cur = pre[0]
            temp = ''
            count = 0
        return ans