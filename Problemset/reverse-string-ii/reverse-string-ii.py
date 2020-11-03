
# @Title: 反转字符串 II (Reverse String II)
# @Author: qinxinlei
# @Date: 2018-10-23 16:37:10
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l=len(s)
        ans=""
        for i in range(0,l,2*k):
            if 2*k>l-i:
                if k>l-i:
                    ans+=s[i:][::-1]
                else:
                    ans+=s[i:i+k][::-1]+s[i+k:l]
            else:
                ans+=s[i:i+k][::-1]+s[i+k:i+2*k]
        return ans
