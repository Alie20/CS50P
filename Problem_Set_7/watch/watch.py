import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"^<iframe(.)+</iframe>$",s,re.IGNORECASE):
        if matches := re.search("https?://(?:www\.)?youtube\.com/embed/(.+)",s,re.IGNORECASE):
            title = matches.group(1)
            link = title.split("\"")
            return (f"https://youtu.be/{link[0]}")

if __name__ == "__main__":
    main()
