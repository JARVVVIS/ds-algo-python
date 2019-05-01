## program to print the nth fibonacci number
## 0 1 1 2 3 ....

## method-1
## Time complexity - exponential
## Space - 1
def recursion(n):
    if n==0:
        return 0
    if n==1 :
        return 1
    return recursion(n-1)+recursion(n-2)
    
## using DP- to store repeated values
## time-> O(n)
## space -> O(n)
def dp(n):
    arr = [0]*(n+1)
    arr[0],arr[1] = 0,1
    for i in range(2,n+1):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n]

## space optimization on DP
## O(n) and O(1)
def dp_optimize(n):
    a,b = 0,1
    if n==0:
        return a 
    for i in range(2,n+1):
        c = a+b
        a = b 
        b = c  
    return b

def main():
    print("Enter N to find the Nth fibonacci number")
    n = int(input())
    ans1 = recursion(n)
    ans2 = dp(n) 
    ans3 = dp_optimize(n) 
    print('Ans by recursion {} ; ans by dp {} ; ans by optimized dp {}'.format(ans1,ans2,ans3))

if __name__ == '__main__':
    main()