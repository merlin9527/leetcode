#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        count = 1
        res = ""
        for i in range(len(s)):
            if i == 0:
                count = 1
            elif s[i] == s[i-1]:
                count += 1
            elif s[i] != s[i-1]:
                ss = f"{count}{s[i-1]}"
                res += ss
                count = 1

            if i == len(s)-1:
                ss = f"{count}{s[i]}" 
                res += ss
        return res 
# @lc code=end

