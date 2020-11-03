
# @Title: 活字印刷 (Letter Tile Possibilities)
# @Author: qinxinlei
# @Date: 2019-06-26 11:51:46
# @Runtime: 120 ms
# @Memory: N/A

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len({s[:i] for s in itertools.permutations(tiles) for i in range(1, 8)})
