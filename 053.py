class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curans = 0
        maxans = nums[0]
        for i in range(len(nums)):
            curans += nums[i]
            maxans = max(curans, maxans)
            if curans < 0:
                curans = 0
        return maxans
