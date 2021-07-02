numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
squared_numbers = [x * x for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]

#Write your code 👆 above:

print(squared_numbers)
print(even_numbers)

file1_data = []
with open("file1.txt", mode="r") as f:
    while True:
        t = f.readline()
        t.strip()

        if len(t) == 0:
            break

        file1_data.append(int(t))

result = []
with open("file2.txt", mode="r") as f:
    while True:
        t = f.readline()
        t.strip()

        if len(t) == 0:
            break

        result.append(int(t))

result = [x for x in result if x in file1_data]

new_result = []
for x in result:
    if x in file1_data:
        new_result.append(x)

print(result)

with open("file1.txt") as file1:
    file1_data = file1.readlines()
    file1_data = [value.strip() for value in file1_data]

with open("file2.txt") as file2:
    file2_data = file2.readlines()
    file2_data = [value.strip() for value in file2_data]

results = [int(value) for value in file1_data if value in file2_data]
print(result)
