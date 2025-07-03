# with open("file1.txt") as file1:
#     file1_output = file1.readlines()
#     output1 = [num.strip() for num in file1_output]
#
#
# with open("file2.txt") as file2:
#     file2_output = file2.readlines()
#     output2 = [num.strip() for num in file2_output]
#
#
# result = [int(num) for num in output1 and output2]
# print(result)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
# print(words)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
#
# # Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

# importing pandas library
import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Looping through a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.score)