
# @Title: 找到字符串中所有字母异位词 (Find All Anagrams in a String)
# @Author: qinxinlei
# @Date: 2018-11-11 16:58:48
# @Runtime: 104 ms
# @Memory: N/A

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        cnt1=[0]*26
        cnt2=[0]*26
        l=len(p)
        for c in p:
            cnt1[ord(c)-97]+=1
        for c in s[:l-1]:
            cnt2[ord(c)-97]+=1
        ans=[]
        for i in range(len(s)-l+1):
            cnt2[ord(s[i+l-1])-97]+=1
            if cnt1==cnt2:
                ans.append(i)
            cnt2[ord(s[i])-97]-=1
        return ans
