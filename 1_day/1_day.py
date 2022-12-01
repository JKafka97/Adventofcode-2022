file1 = open('.\\1_day\\text.txt', 'r')
Lines = file1.readlines()
  
count = 0
my_list = []

for line in Lines:
    try:
        count+= int(line.replace("\n", ""))
    except: 
        my_list.append(count)
        count = 0
        
my_list.sort()
print(my_list[-1])

# print(my_list[-1] + my_list[-2] + my_list[-3])
