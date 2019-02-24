## haar element ke liye useey chota element dhundo and then swap karro
## basically har moment pe left main sorted array bannta rahega





def sort(arr,size):
    for i in range(size):
        min_index = i #this keeps track of next smallest element (element that will be at the ith position)
        j=i+1 #the unsorted part
        for k in range(j,size):
            if arr[min_index] > arr[k] : #we need to swap
                min_index = k #this is the element which deserves
        
        temp=None #nevertheless do the swapping
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp

    return arr






def main():
    size  = int(input())
    arr  = [int(x) for x in input().split()]
    soreted_arr = sort(arr,size)
    print(soreted_arr)


if __name__ == '__main__':
    main()