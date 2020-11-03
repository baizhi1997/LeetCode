
# @Title: 猜数字游戏 (Bulls and Cows)
# @Author: qinxinlei
# @Date: 2018-12-04 12:35:08
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        x=sum(secret[i]==guess[i] for i in range(len(secret)))
        dic=collections.Counter(secret)&collections.Counter(guess)
        y=sum(dic.values())
        return "%dA%dB" %(x,y-x)
