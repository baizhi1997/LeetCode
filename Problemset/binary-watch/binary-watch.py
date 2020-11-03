
# @Title: 二进制手表 (Binary Watch)
# @Author: qinxinlei
# @Date: 2018-11-08 16:53:18
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hours=[2**i for i in range(4)]
        minutes=[2**i for i in range(6)]
        ans=[]
        for i in range(num+1):
            for h in itertools.combinations(hours,i):
                x=sum(h)
                if x<12:
                    for m in itertools.combinations(minutes,num-i):
                        y=sum(m)
                        if y<60:
                            ans.append("%d:%02d"%(x,y))
        return ans
