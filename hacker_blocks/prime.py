import math

def seive(number):
    prime = [True for i in range(number+1)]

    for i in range(2,int(math.sqrt(number))+1):
        if(prime[i]):
            for j in range(i*i,number+1,i):
                prime[j] = False
    
    return prime[number]






def main():
    n = int(input())
    ans = seive(n)
    if(ans):
        print("Prime")
    else:
        print("Not Prime")

if __name__ == '__main__':
    main()