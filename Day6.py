with open('data/input-6.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines][0]
for i in range(0, len(lines)):
    if len(set(lines[i:i+4])) == 4:
        print(lines[i:i+4])
        print(i+4)
        break

#Part two

for j in range(0, len(lines)):
    if len(set(lines[j:j+14])) == 14:
        #print(lines[j:j+14])
        #print(j+14)
        break


if __name__ == "__main__":
    print(lines)
    print('_______Part Two_______')
    print(lines[j:j+14])
    print(j+14)