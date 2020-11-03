
# @Title: 卡牌分组 (X of a Kind in a Deck of Cards)
# @Author: qinxinlei
# @Date: 2018-10-25 16:22:45
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dic=collections.defaultdict(int)
        for i in deck:
            dic[i]+=1
        x=dic[deck[0]]
        for i in dic.values():
            while i%x!=0:
                i,x=x,i%x
        return x!=1
