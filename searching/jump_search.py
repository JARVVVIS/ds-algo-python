from math import sqrt

def search(arr,l,r,x):
    for i in range(l,r+1):
        if arr[i]==x:
            return i
    return -1


def main():
    arr = [int(x) for x in input().split()]
    print('Enter number to be found')
    x = int(input())
    jump = int(sqrt(len(arr))) #optimal jump
    size = len(arr)
    ans=-1
    for i in range(0,size,jump):
        if(arr[i]==x):
            ans = i 
            break
        elif arr[i]>x: #interval milgya
            l=i-jump+1
            r = i-1
            ans = search(arr,l,r,x)
            break

    print("Required ans is {}".format(ans))


if __name__ == '__main__':
    main()