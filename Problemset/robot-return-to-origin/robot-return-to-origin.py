
# @Title: 机器人能否返回原点 (Robot Return to Origin)
# @Author: qinxinlei
# @Date: 2018-10-18 18:15:52
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L')==moves.count('R') and moves.count('U')==moves.count('D')
