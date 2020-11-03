
# @Title: 商品折扣后的最终价格 (Final Prices With a Special Discount in a Shop)
# @Author: qinxinlei
# @Date: 2020-07-29 12:13:57
# @Runtime: 68 ms
# @Memory: 13.4 MB

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack, result = [], [i for i in prices]
        for i in range(len(prices)):
            # 当stack非空且stack栈顶元素在prices对应的值大于prices[i]时触发while循环
            while stack and prices[stack[-1]] >= prices[i]:
                result[stack[-1]] -= prices[i] # 将stack中所有对应在prices的满足价格条件的值都减去prices[i]
                stack.pop() # 弹出栈顶元素
            stack.append(i) # 储存索引
        return result 

