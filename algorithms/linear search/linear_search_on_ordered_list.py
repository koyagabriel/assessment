import random

"""
Pseudocode

Set i to 0.
If Li ≥ T, go to step 4.
Increase i by 1 and go to step 2.
If Li = T, the search terminates successfully; return i. Else, the search terminates unsuccessfully.
"""

target = 50
random_list = sort(random.sample(range(1, 100), 10))
i = 0
length = len(random_list)
print(random_list)

for value in random_list:
    if value >= target:
        if value == target:
            print(f'The index of the target number is {i}')
        else:
            print('Target value does not exist in the list')
        break

    i += 1
