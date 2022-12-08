with open('data/input-2.txt') as f:
    lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
play_dict = {
    'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
    'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'
            }

point_dict = {
    'Rock': 1, 'Paper': 2, 'Scissors': 3,
    'Rock Rock': 3, 'Rock Paper': 6, 'Rock Scissors': 0,
    'Paper Rock': 0, 'Paper Paper': 3, 'Paper Scissors': 6,
    'Scissors Rock': 6, 'Scissors Paper': 0, 'Scissors Scissors': 3,
              }

translated = [' '.join([play_dict[play] for play in line.split(' ')]) for line in lines]
play_points = [point_dict[line.split(' ')[1]] for line in translated]
result_points = [point_dict[line] for line in translated]

#_____________ Second Part _____________

with open('data/input-2.txt') as f:
    lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
opponent, me = map(list, zip(*(line.split(" ") for line in lines)))
names_dict = {
    'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
    'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'
            }

play_dict = {
    'Rock Win': 'Paper', 'Rock Draw': 'Rock', 'Rock Lose': 'Scissors',
    'Paper Win': 'Scissors', 'Paper Draw': 'Paper', 'Paper Lose': 'Rock',
    'Scissors Win': 'Rock', 'Scissors Draw': 'Scissors', 'Scissors Lose': 'Paper',
              }

points_dict = {
    'Rock': 1, 'Paper': 2, 'Scissors': 3,
    'Win': 6, 'Draw': 3, 'Lose': 0,
}

translated = [' '.join([names_dict[play] for play in line.split(' ')]) for line in lines]
play_points_1 = [points_dict[play_dict[line]] for line in translated]
result_points_1 = [points_dict[names_dict[line]] for line in me]

if __name__ == "__main__":
    #________________Part One_______________
    print('Play points:', sum(play_points))
    print('Result points:', sum(result_points))
    print('Sum of points:', sum(play_points)+sum(result_points))
    #________________Part Two_______________
    print('________________Part Two_______________')
    print('Play points:', sum(play_points_1))
    print('Result points:', sum(result_points_1))
    print('Sum of points:', sum(play_points_1) + sum(result_points_1))