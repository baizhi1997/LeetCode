
# @Title: 重新排列字符串 (Shuffle String)
# @Author: qinxinlei
# @Date: 2020-07-26 17:35:21
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tmp = sorted(list(range(len(indices))), key = lambda x: indices[x])
        return ''.join([s[i] for i in tmp])
