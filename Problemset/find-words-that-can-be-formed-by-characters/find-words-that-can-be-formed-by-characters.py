
# @Title: 拼写单词 (Find Words That Can Be Formed by Characters)
# @Author: qinxinlei
# @Date: 2019-08-26 21:06:02
# @Runtime: 92 ms
# @Memory: N/A

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for w in words:
            flag = True
            for c in w:
                if w.count(c) > chars.count(c):
                    flag = False
                    break
            if flag:
                ans += len(w)
        return ans
