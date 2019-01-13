class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for i in range(2):
            nums.remove(max(nums))
        return max(nums)