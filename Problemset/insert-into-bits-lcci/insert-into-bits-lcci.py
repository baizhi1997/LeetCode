
# @Title: 插入 (Insert Into Bits LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 13:27:15
# @Runtime: 44 ms
# @Memory: 13.2 MB

class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        if N<=M: return M
        tem = "1"*(32-j-1) + "0"*(j-i+1) + "1"*i
        return (int(tem,base=2)&N)|(M<<i)

