
# @Title: 子串能表示从 1 到 N 数字的二进制串 (Binary String With Substrings Representing 1 To N)
# @Author: qinxinlei
# @Date: 2019-03-29 20:36:58
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        return all(bin(i)[2:] in S for i in range(N,0,-1))
