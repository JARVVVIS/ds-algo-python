import math
from math import gcd


def main():
    t  = int(input()) #take input of number of test case
    while(t>0):
        input_list = [int(x) for x in input().split()]
        n = input_list[0]
        a = input_list[1]
        b = input_list[2]
        k = input_list[3]
        a1 = int(n//a)
        b1 = int(n//b)
        lcm  = int((a*b)/gcd(a,b))
        lcm1  = int(n//lcm)
        count = int(a1+b1-lcm1*2)
        if(count>=k):
            print("Win")
        else:
            print("Lose")
        t-=1

if __name__ == '__main__':
    main()