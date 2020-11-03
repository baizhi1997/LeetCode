
# @Title: 等价多米诺骨牌对的数量 (Number of Equivalent Domino Pairs)
# @Author: qinxinlei
# @Date: 2019-08-08 16:32:16
# @Runtime: 272 ms
# @Memory: N/A

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = collections.defaultdict(int)
        for d in dominoes:
            x, y = (d[0], d[1]) if d[0] < d[1] else (d[1], d[0])
            dic[(x, y)] += 1
        return sum(v * (v - 1) // 2 for v in dic.values())
