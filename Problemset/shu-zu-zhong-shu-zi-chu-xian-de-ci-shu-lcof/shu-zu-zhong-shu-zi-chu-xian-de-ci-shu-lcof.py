
# @Title: 数组中数字出现的次数 (数组中数字出现的次数 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-03 21:44:20
# @Runtime: 60 ms
# @Memory: 14.5 MB

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]

