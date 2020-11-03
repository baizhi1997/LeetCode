
# @Title: 模式匹配 (Pattern Matching LCCI)
# @Author: qinxinlei
# @Date: 2020-07-18 23:51:52
# @Runtime: 32 ms
# @Memory: 13.4 MB

class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        x, y = pattern.count('a'), pattern.count('b')
        l = len(value)
        if x == 0:
            return value[:l//y]*y == value
        if y == 0:
            return value[:l//x]*x == value
        for l1 in range(l//x+1):
            if (l-x*l1)%y == 0:
                l2 = (l-x*l1)//y
                stra = 0
                strb = 0
                i = 0
                for c in pattern:
                    if c == 'a':
                        if value[i:i+l1] != stra and stra != 0:
                            break
                        stra = value[i:i+l1]
                        i += l1
                    else:
                        if value[i:i+l2] != strb and strb != 0:
                            break
                        strb = value[i:i+l2]
                        i += l2
                else:
                    return stra != strb
        return False
