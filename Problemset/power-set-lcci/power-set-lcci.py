
# @Title: 幂集 (Power Set LCCI)
# @Author: qinxinlei
# @Date: 2020-06-02 18:24:59
# @Runtime: 36 ms
# @Memory: 13.2 MB

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        import itertools
        res = [[],]
        for i in range(1,len(nums)+1):
            for item in itertools.combinations(nums, i):
                res.append(list(item))
        return res

