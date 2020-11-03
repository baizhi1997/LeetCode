
# @Title: 最短超串 (Shortest Supersequence LCCI)
# @Author: qinxinlei
# @Date: 2020-07-16 00:57:38
# @Runtime: 148 ms
# @Memory: 25.9 MB

class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        dic = {x:1 for x in small}
        v = sum(dic.values())
        ans = []
        tmp = float('inf')
        l = 0
        r = 0
        while r < len(big) or v == 0:
            if v > 0:
                if big[r] in dic:
                    dic[big[r]] -= 1
                    if dic[big[r]] == 0:
                        v -= 1
                r += 1
            else:
                if big[l] in dic:
                    if dic[big[l]] == 0:
                        v += 1
                        if r - l < tmp:
                            ans = [l, r-1]
                            tmp = r - l
                    dic[big[l]] += 1
                l += 1
        return ans
