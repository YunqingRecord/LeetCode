class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        loc = nums.index(m)
        for i in nums:
            if m == i:
                pass
            elif m < 2 * i:
                return -1
        return loc



