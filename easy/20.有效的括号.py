#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        l = ["?"]
        for i in s:
            if i in d.keys():
                l.append(i)
            elif d.get(l.pop()) != i:
                return False
        return len(l) == 1
            
# @lc code=end

