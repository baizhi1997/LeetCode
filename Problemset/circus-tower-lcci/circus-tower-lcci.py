
# @Title: 马戏团人塔 (Circus Tower LCCI)
# @Author: qinxinlei
# @Date: 2020-07-17 15:15:29
# @Runtime: 376 ms
# @Memory: 16.2 MB

class Solution:
    import bisect
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:       
       dp=[]
       for a,b in sorted(zip(height,weight),key = lambda x:[x[0],-x[1]]):
           pos = bisect.bisect_left(dp,b)
           dp[pos:pos+1] = [b]
       return len(dp)

