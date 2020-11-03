
# @Title: 串联所有单词的子串 (Substring with Concatenation of All Words)
# @Author: qinxinlei
# @Date: 2019-05-01 16:01:13
# @Runtime: 56 ms
# @Memory: N/A

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        m, n = len(words[0]), len(words)
        res, table = [], {}
        for w in words:
            table[w] = table.get(w, 0) + 1
        for i in range(m):
            start, cur, counts = i, i, {}
            while start <= len(s) - m * n:
                w, cur = s[cur:cur + m], cur + m
                if w not in table:
                    start, counts = cur, {}
                    continue
                counts[w] = counts.get(w, 0) + 1
                while counts[w] > table[w]:
                    counts[s[start:start + m]] -= 1
                    start += m
                if cur - start == m * n:
                    res.append(start)
        return res
