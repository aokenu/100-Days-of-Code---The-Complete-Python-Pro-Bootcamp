#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Read the starting_letter file
with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    print(letter)

# Reading the name of the invitees and strip off the unwanted characters
with open("Input/Names/invited_names.txt") as names:
    invitees = names.readlines() # Read each line of the file and convert the items into a list
    stripped_names = [name.strip() for name in invitees]
    print(stripped_names)

# Save a copy for each of the invitees on the Output folder
for n in stripped_names:
    final_letter = letter.replace("[name]", n)
    print(final_letter)
    with open(f"Output/ReadyToSend/{n}.doc", "w") as f_file:
        f_file.write(final_letter) # write to the Output folder


# Saving the final letter into folder


