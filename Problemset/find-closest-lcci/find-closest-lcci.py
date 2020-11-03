
# @Title: 单词距离 (Find Closest LCCI)
# @Author: qinxinlei
# @Date: 2020-06-17 21:54:55
# @Runtime: 148 ms
# @Memory: 25.8 MB

class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        dic = {}
        for i, w in enumerate(words):
            if w not in dic:
                dic[w] = [i]
            else:
                dic[w].append(i)
        i = 0
        j = 0
        ans = sys.maxsize
        while i < len(dic[word1]) and j < len(dic[word2]):
            tmp = abs(dic[word1][i] - dic[word2][j])
            if tmp < ans:
                ans = tmp
            if dic[word1][i] <= dic[word2][j]:
                i += 1
            else:
                j += 1
        return ans
