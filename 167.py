class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        ori = nums
        nums = sorted(nums)
        lf = 0
        ri = len(nums) - 1
        while lf < ri:
            if nums[lf] + nums[ri] > target:
                ri -= 1
            elif nums[lf] + nums[ri] < target:
                lf += 1
            else:
                m = ori.index(nums[lf])
                n = ori.index(nums[ri])
                ans.append(m+1)
                ans.append(n+1)
                if m == n:
                    ans.pop()
                    ans.pop()
                    for i in range(len(ori)):
                        if ori[i] == nums[lf]:
                            ans.append(i+1)
                return ans