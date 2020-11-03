
# @Title: T9键盘 (T9 LCCI)
# @Author: qinxinlei
# @Date: 2020-06-16 22:35:58
# @Runtime: 52 ms
# @Memory: 14.6 MB

class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        dic = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans = []
        for word in words:
            flag = True
            for n, c in zip(num, word):
                if c not in dic[n]:
                    flag = False
                    break
            if flag:
                ans.append(word)
        return ans
