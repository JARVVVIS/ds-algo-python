def main():
    print('Enter the elements: ',end=' ')
    arr = [int(x) for x in input().split()]
    print('Enter element to be searched: ')
    x = int(input())
    for i,element in enumerate(arr):
        if element == x:
            print('Element found at {} index'.format(i))
            break 
        
if __name__ == '__main__':
    main()