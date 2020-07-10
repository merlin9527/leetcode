#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if (val not in nums) or (not nums):
            return len(nums)
        else:
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == val:
                    nums.pop(i)
            return len(nums)


# @lc code=end

