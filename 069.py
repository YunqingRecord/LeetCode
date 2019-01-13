import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = ''
        m = math.sqrt(x)
        m = str(m)
        for i in m:
            if i != '.':
                n += i
            else:
                return int(n)


def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    m = math.sqrt(x)
    m = math.floor(m)
    return m
