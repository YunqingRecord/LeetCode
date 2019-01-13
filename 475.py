import bisect


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        radius = float('inf')
        ans = 0
        houses = sorted(houses)
        heaters= sorted(heaters)
        for house in houses:
            lf = bisect.bisect_right(heaters, house)
            if lf > 0:
                radius = min(radius, house-heaters[lf-1])
            ri = bisect.bisect_left(heaters, house)
            if ri < len(heaters):
                radius = min(radius, heaters[ri] - house)
            ans = max(ans, radius)
        return ans
