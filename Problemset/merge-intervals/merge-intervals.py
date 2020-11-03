
# @Title: 合并区间 (Merge Intervals)
# @Author: qinxinlei
# @Date: 2018-09-24 15:14:37
# @Runtime: 44 ms
# @Memory: N/A

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        if len(intervals)<=1:
            return intervals
        ans=[intervals[0]]
        j=0
        for interval in intervals[1:]:
            if interval.start>ans[j].end:
                ans.append(interval)
                j+=1
            else:
                ans[j].end=max(ans[j].end,interval.end)
        return ans
