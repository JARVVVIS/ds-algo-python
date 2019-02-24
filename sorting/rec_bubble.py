

def sort_rec(arr,size):
    if(size==1): #recurssion is only used as loop
        return 


    for i in range(size-1):
        if arr[i]>arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    
    sort_rec(arr,size-1)
    return arr



def main():
    arr = [int(x) for x in input().split()]
    size = len(arr)
    sorted_arr = sort_rec(arr,size)
    print(sorted_arr)




if __name__ == '__main__':
    main()