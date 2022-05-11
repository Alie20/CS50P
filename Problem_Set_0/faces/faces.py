def main ():
    sentence = input("Enter your sentence")
    convert(sentence)
def convert(msg):
    msg = msg.replace(":)",'🙂')
    msg = msg.replace(":(",'🙁')
    print(msg)

main()