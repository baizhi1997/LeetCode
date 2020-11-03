
# @Title: 组合总和 III (Combination Sum III)
# @Author: qinxinlei
# @Date: 2020-06-15 20:43:21
# @Runtime: 48 ms
# @Memory: 13.4 MB

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def back(candidates, cur, target, length):
            if len(cur) == length and target == 0: 
                res.append(cur.copy())
            for i in range(len(candidates)):
                if len(cur) > 0 and candidates[i] < cur[-1]:  
                    continue
                cur.append(candidates[i])
                back(candidates[:i] + candidates[i + 1:], cur, target - candidates[i], length)
                cur.pop() 

        res = []
        nums = [i for i in range(1, 10)]
        back(nums, [], n, k)
        return res

