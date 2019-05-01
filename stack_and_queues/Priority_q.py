

class Node:
    ##  Node of a linked List has priority as well
    def __init__(self,value,priority):
        self.data = value
        self.link = None 
        self.prt = priority

class PriorityQ:
    ## We need the front refrence only 
    def __init__(self):
        self.front = None 
        self.size = 0
    
    def isEmpty():
        return self.size == 0
    
    def enqueue(self,item,prt):
        ## if same priority then FIFO principle

        ## make a temp Node
        temp = Node(item,prt)

        ## if first elememt or temp having priority higher than the best priority
        if self.size == 0 or temp.prt < self.front.prt:
            ## insert at the front
            temp.link = self.front
            self.front = temp
        else:
            ## else move till you find apt. priority
            ## traverse the linked list 
            p = self.front 
            while p.link != None and p.link.prt <= temp.prt:
                p = p.link 
            temp.link = p.link 
            p.link = temp
        self.size += 1

    def dequeue(self):
            ## this will be normal only 
        if self.size == 0:
            print("Nothing to delete")
        else :
            data = self.front 
            self.front = self.front.link

            print('{} was deleted'.format(data))
    

def main():
    q = PriorityQ()
    q.dequeue()
    for i in range(20):
        q.enqueue(i,i+10)
    q.enqueue(100000,23)
    p = q.front
    while p.link != None :
        print(p.data,p.prt)
        p = p.link
    print(p.data,p.prt)




if __name__ == '__main__':
    main()