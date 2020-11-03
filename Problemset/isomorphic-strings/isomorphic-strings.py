
# @Title: 同构字符串 (Isomorphic Strings)
# @Author: qinxinlei
# @Date: 2018-11-10 14:04:09
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dic={}
        set1=set()
        for i in range(len(s)):
            if s[i] in dic:
                if t[i]!=dic[s[i]]:
                    return False
            elif t[i] in set1:
                return False
            else:
                dic[s[i]]=t[i]
                set1.add(t[i])
        return True
