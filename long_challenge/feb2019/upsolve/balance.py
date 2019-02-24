from collections import Counter


def num_op(comps):
    p=0
    n=0
    for i in comps:
        if i<0:
            n-=i
        elif i>0:
            p+=i
    return min(p,n)+abs(p-n)

def main():
    t = int(input()) #test case
    while(t):
        s = input()
        n = len(s)
        ctrs = Counter(s) #sorted characters
        lim = min(26,n)  #kitne total diff type ke charaters ho skte hai
        ans = 10000001 #dummy to start with
        for i in range(1,lim+1):
            #haar ke liye check karengey ke itne ke liye possible hai bhi yaa nahi
            #like onlt 1 char,2 char ,3 char
            if(n%i != 0):
                continue #possible he nahi hai
            
            req = n//i #req by each char
            tot = 0
            comps = []
            for val in ctrs:
                if(tot==i):
                    break
                comps.append(ctrs[val]-req)
                tot +=1
            #comps is a list storing ek particular i ke liye kya deficits hai char ke
            res = num_op(comps)
            if res<ans:
                ans=res

        print(ans)

        t-=1



if __name__ == '__main__':
    main()