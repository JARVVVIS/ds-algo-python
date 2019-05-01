## Deletion end -> Front 
## insertion end -> rear

## a node of Linked List (has value and link as attributes)
class Node:
    def __init__(self,value):
        self.data = value
        self.link = None

class Queue:

    ## Double Ended Linked List (rear and top both set to None)
    def __init__(self):
        self.top = None 
        self.rear = None 
        self.size = 0
    
    ## function to check if it's empty
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self,item):
        self.size += 1
        ## create a Node of the given data
        temp = Node(item)
        ## last ke naam main temp dalle
        if self.top == None:
            self.top = temp
        else:
            self.rear.link = temp
        self.rear = temp 


    def dequeue(self):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.link
            print('{} was deleted'.format(data))
        
        else:
            print('Nothing to Delete Bruhhhh')

    def peek(self):
        if not self.isEmpty():
            data = self.top.data
            print('The front of queue is {}'.format(data))
        else:
            print('Nothing to show')

def main():
    q = Queue()
    q.dequeue()
    q.peek()
    for i in range(10):
        q.enqueue(i)
        q.peek()
        print('and in last is {}'.format(q.rear.data))
    q.enqueue(1000)
    q.peek()
    print('and in last is {}'.format(q.rear.data))
    q.dequeue()
    q.peek()
    print('and in last is {}'.format(q.rear.data))





if __name__ == '__main__':
    main()