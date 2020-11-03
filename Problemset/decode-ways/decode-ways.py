
# @Title: 解码方法 (Decode Ways)
# @Author: qinxinlei
# @Date: 2018-10-01 21:05:02
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':
            return 0
        dp1_prev=1
        dp2_prev=0
        for i in range(1,len(s)):
            if s[i]!='0':
                dp1_cur=dp1_prev+dp2_prev
            else:
                dp1_cur=0    
            if s[i-1]=='1' or (s[i-1]=='2' and int(s[i])<7):
                dp2_cur=dp1_prev
            else:
                dp2_cur=0
            dp1_prev,dp2_prev=dp1_cur,dp2_cur
        return dp1_prev+dp2_prev
