class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        numer = ['0', '1', '2', '3', '4',
                 '5', '6', '7', '8', '9']
        cou = s.count(' ')
        if s == '':
            return True
        elif cou != 0:
            s = s.replace(' ', '')
        s = list(s.lower())

        # 到此，S去掉空格并且变成小写字母
        ans = []
        l = ''
        lf = 0
        ri = len(s) - 1

        while lf < ri:
            if 'a' <= s[lf] <= 'z' or s[lf] in numer:
                l = s[lf]
                lf += 1
            else:
                lf += 1
                break
            while ri >= lf:
                if 'a' <= s[ri] <= 'z' or s[ri] in numer:
                    if l == s[ri]:
                        ri -= 1
                        break
                    else:
                        return False
                else:
                    ri -= 1
        return True

