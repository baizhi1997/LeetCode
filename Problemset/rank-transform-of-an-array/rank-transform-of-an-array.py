
# @Title: 数组序号转换 (Rank Transform of an Array)
# @Author: qinxinlei
# @Date: 2020-08-02 22:50:26
# @Runtime: 444 ms
# @Memory: 33.7 MB

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic={}
        L=sorted(list(set(arr)))
        for i,element in enumerate(L):
            dic[element]=i+1
        return [dic[i] for i in arr]


