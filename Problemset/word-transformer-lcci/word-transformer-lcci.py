
# @Title: 单词转换 (Word Transformer LCCI)
# @Author: qinxinlei
# @Date: 2020-07-19 00:50:55
# @Runtime: 136 ms
# @Memory: 17.3 MB

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        # BFS
        hashmap = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hashmap[word[:i] + '*' + word[i + 1:]].append(word)
        queue = collections.deque([beginWord])
        w_dict = {beginWord: [beginWord]}
        while queue:
            word = queue.popleft()
            if word == endWord:
                return w_dict[word]
            for i in range(len(word)):
                if word[:i] + '*' + word[i + 1:] in hashmap:
                    for tmp in hashmap[word[:i] + '*' + word[i + 1:]]:
                        if tmp not in w_dict:
                            w_dict[tmp] = w_dict[word] + [tmp]
                            queue.append(tmp)
        return []

