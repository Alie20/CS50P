import sys,csv

if (len(sys.argv)>3):
    sys.exit("Too many command-line arguments")
elif(len(sys.argv) < 3):
    sys.exit("Too few command-line arguments")
elif not (sys.argv[1].endswith('.csv')):
    sys.exit("Not a CSV file")
else:
    try:
        data = []
        with open(sys.argv[1], newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                last,first = row["name"].strip().split(',')
                data1 = {"first":first.strip(),"last":last.strip(),"house":row["house"]}
                data.append(data1)
        print(data)

        with open(sys.argv[2],"w") as file:
            fieldnames = ['first', 'last','house']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for data_ in data:
                writer.writerow(data_)

    except FileNotFoundError:
        sys.exit("File not Found")
