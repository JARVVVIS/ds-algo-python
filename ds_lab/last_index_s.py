## 6. Finding last and first index of 1 in a sorted array in complexity logn.

def find_first(arr,l,r,x):
    if l<r:
        mid = l+(r-l)//2
        print(mid)
        ## incase searching for first two equals
        if arr[mid] == x and mid == 0:
            return mid
        if arr[mid] == x and x>arr[mid-1]:
            return mid
        elif arr[mid]<x:
            return find_first(arr,mid+1,r,x)
        else:
            return find_first(arr,l,mid-1,x)

def find_last(arr,l,r,x):
    if l<=r:
        mid = l+(r-l)//2
        ## if last two elements are same and being searched
        if arr[mid] == x and mid==len(arr)-1:
            return mid
        ## wont work for second last element (given last two are same)
        if arr[mid] == x and x<arr[mid+1]:
            return mid
        elif arr[mid] > x:
            return find_last(arr,l,mid-1,x)
        else:
            return find_last(arr,mid+1,r,x)
    return -1

def main():
    print('Enter elements: ',end=' ')
    arr = [int(x) for x in input().split()]
    print('Enter element to be searched ')
    x = int(input())
    last_idx = find_last(arr,0,len(arr)-1,x)
    first_idx = find_first(arr,0,len(arr)-1,x)
    print('The first index is {} and the last index is {}'.format(first_idx,last_idx))

if __name__ == '__main__':
    main()