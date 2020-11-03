
# @Title: 在既定时间做作业的学生人数 (Number of Students Doing Homework at a Given Time)
# @Author: qinxinlei
# @Date: 2020-07-28 14:11:30
# @Runtime: 32 ms
# @Memory: 13.4 MB

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        index1 = sum(st <= queryTime for st in startTime)
        index2 = sum(et < queryTime for et in endTime)
        return index1 - index2
