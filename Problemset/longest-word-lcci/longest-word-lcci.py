
# @Title: 最长单词 (Longest Word LCCI)
# @Author: qinxinlei
# @Date: 2020-07-17 12:27:47
# @Runtime: 44 ms
# @Memory: 13.4 MB

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = list(set(words))
        words.sort()
        words.sort(key = lambda x:-len(x))
        temp = set(words[:])
        res = ''
        for word in words:
            temp.remove(word)
            if self.findresult(word,temp):
                return word   
        return res
            
    def findresult(self,word,words):
        if len(word) == 0:return True
        for i in range(1,len(word)+1):
            if word[:i] in words and self.findresult(word[i:],words):
                return True
        return False
