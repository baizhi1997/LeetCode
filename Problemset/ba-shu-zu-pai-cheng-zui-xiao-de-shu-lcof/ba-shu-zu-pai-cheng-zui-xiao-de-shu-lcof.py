
# @Title: 把数组排成最小的数 (把数组排成最小的数 LCOF)
# @Author: qinxinlei
# @Date: 2020-07-03 15:48:42
# @Runtime: 52 ms
# @Memory: 13.3 MB

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b: return 1
            elif a < b: return -1
            else: return 0
        strs = [str(num) for num in nums]
        strs.sort(key = functools.cmp_to_key(sort_rule))
        return ''.join(strs)

