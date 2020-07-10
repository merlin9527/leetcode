#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        flag = True if x >= 0 else False
        x = str(abs(x))
        x = int(x[::-1])
        if not flag:
            x = 0 - x
        if -2**31 < x < 2**31:
            return x
        else:
            return 0 

# @lc code=end

