#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        else:
            for i in range(len(nums)-1, 0, -1):
                if nums[i] == nums[i-1]:
                    nums.pop(i)
            return len(nums)
            
# @lc code=end

