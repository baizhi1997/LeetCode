
# @Title: 可被 5 整除的二进制前缀 (Binary Prefix Divisible By 5)
# @Author: qinxinlei
# @Date: 2019-04-08 20:32:45
# @Runtime: 96 ms
# @Memory: N/A

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans=[]
        tmp=0
        for a in A:
            tmp=(tmp*2+a)%5
            if tmp:
                ans.append(False)
            else:
                ans.append(True)
        return ans
