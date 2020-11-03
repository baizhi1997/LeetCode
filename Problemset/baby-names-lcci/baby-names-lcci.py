
# @Title: 婴儿名字 (Baby Names LCCI)
# @Author: qinxinlei
# @Date: 2020-07-17 12:04:42
# @Runtime: 340 ms
# @Memory: 17.4 MB

class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        p, d, q = {}, {}, collections.defaultdict(int)
        for s in synonyms:
            a, b = s[1: -1].split(',')
            pa, pb = p.setdefault(a, [a]), p.setdefault(b, [b])
            if pa is not pb:
                pa.extend(pb)
                for c in pb:
                    p[c] = pa
        for name in p:
            d.setdefault(id(p[name]), min(p[name]))
        for s in names:
            i = s.find('(')
            name, count = s[: i], int(s[i + 1: -1])
            q[name in p and d[id(p[name])] or name] += count
        return [f'{name}({count})' for name, count in q.items()]

