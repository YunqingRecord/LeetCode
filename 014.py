class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        mi = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < mi:
                mi = len(strs[i])
        '''
        到此，确定了最小的字符串长度
        '''
        m = 0
        ans = ''
        while m < mi:
            flag = 0
            cur = strs[0][m]
            for i in range(len(strs)):
                if strs[i][m] == cur:
                    flag += 1
                else:
                    return ans
                if flag == len(strs):
                    ans += cur
            m += 1
        return ans