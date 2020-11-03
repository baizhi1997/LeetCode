
# @Title: 字典序排数 (Lexicographical Numbers)
# @Author: qinxinlei
# @Date: 2020-06-16 23:03:59
# @Runtime: 100 ms
# @Memory: 20.2 MB

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = list(range(1, n+1))
        return sorted(ans, key=str)
