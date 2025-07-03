# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

#TODO 1. Create a dictionary in this format:
#reading the data file
data = pd.read_csv("nato_phonetic_alphabet.csv")
# print(data)

nato_code = {}

nato_data = {row.letter: row.code for index, row in data.iterrows()}
print(nato_data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Type a name: ").upper()
for letter in user_word:





