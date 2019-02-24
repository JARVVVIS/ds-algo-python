def replace(string,c1,c2):
    if(len(string)==0):
        return string

    string2 = replace(string[1:],c1,c2)
    if string[0]==c1:
          return c2+string2
    return string[0]+string2
  


def main():
    string = (input())
    c1,c2 = input().split()
    new_str = replace(string,c1,c2)
    print(new_str)
    
    


if __name__ == '__main__':
    main()