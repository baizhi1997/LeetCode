
# @Title: 按序打印 (Print in Order)
# @Author: qinxinlei
# @Date: 2019-08-08 19:39:17
# @Runtime: 76 ms
# @Memory: N/A

from threading import Semaphore
class Foo:
    def __init__(self):
        self.two = Semaphore(0)
        self.three = Semaphore(0)

        
    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.two.release()

        
    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.two:
            printSecond()
            self.three.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.three:
            printThird()
