
# @Title: 前K个高频单词 (Top K Frequent Words)
# @Author: qinxinlei
# @Date: 2018-12-02 21:12:46
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic=collections.Counter(words)
        return heapq.nsmallest(k,dic,key=lambda x:(-dic[x],x))

