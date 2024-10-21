class MyQueue:
    def __init__(self):
        self.front = self.back = -1
        self.arr = list()
    def push(self, x):
        self.back += 1
        self.arr.append(x)
        if self.front==-1:
            self.front += 1
    def pop(self):
        if not self.arr:
            #raise Exception("Queue is empty.")
            return -1
        ret = self.arr[self.front]
        self.front += 1
        if self.front > self.back:
            self.front = self.back = -1
            self.arr.clear()
        return ret
