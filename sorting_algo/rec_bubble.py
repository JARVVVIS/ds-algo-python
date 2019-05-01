## just for fun things
def rec_bubble(arr):
    ## bring the largest element to the last
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            ## now call the function on last-1 elements
            ## we are basically passing the same array
            ## and calling the recursion stack n times
            ## same as loop
            rec_bubble(arr)

def main():
    print('Enter elements: ')
    arr = [int(x) for x in input().split()]
    rec_bubble(arr)
    ## print the sorted array
    print('Sorted array: {}'.format(arr))

if __name__ == '__main__':
    main()