import random


def main():
    level = get_level()
    score = generate_integer(level)
    print(f"Score: {score}")
    ...


def get_level():
    while True:
        try:
            a = int(input("Level: "))
            if (1<=a<=3):
                return a
            else:
                continue
        except ValueError:
                pass
def generate_integer(level):
    score = 0

    for i in range(10):
        if (level == 1):
            start = 10**(int(level)-1)-1
            end = (10**int(level)-1)
        else:
            start = 10**(int(level)-1)
            end = (10**int(level)-1)


        n1 = random.randint(start,end)
        n2 = random.randint(start,end)
        for i in range(3):
            try:
                ans = int(input(f"{n1} + {n2} = "))
                if (ans == n1+n2):
                    score +=1
                    break
                else:
                    if i<2:
                        print("EEE")
                        continue
                    else:
                        print("EEE")
                        print(f"{n1} + {n2}= {n1+n2}")
            except ValueError:
                print("EEE")
                if i >=2:
                    print(f"{n1} + {n2}= {n1+n2}")
                    pass

    return score

if __name__ == "__main__":
    main()

