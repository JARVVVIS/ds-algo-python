def swap(arr,i):
    temp = arr[i]
    arr[i] = arr[arr[i]]
    arr[arr[i]] = temp



def rearrange(arr,size):
    i = 0 
    while i<size:
        if arr[i] >= 0 and arr[i]!=i:
            temp = arr[i]
            arr[i] = arr[arr[i]]
            arr[temp] = temp
        else:
            print(arr[i],i)
            i+=1



def main():
    inp =  [-1 ,-1 ,6 ,1 ,9, 3 ,2 ,-1 ,4, -1]
    # arr = [int(x) for x in input().split()] #take input of array
    # size = len(arr) #size of array
    rearrange(inp,len(inp))
    print(inp)


if __name__ == '__main__':
    main()