height = float(input("HEIGHT = "))
weight = int(input("WEIGHT = "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
else:
    bmi = weight / height ** 2
    print(f"BMI = {bmi}")

