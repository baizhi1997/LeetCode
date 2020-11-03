
# @Title: 词典中最长的单词 (Longest Word in Dictionary)
# @Author: qinxinlei
# @Date: 2018-11-18 21:21:01
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        ans=""
        x=0
        set1=set()
        for word in words:
            l=len(word)
            if l==1 or word[:l-1] in set1:
                set1.add(word)
                if l>x:
                    x=l
                    ans=word
        return ans
