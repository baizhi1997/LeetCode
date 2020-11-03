
# @Title: 单词频率 (Words Frequency LCCI)
# @Author: qinxinlei
# @Date: 2020-06-03 00:17:55
# @Runtime: 440 ms
# @Memory: 41.4 MB

class WordsFrequency:

    def __init__(self, book: List[str]):
        self.dic = collections.Counter(book)

    def get(self, word: str) -> int:
        return self.dic[word]



# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
