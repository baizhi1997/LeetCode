
# @Title: 重复 N 次的元素 (N-Repeated Element in Size 2N Array)
# @Author: qinxinlei
# @Date: 2019-03-01 16:44:00
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        set1=set()
        for x in A:
            if x not in set1:
                set1.add(x)
            else:
                return x
