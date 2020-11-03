
# @Title: 堆箱子 (Pile Box LCCI)
# @Author: qinxinlei
# @Date: 2020-07-19 23:05:40
# @Runtime: 1600 ms
# @Memory: 14 MB

class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        dp = [0 for _ in range(len(box))]
        box.sort()

        for i in range(len(box)):
            dp[i] = box[i][2]
            for j in range(i):
                if box[j][0] < box[i][0] and box[j][1] < box[i][1] and box[j][2] < box[i][2]:
                    dp[i] = max(dp[i], dp[j] + box[i][2])
        return max(dp)

