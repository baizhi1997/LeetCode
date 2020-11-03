
# @Title: 汉诺塔问题 (Hanota LCCI)
# @Author: qinxinlei
# @Date: 2020-07-09 16:22:52
# @Runtime: 48 ms
# @Memory: 13.4 MB

class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.move(n, A, B, C)

    def move(self,n, A, B, C):
        if n == 1:
            C.append(A[-1])
            A.pop()
            return 
        else:
            self.move(n-1, A, C, B)
            C.append(A[-1])
            A.pop()
            self.move(n-1,B, A, C)

