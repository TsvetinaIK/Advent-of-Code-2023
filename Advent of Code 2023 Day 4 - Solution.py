with open('Advent of Code 2023 Day 4 - Input.txt', 'r') as my_file:
    lines = my_file.read().strip().split('\n')

lines_transformed = []
card = []
num_had = []
points = 0
final_points = 0

for line in lines:
    line = line.strip(' ').split(':')
    for sets in line:
        line = sets.strip(' ').split(' | ')
    lines_transformed.append(line)      

for set in lines_transformed:
    card = set[0].split(' ')
    num_had = set[1].split(' ')
    for num in card:
        if num != '':
            if num in num_had:
                if points != 0:
                    points *= 2
                if points == 0:
                    points = 1

    final_points += points
    points = 0

print('Answer for Advent of Code 2023 Day 4, Part 1:', final_points)

#----------------------------------------------------------------------------------------#

matches = 0
l_matches = []
card_num = 1
l_card_num = []
l_cur_cards = [1]*len(lines_transformed)

for set in lines_transformed:
    card = set[0].split(' ')
    num_had = set[1].split(' ')
    for num in card:
        if num != '':
            if num in num_had:
                matches += 1
    
    l_card_num.append(card_num)
    l_matches.append(matches)
    matches = 0
    card_num += 1

for i in range(196):
    if l_matches[i] != 0:
        for j in range(l_matches[i]):
            l_cur_cards[i+1+j] += l_cur_cards[i]

print('Answer for Advent of Code 2023 Day 4, Part 2:', sum(l_cur_cards))