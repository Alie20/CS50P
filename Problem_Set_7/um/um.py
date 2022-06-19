import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    a = s.split(" ")
    for i in a:
        if re.search(r'(\bum\b)+',i,re.IGNORECASE):
            count = count + 1
    return count




if __name__ == "__main__":
    main()