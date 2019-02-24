


def main():
    arr = [int(x) for x in input().split()]#create an array
    size = len(arr)
    print('Enter the number to be searched ')
    x = int(input())
    ans = -1
    for i in range(size):
        if arr[i]==x:
            ans=i
            break
    print('Index of the number is {} '.format(ans))


if __name__ == '__main__':
    main()