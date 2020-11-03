
# @Title: “气球” 的最大数量 (Maximum Number of Balloons)
# @Author: qinxinlei
# @Date: 2020-08-02 13:24:21
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = collections.Counter(text)
        return min(dic['b'], dic['a'], dic['l']//2, dic['o']//2, dic['n'])
