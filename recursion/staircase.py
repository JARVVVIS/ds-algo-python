# problem statement
# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.


def count_stairs(stairs):
    output = [0 for i in range(stairs+1)]
    output[0]=1
    output[1]=1
    output[2]=2
    output[3]=4
    for i in range(4,stairs+1):
        output[i]=output[i-1]+output[i-2]+output[i-3]
    return output[stairs]



def main():
    stairs = int(input())
    print(count_stairs(stairs))


if __name__ == '__main__':
    main()