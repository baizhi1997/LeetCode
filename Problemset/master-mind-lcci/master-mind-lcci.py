
# @Title: 珠玑妙算 (Master Mind LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 13:21:01
# @Runtime: 40 ms
# @Memory: 13.5 MB

class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        from collections import Counter
        total = sum((Counter(solution) & Counter(guess)).values())
        right = sum(1 for (i, j) in zip(solution, guess) if i == j)
        return [right, total - right]

