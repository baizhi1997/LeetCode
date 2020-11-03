
# @Title: 负二进制转换 (Convert to Base -2)
# @Author: qinxinlei
# @Date: 2019-04-08 20:24:53
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def baseNeg2(self, N: int) -> str:
        if N==0:
            return '0'
        ans=""
        while N:
            tmp=(N+2)%4
            N=(N+2)//4
            if tmp==0:
                ans+="01"
            elif tmp==1:
                ans+="11"
            elif tmp==2:
                ans+="00"
            else:
                ans+="10"
        if ans[-1]=='0':
            ans=ans[:-1]
        return ans[::-1]
