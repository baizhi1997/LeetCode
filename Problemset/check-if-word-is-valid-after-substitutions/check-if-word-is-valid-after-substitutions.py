
# @Title: 检查替换后的词是否有效 (Check If Word Is Valid After Substitutions)
# @Author: qinxinlei
# @Date: 2019-03-03 20:13:09
# @Runtime: 384 ms
# @Memory: N/A

class Solution:
    def isValid(self, S: str) -> bool:
        if not S:
            return True
        if "abc" not in S:
            return False
        i=S.find("abc")
        return self.isValid(S[:i]+S[i+3:])
