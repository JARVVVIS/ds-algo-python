#first sort the first 1-n elements 
# put the last element at correct position

def rec_insert(arr,size):
    if(size<=1):
        return
    rec_insert(arr,size-1)
    j=size-2
    key = arr[size-1]
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1] = key
    return arr


def main():
    arr = [int(x) for x in input().split()]
    size = len(arr)
    arr  = rec_insert(arr,size)
    print(arr)





if __name__ == '__main__':
    main()