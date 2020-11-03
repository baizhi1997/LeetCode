
# @Title: IP 地址无效化 (Defanging an IP Address)
# @Author: qinxinlei
# @Date: 2019-08-08 16:37:15
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
