
# @Title: 有重复字符串的排列组合 (Permutation II LCCI)
# @Author: qinxinlei
# @Date: 2020-07-03 17:02:08
# @Runtime: 60 ms
# @Memory: 13.5 MB

class Solution:
    def permutation(self, S: str) -> List[str]:
        n=len(S)
        if n==0:
            return [""]
        res=[]
        for i in range(n):
            if S[i] in S[:i]:
                continue
            for s1 in self.permutation(S[:i]+S[i+1:]):
                res.append(S[i]+s1)
        return res
