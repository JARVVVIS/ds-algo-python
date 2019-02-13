def main():
    t = int(input())
    while(t):
        num = int(input())
        t_ = list(input())
        tower = [int(x) for x in t_ ]
        count=0
        for i in range(num):
            if i==num-1:
                if tower[i]==0 and tower[i-1]==0:
                    tower[i]=1
                    count+=1
            else:
                if tower[i] == 0 and tower[i-1] ==0 and tower [i+1]==0:
                    tower[i]=1
                    count+=1
        print(count)
        t-=1


if __name__ == '__main__':
    main()