
# @Title: 外观数列 (Count and Say)
# @Author: qinxinlei
# @Date: 2018-10-01 16:14:33
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans="1"
        for i in range(1,n):
            tmp=""
            pre=ans[0]
            cnt=0
            for j in ans:
                if j==pre:
                    cnt+=1
                else:
                    tmp+=(str(cnt)+pre)
                    pre=j
                    cnt=1
            ans=tmp+str(cnt)+pre
        return ans
