


def main():
    t = int(input())
    while _ in range(t):
        number = int(input())
        number = list(number) #convert the list to number
        check_1 = div3(number)
        if(check_1):
            print("Yes")
            break
        else:
            if(div4(number)):
                print("Yes")
                break
        print("NO")
        

            



if __name__ == '__main__':    
    main()