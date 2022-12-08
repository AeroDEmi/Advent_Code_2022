import numpy as np
import bottleneck as bn
with open('data/input.txt') as f:
    lines = f.readlines()
    lines = [number.replace('\n','') for number in lines]
    lines = [int(number) if not number == '' else 'break' for number in lines]
    all_array=np.array([])
    i=0
    for line in lines:
        if line == 'break':
            all_array = np.append(all_array, i)
            i = 0
        else:
            i += line



if __name__ == "__main__":
    print(bn.partition(all_array, all_array.size-3)[-3:], all_array[np.argmax(all_array)])
    print(np.sum(bn.partition(all_array, all_array.size-3)[-3:]))
