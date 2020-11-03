
# @Title: 灯泡开关 IV (Bulb Switcher IV)
# @Author: qinxinlei
# @Date: 2020-07-26 17:45:39
# @Runtime: 52 ms
# @Memory: 13.6 MB

class Solution:
    def minFlips(self, target: str) -> int:
        return target.count("01")+target.count("10")+int(target[0])
        
