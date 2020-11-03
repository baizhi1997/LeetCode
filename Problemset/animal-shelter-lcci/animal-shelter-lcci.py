
# @Title: 动物收容所 (Animal Shelter LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 15:43:42
# @Runtime: 192 ms
# @Memory: 21.2 MB

class AnimalShelf:

    def __init__(self):
        self.cats = [] #猫的队列
        self.dogs = [] #狗的队列


    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0: #若是猫，入猫队
            self.cats.append(animal)
        else: #若是狗，入狗队
            self.dogs.append(animal)


    def dequeueAny(self) -> List[int]:
        if self.dogs and self.cats: #猫狗都存在，比较编号大小，领养编号小的
            if self.dogs[0][0] < self.cats[0][0]:
                return self.dogs.pop(0)
            else:
                return self.cats.pop(0)
        elif self.cats: #若只有猫存在
            return self.cats.pop(0)
        elif self.dogs: #若只有狗存在
            return self.dogs.pop(0)
        else:
            return [-1,-1]


    def dequeueDog(self) -> List[int]:
        if self.dogs:
            return self.dogs.pop(0)
        else:
            return [-1,-1]


    def dequeueCat(self) -> List[int]:
        if self.cats:
            return self.cats.pop(0)
        else:
            return [-1,-1]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
