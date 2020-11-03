
# @Title: 拼车 (Car Pooling)
# @Author: qinxinlei
# @Date: 2019-06-25 11:04:16
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dic = collections.defaultdict(int)
        for t in trips:
            dic[t[1]] -= t[0]
            dic[t[2]] += t[0]
        for i in sorted(dic.keys()):
            capacity += dic[i]
            if capacity < 0:
                return False
        return True
