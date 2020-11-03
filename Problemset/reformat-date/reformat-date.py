
# @Title: 转变日期格式 (Reformat Date)
# @Author: qinxinlei
# @Date: 2020-08-02 16:06:21
# @Runtime: 32 ms
# @Memory: 13.1 MB

class Solution:
    def reformatDate(self, date: str) -> str:
        month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day, month, year = date.split()
        day = int(day[:-2])
        month = month_list.index(month)+1
        ans = year+'-'
        if month < 10:
            ans += '0'
        ans += str(month)+'-'
        if day < 10:
            ans += '0'
        ans += str(day)
        return ans
