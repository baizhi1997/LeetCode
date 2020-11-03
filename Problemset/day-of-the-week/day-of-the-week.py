
# @Title: 一周中的第几天 (Day of the Week)
# @Author: qinxinlei
# @Date: 2020-08-02 15:13:49
# @Runtime: 32 ms
# @Memory: 13.4 MB

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dic = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',
               5:'Friday',6:'Saturday',0:'Sunday'}
        week_num = int(datetime.datetime(year,month,day).strftime("%w"))
        return dic[week_num]

