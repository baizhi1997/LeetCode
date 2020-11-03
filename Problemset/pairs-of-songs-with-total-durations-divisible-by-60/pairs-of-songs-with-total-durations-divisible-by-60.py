
# @Title: 总持续时间可被 60 整除的歌曲 (Pairs of Songs With Total Durations Divisible by 60)
# @Author: qinxinlei
# @Date: 2019-03-18 09:41:26
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic=collections.Counter([x%60 for x in time])
        return sum(dic[i]*dic[60-i] for i in range(1,30))+dic[30]*(dic[30]-1)//2+dic[0]*(dic[0]-1)//2
