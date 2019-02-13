def main():
    t = int(input())
    while(t):
        num = int(input())
        attack = [int(x) for x in input().split()]
        defence = [int(x) for x in input().split()]
        total = [0 for x in range(num)]
        for i in range(num):
            if(i==num-1):
                total[i]=attack[0]+attack[i-1]
            else:
                total[i] = attack[i+1]+attack[i-1]
        count = -1
        for i in range(num):
            if(defence[i]>total[i] and count<defence[i]):
                count = defence[i]
        print(count)
        t-=1



if __name__ == '__main__':
    main()