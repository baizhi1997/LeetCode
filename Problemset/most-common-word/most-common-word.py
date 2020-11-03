
# @Title: 最常见的单词 (Most Common Word)
# @Author: qinxinlei
# @Date: 2018-11-18 20:13:49
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for c in "!?',;.":
            paragraph=paragraph.replace(c,' ')
        paragraph=paragraph.lower().split()
        dic=collections.Counter(paragraph)
        ans=""
        l=0
        for key in dic:
            if key not in banned and dic[key]>l:
                ans=key
                l=dic[key]
        return ans
