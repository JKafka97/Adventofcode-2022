file1 = open('.\\2_day\\text.txt', 'r')
Lines = file1.readlines()

strategy = { "A": 0, "X": 0, "B": 1, "Y": 1, "C": 2, "Z": 2 }
count = 0

for line in Lines:
    elf, resault = line.replace("\n", "").split(" ")
    elf = strategy[elf] -1 #-1 protože změna logiky
    resault = strategy[resault]  

    count += resault * 3 #lineární průběh => X == prohra, Y == remíza a Z == výhra
    count +=  ((resault + elf) % 3) + 1  #
    
print(count)
