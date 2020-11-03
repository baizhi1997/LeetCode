
# @Title: 课程表 (Course Schedule)
# @Author: qinxinlei
# @Date: 2019-07-11 16:41:26
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic1 = collections.defaultdict(int)
        dic2 = collections.defaultdict(list)
        for p in prerequisites:
            dic1[p[0]] += 1
            dic2[p[1]].append(p[0])
        q = [i for i in range(numCourses) if dic1[i] == 0]
        while q:
            x = q.pop()
            for i in dic2[x]:
                dic1[i] -= 1
                if dic1[i] == 0:
                    q.append(i)
        return all(dic1[i] == 0 for i in range(numCourses))
