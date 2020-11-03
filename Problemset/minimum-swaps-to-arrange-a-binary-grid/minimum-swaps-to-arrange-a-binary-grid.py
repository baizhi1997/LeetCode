
# @Title: 排布二进制网格的最少交换次数 (Minimum Swaps to Arrange a Binary Grid)
# @Author: qinxinlei
# @Date: 2020-08-06 12:56:41
# @Runtime: 104 ms
# @Memory: 13.9 MB

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        # 统计每一行 从右向左连续0的个数
        n = len(grid)
        zero_nums = []
        for i in range(n):
            j = n - 1
            while j >= 0 and grid[i][j] == 0: j -= 1
            zero_nums.append(n - 1 - j)
        # 贪心算法，从上到下查找满足条件的最小下标，即为交换到当前行的次数
        cnt = 0
        for i in range(n - 1):
            need_zeros = n - 1 - i

            j = i
            while j < len(zero_nums) and zero_nums[j] < need_zeros: j += 1
            
            # 没找到则说明不满足条件
            if j == len(zero_nums): return -1

            # 增加交换次数
            cnt += j - i
            # 交换数值
            while j > i:
                zero_nums[j], zero_nums[j-1]= zero_nums[j-1], zero_nums[j]
                j -= 1
        return cnt

                
