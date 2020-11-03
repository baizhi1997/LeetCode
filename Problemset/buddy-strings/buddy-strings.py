
# @Title: 亲密字符串 (Buddy Strings)
# @Author: qinxinlei
# @Date: 2018-11-04 21:37:13
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!=len(B):
            return False
        if A==B:
            return len(A)>len(set(A))
        cnt=0
        tmp=[]
        for i in range(len(A)):
            if A[i]!=B[i]:
                cnt+=1
                if cnt>2:
                    return False
                tmp+=[A[i],B[i]]
        return cnt==2 and tmp[0]==tmp[3] and tmp[1]==tmp[2]
