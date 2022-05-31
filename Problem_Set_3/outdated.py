month = {
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}

no = [1,2,3,4,5,6,7,8,9,10,11,12]

while(True):
    data = input("Date").rstrip()
    date1 = data.replace(",","").split()
    date2 = data.split("/")
    try:
        if (date1[0] in month):
            if ("," in data):
                if (int(date1[1])>=31):
                    continue
                print(f"{date1[2]}-{month[date1[0]]}-{int(date1[1]):02d}")
                break
            else:
                continue
        elif (int(date2[0]) in no):
            if (int(date2[1])>=31):
                continue
            else:
                print(f"{date2[2]}-{int(date2[0]):02d}-{int(date2[1]):02d}",end="")
                break
    except ValueError:
        pass

