
# @Title: 多次搜索 (Multi Search LCCI)
# @Author: qinxinlei
# @Date: 2020-07-16 00:30:36
# @Runtime: 744 ms
# @Memory: 38.5 MB

class Node(object):
    def __init__(self, idx=None):
        self.dic = {}
        self.word_end = False
        # self.word_idx = idx

class Trie(object):
    def __init__(self):
        self.root = {}
    def insert_word(self, word, idx):
        if word=="" : return
        cur_dic = self.root
        for char in word:
            cur_dic.setdefault(char, Node(idx))
            ob = cur_dic[char]
            # ob.word_idx = idx
            cur_dic = ob.dic
        ob.word_end = True
        ob.word_idx = idx


class Solution:
    def multiSearch(self, big, smalls):
        self.build_tree(smalls)
        rt = [[] for _ in range(len(smalls))]
        for i in range(len(big)):
            cur = self.trie.root
            for j in range(i, len(big)):
            # for location, char in enumerate(big[i:]):
                if big[j] in cur:
                    ob = cur[big[j] ]
                    # _idx = ob.word_idx
                    _end = ob.word_end
                    cur = ob.dic
                    if _end: rt[ob.word_idx].append(i)
                else: break
        return rt

    def build_tree(self, smalls):
        self.trie = Trie()
        for idx, word in enumerate(smalls):
            self.trie.insert_word(word, idx)

