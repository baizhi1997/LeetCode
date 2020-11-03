
# @Title: 查找常用字符 (Find Common Characters)
# @Author: qinxinlei
# @Date: 2019-03-03 19:22:06
# @Runtime: 80 ms
# @Memory: N/A

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cnt=collections.Counter
        tmp=cnt(A[0])
        for i in range(1,len(A)):
            tmp=tmp&cnt(A[i])
        ans=[]
        for k,v in tmp.items():
            ans+=[k]*v
        return ans
