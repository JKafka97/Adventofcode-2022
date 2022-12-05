import string

file1 = open('.\\3_day\\text.txt', 'r')
Lines = file1.readlines()

my_dict = {}
my_list = []
score = 0
alphabet = string.ascii_lowercase + string.ascii_uppercase

for count, value in enumerate(alphabet):
    my_dict[value] = count + 1

for line in Lines:
    my_list.append(line.replace("\n", ""))
    if len(my_list) < 3:
        continue
    match = set(my_list[0]).intersection(set(my_list[1]), set(my_list[2]))
    score +=  my_dict[match.pop()]
    my_list.clear()

print(score)
    