class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return -1
        '''
        division of special situation
        '''
        lsum = 0
        rsum = 0
        for i in range(0, len(nums)):
            for m in range(i):
                lsum += nums[m]
            for n in reversed(range(i+1, len(nums))):
                rsum += nums[n]
            if lsum == rsum:
                return i
            else:
                lsum, rsum = 0, 0
        return -1
'''
failed of big data input
'''