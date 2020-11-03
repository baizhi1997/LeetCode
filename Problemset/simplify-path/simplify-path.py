
# @Title: 简化路径 (Simplify Path)
# @Author: qinxinlei
# @Date: 2018-10-01 17:23:54
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        items=path.split("/")
        for i in items:
            if i=="..":
                if len(stack):
                    stack.pop()
            elif i not in ("","."):
                stack.append(i)     
        return "/"+"/".join(stack)
    
