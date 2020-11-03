
# @Title: 加油站 (Gas Station)
# @Author: qinxinlei
# @Date: 2019-05-13 14:51:05
# @Runtime: 28 ms
# @Memory: N/A

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tmp = [x - y for x, y in zip(gas, cost)]
        cur = 0
        ans = 0
        for i, val in enumerate(tmp + tmp):
            cur += val
            if cur < 0:
                ans = i + 1
                if ans >= len(tmp):
                    return -1
                cur = 0
        return ans
