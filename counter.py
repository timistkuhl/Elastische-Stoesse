class Counter:

    def __init__(self, startCount: int = 0):
        self.currentCount = startCount
        
    def countUp(self, increment: int):
        self.currentCount += increment