class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        pos = []
        m = ''
        if len(A) < 2 or len(B) < 2:
            return False
        elif len(A) != len(B):
            return False

        if len(A) == len(B):
            for i in range(len(A)):
                if A[i] != B[i]:
                    pos.append(i)
            if len(pos) != 0 and len(pos) != 2:
                return False
            elif len(pos) == 0:
                if len(set(list(A))) < len(list(A)):
                    return True
                else:
                    return False
            elif len(pos) == 2:
                A = list(A)
                A[pos[0]], A[pos[1]] = A[pos[1]], A[pos[0]]
                for a in A:
                    m += a
                if m == B:
                    return True
                else:
                    return False

