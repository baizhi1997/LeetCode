
# @Title: 最大数值 (Maximum LCCI)
# @Author: qinxinlei
# @Date: 2020-07-08 11:02:27
# @Runtime: 44 ms
# @Memory: 13.4 MB

class Solution:
    def maximum(self, a: int, b: int) -> int:
        return b if bin(a // 2 - b // 2)[0] == '-' else a

