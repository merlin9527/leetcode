#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a = 1
            b = 2
            res = 0
            for _ in range(3, n+1):
                res = a + b
                a = b
                b = res
        return res
            
# @lc code=end

