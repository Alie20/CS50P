import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip):
        a = ip.split('.')
        if len(a) != 4:
            return False
        for _ in a:
            if int(_)>255 or int(_)<0:
                return False
        return True
    else:
        return False




if __name__ == "__main__":
    main()
