
# @Title: 检查整数及其两倍数是否存在 (Check If N and Its Double Exist)
# @Author: qinxinlei
# @Date: 2020-08-02 19:53:12
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        set1 = set()
        for n in arr:
            if n in set1:
                return True
            set1.add(n*2)
            if not n&1:
                set1.add(n//2)
        return False
