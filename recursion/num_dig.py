def count_dig(num,count=0):
    if(num<=9):
        count += 1
        print(count)
        return
    count_dig(num//10,count+1)


def main():
    num = int(input())
    count_dig(num)




if __name__ == '__main__':
    main()