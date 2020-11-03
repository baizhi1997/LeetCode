
# @Title: 自定义字符串排序 (Custom Sort String)
# @Author: qinxinlei
# @Date: 2018-11-22 13:56:45
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dic={}
        for i,c in enumerate(S):
            dic[c]=i
        tmp=''
        pre=''
        for c in T:
            if c in dic:
                tmp+=c
            else:
                pre+=c
        return pre+''.join(sorted(tmp,key=lambda c:dic[c]))
