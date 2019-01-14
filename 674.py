class Solution:
    def findLengthOfLCIS(self, nums):
        if nums == []:
            return 0
        cur = []
        cur.append(nums[0])
        ans = 0
        i = 1
        flag = 0
        while i <= len(nums) - 1:
            if nums[i] <= nums[i - 1]:
                flag = 1
                if ans < len(cur):
                    ans = len(cur)
                if ans >= 1 / 2 * len(nums):
                    return ans
                cur.clear()
                cur.append(nums[i])
                i += 1
            else:
                cur.append(nums[i])
                i += 1
                if ans < len(cur):
                    ans = len(cur)
        if flag == 0:
            return len(cur)
        else:
            return ans
