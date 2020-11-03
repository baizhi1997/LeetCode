
# @Title: 实现一个魔法字典 (Implement Magic Dictionary)
# @Author: qinxinlei
# @Date: 2018-12-01 17:38:03
# @Runtime: 32 ms
# @Memory: N/A

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic=collections.defaultdict(list)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i in dict:
            self.dic[len(i)].append(i)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return any(sum([a!=b for a,b in zip(word,s)])==1 for s in self.dic[len(word)])

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
