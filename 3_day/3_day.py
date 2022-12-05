import string

file1 = open('.\\3_day\\text.txt', 'r')
Lines = file1.readlines()

my_dict = {}
score = 0
alphabet = string.ascii_lowercase + string.ascii_uppercase

for count, value in enumerate(alphabet):
    my_dict[value] = count + 1

for line in Lines:
    lenght = len(line)//2
    match = set(line[:lenght]).intersection(line[lenght:])
    score +=  my_dict[match.pop()]

print(score)
    