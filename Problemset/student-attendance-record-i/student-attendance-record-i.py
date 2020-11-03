
# @Title: 学生出勤记录 I (Student Attendance Record I)
# @Author: qinxinlei
# @Date: 2018-11-06 16:04:26
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A')<=1 and s.find('LLL')==-1
