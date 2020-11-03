
# @Title: 检查单词是否为句中其他单词的前缀 (Check If a Word Occurs As a Prefix of Any Word in a Sentence)
# @Author: qinxinlei
# @Date: 2020-08-02 11:49:05
# @Runtime: 40 ms
# @Memory: 13.5 MB

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ans = -1
        l = len(searchWord)
        for i, word in enumerate(sentence.split(' ')):
            if len(word) >= l and word[:l] == searchWord:
                ans = i+1
                break
        return ans
