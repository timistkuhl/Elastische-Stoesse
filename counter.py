class Counter:

    def __init__(self, startCount):
        self.startCount = startCount
        self.currentCount = startCount
        
    def countUp(self, increment: int):
        self.currentCount += increment