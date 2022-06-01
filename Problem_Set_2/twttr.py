sentence = input("enter your sentence ")
new = ''
for i in range(len(sentence)):
    if not ((sentence[i].lower() == 'a') or
    (sentence[i].lower() == 'e') or
    (sentence[i].lower() == 'o') or
    (sentence[i].lower() == 'u') or
     (sentence[i].lower() == 'i')):
        new += sentence[i]
print(new)