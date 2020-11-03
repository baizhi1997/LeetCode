
# @Title: 插入区间 (Insert Interval)
# @Author: qinxinlei
# @Date: 2018-09-25 17:11:55
# @Runtime: 36 ms
# @Memory: N/A

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i,j=0,0
        x,y=newInterval.start,newInterval.end
        while i<len(intervals):
            if x<=intervals[i].end:
                break
            else:
                i+=1
        while j<len(intervals):
            if y<intervals[j].start:
                break
            else:
                j+=1
        if i==j:
            intervals.insert(i,newInterval)
        else:
            intervals[i].start=min(x,intervals[i].start)
            intervals[i].end=max(y,intervals[j-1].end)
            del intervals[i+1:j]
        return intervals
