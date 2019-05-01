## using hashmaps a.k.a dictionaries
def print_duplicates(arr):
    dict = {}
    for ele in arr:
        try:
            dict[ele] += 1
        except:
            dict[ele] = 1
    
    for item in dict:
        if(dict[item]>1):
            print(item,end=' ')

def main():
    print('Enter elements: ',end=' ')
    arr = [int(x) for x in input().split()]
    print_duplicates(arr)

if __name__ == '__main__':
    main()