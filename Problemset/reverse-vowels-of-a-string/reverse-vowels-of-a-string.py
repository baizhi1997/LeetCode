
# @Title: 反转字符串中的元音字母 (Reverse Vowels of a String)
# @Author: qinxinlei
# @Date: 2018-11-10 13:22:54
# @Runtime: 60 ms
# @Memory: N/A

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        vowels=set("aeiouAEIOU")
        l=0
        r=len(s)-1
        while l<r:
            while s[l] not in vowels and l<r:
                l+=1
            while s[r] not in vowels and l<r:
                r-=1
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return ''.join(s)
      r-=1
        return ''.join(s)
