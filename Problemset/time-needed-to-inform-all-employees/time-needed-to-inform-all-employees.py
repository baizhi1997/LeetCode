
# @Title: 通知所有员工所需的时间 (Time Needed to Inform All Employees)
# @Author: qinxinlei
# @Date: 2020-09-17 16:57:11
# @Runtime: 532 ms
# @Memory: 42.4 MB

from collections import defaultdict

class Solution:
    total = 0

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tmp = defaultdict(list)

        for i in range(len(manager)):
            tmp[manager[i]].append(i)
    
        self.dfs(tmp, informTime, headID, 0)
        return self.total

    def dfs(self, tmp, informTime, head_id, total):
        if not tmp[head_id]:
            self.total = max(self.total, total)

        for id_ in tmp[head_id]:
            self.dfs(tmp, informTime, id_, total+informTime[head_id])


