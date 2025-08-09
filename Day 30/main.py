# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sashdiqw"])
# except FileNotFoundError:
#     file = open("a_file1.txt", "w")
#     file.write("The error exception works!")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise FileNotFoundError
#     # file.close()
#     # print("file was closed.")

# height = float(input("height: "))
# weight = int(input("weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)

#
# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise ValueError("Age can't be negative!")
# except ValueError as ve:
#     print("Oops:", ve)
# else:
#     print("Thanks for telling me your age!")
# finally:
#     print("End of conversation.")


# fruits = ["Apple", "Pear", "Orange"]
#
# # Catch the exception and make sure the code runs without crashing.
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError as message:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
           total_likes += post['Likes']

        except KeyError:
            pass

    return total_likes

print(count_likes(facebook_posts))