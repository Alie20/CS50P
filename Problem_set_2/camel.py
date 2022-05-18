name = input("Enter the name")
modified_name = ''
for i in range(len(name)):
    if not (name[i].isupper()):
        modified_name += name[i]
    else:
        modified_name +="_"
        modified_name += name[i].lower()
print(modified_name)

