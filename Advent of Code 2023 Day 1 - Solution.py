with open('Advent of Code 2023 Day 1 - Input.txt', 'r') as my_file:
    lines = my_file.read().split('\n')

my_string = "abcdefghijklmnopqrstuvwxyz"

temp_list = []
temp_sum = 0
final_sum = 0
temp_output = []

for line in lines:
    for char in line:
        if char not in my_string:
            temp_list.append(char)
    temp_output = temp_list[0] + temp_list[-1]
    final_sum += int(temp_output)
    temp_list = []
    temp_sum = 0

print('Answer for Advent of Code 2023 Day 1:',  final_sum)

#----------------------------------------------------------------------------------------#

lines_transformed = []

temp_list2 = []
temp_sum2 = 0
final_sum2 = 0
temp_output2 = []

for line in lines:
    line_transformed = line.replace('one', 'o1ne').replace('two', 't2wo').replace('three', 'th3ree').replace('four', 'fo4ur').replace('five', 'fi5ve').replace('six', 'si6x').replace('seven', 'se7ven').replace('eight', 'ei8ght').replace('nine', 'ni9ne')
    lines_transformed.append(line_transformed)

for line in lines_transformed:
    for char in line:
        if char not in my_string:
            temp_list2.append(char)
    temp_output2 = temp_list2[0] + temp_list2[-1]
    final_sum2 += int(temp_output2)
    temp_list2 = []
    temp_sum2 = 0

print('Answer for Advent of Code 2023 Day 1, Part 2:',  final_sum2)
