def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def main():
    print('Enter elements: ',end = ' ')
    arr = [int(x) for x in input().split()]
    insertion(arr)
    ## print sorted array
    print('Sorted array {}'.format(arr))

if __name__ == '__main__':
    main()