# create a new list from numbers, where you added 1 to each value
numbers = [1, 2, 3]

new_set = {x + 1 for x in numbers}

print(new_set)

new_list = [x + 1 for x in numbers if x % 2 == 1]

print(new_list)

name = "Angela"

name_nato = list(name) # [l for l in name]

print(name_nato)


# list > range > string > tuple


range_list = [x * 2 for x in range(1, 5)]

print(range_list)


names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
name_list = [name for name in names if len(name) <= 4]
print(name_list)

name_list = [name.upper() for name in names if len(name) > 4]
print(name_list)