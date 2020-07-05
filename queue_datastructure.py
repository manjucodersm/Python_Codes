from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def frent(self):
        return self.buffer[-1]

    def is_empty(self):
        return self.size() == 0

queue = Queue()
queue.enqueue(1)
count = 0

while count < 10:
    num = queue.dequeue()
    queue.enqueue(num * 10)
    queue.enqueue((num * 10) + 1)
    print(num)
    count += 1
