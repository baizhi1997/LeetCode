
# @Title: 文本左右对齐 (Text Justification)
# @Author: qinxinlei
# @Date: 2019-05-06 20:24:06
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def fullJustify(self, words: 'List[str]', maxWidth: 'int') -> 'List[str]':
        res, curr, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(curr) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    if len(curr) == 1:
                        curr[0] += ' '
                        continue
                    curr[i % (len(curr)-1 or 1)] += ' '
                res.append(''.join(curr))
                curr, num_of_letters = [], 0
            curr += [w]
            num_of_letters += len(w)
        return res + [' '.join(curr).ljust(maxWidth)]
