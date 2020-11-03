
# @Title: 密钥格式化 (License Key Formatting)
# @Author: qinxinlei
# @Date: 2018-11-12 11:30:28
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S=S.replace('-','').upper()[::-1]
        ans=[]
        for i in range(0,len(S),K):
            ans.append(S[i:i+K])
        return '-'.join(ans)[::-1]
