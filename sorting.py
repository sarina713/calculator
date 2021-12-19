
# get user to input a list of numbers
# bubble sort



# get number from the user
count = int(input("How many numbers would you like to input"))

number_list = []

for i in range(0, count):
    temp_num = input("Please enter a number: ")

    try:
        number_list.append(int(temp_num))

    except Exception as ex:
        print("Please only eneter a whole number")
        count += 1

ordered_list = number_list
continue_loop = True

while(continue_loop):
    item_moved = 0 

    for x in range(0, len(ordered_list) - 1):
        if (ordered_list[x] > ordered_list[x+1]):
            temp_num = ordered_list[x]

            ordered_list[x] = ordered_list[x+1]
            ordered_list[x+1] = temp_num

            item_moved += 1
        
    if (item_moved == 0):
        continue_loop = False

print(ordered_list)

for z in range (0, len(ordered_list)):
    print(ordered_list[z])