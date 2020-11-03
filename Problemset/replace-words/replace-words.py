
# @Title: 单词替换 (Replace Words)
# @Author: qinxinlei
# @Date: 2018-11-28 22:20:45
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        lengths=sorted(set([len(r) for r in dict]))
        root=set(dict)
        ans=[]
        for word in sentence.split():
            for i in lengths:
                if word[:i] in root:
                    ans.append(word[:i])
                    break
            else:
                ans.append(word)
        return ' '.join(ans)
