with open('data/input-4.txt') as f:
    lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
b = [i.split(',') for i in lines]
b = [i.split('-') for j in b for i in j]
flat_list = [int(item) for sublist in b for item in sublist]
grouped = list(zip(*[iter(flat_list)]*4))
sum_ = 0
for group in grouped:
    if group[0] >= group[2] and group[1] <= group[3]:
        sum_ += 1
    elif group[0] <= group[2] and group[1] >= group[3]:
        sum_ += 1

#_____________Second Part_________

sum_two = 0
for group in grouped:
    if group[1] >= group[2] and group[1] <= group[3]:
        sum_two += 1
    elif group[3] >= group[0] and group[3] <= group[1]:
        sum_two += 1
    elif group[2] >= group[0] and group[3] <= group[1]:
        sum_two += 1
    elif group[0] >= group[2] and group[1] <= group[3]:
        sum_two += 1

if __name__ == "__main__":
    print(sum_)
    print('_______Part Two_______')
    print(sum_two)