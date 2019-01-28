#binary search program implemented


def binary_search(array,x,l,r):
    if(l<=r):
        mid = (l+r)//2
        if array[mid] == x:
            return mid
        elif array[mid]>x:
            return binary_search(array,x,l,mid-1)
        else:
            return binary_search(array,x,mid+1,r)
    
    return -1



def main():
    print("Enter the size of array")
    size = int(input())
    print("Enter the array")
    array = [int(x) for x in input().split()]
    print("Enter the number to be searched")
    x = int(input())
    print(binary_search(array,x,0,size-1))


if __name__ == '__main__':
    main()