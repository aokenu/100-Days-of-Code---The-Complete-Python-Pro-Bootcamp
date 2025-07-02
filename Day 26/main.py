with open("file1.txt") as file1:
    file1_output = file1.readlines()
    output1 = [num.strip() for num in file1_output]


with open("file2.txt") as file2:
    file2_output = file2.readlines()
    output2 = [num.strip() for num in file2_output]


result = [int(num) for num in output1 and output2]
print(result)