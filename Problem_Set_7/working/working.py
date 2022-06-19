import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #check the pattern
    if matches :=re.search('^(\d+:?[\d]*) (AM|PM) to (\d+:?[\d]*) (AM|PM)',s):

        # save the data
        period = []
        period.append(matches.group(2))
        period.append(matches.group(4))

        # check if there is two number or one
        if ":" in matches.group(1):
            flag = 0
            first_one , first_two = matches.group(1).split(":")
            end_one , end_two = matches.group(3).split(":")
        else:
            flag = 1
            first_one = matches.group(1)
            end_one= matches.group(3)
            first_two = "00"
            end_two = "00"

        # check the number is valid or not & change the value accoriding to time
        if (flag == 0 and (int(first_two) >59 or int(end_two) >59)):
            raise ValueError
        else :
            if (period[0] == "PM"):
                if (int(first_one) <12 ):
                    first_one = (int(first_one)+12)%24
                else:
                    raise ValueError
            elif (period[0] == "AM"):
                first_one = (int(first_one)+12)%12

            if (period[1] == "PM"):
                if (int(end_one) <12):
                    end_one = (int(end_one)+12)%24
            elif (period[1] == "AM"):
                end_one = (int(end_one)+12)%12


        time = f"{str(first_one).zfill(2)}:{first_two.zfill(2)} to {str(end_one).zfill(2)}:{end_two.zfill(2)}"

    else:
        raise ValueError
    return(time)

if __name__ == "__main__":
    main()
