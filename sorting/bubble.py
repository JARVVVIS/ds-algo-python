#swap the adjacant elements if they are in wrong order


def sort(arr,size):
#if the array is already sorted then no swap will happen 
#we should break the j loop in that case -> O(n)
    swap = False
    for j in range(size-1):
        for i in range(size-1):
            if arr[i]>arr[i+1]:
                swap = True
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1]  = temp
        
        if swap == False:
           break 
    
    return arr




def main():
    arr = [int(x) for x in input().split()]
    size = len(arr)
    sorted_arr = sort(arr,size)
    print(sorted_arr)



if __name__ == '__main__':
    main()