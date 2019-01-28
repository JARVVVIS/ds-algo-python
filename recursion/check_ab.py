# rules
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'


def check_string(string):
   if len(string) == 0:
       return False
    if string[0] != 'a':
        return False
    if string[1] != 'a' and string[1:3] != 'bb':
        return False
    






def main():
    string = input()
    if check_string(string):
        print("True")
    else:
        print("False")




if __name__ == '__main__':
    main()