food = {}
while (True):
    try:
        item = input().upper()
        if item in food :
            food[item] += 1
        else:
            food[item] =1
    except EOFError:
        print("",end="")
        break

for item in sorted(food):
    print (f"{food[item]} {item}")