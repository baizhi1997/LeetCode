
# @Title: Bigram 分词 (Occurrences After Bigram)
# @Author: qinxinlei
# @Date: 2019-06-24 18:00:31
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        tmp = text.split()
        ans = []
        for i in range(len(tmp)-2):
            if tmp[i] == first and tmp[i+1] == second:
                ans.append(tmp[i+2])
        return ans
