file = 'txt/notHere.txt'

try:
    with open(file) as obj:
        contents = obj.read()
    print(contents.rstrip())
except FileNotFoundError:
    msg = f"Sorry, the file {file} does not exist."
    print(msg)
