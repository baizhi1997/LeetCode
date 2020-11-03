
# @Title: 找出数组游戏的赢家 (Find the Winner of an Array Game)
# @Author: qinxinlei
# @Date: 2020-08-06 13:17:50
# @Runtime: 92 ms
# @Memory: 23.7 MB

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr)-1:
            return max(arr)
        cnt = 0
        tmp = arr[0]
        for i in range(1, len(arr)):
            if tmp > arr[i]:
                cnt += 1
            else:
                tmp = arr[i]
                cnt = 1
            if cnt == k:
                return tmp
        return tmp
