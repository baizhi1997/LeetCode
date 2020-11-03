
# @Title: 猜数字 (Guess Numbers)
# @Author: qinxinlei
# @Date: 2020-07-24 09:53:26
# @Runtime: 44 ms
# @Memory: 13.4 MB

class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(x == y for x, y in zip(guess, answer))
