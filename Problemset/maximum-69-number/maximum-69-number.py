
# @Title: 6 和 9 组成的最大数字 (Maximum 69 Number)
# @Author: qinxinlei
# @Date: 2020-07-28 16:22:18
# @Runtime: 24 ms
# @Memory: 13.2 MB

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                break
        return int(''.join(num))
