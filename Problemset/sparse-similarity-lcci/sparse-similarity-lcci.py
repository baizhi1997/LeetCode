
# @Title: 稀疏相似度 (Sparse Similarity LCCI)
# @Author: qinxinlei
# @Date: 2020-07-19 20:14:41
# @Runtime: 1964 ms
# @Memory: 36.2 MB

class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        ans, n, docs = [], len(docs), [*map(set, docs)]
        for i, j in itertools.combinations(range(n), 2):
            r = (p := len(docs[i] & docs[j])) / (len(docs[i]) + len(docs[j]) - p)
            r and ans.append(f'{i},{j}: {r + 1e-9:.4f}')
        return ans

