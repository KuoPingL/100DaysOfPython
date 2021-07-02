# FileNotFoundError
# with open("a_file.txt") as f:
#     f.read()

print("\n--------- FILE NOT FOUND ERROR ----------\n")

try:
    file = open("a_file.txt")
except:
    print("File Not Found")

# KeyError
a_dic = {"key": "value"}
# value = a_dic["fake"]

print("\n--------- KEY ERROR ----------\n")

try:
    value = a_dic["fake"]
except FileNotFoundError:
    print("File Not Found")
except KeyError:
    print("Incorrect Key")

# TypeError
text = "abc"
# print(text + 15)

print("\n--------- TYPE ERROR ----------\n")

try:
    print(text + 15)
except FileNotFoundError:
    print("File Not Found")
except KeyError:
    print("Incorrect Key")
except TypeError as error_message:
    print(f"Incorrect Type: {error_message}")

print("\n--------- MIXED ----------\n")

try:
    file = open("test.txt")
except FileNotFoundError:
    print("File Not Found: Create File")
    file = open("test.txt", mode="w")
    file.write("File Created")
except KeyError:
    print("Incorrect Key")
except TypeError as error_message:
    print(f"Incorrect Type: {error_message}")
else:
    content = file.read()
    print(content)
finally:
    # https://stackoverflow.com/questions/1592565/determine-if-variable-is-defined-in-python
    try:
        file
    except NameError:
        print("file not defined")
    else:
        file.close()
        print("All Done")

# four keywords
# try - something that might cause an exception
# except - do this if there was an exception
# else - do this if there were no exceptions
# finally - do this no matter what happens
