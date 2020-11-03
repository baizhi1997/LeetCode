
# @Title: 最大交换 (Maximum Swap)
# @Author: qinxinlei
# @Date: 2018-11-25 15:35:17
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=list(str(num))
        tmp=sorted(num,reverse=True)        
        l=len(num)
        for i in range(l):
            if tmp[i]!=num[i]:
                idx=(l-1)-(num[i+1:][::-1].index(tmp[i]))
                num[idx],num[i]=num[i],num[idx]
                break
        return int(''.join(num))
