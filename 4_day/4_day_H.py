file1 = open('.\\4_day\\text.txt', 'r')
Lines = file1.readlines()

i = 0

for line in Lines:
    elf1, elf2 = line.replace("\n", "").split(",")
    elf1_low, elf1_max = elf1.split("-")
    elf2_low, elf2_max = elf2.split("-")
    elf1_range = list(range(int(elf1_low), int(elf1_max) +1))
    elf2_range = list(range(int(elf2_low), int(elf2_max) +1))
    if any( item in elf1_range for item in  elf2_range) or any( item in elf2_range for item in  elf1_range):
        i += 1
print(i)