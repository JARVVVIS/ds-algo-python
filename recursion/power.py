def rec_power(num,power):
    if(power<=0):
        return 1
    if(power==1):
        return num
    return num*rec_power(num,power-1)




def main():
    print("Enter number and respective power")
    num,power = [int(x) for x in input().split()]
    print(rec_power(num,power))

if __name__ == '__main__':
    main()