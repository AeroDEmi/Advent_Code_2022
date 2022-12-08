from anytree import Node, PreOrderIter


def iterate_children(parent_node):
    sum_i = 0
    for node in parent_node.children:
        if hasattr(node, 'size'):
            sum_i += node.size
        else:
            sum_i += iterate_children(node)
    parent_node.size = sum_i
    return sum_i


def iterate_dir_nodes(parent_node, th=100000):
    sum_all = 0
    for node in parent_node.descendants:
        if 'dir' in node.name and hasattr(node, 'size'):
            if node.size <= th:
                sum_all += node.size
    return sum_all


def iterate_size_dirs(parent_node):
    dict_ = {}
    for node in PreOrderIter(parent_node):
        if 'dir ' in node.name:
            dict_[node.name] = node.size
    return dict_


with open('data/input-7.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

my_dict = {}
i = 0
names = []
for line in lines:
    if line.startswith('$ cd ') and '..' not in line:
        name = line.replace('$ cd', 'dir')
        if i == 0:
            my_dict[name] = Node(name, parent=None)
            names.append(name)
            parent = names[-1]
            i += 1
            continue
        else:
            my_dict[name] = Node(name, parent=my_dict[parent])
            names.append(name)
            parent = names[-1]
            continue
    elif line.startswith('$ cd ..'):
        names.pop(-1)
        parent = names[-1]
        continue

    if line == '$ ls':
        continue
    if any(char.isdigit() for char in line) and 'dir' not in line:
        my_dict[line] = Node(line.split(' ')[1], parent=my_dict[parent], size=int(line.split(' ')[0]))

iterate_children(my_dict['dir /'])

result = iterate_dir_nodes(my_dict['dir /'])

# for pre, fill, node in RenderTree(my_dict['dir /']):
#     print("{}{} {:,}".format(pre, node.name, node.size))

#___________Part Two_______________

sizes_dict = iterate_size_dirs(my_dict['dir /'])
available = 70000000 - my_dict['dir /'].size
minimum = 30000000 - available
print('Available: {:,}, minimum: {:,}'.format(available, minimum))
sizes_dict = dict(sorted(sizes_dict.items(), key=lambda item: item[i]))
minimum_dirs = {k: v for (k,v) in sizes_dict.items() if v > minimum}

if __name__ == "__main__":
    print('_______Part One_______')
    print('{}'.format(result))
    print('_______Part Two_______')
    print(list(minimum_dirs.items())[0])