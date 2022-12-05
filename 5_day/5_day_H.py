file1 = open('.\\5_day\\text.txt', 'r')
Lines = file1.readlines()

key = [["W", "D", "G", "B", "H", "R", "V"], 
         ["J", "N", "G", "C", "R", "F"],
         ["L", "S", "F", "H", "D", "N", "J"],
         ["J", "D", "S", "V"],
         ["S", "H", "D", "R", "Q", "W", "N", "V"],
         ["P", "G", "H", "C", "M"],
         ["F", "J", "B", "G", "L", "Z", "H", "C"],
         ["S", "J", "R"],
         ["L", "G", "S", "R", "B", "N", "V", "M"]]

for line in Lines:
    info = line.replace("\n", "").split(" ")
    number_of_elements = int(info[1])
    start_row = int(info[3])
    final_row = int(info[-1])
    removed_symbols = key[start_row -1][len(key[start_row -1]) - number_of_elements:]
    key[start_row -1] = key[start_row -1][:-number_of_elements]
    key[final_row -1] += removed_symbols
        
print("".join([i[-1] for i in key]))