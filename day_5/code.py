import itertools

with open('input.txt', 'r') as f:
  content = f.read().splitlines()

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

max_id = 0
id_list = []

for seat in content:
    rows = list(range(0,128))
    columns = list(range(0, 8))
    for character in seat:
        if character == 'F':
            rows = split_list(rows)[0]
        elif character == 'B':
            rows = split_list(rows)[1]
        if character == 'L':
            columns = split_list(columns)[0]
        elif character == 'R':
            columns = split_list(columns)[1]
    id = rows[0] * 8 + columns[0]
    id_list.append(id)
    if id > max_id:
        max_id = id

for x in itertools.combinations(id_list, 2):
    diff = abs(x[0] - x[1])
    mid = (x[0]+x[1])/2
    if diff == 2 and mid not in id_list:
        print(mid)
