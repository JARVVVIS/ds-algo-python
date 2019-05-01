## doing insertion sort recursively
def insertion_rec(arr,count):
    if count == len(arr):
        return
    key = arr[count]
    i = count-1
    while(i>=0 and arr[i]>key):
        arr[i+1] = arr[i]
        i = i-1
    arr[i+1] = key
    print(arr)
    insertion_rec(arr,count+1)

def main():
    print('Enter elements: ',end=' ')
    arr = [int(x) for x in input().split()]
    ##insertion sort
    insertion_rec(arr,1)
    print('Sorted array {}'.format(arr))

if __name__ == '__main__':
    main()