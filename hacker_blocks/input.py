def main():
    add = []
    check = True
    while(check):
        num = int(input())
        add.append(num)
        if(sum(add)<=0):
            add.pop()
            check = False
    if(len(add)==0):
        print(0)
    else:
        for i in add:
            print(i)



if __name__ == '__main__':
    main()