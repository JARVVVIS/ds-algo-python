def main():
    t = int(input())
    while(t):
        num = int(input())
        ing = [int(x) for x in input().split()]
        ans = sum(ing)-(num-1)*1
        print(ans)
        t-=1

if __name__ == '__main__':
    main()