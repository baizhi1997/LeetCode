
# @Title: 最大数 (Largest Number)
# @Author: qinxinlei
# @Date: 2018-12-05 18:14:15
# @Runtime: 60 ms
# @Memory: N/A

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
