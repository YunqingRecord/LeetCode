class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lf = 0
        ri = len(nums)-1
        while lf < ri:
            if nums[lf] < target:
                lf += 1
            elif nums[ri] > target:
                ri -= 1
        if nums[lf] == target or nums[ri] == target:
            return nums.index(target)
        else:
            return -1


'''
Right # Left Needle  /  relatively slow   
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lf = 0
        ri = len(nums)-1
        while lf < ri:
            mid = (lf+ri) // 2
            if nums[mid] > target:
                ri = mid
            elif nums[mid] < target:
                lf = mid
        if nums[lf] ==  target or nums[ri] == target:
            return nums.index(target)
        else:
            return -1



