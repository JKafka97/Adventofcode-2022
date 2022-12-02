file1 = open('.\\2_day\\text.txt', 'r')
Lines = file1.readlines()

strategy = { "A": 1, "X": 0, "B": 2, "Y": 1, "C": 3, "Z": 2 }
count = 0
points = [1, 2, 3]

for line in Lines:
    elf, me = line.replace("\n", "").split(" ")
    elf = strategy[elf] -1
    me = strategy[me]
    
    if elf == me:
        count += 3      
    elif (me - elf) % 3 == 1:
        count += 6   
    
    count += me + 1
            
print(count)