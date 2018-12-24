import random

"""
Pseudocode

Set i to 0.
If Li = T, the search terminates successfully; return i.
Increase i by 1.
If i < n, go to step 2. Otherwise, the search terminates unsuccessfully.
"""

target = 50
random_list = random.sample(range(1, 100), 10)
i = 0
length = len(random_list)
print(random_list)

for value in random_list:
    if value == target:
        print(f'The index of the target number is {i}')
        break

    i += 1

    if i < length: continue

    print('Target value does not exist in the list')
