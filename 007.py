class Solution:
    def reverse(self, x):
        strr = list(str(x))
        ans = []
        final = ''
        if strr[0] == '-':
            ans.append(strr[0])
            strr.remove(strr[0])
        for i in reversed(strr):
            ans.append(i)
        for el in ans:
            final += el
        final = int(final)
        if final >= 2**31 or final < (-2**31) or final == 0 :
            return 0
        return int(final)