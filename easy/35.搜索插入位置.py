#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)-1, -1, -1):
                if nums[i] < target:
                    nums.insert(i+1, target)
                    return i+1
                elif nums[i] == target:
                    nums.insert(i, target)
                    return i
# @lc code=end

