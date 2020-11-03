
# @Title: 给定数字能组成的最大时间 (Largest Time for Given Digits)
# @Author: qinxinlei
# @Date: 2018-12-02 10:45:21
# @Runtime: 140 ms
# @Memory: N/A

class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort()
        for i in range(23,-1,-1):
            tmp1=[]
            if i>9:
                tmp1+=[i//10,i%10]
            else:
                tmp1+=[0,i]
            for j in range(59,-1,-1):
                tmp2=tmp1[:]
                if j>9:
                    tmp2+=[j//10,j%10]
                else:
                    tmp2+=[0,j]
                if sorted(tmp2)==A:
                    return str(tmp2[0])+str(tmp2[1])+':'+str(tmp2[2])+str(tmp2[3])
        return ""
