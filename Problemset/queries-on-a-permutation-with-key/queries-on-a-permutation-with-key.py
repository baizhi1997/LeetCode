
# @Title: 查询带键的排列 (Queries on a Permutation With Key)
# @Author: qinxinlei
# @Date: 2020-06-02 18:13:09
# @Runtime: 80 ms
# @Memory: 13.5 MB

class BIT:
    def __init__(self, n):
        self.n = n
        self.a = [0] * (n + 1)
    
    @staticmethod
    def lowbit(x):
        return x & (-x)
    
    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.a[x]
            x -= BIT.lowbit(x)
        return ret
    
    def update(self, x, dt):
        while x <= self.n:
            self.a[x] += dt
            x += BIT.lowbit(x)
        
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        n = len(queries)
        bit = BIT(m + n)
        
        pos = [0] * (m + 1)
        for i in range(1, m + 1):
            pos[i] = n + i
            bit.update(n + i, 1)
        
        ans = list()
        for i, query in enumerate(queries):
            cur = pos[query]
            bit.update(cur, -1)
            ans.append(bit.query(cur))
            cur = pos[query] = n - i
            bit.update(cur, 1)
        return ans

