
# @Title: 删除最外层的括号 (Remove Outermost Parentheses)
# @Author: qinxinlei
# @Date: 2019-04-08 21:42:22
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans=""
        tmp=0
        for c in S:
            if c=='(':
                tmp+=1
                if tmp>1:
                    ans+=c
            else:
                tmp-=1
                if tmp>0:
                    ans+=c
        return ans
