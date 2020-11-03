
# @Title: 2出现的次数 (Number Of 2s In Range LCCI)
# @Author: qinxinlei
# @Date: 2020-07-18 20:31:37
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        s= str(n) 
        x= 2
        count = 0
        for i in range(len(s)):
            current = int(s[i])
            high = 0 if s[:i]=='' else int(s[:i])
            low =0 if s[i+1:]=='' else int(s[i+1:])
            if current>x:
                count+=(high+1)*(10**len(s[i+1:]))
            elif current<x:
                count += (high) * (10 ** len(s[i + 1:]))
            else:
                count +=(high) * (10 ** len(s[i + 1:]))+low+1
        return count

