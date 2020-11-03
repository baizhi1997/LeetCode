
# @Title: 字符串压缩 (Compress String LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 11:45:22
# @Runtime: 60 ms
# @Memory: 13.6 MB

class Solution:
    def compressString(self, S: str) -> str:
        ans = ''
        pre = ''
        cnt = 0
        for s in S + ' ':
            if s == pre:
                cnt += 1
            else:
                if cnt != 0:
                    ans += (pre + str(cnt))
                pre = s
                cnt = 1
        return ans if len(ans) < len(S) else S
