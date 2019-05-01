## insertion and deletion are only on one end o(1)
## stacks are linear data structures
## array high index -> top , low index -> bottom
## LIFO 

class Stack:

    def __init__(self):
        self.capacity = 10
        self.stack = [None]*self.capacity
        self.top = -1
    
    def isEmpty(self):
        return self.top == -1

    def push(self,item):
        if self.top < self.capacity-1:
            self.top += 1
            self.stack[self.top] = item
        else:
            print("Stack Overflow bitch")
    
    def pop(self):
        if self.top != -1:
            data = self.stack[self.top]
            self.top -= 1  
            print('{} was popped'.format(data))   
        else:
            print("Stack Underflow bitch")

    def peek(self):
        if self.top != -1:
            return self.top

        else:
            print("Nothing to show")



def main():
    
    # create the object
    s = Stack();
    print(s.isEmpty())
    s.pop()
    s.peek()
    for i in range(20):
        print(i)
        print(s.top,s.capacity)
        s.push(i)
    print(' Last {} {}'.format(s.top,s.capacity))
    s.push(10)
    s.pop()






if __name__ == '__main__':
    main()