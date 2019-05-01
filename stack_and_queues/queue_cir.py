## implementing queue from circular linked list
## maintain only one refrence

class Node:
    def __init__(self,value):
        self.data = value
        self.link = None 

class Queue:

    def __init__(self):
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self,item):
        ## create a node
        
        temp = Node(item)
        if self.size == 0:
            self.rear = temp
            self.rear.link = self.rear
        ## add element to the last place
        ## imp to do to get adress of first element
        temp.link = self.rear.link
        self.rear.link = temp 
        self.rear = temp
        self.size += 1

    def dequeue(self):
        if not self.isEmpty():
            ## check if there is only one eleemnt
            if self.size == 1:
                temp = self.rear
                self.rear = None
                print('{} was deleted'.format(temp.data))

            else:
                temp = self.rear.link
                self.rear.link  = self.rear.link.link
                print('{} was deleted'.format(temp.data))
        else:
            print('Nothing to delete')

    
    def peek(self):
        if self.size == 0 :
            print('Nothing to show')
        else:
            val  = self.rear.link.data 
            print('{} is in front of the queue'.format(val))


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