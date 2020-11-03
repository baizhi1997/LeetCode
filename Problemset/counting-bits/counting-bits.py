
# @Title: 比特位计数 (Counting Bits)
# @Author: qinxinlei
# @Date: 2018-11-22 13:07:59
# @Runtime: 108 ms
# @Memory: N/A

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans=[0]
        i=1
        while i<num+1:
            i*=2
            for j in range(len(ans)):
                ans.append(ans[j]+1)
        return ans[:num+1]
