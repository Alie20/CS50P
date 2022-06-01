import random
while (True):
    try:
        n = int(input("Level: "))
        number = random.randint(1,n)
        while(True):
            try :
                g = int(input("Guess: "))
                if (g == number):
                    print("Just Right!")
                    break
                elif (g>number):
                    print("Too large!")
                elif (g<number):
                    print("Too small!")
            except ValueError:
                continue
        break
    except ValueError:
        continue


