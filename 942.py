class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)
        ni, nd = 0, N
        ans = []
        for s in S:
            if s == 'I':
                ans.append(ni)
                ni += 1
            elif s == 'D' :
                ans.append(nd)
                nd -= 1
        ans.append(ni)

        return ans




