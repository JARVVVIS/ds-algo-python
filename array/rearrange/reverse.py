def reverse(arr,l,r):
    if(l<r):
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp 
        reverse(arr,l+1,r-1)
    return




def main():
    arr = [int(x) for x in input().split()]
    size = len(arr)
    reverse(arr,0,size-1)
    print(arr)


if __name__ == '__main__':
    main()