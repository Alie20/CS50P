from math import floor
def main():
    result = input("Fraction: ")
    fraction = convert(result)
    gauge = fraction(gauge)
    print(gauge)

def convert (result):
    while(True):
        try:
            result = result.split("/")
            x = int(result[0])
            y = int(result[1])
            z = x/y
            if z <=1:
                p = int(z*100)
                return p
            else:
                result = inpur("Fraction: ")
                pasee
        except (ZeroDivisionError ,ValueError):
                raise
def gauge(percentage):
    if percentage <=1 :
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__=="__main__":
    main()