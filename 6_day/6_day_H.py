file1 = open('.\\6_day\\text.txt', 'r')
line = file1.read().strip()

i =  0
while True:
    diff = line[i : i+14]
    if len(set(diff)) == 14:
        print(diff, i+14)
        break
    i += 1
