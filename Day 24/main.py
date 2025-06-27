# Reading a file
with open("my_file.txt") as file:
    content = file.read()

    print(content)


# Writing into a file
with open("my_file.txt", mode="a") as file:
    file.write("\nMir geht's gut")


# Creating and opening a file
with open("new_file.txt", mode="w") as file:
    file.write("\nMir geht's gut")

