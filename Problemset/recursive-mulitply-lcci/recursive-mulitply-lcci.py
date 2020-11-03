
# @Title: 递归乘法 (Recursive Mulitply LCCI)
# @Author: qinxinlei
# @Date: 2020-06-17 20:31:55
# @Runtime: 48 ms
# @Memory: 13.1 MB

class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A == 0:
            return 0
        if A & 1:
            return self.multiply(A-1, B) + B
        return self.multiply(A>>1, B<<1)

