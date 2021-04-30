import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
# nato_dict = {item.letter: item.code for item in nato.itertuples()}
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter a word to be encoded with NATO : ").upper()
user_input = [letter for letter in user_input]

result = [nato_dict[letter] for letter in user_input if letter != " "]
print(result)

