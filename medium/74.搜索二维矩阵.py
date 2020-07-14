#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = False
        if not matrix:
            return flag
        start_index = 0  # 定义遍历行值的索引偏移量
        for rows in matrix:  # 从矩阵的右上角开始遍历,遍历出矩阵中的每一行
            for col in range(len(rows)-1-start_index, -1, -1):
                if rows[col] > target and col == 0:  # 行值如果比目标值大的话说明该列中不存在与目标值相符的项
                    start_index += 1
                elif rows[col] == target:  # 行值如果和目标值相等说明目标值存在矩阵中
                    flag = True
                    return flag
                else:  # 目标值大于的行值的最大值说明这一行中不存在与目标值相符的项
                    continue
        return flag

# @lc code=end

