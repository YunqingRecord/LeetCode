class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        score = 0
        valid = []
        for op in ops:
            try:
                integer = int(op)
                valid.append(integer)
                score += integer
            except:
                if op == 'C':
                    integer = valid[-1]
                    score -= integer
                    valid.pop()
                elif op == 'D':
                    integer = 2 * valid[-1]
                    valid.append(integer)
                    score += integer
                else:
                    integer = valid[-1] + valid[-2]
                    valid.append(integer)
                    score += integer
        return score
