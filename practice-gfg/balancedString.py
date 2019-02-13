alpha = list("abcdefghijklmnopqrstuvwxyz")

def gen_even(num):
    string=[0 for i in range(num)]
    for i in range(num//2):
            string[i]=alpha[i]
    for i in range(num,num//2,-1):
            string[i-1]=alpha[i-num-1]
    return string

def gen_odd(num):
    string=[0 for i in range(num)]
    for i in range(num//2+1):
            string[i]=alpha[i]
    for i in range(num,num//2+1,-1):
            string[i-1]=alpha[i-num-1]
    return string


def manipulate(num):
    list1 = list(str(num))
    list2 = [int(x) for x in list1]
    if(num%2==0):
        list_ = gen_even(num)
        str_  = ''.join(list_)
        return str_
    elif(num%2!=0 and sum(list2)%2!=0):
        list_ = gen_even(num)
        str_  = ''.join(list_)
        return str_
    else:
        list_ = gen_even(num)
        str_  = ''.join(list_)
        return str_

def main():
    t = int(input())
    while(t):
        num = int(input())
        string = ''
        while(num>0):
            str_ = manipulate(num)
            string +=str_
            num-=26
        print(string)
        t-=1







if __name__ == '__main__':
    main()