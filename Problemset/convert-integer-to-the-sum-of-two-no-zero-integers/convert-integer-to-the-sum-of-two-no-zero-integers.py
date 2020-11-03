
# @Title: 将整数转换为两个无零整数的和 (Convert Integer to the Sum of Two No-Zero Integers)
# @Author: qinxinlei
# @Date: 2020-08-02 14:59:20
# @Runtime: 32 ms
# @Memory: 13.4 MB

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' not in str(n-i) and '0' not in str(i):
                return [i, n-i]
