#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            length = len(nums)
            middle = length // 2
            
            left_max = self.maxSubArray(nums=nums[0:middle])
            right_max = self.maxSubArray(nums=nums[middle:length])
            
            left_val = nums[middle - 1]
            left_res = 0
            for i in range(middle-1, -1 , -1):
                left_res += nums[i]
                left_val = max(left_res, left_val)
            
            right_val = nums[middle]
            right_res = 0
            for j in range(middle, length):
                right_res += nums[j]
                right_val = max(right_res, right_val)
            
            return max(left_max, right_max, right_val+left_val)
            

            
                     
# @lc code=end

