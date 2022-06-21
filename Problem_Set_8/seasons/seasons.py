from datetime import date
import datetime
import sys
import inflect


def main():
    data = input("Data of birth: ")
    if check(data):
        days = diff(data)
        print(convert(days))


def check(data):
    # check the date
    try:
        date_= data.split("-")
        if len(date_) == 3 :
            date(int(date_[0]),int(date_[1]),int(date_[2]))
            return 1
        else:
            raise ValueError
    except :
        sys.exit("Invalid Date")

def diff(date2):
    now = datetime.datetime.today().strftime ('%Y-%m-%d')
    dat = "2000-01-01"
    d1 = datetime.datetime.strptime(dat, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    delta = d1 - d2
    return delta.days*60*24

def convert(days):
    p = inflect.engine()
    words = p.number_to_words(days, andword="")
    return(f"{words.capitalize()} minutes")







if __name__ == "__main__":
    main()
