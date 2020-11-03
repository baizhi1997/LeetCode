
# @Title: 字符串的排列 (字符串的排列  LCOF)
# @Author: qinxinlei
# @Date: 2020-07-03 16:54:53
# @Runtime: 204 ms
# @Memory: 15.4 MB

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
