class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.curr_index = 0
        # self.buffer = [None] * self.capacity
        self.buffer = [0] * self.capacity

    def append(self, item):
        self.buffer[self.curr_index] = item
        self.curr_index += 1
        # if len(self.buffer) == self.capacity -1:
        if self.curr_index == self.capacity:
            self.curr_index = 0
            # self.buffer[self.curr_index] = item

    def get(self):
        return [i for i in self.buffer if i is not 0]

a = ["a", "b", "c", "d", "e"]
print(len(a))
"""
index =  [0 1 2 3]
buffer = [a]
"""