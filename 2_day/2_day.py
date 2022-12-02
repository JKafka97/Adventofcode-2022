file1 = open('.\\2_day\\text.txt', 'r')
Lines = file1.readlines()

strategy = { "A": 0, "X": 0, "B": 1, "Y": 1, "C": 2, "Z": 2 }
count = 0

for line in Lines:
    elf, me = line.replace("\n", "").split(" ")
    elf = strategy[elf]
    me = strategy[me]
    
    if elf == me:
        count += 3
    elif (me - elf) % 3 == 1:
        count += 6   
    
    count += me + 1
        
print(count)