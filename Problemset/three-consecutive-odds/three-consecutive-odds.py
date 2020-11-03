
# @Title: 存在连续三个奇数的数组 (Three Consecutive Odds)
# @Author: qinxinlei
# @Date: 2020-08-17 15:47:41
# @Runtime: 52 ms
# @Memory: 13.4 MB

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for num in arr:
            if num & 1:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False
