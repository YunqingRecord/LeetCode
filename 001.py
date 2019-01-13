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
                ans.append(m)
                ans.append(n)
                if m == n:
                    ans.pop()
                    ans.pop()
                    for i in range(len(ori)):
                        if ori[i] == nums[lf]:
                            ans.append(i)
                return ans


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ans = []
    ori = nums
    nums = sorted(nums)
    lf = 0
    ri = len(nums)-1
    while lf < ri:
        if nums[lf]+nums[ri] > target:
            ri -= 1
        elif nums[lf]+nums[ri] < target:
            lf += 1
        else:
            m = ori.index(nums[lf])
            n = ori.index(nums[ri])
            ans.append(m)
            ans.append(n)
            if m == n:
                ans.clear()
                for i in range(len(ori)):
                    if ori[i] == nums[lf]:
                        ans.append(i)
            return ans


nums1 = [3, 3]
target1 = 6
ans = twoSum(nums1, target1)
print(ans)