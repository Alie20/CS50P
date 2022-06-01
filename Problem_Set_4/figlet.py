import sys
import pyfiglet

figlet = pyfiglet.Figlet()
fonts = figlet.getFonts()
if (len(sys.argv) == 3):
    if (sys.argv[1] =="-f" or sys.argv[1] == "--font"):
        try:
            if(sys.argv[2] in fonts):
                name = input("Input: ")
                print(pyfiglet.figlet_format(name,font = sys.argv[2]))
            else:
                sys.exit("Invalid usage")
        except:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
elif (len(sys.argv) == 2):
    sys.exit("Invalid usage")
else:
    name = input("Input: ")
    print(pyfiglet.figlet_format(name,font = "slant"))