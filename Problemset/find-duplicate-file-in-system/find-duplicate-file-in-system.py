
# @Title: 在系统中查找重复文件 (Find Duplicate File in System)
# @Author: qinxinlei
# @Date: 2018-12-01 15:01:00
# @Runtime: 124 ms
# @Memory: N/A

class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for p in paths:
            s=p.split()
            s[0]+='/'
            for tmp in s[1:]:
                a,b=tmp.split('(')
                if b in dic:
                    dic[b].append(s[0]+a)
                else:
                    dic[b]=[s[0]+a]
        return [v for v in dic.values() if len(v)>1]
