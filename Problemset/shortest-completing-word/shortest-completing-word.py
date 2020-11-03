
# @Title: 最短补全词 (Shortest Completing Word)
# @Author: qinxinlei
# @Date: 2018-10-31 21:14:08
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        l=sys.maxsize
        ans=""
        dic=collections.Counter()
        for c in licensePlate.lower():
            if c.isalpha():
                dic[c]+=1
        for word in words:
            flag=True
            for c in dic:
                if word.count(c)<dic[c]:
                    flag=False
                    break
            if flag and len(word)<l:
                ans=word
                l=len(word)
        return ans
