## quicksort implementation

## pivot around the last element
def partition(arr,l,r):
    i = l
    pivot = arr[l]
    ## not the first element as it is the pivot itself
    for j in range(l,r+1):
        if arr[j]<pivot:
            ## since we have taken i=-1; increment first
            i+=1
            temp  = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    print(arr)
    ## swap the correct position of pivot
    temp = arr[i]
    arr[i] = arr[l]
    arr[l] = temp
    
    return i

def quick_sort(arr,l,r):
    if l < r:
        ## calculate the partition index
        p = partition(arr,l,r)

        quick_sort(arr,l,p-1)
        quick_sort(arr,p+1,r)


def main():
    print('Enter elements',end=' ')
    arr = [int(x) for x in input().split()]
    quick_sort(arr,0,len(arr)-1)
    ## print sorted array
    print(arr)

if __name__ == '__main__':
    main()

