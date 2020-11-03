
# @Title: 判断能否形成等差数列 (Can Make Arithmetic Progression From Sequence)
# @Author: qinxinlei
# @Date: 2020-07-05 10:45:51
# @Runtime: 48 ms
# @Memory: 13.2 MB

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        dx = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != dx:
                return False
        return True
            
