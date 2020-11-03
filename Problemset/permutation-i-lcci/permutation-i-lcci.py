
# @Title: 无重复字符串的排列组合 (Permutation I LCCI)
# @Author: qinxinlei
# @Date: 2020-06-02 00:20:38
# @Runtime: 68 ms
# @Memory: 20.1 MB

class Solution:
    def permutation(self, S: str) -> List[str]:
        if not S:
            return [""]
        if len(S) == 1:
            return [S]
        tmp = self.permutation(S[1:])
        ans = []
        for s in tmp:
            for i in range(len(tmp[0])+1):
                ans.append(s[0:i]+S[0]+s[i:])
        return ans
