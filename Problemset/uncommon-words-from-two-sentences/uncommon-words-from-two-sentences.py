
# @Title: 两句话中的不常见单词 (Uncommon Words from Two Sentences)
# @Author: qinxinlei
# @Date: 2018-10-20 13:04:57
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        cnt=collections.Counter((A+' '+B).split())
        return [s for s in cnt if cnt[s]==1]
[s]==1]
