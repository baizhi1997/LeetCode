
# @Title: 键盘行 (Keyboard Row)
# @Author: qinxinlei
# @Date: 2018-10-20 13:06:16
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1=set("qwertyuiopQWERTYUIOP")
        set2=set("asdfghjklASDFGHJKL")
        set3=set("zxcvbnmZXCVBNM")
        ans=[]
        for word in words:
            set4=set(word)
            if set4<=set1 or set4<=set2 or set4<=set3:
                ans.append(word)
        return ans
