
# @Title: 子数组和排序后的区间和 (Range Sum of Sorted Subarray Sums)
# @Author: qinxinlei
# @Date: 2020-07-31 15:58:49
# @Runtime: 364 ms
# @Memory: 36.1 MB

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        if not nums:
            return 0
        sum_nums = []
        
        for i in range(n):
            temp = nums[i]
            sum_nums.append(temp)  # 首先把数字本身加入列表
            for j in range(i+1, n):
                # 这里往后遍历，每次都加上一个数再加入列表
                temp += nums[j]
                sum_nums.append(temp)
                
        
        sum_nums.sort()  # 排序
        res = sum(sum_nums[left-1:right])  # 求和
        
        
        return res % 1000000007

