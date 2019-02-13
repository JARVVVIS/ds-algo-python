def main():
    t = int(input())
    while(t):
        num = int(input())
        strings = []
        while(num):
            strings.append(input())
            num-=1
        
        a = strings[0]
        for x in strings:
            a = (set(a)&set(x))
         
        print(len(a))
        t-=1

if __name__ == '__main__':
    main()