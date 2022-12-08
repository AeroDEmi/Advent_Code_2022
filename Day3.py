import string


lower_case = list(string.ascii_letters)
value_letter = dict(enumerate(lower_case, start=1))
letter_value = {v: k for k, v in value_letter.items()}

with open('data/input-3.txt') as f:
    lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
lines = [list(set(line[:len(line)//2]) & set(line[len(line)//2:])) for line in lines]
numbers = [letter_value[letter[0]] for letter in lines]

#_____________ Second Part _____________
with open('data/input-3.txt') as f:
    lines_two = f.readlines()
lines_two = [line.replace('\n', '') for line in lines_two]
grouped = list(zip(*[iter(lines_two)]*3))
intersection = [list(set(group[0]) & set(group[1]) & set(group[2])) for group in grouped]
numbers_two = [letter_value[letter[0]] for letter in intersection]




if __name__ == "__main__":
    print(sum(numbers))
    print('_____________ Second Part _____________')
    print(sum(numbers_two))