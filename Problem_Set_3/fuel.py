from math import floor
def get_ratio ():
    while(True):
        try:
            result = input("Fraction: ")
            result = result.split("/")
            try:
                x = int(result[0])
                y = int(result[1])
                if (y !=0) and (y >=x):
                    break
            except ValueError:
                pass
        except TypeError:
            pass
    return result
def main():
    result = get_ratio()
    x = int(result[0])
    y = int(result[1])
    total = x/y
    if (total >= 0.99):
        print("F")
    elif (total <=0.1):
        print("E")

    else:
        print(f"{round(x/y*100)}%")

main()