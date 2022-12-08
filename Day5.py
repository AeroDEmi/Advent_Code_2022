with open('data/input-5.txt') as f:
    lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
boxes = [line for line in lines[:8]]
rules = [line for line in lines[10:]]

array_1 = []
array_2 = []
array_3 = []
array_4 = []
array_5 = []
array_6 = []
array_7 = []
array_8 = []
array_9 = []
for i in boxes[::-1]:
    array_1.append(i[1])
    array_2.append(i[5])
    array_3.append(i[9])
    array_4.append(i[13])
    array_5.append(i[17])
    array_6.append(i[21])
    array_7.append(i[25])
    array_8.append(i[29])
    array_9.append(i[33])

array_1 = [i for i in array_1 if i != ' ']
array_2 = [i for i in array_2 if i != ' ']
array_3 = [i for i in array_3 if i != ' ']
array_4 = [i for i in array_4 if i != ' ']
array_5 = [i for i in array_5 if i != ' ']
array_6 = [i for i in array_6 if i != ' ']
array_7 = [i for i in array_7 if i != ' ']
array_8 = [i for i in array_8 if i != ' ']
array_9 = [i for i in array_9 if i != ' ']

dicts = {
    'array_1': array_1,
    'array_2': array_2,
    'array_3': array_3,
    'array_4': array_4,
    'array_5': array_5,
    'array_6': array_6,
    'array_7': array_7,
    'array_8': array_8,
    'array_9': array_9,
}

for rule in rules[:]:
    number, stack_from, stack_to = [int(s) for s in rule.split() if s.isdigit()]
    move = dicts['array_{}'.format(stack_from)][-number:][::-1] # change this to [::] for part two
    dicts['array_{}'.format(stack_from)] = dicts['array_{}'.format(stack_from)][:-number]
    dicts['array_{}'.format(stack_to)].append(move)
    dicts['array_{}'.format(stack_to)] = [i for sub in dicts['array_{}'.format(stack_to)] for i in sub]

answer = ''
for i in dicts.values():
    answer += i[-1]

if __name__ == "__main__":
    print(answer)
