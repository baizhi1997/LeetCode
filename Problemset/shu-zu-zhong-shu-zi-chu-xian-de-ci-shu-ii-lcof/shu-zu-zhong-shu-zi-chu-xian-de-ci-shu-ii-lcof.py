
# @Title: 数组中数字出现的次数 II (数组中数字出现的次数 II LCOF)
# @Author: qinxinlei
# @Date: 2020-05-14 17:38:41
# @Runtime: 76 ms
# @Memory: 14.4 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
        
