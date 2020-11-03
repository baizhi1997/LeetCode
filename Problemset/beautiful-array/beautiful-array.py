
# @Title: 漂亮数组 (Beautiful Array)
# @Author: qinxinlei
# @Date: 2019-03-13 17:46:43
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        ans=[1]
        while len(ans)<N:
            ans=[i*2-1 for i in ans]+[i*2 for i in ans]
        return [i for i in ans if i<= N]
