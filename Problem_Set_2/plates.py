def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (((len(s)>6) or (len(s)<2)) or not((s[0].isalpha()) and (s[1].isalpha()))):
        #print("2")
        return False
    i = 0

    while i < len(s):
        if s[i].isdigit():
            if s[i] == '0':
                #print("1")
                return False
            else:
                break
        i=i+1
    for charachter in (s):
        if (charachter == "." or charachter == "," or charachter == "!" or charachter == "?"):
            #print('3')
            return False

    for i in range(len(s)-1):
        if s[i].isdigit():
            if s[i+1].isalpha():
                return False

    return True


main()