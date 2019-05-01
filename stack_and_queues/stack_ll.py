## Implementing stack using a single Linked List

class Node:

    def __init__(self,value):
        self.data = value
        self.link = None 

class Stack:
    def __init__(self):
        ## initialize the head 
        self.top = None 
        self.size = 0
    
    def isEmpty(self):
        ## if head is None then empty
        return self.top == None

    def size(self):
        return self.size
        
    def push(self,x):
        self.size += 1
        ## push the element at top of stack
        temp = Node(x)
        temp.link = self.top 
        ## a node object
        self.top = temp
    
    def pop(self):
        if self.isEmpty():
            print("NOthing to pop")
        else:
            data = self.top.data
            self.top = self.top.link
            print('{} pooped'.format(data))
            return data

    def peek(self):
        if self.isEmpty():
            print("You Perv")
        else:
            return self.top.data




def main():
    s = Stack()
    print(s.isEmpty())
    s.pop()
    s.peek()
    for i in range(20):
        s.push(i)
        print(s.top.data)
    print(' Last {}'.format(s.size))
    s.push(10)
    s.pop()



if __name__ == '__main__':
    main()