
import pandas
data = pandas.read_csv(
    "D:/Coding/python/projects/NATO-alphabet-start/Nato_phonetic_alphabet.csv")
# print(data.to_dict)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {
    row.letter: row.code for (index, row) in data.iterrows()
}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("\nEnter the word").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
