
# @Title: 打印从1到最大的n位数 (打印从1到最大的n位数 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 22:56:55
# @Runtime: 36 ms
# @Memory: 19.1 MB

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10**n))
