#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,j in enumerate(nums):
            dic[j] = i
        for i,n in enumerate(nums):
            j = dic.get(target - n)
            if j is not None and j != i:
                return [i, j]
            else:
                continue

# @lc code=end

