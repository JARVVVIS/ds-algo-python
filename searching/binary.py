def binary_search(arr,l,r,x):
    if l<r:
        mid = l+(r-l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,l,mid-1,x)
        else:
            return binary_search(arr,mid+1,r,x)
    return -1


def main():
    print('Enter elements: ',end=' ')
    arr = [int(x) for x in input().split()]
    print('Enter element to be searched: ')
    x = int(input())
    idx = binary_search(arr,0,len(arr)-1,x)
    print('Element found at index {}'.format(idx))
    
if __name__ == '__main__':
    main()