## Count ways to reach the n’th stair
## person can climb either 1,2 or 3 stairs at a time

def main():
    print('Enter number of stairs ',end=' ')
    n = int(input())
    arr = [0]*(n+1)
    arr[0],arr[1],arr[2]=1,1,2
    for i in range(3,n+1):
        ## do the memotisation
        arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
    print('Number of ways are {}'.format(arr[n]))

if __name__ == '__main__':
    main()