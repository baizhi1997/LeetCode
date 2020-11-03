
# @Title: 数字流的秩 (Rank from Stream LCCI)
# @Author: qinxinlei
# @Date: 2020-07-13 15:48:38
# @Runtime: 88 ms
# @Memory: 14.1 MB

class StreamRank:
    def __init__(self):
        self.stack = []

    def track(self, x: int) -> None:
        # 插入并排序
        bisect.insort(self.stack, x)

    def getRankOfNumber(self, x: int) -> int:
        # 插入位置即为小于或等于该数的个数
        return bisect.bisect(self.stack, x)


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)
