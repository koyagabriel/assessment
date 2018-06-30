import random

"""
Pseudocode

Set index to 0.
If Li = T, go to step 4.
Increase i by 1 and go to step 2.
If i < n, the search terminates successfully; return i. Else, the search terminates unsuccessfully.
"""

target = 50
random_list = random.sample(range(1, 100), 10)
i = 0
length = len(random_list)
random_list.append(target)
print(random_list)

for value in random_list:
    if value == target:
        if i < length:
            print(f'The index of the target number is {i}')
        else:
            print('Target value does not exist in the list')
        break

    i += 1
