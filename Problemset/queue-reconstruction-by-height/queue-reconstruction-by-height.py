
# @Title: 根据身高重建队列 (Queue Reconstruction by Height)
# @Author: qinxinlei
# @Date: 2018-11-23 14:44:57
# @Runtime: 84 ms
# @Memory: N/A

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        tmp=sorted(people,key=lambda x:(-x[0],x[1]))
        ans=[]
        for p in tmp:
            ans.insert(p[1],p)
        return ans
