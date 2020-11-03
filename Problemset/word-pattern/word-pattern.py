
# @Title: 单词规律 (Word Pattern)
# @Author: qinxinlei
# @Date: 2020-11-02 15:04:12
# @Runtime: 44 ms
# @Memory: 13.5 MB

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res=s.split()
        return list(map(pattern.index, pattern))==list(map(res.index,res))

