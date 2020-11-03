
# @Title: 钥匙和房间 (Keys and Rooms)
# @Author: qinxinlei
# @Date: 2018-11-22 15:14:06
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        set1=set()
        stack=[0]
        while stack:
            p=stack.pop()
            if p not in set1:
                set1.add(p)
                stack+=rooms[p]
        return len(set1)==len(rooms)
