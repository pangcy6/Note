with open('txt/pi.txt') as file:
    lines = file.readlines()

print(lines)    # Confirm list

for line in lines:
    print(line.rstrip())
