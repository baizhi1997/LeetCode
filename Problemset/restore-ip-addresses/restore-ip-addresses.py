
# @Title: 复原IP地址 (Restore IP Addresses)
# @Author: qinxinlei
# @Date: 2019-01-03 15:22:16
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(w):
            return w and int(w) <= 255 and (w == '0' or w[0] != '0')
        ans = []
        for i in range(1, 4):
            w1 = s[:i]
            if is_valid(w1):
                for j in range(i+1, i+4):
                    w2 = s[i:j]
                    if is_valid(w2):
                        for k in range(j+1, j+4):
                            w3, w4 = s[j:k], s[k:]
                            if is_valid(w3) and is_valid(w4):
                                ans.append(w1 + '.' + w2 + '.' + w3 + '.' + w4)
        return ans
