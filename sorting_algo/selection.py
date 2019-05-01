def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

def main():
    print('Enter elements: ',end=' ')
    arr = [int(x) for x in input().split()]
    selection_sort(arr)
    ## sorted array
    print('Sorted array is: {}'.format(arr))

if __name__ == '__main__':
    main()