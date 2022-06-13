from tabulate import tabulate

import sys

if (len(sys.argv)>2):
    sys.exit("Too many command-line arguments")
elif(len(sys.argv) == 1):
    sys.exit("Too few command-line arguments")
elif not (sys.argv[1].endswith('.csv')):
    sys.exit("Not a Python file")
else:
    try:
        pizza=[]
        with open(sys.argv[1],"r")as file:
            lines = file.readlines()
        for line in lines:
            row = line.strip().split(",")
            pizza.append(row)
        headers = pizza[0]
        print(tabulate(pizza[1:],headers,tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not Found")
