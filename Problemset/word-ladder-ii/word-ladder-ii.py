
# @Title: 单词接龙 II (Word Ladder II)
# @Author: qinxinlei
# @Date: 2019-05-08 15:26:58
# @Runtime: 72 ms
# @Memory: N/A

from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList or not endWord or not beginWord:
            return []
        wordList = set(wordList)
        forward, backward = {beginWord}, {endWord}
        direction = 1
        parents = defaultdict(set)
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
                direction *= -1
            next_foward = set()
            wordList -= forward
            for word in forward:
                for i in range(len(word)):
                    first, second = word[:i], word[i+1:]
                    for ch in string.ascii_lowercase:
                        combined_word = first + ch + second
                        if combined_word in wordList:
                            next_foward.add(combined_word)
                            if direction == 1:
                                parents[combined_word].add(word)
                            else:
                                parents[word].add(combined_word)
            if next_foward & backward:
                results = [[endWord]]
                while results[0][0] != beginWord:
                    results = [ [parent] + result for result in results for parent in parents[result[0]] ]
                return results
            forward = next_foward
        return []
