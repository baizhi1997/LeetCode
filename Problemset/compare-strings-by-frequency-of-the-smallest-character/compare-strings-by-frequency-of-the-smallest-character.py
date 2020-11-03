
# @Title: 比较字符串最小字母出现频次 (Compare Strings by Frequency of the Smallest Character)
# @Author: qinxinlei
# @Date: 2019-08-26 21:45:10
# @Runtime: 68 ms
# @Memory: N/A

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = sorted(w.count(min(w)) for w in words)
        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]
