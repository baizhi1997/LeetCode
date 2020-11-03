
# @Title: 按递增顺序显示卡牌 (Reveal Cards In Increasing Order)
# @Author: qinxinlei
# @Date: 2018-12-02 12:22:51
# @Runtime: 96 ms
# @Memory: N/A

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        def f(deck):
            if len(deck)==1:
                return deck
            tmp=f(deck[1:])
            return [deck[0]]+[tmp[-1]]+tmp[:-1]
        return f(deck)
