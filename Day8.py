import numpy as np

with open('data/input-8.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

# lines = ['30373',
#          '25512',
#          '65332',
#          '33549',
#          '35390']

matrix = np.array([[int(d) for d in line] for line in lines])


def check_visible(matrix, i, j):
    middle = matrix[i, j]
    top = matrix[i - 1, j]
    right = matrix[i, j + 1]
    down = matrix[i + 1, j]
    left = matrix[i, j - 1]

    if middle > top:
        upper = matrix[:i - 1, j]
        if all(middle > upper):
            return True

    if middle > right:
        right_n = matrix[i, j + 1:]
        if all(middle > right_n):
            return True

    if middle > down:
        lower = matrix[i + 1:, j]
        if all(middle > lower):
            return True

    if middle > left:
        left_n = matrix[i, :j - 1]
        if all(middle > left_n):
            return True

    return False


sum_ = 0
for i in range(1, matrix.shape[0] - 1):
    for j in range(1, matrix.shape[1] - 1):
        if check_visible(matrix, i, j):
            sum_ += 1

matrix = np.array([[int(d) for d in line] for line in lines])


# ________ Part Two __________


def scenic_score(matrix, i, j):
    middle = matrix[i, j]
    top = matrix[:i, j]
    right = matrix[i, j + 1:]
    down = matrix[i + 1:, j]
    left = matrix[i, :j]

    #     print(middle, top, right, down, left)

    top_n = 0
    for number in top[::-1]:
        if middle > number:
            top_n += 1
        else:
            top_n += 1
            break

    left_n = 0
    for number in left[::-1]:
        if middle > number:
            left_n += 1
        else:
            left_n += 1
            break

    right_n = 0
    for number in right[::]:
        if middle > number:
            right_n += 1
        else:
            right_n += 1
            break

    down_n = 0
    for number in down[::]:
        if middle > number:
            down_n += 1
        else:
            down_n += 1
            break

    return top_n * left_n * right_n * down_n, top_n, left_n, right_n, down_n


max_score = 0
for i in range(1, matrix.shape[0]-1):
    for j in range(1, matrix.shape[1]-1):
        score = scenic_score(matrix, i, j)
        if score[0] > max_score:
            max_score = score[0]


if __name__ == "__main__":
    print('_______Part One_______')
    print(sum_ + (matrix.shape[0] * 2) + (matrix.shape[1] - 2) * 2)
    print('_______Part Two_______')
    print(max_score)