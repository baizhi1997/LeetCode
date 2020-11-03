
# @Title: 单词矩阵 (Word Rectangle LCCI)
# @Author: qinxinlei
# @Date: 2020-07-19 19:42:12
# @Runtime: 3876 ms
# @Memory: 28.2 MB

class Trie:
    def __init__(self):
        self.root = [{}, False]
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur[0]:
                cur[0][c] = [{}, False]
            cur = cur[0][c]
        cur[1] = True

class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        area = 0
        res = []
        trie = Trie()
        for word in words:
            trie.addWord(word)

        def dfs(arr, li):
            for word in words:
                if len(word) != len(arr):   continue
                for i, c in enumerate(word):
                    if c not in arr[i][0]: break
                else:
                    temp = arr[:]
                    flag = True
                    for i, c in enumerate(word):
                        temp[i] = temp[i][0][c]
                        flag &= temp[i][1]
                    li.append(word)
                    if flag:
                        h, w = len(li), len(word)
                        nonlocal area, res
                        if h * w > area:
                            area = h * w
                            res = li[:]
                    dfs(temp, li)
                    li.pop()

        ll = sorted(set(len(word) for word in words), reverse = True)
        for l in ll:
            if l * ll[0] < area:   break
            dfs([trie.root] * l, [])
        return res

