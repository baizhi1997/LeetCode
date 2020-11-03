
# @Title: 航班预订统计 (Corporate Flight Bookings)
# @Author: qinxinlei
# @Date: 2019-08-28 16:15:50
# @Runtime: 996 ms
# @Memory: N/A

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        s = [0] * (n + 1)
        for i, j, k in bookings:
            s[i - 1] += k
            s[j] += -k
        for i in range(n - 1):
            s[i + 1] += s[i]
        return s[:-1]
