with open("file1.txt") as file1:
    file_content1 = file1.read().split()

with open("file2.txt") as file2:
    file_content2 = file2.read().split()

# Write your code above 👆
result = [int(item) for item in file_content1 if item in file_content2]
print(result)
