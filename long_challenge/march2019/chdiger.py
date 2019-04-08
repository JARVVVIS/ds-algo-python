def magic(num):
    return int(''.join(str(i) for i in num))
def main():
    t = int(input())
    while(t):
        num,d = [int(x) for x in input().split()]
        ls=[int(x) for x in str(num)]
        for i in range(1,len(ls)):
            if i==1 and ls[i]==0:
                continue
            if ls[i-1]<=ls[i]:
                continue
            elif ls[i]<ls[i-1]:
                ls_l = ls[:i-1]
                ls_r = ls[i:]
                ls = ls_l+ls_r
                ls.append(d)
                break
        if ls[-1]>d:
            ls[-1]=d

        print(magic(ls))
        t-=1

if __name__ == '__main__':
    main()