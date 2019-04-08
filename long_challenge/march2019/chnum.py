def main():
    t = int(input())
    while(t):
        size = int(input())
        arr  = [int(x) for x in input().split()]
        pos = 0 
        for j in arr:
            if j>0 :
                pos+=1
        pos = max(pos,size-pos)
        if pos==size:
            print(pos,pos)
        else:
            print(pos,size-pos)
        t-=1





if __name__ == '__main__':
    main()