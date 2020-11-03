
# @Title: 查找和替换模式 (Find and Replace Pattern)
# @Author: qinxinlei
# @Date: 2018-11-20 21:18:27
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans=[]
        for word in words:
            if len(set(zip(word,pattern)))==len(set(word)) and len(set(zip(pattern,word)))==len(set(pattern)) and len(set(word))==len(set(pattern)):
                ans.append(word)
        return ans
