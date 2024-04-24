class Foo:
    def __init__(self):
        self.firstCalled = False
        self.secondCalled = False
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.firstCalled = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.firstCalled: continue     
        printSecond()
        self.secondCalled = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.secondCalled: continue   
        printThird()