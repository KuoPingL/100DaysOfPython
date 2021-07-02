import random

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(0, 100) for student in names}

print(student_scores)

passed_students = {key: value for (key, value) in student_scores.items() if value >= 60}

print(passed_students)

# Exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# letters = sentence.split(" ")
letters = sentence.split()
print(letters)
result = {letter: len(letter) for letter in letters}
print(result)

# Exercise 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: ((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}

print(weather_f)



