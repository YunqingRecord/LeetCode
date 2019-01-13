class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        AT = []
        i = 0
        while i < len(A[0]):
            atm = []
            for a in A:
                atm.append(a[i])
            i += 1
            AT.append(atm)
        return AT







