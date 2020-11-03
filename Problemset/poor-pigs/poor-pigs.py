
# @Title: 可怜的小猪 (Poor Pigs)
# @Author: qinxinlei
# @Date: 2018-11-18 21:44:36
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        i=0
        x=minutesToTest/minutesToDie+1
        while pow(x,i)<buckets:
            i+=1
        return i
