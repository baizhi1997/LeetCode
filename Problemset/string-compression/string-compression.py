
# @Title: 压缩字符串 (String Compression)
# @Author: qinxinlei
# @Date: 2018-11-12 13:45:50
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cur=chars[0]
        cnt=0
        ans=[]
        for c in chars+[' ']:
            if c==cur:
                cnt+=1
            else:
                ans+=[cur]
                if cnt!=1:
                    ans+=list(str(cnt))
                cnt=1
                cur=c
        chars[:]=ans
        return len(chars)
