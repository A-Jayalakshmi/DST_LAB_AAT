# Enter your code here. Read input from STDIN. Print output to STDOUT
class QueueHandler(object):
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def front(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]
        
    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
        
    def enqueue(self, value):
        self.stack_in.append(value)

queue = QueueHandler()
n = int(input())
for _ in range(n):
    query = input().strip().split()
    if int(query[0]) == 1:
        queue.enqueue(int(query[1]))
    elif int(query[0]) == 2:
        queue.dequeue()
    else:
        print(queue.front())
