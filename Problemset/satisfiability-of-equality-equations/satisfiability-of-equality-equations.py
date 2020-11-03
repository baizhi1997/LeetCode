
# @Title: 等式方程的可满足性 (Satisfiability of Equality Equations)
# @Author: qinxinlei
# @Date: 2019-03-05 14:48:38
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dic={}
        for equation in equations:
            if equation[1]=='=':
                x,y=equation[0],equation[3]
                if x not in dic:
                    dic[x]=set(x)
                if y not in dic:
                    dic[y]=set(y)
                s=dic[x]|dic[y]
                for i in s:
                    dic[i]=s
        for equation in equations:
            if equation[1]=='!':
                x,y=equation[0],equation[3]
                if x==y or x in dic and y in dic[x]:
                    return False
        return True
