# implementation of jump search
import math

def linear_search(arr,l,r,x):
    print(l,r)
    for i in range(l,r):
        if arr[i] == x:
            return i
    return -1

def jump_search(arr,x):
    n = len(arr)-1
    ## block size
    m = int(math.sqrt(n))
    ans = -1
    for i in range(0,len(arr),m):
        print(i)
        if arr[i]<x:
            continue
        elif arr[i] == x:
            ans = i
            break
        else:
            ans =  linear_search(arr,(i-m),i,x)
            break
    return ans
            

def main():
    print('Enter Element ',end=' ')
    arr = [int(x) for x in input().split()]
    print('Enter the element to be searched: ')
    x = int(input())
    idx = jump_search(arr,x)
    print('Element found at {} index'.format(idx))

if __name__ == '__main__':
    main()