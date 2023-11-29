import numpy as np
import os
from datasets.h2outils import *
import random

single_object = False
wanted_object = ['lotion']

root = '../h2o/action_labels'
input_files = ['/action_train.txt', '/action_val.txt']
first_line = []
all_wanted_data = []
train_dir = '../h2o/action_labels/action_my_train.txt'
#val_dir = '../h2o/action_labels/action_my_val.txt'
test_dir = '../h2o/action_labels/action_my_test.txt'
for f in input_files:
    pth = root + f
    print(pth)
    with open(pth, 'r') as file:
        all = file.readlines()
        first_line = all[0]
        file_data = all[1:]
        #print(file_data)
        for line in file_data:
            strip_line = line.strip('\n').split(' ')
            action_idx = int(strip_line[2])
            #print(action_idx)
            if action_idx <= 19:
                all_wanted_data.append(line)

random.shuffle(all_wanted_data)
total_lines = len(all_wanted_data)
train_size = int(0.7 * total_lines)
train_data = all_wanted_data[:train_size]
test_data = all_wanted_data[train_size:]

for i, line in enumerate(train_data, start=1):
    parts = line.split()
    parts[0] = str(i)
    new_line = ' '.join(parts)
    train_data[i - 1] = new_line + '\n'
for i, line in enumerate(test_data, start=1):
    parts = line.split()
    parts[0] = str(i)
    new_line = ' '.join(parts)
    test_data[i - 1] = new_line + '\n'

print(f"ALL Data size: {len(all_wanted_data)}")
print(f"Train set size: {len(train_data)}")
print(f"Test set size: {len(test_data)}")

print(train_dir)
with open(train_dir, 'w') as file:
    file.write(first_line)
    file.writelines(train_data)
with open(test_dir, 'w') as file:
    file.write(first_line)
    file.writelines(test_data)