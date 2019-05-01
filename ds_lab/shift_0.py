## 1 ->  Shifting of all 0's to right using single array
def main():
    print('Enter array Elements: ',end=' ')
    arr = [int(x) for x in input().split()]
    size = len(arr)
    #i-> index of non zero errors
    #j-> index of array in general
    #count-> number of zeros
    i,j,count =0,0,0
    while(j<size):
        if arr[j] != 0:
            ## copy anyways
            arr[i] = arr[j]
            ## increment both
            i+=1
            j+=1
        else:
            ## only increment the general index
            j+=1
            ## increment zero count
            count += 1
    ## copy number of zeros at the end
    for k in range(size-count,size):
        arr[k] = 0
    print('Final {}'.format(arr))


if __name__ == '__main__':
    main()