
def sort_insertion(arr,size):
    for i in range(size):
        key = arr[i] #to keep check of the variable which we are moving into the sorted array
        j=i-1
        while(j>=0 and arr[j]>key): #if our element is smaller
            arr[j+1] = arr[j] #shift by one
            j-=1
        
        arr[j+1] = key #j-=1 would have been done 1 extra time

    return arr
        






def main():
    arr = [int(x) for x in input().split()] #make the array
    size = len(arr) #size of array
    sorted_arr = sort_insertion(arr,size)
    print(sorted_arr)


if __name__ == '__main__':
    main()