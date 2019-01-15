class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        lf = 1
        ri = (1/2)*num
        while lf <= ri:
            mid = (lf+ri)//2
            if mid**2 > num:
                ri = mid - 1
            elif mid**2 < num:
                lf = mid+1
            else:
                return True
        return False
