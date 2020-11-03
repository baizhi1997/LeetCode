
# @Title: 常数时间插入、删除和获取随机元素 (Insert Delete GetRandom O(1))
# @Author: qinxinlei
# @Date: 2018-12-04 11:51:27
# @Runtime: 92 ms
# @Memory: N/A

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr=[]
        self.dic={}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        self.dic[val]=len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        k,newVal=self.dic[val],self.arr[-1]
        self.arr[k]=newVal
        self.dic[newVal]=k
        self.arr.pop()
        self.dic.pop(val, None)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
