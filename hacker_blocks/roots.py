import math

def main():
    num=input().split()
    num = [int(x) for x in num]
    if(num[1]**2-4*num[0]*num[2]>0):
        print("Real and Distinct")
        root1 = ((-num[1]+math.sqrt(num[1]**2-4*num[0]*num[2]))/2*num[0])
        root2 = ((-num[1]-math.sqrt(num[1]**2-4*num[0]*num[2]))/2*num[0])
        print(root2 , " " , root1)
    elif(num[1]**2-4*num[0]*num[2]==0):
        print("Real and Equal")
        root = -num[1]/2*num[1]
        print(root," ",root)
    else:
        print("Imaginary")


if __name__ == '__main__':
    main()