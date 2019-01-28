# poor approach
def print_num(num,i=[]):
    if num == 1:
        i.append(num)
        i.reverse()
        print(" ".join(map(str,i)))
        return
    i.append(num)
    print_num(num-1,i)


    
def main():
    num = int(input())
    print_num(num)

if __name__ == '__main__':
    main()