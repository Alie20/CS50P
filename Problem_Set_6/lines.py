import sys

if (len(sys.argv)>2):
    sys.exit("Too many command-line arguments")
elif(len(sys.argv) == 1):
    sys.exit("Too few command-line arguments")
elif not (sys.argv[1].endswith('.py')):
    sys.exit("Not a Python file")
else:
    try:
        count = 0
        with open(sys.argv[1],"r")as file:
            lines = file.readlines()
            for line in lines:
                if line.isspace() or line.lstrip().startswith('#'):
                    continue
                else:
                    count +=1
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(count)
    with open("FILENAME","w") as file1:
        file1.write(str(count))