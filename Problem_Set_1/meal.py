def main():
    time = input('What is the time')
    converted_time = convert(time)
    if (7 <= converted_time <=8 ):
        print('breakfast time')
    elif (12 <= converted_time <=13 ):
        print('lunch time')
    elif (18 <= converted_time <= 19):
        print('dinner time')


def convert(time):
    count = 0
    time = time.split(':')
    count += int(time[0])
    count += int(time[1])/60
    return (count)


if __name__ == "__main__":
    main()
