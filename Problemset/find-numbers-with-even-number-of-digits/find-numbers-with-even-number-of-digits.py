
# @Title: 统计位数为偶数的数字 (Find Numbers with Even Number of Digits)
# @Author: qinxinlei
# @Date: 2020-07-28 13:52:08
# @Runtime: 48 ms
# @Memory: 13.3 MB

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(num))%2==0 for num in nums)
