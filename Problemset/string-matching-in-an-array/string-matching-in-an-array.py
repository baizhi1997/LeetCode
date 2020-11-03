
# @Title: 数组中的字符串匹配 (String Matching in an Array)
# @Author: qinxinlei
# @Date: 2020-08-02 15:25:41
# @Runtime: 36 ms
# @Memory: 13.3 MB

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x:len(x))
        ans = []
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans
