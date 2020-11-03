
# @Title: 唯一摩尔斯密码词 (Unique Morse Code Words)
# @Author: qinxinlei
# @Date: 2018-10-17 18:49:41
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        list1=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        set1=set()
        for word in words:
            s=""
            for c in word:
                s+=list1[ord(c)-ord('a')]
            set1.add(s)
        return len(set1)
