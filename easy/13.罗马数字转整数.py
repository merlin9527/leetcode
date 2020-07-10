#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        if dic.get(s):
            return dic.get(s)
        else:
            l = list(s)
            res_list = []
            max_index = len(l) - 1
            for index, value in enumerate(l):
                next_index = index + 1
                if next_index <= max_index:
                    next_value = l[next_index]
                    if (value == "I" and next_value in ["V", "X"]) or (value == "X" and next_value in ["L", "C"]) or (value == "C" and next_value in ["D", "M"]):
                        res_list.append(-dic.get(value))
                    else:
                        res_list.append(dic.get(value))
                else:
                    res_list.append(dic.get(value))
            return sum(res_list)
                    
                        
                

# @lc code=end

