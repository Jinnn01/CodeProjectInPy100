try:
    file = open("a_file.txt", "r")
    dict = {"key": "value"}
    data = dict["key"]

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("This is a test")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File has colsed")
