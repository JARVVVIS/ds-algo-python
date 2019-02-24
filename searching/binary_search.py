

def binary_search(arr,l,r,x):
    ans = -1
    if l < r:
        mid = l + (r-l)//2 #mid which we will search first
        if arr[mid]==x:
            ans=mid
            return mid
        elif arr[mid] > x:
            return binary_search(arr,l,mid-1,x)
        else:
            return binary_search(arr,mid+1,r,x)






def main():
    arr = [int(x) for x in input().split()] #input array
    print('Enter the number to be searched ')
    x = int(input()) #enter the number
    idex = binary_search(arr,0,len(arr)-1,x)
    print("index of number is {}".format(idex))


if __name__ == '__main__':
    main()