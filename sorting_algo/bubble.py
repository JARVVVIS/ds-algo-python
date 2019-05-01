def bubble_sort(arr):
    for i in range(len(arr)):
        swap = 0
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap+=1
        if swap==0:
            ## array alerady sorted 
            break

def main():
    print('Enter Elements: ',end=' ')
    arr = [int(x) for x in input().split()]
    bubble_sort(arr)
    ## print sorted array
    print('Sorted array {}'.format(arr))


if __name__ == '__main__':
    main()