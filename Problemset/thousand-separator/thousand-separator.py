
# @Title: 千位分隔数 (Thousand Separator)
# @Author: qinxinlei
# @Date: 2020-10-28 22:38:02
# @Runtime: 24 ms
# @Memory: 13.5 MB

class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)[::-1]
        new_n = ''
        for i,num in enumerate(n):
            new_n+=num
            if (i+1)%3==0 and (i+1)!= len(n):
                new_n+='.'
        return new_n[::-1]

