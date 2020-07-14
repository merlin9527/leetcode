#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            middle = left + (right - left) // 2
            middle_square = middle ** 2
            if middle_square == x:
                return middle
            elif middle_square > x:
                right = middle - 1
            else:
                left = middle + 1
        return right
# @lc code=end

