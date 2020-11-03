
# @Title: 和为s的连续正数序列 (和为s的连续正数序列 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 23:56:23
# @Runtime: 48 ms
# @Memory: 13.4 MB

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        n = 2
        total = []
        while n:
            tmp = []
            x = target - sum(range(1,n))
            if x % n == 0 and x // n > 0:
                tmp += range(x//n, x//n+n)
                total.append(tmp)
            elif x <= 0:
                break
            n += 1
        return total[::-1]
                
