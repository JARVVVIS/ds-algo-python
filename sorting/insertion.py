def insertion_sort(arr,size):
    for i in range(1,size):
        key = arr[i] #keep track of the current element
        j = i-1 #this varibale will loop over all the before element to put at right position
        while(j>=0 and arr[j]>key): #kitne elements choote hai
            arr[j+1]=arr[j] #shift by 1
            j-=1 #check the next previous element
        arr[j+1] = key #now put the element at sweet spot
    return arr


def main():
    arr = [int(x) for x in input().split()]
    size = len(arr)
    arr = insertion_sort(arr,size)
    print(arr)



if __name__ == '__main__':
    main()