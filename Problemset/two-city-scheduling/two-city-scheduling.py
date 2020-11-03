
# @Title: 两地调度 (Two City Scheduling)
# @Author: qinxinlei
# @Date: 2019-05-19 21:54:58
# @Runtime: 28 ms
# @Memory: N/A

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum([v[i // (len(costs) // 2)] for i, v in enumerate(sorted(costs, key=lambda c: c[0] - c[1]))])
