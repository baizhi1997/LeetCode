
# @Title: 独一无二的出现次数 (Unique Number of Occurrences)
# @Author: qinxinlei
# @Date: 2020-07-31 13:01:10
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = collections.Counter(arr)
        return len(set(dic.values())) == len(dic)
