## a devide and conquer algorithm

## merge two subarrays
def merge(arr,l,r,mid):
    ## create an auxillary array
    temp = [0]*(r-l+1)
    i,j,k = l,mid+1,0
    while(i<=mid and j<=r):
        if arr[i]<=arr[j]:
            temp[k] = arr[i]
            ## move to next element on first subarray
            i+=1
        else:
            temp[k] = arr[j]
            ## move to next element on second subarray
            j+=1
        ## no matter an element is added in temp
        k+=1
    
    ## check for leftovers
    while(i<=mid):
        temp[k] = arr[i]
        k+=1
        i+=1
    while(j<=r):
        temp[k] = arr[j]
        k+=1
        j+=1
    for i,j in zip(range(len(temp)),range(l,r+1)):
        arr[j] = temp[i]

## sort the arrays
def merge_sort(arr,l,r):
    if l<r:
        ## define midpoint
        mid = l+(r-l)//2
        ## sort the 1st subarray
        merge_sort(arr,l,mid)
        ## sort the 2nd subarray
        merge_sort(arr,mid+1,r)
        ## merge the 2 arrays
        merge(arr,l,r,mid)


def main():
    print('Enter elements ',end=' ')
    arr = [int(x) for x in input().split()]
    ## call merge sort to sort the whole array
    merge_sort(arr,0,len(arr)-1)
    ## print the merged array
    print(arr)

if __name__ == '__main__':
    main()
