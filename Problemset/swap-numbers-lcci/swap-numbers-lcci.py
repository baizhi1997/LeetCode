
# @Title: 交换数字 (Swap Numbers LCCI)
# @Author: qinxinlei
# @Date: 2020-06-01 16:46:56
# @Runtime: 44 ms
# @Memory: 13.3 MB

class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = numbers[0] ^ numbers[1]
        numbers[1] = numbers[1] ^ numbers[0]
        numbers[0] = numbers[0] ^ numbers[1]
        return numbers
