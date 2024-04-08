with open('Advent of Code 2023 Day 2 - Input.txt', 'r') as my_file:
    lines = my_file.read().strip().split('\n')

lines_transformed = []

for game in lines:
    game = game.split(':')
    for sets in game:
        game = sets.strip(' ').split(';')
    lines_transformed.append(game)        

game_number = 1
addition = 0
final_sum = 0

for game in lines_transformed:
    for a_set in game:
        if '13 red' in a_set or '14 red' in a_set or '14 green' in a_set:
            addition = 0
            break
        if '15' in a_set or '16' in a_set or '17' in a_set or '18' in a_set or '19' in a_set or '20' in a_set:
            addition = 0
            break
        else:
            addition = game_number
    final_sum += addition
    game_number +=1

print('Answer for Advent of Code 2023 Day 2, Part 1:', final_sum)

#----------------------------------------------------------------------------------------#
num_blue = []
min_num_blue = 0
list_blue = []

num_green = []
min_num_green = 0
list_green = []

num_red = []
min_num_red = 0
list_red = []

final_sum2 = 0


for game in lines_transformed:
    num_blue = []
    min_num_blue = 0

    for a_set in game:
        if 'blue' in a_set:
            a_set = a_set.split(' blue')
            num_blue.append(int(a_set[0][-2:]))

    min_num_blue = max(num_blue)    
    list_blue.append(min_num_blue)
    
for game in lines_transformed:
    num_green = []
    min_num_green = 0

    for a_set in game:
        if 'green' in a_set:
            a_set = a_set.split(' green')
            num_green.append(int(a_set[0][-2:]))
    min_num_green = max(num_green)
    list_green.append(min_num_green)

for game in lines_transformed:
    num_red = []
    min_num_red = 0

    for a_set in game:
        if 'red' in a_set:
            a_set = a_set.split(' red')
            num_red.append(int(a_set[0][-2:]))
    min_num_red = max(num_red)
    list_red.append(min_num_red)

for i in range(0, 100):
    final_sum2 += list_blue[i] * list_green[i] * list_red[i]

print('Answer for Advent of Code 2023 Day 2, Part 2:', final_sum2)