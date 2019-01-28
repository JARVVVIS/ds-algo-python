import numpy as np 

def get_subarr(arr):
    n = len(arr)
    if(len(arr)<=0):
        output = [[]]
        return output
    output = get_subarr(arr[:n-1])
    outputLen = len(output)

    for i in range(0,outputLen):
        output.append(output[i].copy())
        output[outputLen+i].append(arr[n-1]) #uss array pe jakke append kardo
    return output
    


def main():
    arr = [int(x) for x in input().split()]
    output = get_subarr(arr)
    for i in output:
        print(i,end=' ')

if __name__ == '__main__':
    main()