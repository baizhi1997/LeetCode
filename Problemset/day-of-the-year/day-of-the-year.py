
# @Title: 一年中的第几天 (Day of the Year)
# @Author: qinxinlei
# @Date: 2019-08-26 20:47:10
# @Runtime: 28 ms
# @Memory: N/A

class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:])
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            months[1] += 1
        return sum(months[:month-1]) + day
