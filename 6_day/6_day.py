file1 = open('.\\6_day\\text.txt', 'r')
line = file1.read().strip()

i =  0
while True:
    diff = line[i:i+4]
    if len(set(diff)) == 4:
        print(diff, i+4)
        break
    i += 1
