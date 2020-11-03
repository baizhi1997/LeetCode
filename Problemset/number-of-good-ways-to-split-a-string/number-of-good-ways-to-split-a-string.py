
# @Title: 字符串的好分割数目 (Number of Good Ways to Split a String)
# @Author: qinxinlei
# @Date: 2020-07-31 14:04:09
# @Runtime: 140 ms
# @Memory: 13.5 MB

class Solution:
    def numSplits(self, s: str) -> int:
        left = {}
        right = collections.Counter(s)
        res, l, r= 0, 0, len(right)
        for c in s:
            if c not in left:
                left[c] = 1
                l += 1
            else:
                left[c] += 1
            if left[c] == right[c]:
                r -= 1
            if l == r:
                res += 1
        return res
