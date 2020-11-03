
# @Title: 不含 AAA 或 BBB 的字符串 (String Without AAA or BBB)
# @Author: qinxinlei
# @Date: 2019-03-01 15:28:34
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A>=2*B:
            return "aab"*B+'a'*(A-2*B)
        if A>=B:
            return "aab"*(A-B)+"ab"*(2*B-A)
        if B>=2*A:
            return "bba"*A+'b'*(B-2*A)
        return "bba"*(B-A)+"ba"*(2*A-B)
