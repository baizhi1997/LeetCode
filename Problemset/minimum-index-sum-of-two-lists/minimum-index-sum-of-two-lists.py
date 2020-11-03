
# @Title: 两个列表的最小索引总和 (Minimum Index Sum of Two Lists)
# @Author: qinxinlei
# @Date: 2018-11-11 15:53:36
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d={}
        for i,r in enumerate(list1):
            d[r]=i
        ans=[]
        l=math.inf
        for i,r in enumerate(list2):
            if r in d:
                if d[r]+i==l:
                    ans.append(r)
                elif d[r]+i<l:
                    ans=[r]
                    l=d[r]+i
        return ans
