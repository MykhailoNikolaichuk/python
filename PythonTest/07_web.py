from urllib.request import urlopen

# Write a function that
# 1. reads the content at the links below
# 2. saves whichever text file contains the word "jabberwocky"
def find_jabberwocky(address):
    f = urlopen(address)
    myfile = f.read()
    if 'jabberwocky' in str(myfile.lower()):
        print(f"I'm not sure what you mean under save, but 'jabberwocky' was found here - {address}\n Anyway I'll write a file jabber.txt (with some unreadable stuff lol)")
        with open('jabber.txt', 'w') as f:
            f.write(str(myfile))
    pass

text_1 = "https://www.gutenberg.org/files/11/11-0.txt"
text_2 = "https://www.gutenberg.org/files/12/12-0.txt"

find_jabberwocky(text_1)
find_jabberwocky(text_2)