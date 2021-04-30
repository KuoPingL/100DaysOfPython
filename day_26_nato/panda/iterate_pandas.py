import pandas as pd
import random

CSV_FILE = "student_scores.csv"

student_names = ["Angela", "James", "Lily"]
input_data = pd.DataFrame({"students": student_names,
                           "scores": [random.randint(0, 100) for _ in range(len(student_names))]})
input_data.to_csv(CSV_FILE)

output_data = pd.read_csv(CSV_FILE)

# Loop through DataFrame
for (key, value) in output_data.items():
    print(value)

for (index, row) in output_data.iterrows():
    print(index)
    print(row.students)

