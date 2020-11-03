
# @Title: 单词接龙 (Word Ladder)
# @Author: qinxinlei
# @Date: 2019-05-08 14:21:26
# @Runtime: 108 ms
# @Memory: N/A

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        l = len(beginWord)
        dic = collections.defaultdict(list)
        for word in wordList:
            for i in range(l):
                dic[word[:i] + '*' + word[i+1:]].append(word)
        q = [(beginWord, 1)]
        visited = set(beginWord)
        while q:
            cur, level = q.pop(0)
            for i in range(l):
                tmp = cur[:i] + '*' + cur[i+1:]
                for word in dic[tmp]:
                    if word not in visited:
                        if word == endWord:
                            return level + 1
                        visited.add(word)
                        q.append((word, level + 1))
                dic[tmp] = []
        return 0
