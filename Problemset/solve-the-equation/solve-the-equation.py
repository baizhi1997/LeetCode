
# @Title: 求解方程 (Solve the Equation)
# @Author: qinxinlei
# @Date: 2018-11-26 20:16:07
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        i=0
        if equation[0]=='x':
            equation='1'+equation
        while i<len(equation):
            if equation[i]=='x' and equation[i-1] in "+-=":
                equation=equation[:i]+'1'+equation[i:]
                i+=1
            elif equation[i]=='-':
                equation=equation[:i]+'+'+equation[i:]
                i+=1
            i+=1
        e1,e2=equation.split('=')
        l1,l2=e1.strip('+').split('+'),e2.strip('+').split('+')
        a,b=0,0
        for s in l1:
            if s[-1]=='x':
                a+=int(s[:-1])
            else:
                b+=int(s)
        for s in l2:
            if s[-1]=='x':
                a-=int(s[:-1])
            else:
                b-=int(s)
        if a==b==0:
            return "Infinite solutions"
        if a==0:
            return "No solution"
        return "x=%d" % (-b//a)
