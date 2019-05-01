## implementing queue from scratch
## FIFO -> First pushed , will be Pooped First

class Queue:
    def __init__(self):
        self.queue = [None]*10
        self.capacity = 10
        self.rear = -1
    
    def isEmpty(self):
        return self.rear == -1
    
    def enqueue(self,x):
        if self.rear < self.capacity - 1:
            self.rear += 1
            self.queue[self.rear] = x 
        else:
            print("Overflow Bitch")
    
    def dequeue(self):
        if self.isEmpty():
            print("Underflow")
        else:
            data = self.queue[0]
            del self.queue[0]
            return data

    def peek(self):
        if not self.isEmpty():
            print("{} is the front of queue".format(self.queue[0]))

        else:
            print("Nothing to show")


def main():
    q = Queue()
    q.dequeue()
    q.peek()
    for i in range(10):
        q.enqueue(i)
        q.peek()
        print('and in last is {}'.format(q.queue[q.rear]))
    q.enqueue(1000)


if __name__ == '__main__':
    main()