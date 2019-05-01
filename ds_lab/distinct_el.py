## 2.1 Finding unique numbers in an array using python

def main():
    print("Enter array elements: ",end=' ')
    arr = [int(x) for x in input().split()]
    ## sort the array in nLogn
    arr = sorted(arr)
    for i in range(len(arr)):
        if i == len(arr)-1 and arr[i] != arr[i-1]:
            print(arr[i])
            break
        if arr[i] != arr[i+1]:
            print(arr[i],end=' ')
    
if __name__ == '__main__':
    main()
