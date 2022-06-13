import sys
from PIL import Image , ImageOps


if (len(sys.argv)>3):
    sys.exit("Too many command-line arguments")
elif(len(sys.argv) < 3):
    sys.exit("Too few command-line arguments")
elif not ( (sys.argv[1].endswith(".png") and sys.argv[2].endswith(".png")) or (sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".jpg"))):
    sys.exit("Not same extension")
else:
    try:
        photo = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")
    shirt = Image.open("shirt.png")
    size = shirt.size
    im2 = ImageOps.fit(photo, size)
    im2.paste(shirt,shirt)
    im2.save(sys.argv[2])



