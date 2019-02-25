
def merger(arr,l,mid,r):
    L = arr[l:mid+1]
    R = arr[mid+1:r+1]

    i,j,k=0,0,l
    while i<=len(L)-1 and j<=len(R)-1:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1

    #leftovers
    while i<len(L):
        arr[k]=L[i]
        k+=1 
        i+=1
    
    while j<len(R):
        arr[k]=R[j]
        k+=1
        j+=1



def sort(arr,l,r):
    if l < r:
        mid = l+(r-l)//2 
        sort(arr,l,mid) #sort the left subarray
        sort(arr,mid+1,r) #sort the right subarray
        merger(arr,l,mid,r) #merge the sorted arrays



def main():
    arr = [int(x) for x in input().split()] #array input
    size = len(arr)
    sort(arr,0,size-1)
    print(arr)



if __name__ == '__main__':
    main()