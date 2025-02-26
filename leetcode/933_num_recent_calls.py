class RecentCounter:
    def __init__(self):
        self.MAX_SIZE = 3001
        self.queue = [None for i in range(self.MAX_SIZE)]
        self.front = -1
        self.rear = -1
    def is_empty(self):
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False
    def size(self):
        if self.is_empty():
            return 0
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return abs(self.MAX_SIZE - self.front) + self.rear + 1
    def dequeue(self):
        if self.is_empty():
            temp = None
        elif self.size() == 1:
            temp = self.queue[self.front]
            self.front = self.rear = -1
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1)%self.MAX_SIZE
        return temp
    def enqueue(self, t):
        if self.is_empty():
            self.front = self.rear = 0
        else:
            if (self.rear + 1)%self.MAX_SIZE == self.front:
                self.front = (self.front + 1)%self.MAX_SIZE
            self.rear = (self.rear + 1)%self.MAX_SIZE
        self.queue[self.rear] = t
    def peak_front(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def ping(self, t: int) -> int:
        self.enqueue(t)
        while self.peak_front() < t-3000:
            self.dequeue()
        return self.size()
