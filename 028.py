class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        elif needle == '':
            return 0
        else:
            num = 0
            flag = len(needle)
            i = 0
            while i < len(haystack):
                while num < flag:
                    if needle[num] == haystack[i]:
                        num += 1
                        i += 1
                    else:
                        i -= (num - 1)
                        num = 0
                if num == flag:
                    ans = i - flag
                    return ans


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle not in haystack:
        return -1
    elif needle == '':
        return 0
    else:
        num  = 0
        flag = len(needle)
        i = 0
        while i < len(haystack):
            while num < flag:
                if needle[num] == haystack[i]:
                    num += 1
                    i   += 1
                else:
                    i  -= (num-1)
                    num = 0
            if num == flag:
                ans = i-flag
                return ans


haystack = "mississippi"

needle = "issip"

m =strStr(haystack = haystack, needle = needle)
print(m)
