def pass_something():
    pass


def do_something():
    print("did something")


def return_something():
    return True


def return_boolean() -> str:
    return "123"


print(type(return_boolean()))


def function_with_parameter(a, b, c):
    print("function_with_parameter")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")


# todo: do something with parameter
# function_with_parameter(1, 2) # error
function_with_parameter(1, 2, 3)


def function_with_default(a, b, c=1):
    print("function_with_default")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")


function_with_default(1, 2)

# a: position argument
# b, c: named argument
function_with_default(1, c=2, b=3)


# multiple arguments
# *args non-keyword arguments
# tuple
def takes_in_multiple_values(*nums):
    print("takes_in_multiple_values")
    for num in nums:
        print(num)


takes_in_multiple_values(1, 2, 3, 4, 5)

# tuple


# **kwargs keyword arguments
def takes_in_keyword_values(**data):
    print("takes_in_keyword_values")
    print(type(data))
    for k, v in data.items():
        print(f"{k}, {v}")


takes_in_keyword_values(a=1, b=2, c=3)
data = {"a": 1, "b": 2, "c": 3}

class Meals:
    def __init__(self):
        self.lunch = "cookie"
        self.breakfast = "noodle"
        self.dinner = "burger"



def give_me_all_meals() -> Meals:
    return Meals()
