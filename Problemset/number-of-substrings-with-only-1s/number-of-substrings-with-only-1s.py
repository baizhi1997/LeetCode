
# @Title: 仅含 1 的子串数 (Number of Substrings With Only 1s)
# @Author: qinxinlei
# @Date: 2020-09-14 09:55:18
# @Runtime: 84 ms
# @Memory: 13.5 MB

class Solution:
    def numSub(self, s: str) -> int:
        total, consecutive = 0, 0
        length = len(s)
        for i in range(length):
            if s[i] == '0':
                total += consecutive * (consecutive + 1) // 2
                consecutive = 0
            else:
                consecutive += 1
        
        total += consecutive * (consecutive + 1) // 2
        total %= (10**9 + 7)
        return total

