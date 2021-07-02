numbers = [1,
           2, 2,
           3, 3, 3,
           4, 4, 4, 4,
           5, 5, 5, 5, 5]

# List Comprehension
numbers_even = [x for x in numbers if x % 2 == 0]
numbers_odd_double = [x * 2 for x in numbers if x % 2 == 1]

print(numbers_even)
print(numbers_odd_double)

# List to Set
numbers_unique = {x for x in numbers}  # set

print(numbers_unique)

# Generator Object https://ithelp.ithome.com.tw/articles/10230846?sc=pt
# 生成器
numbers_even_tuple = (x for x in {y for y in numbers})
print(numbers_even_tuple)

# print(next(numbers_even_tuple))
# print(next(numbers_even_tuple))
# print(next(numbers_even_tuple))
# print(next(numbers_even_tuple))
# print(next(numbers_even_tuple))
# print(next(numbers_even_tuple))


# for v in numbers_even_tuple:
#     print("Nothing")
#     print(v)
#
import sys
print(sys.getsizeof(numbers_even_tuple))
# print(sys.getsizeof(32)) # int 28 byte

numbers_even_tuple = list(numbers_even_tuple)
print(sys.getsizeof(numbers_even_tuple))
print(numbers_even_tuple)


# 節省空間
def allEven():
    n = 2  # 初始值n=2
    while True:
        yield n
        print("yielded")
        n = n+2


# even = allEven()
# print(next(even))
# print(next(even))
# print(next(even))
# print(next(even))

# 這有點像 Linked List 只能知道下一個，無法知道上一個值
# linked List
# https://oldmo860617.medium.com/ts-%E5%AD%B8%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E8%88%87%E6%BC%94%E7%AE%97%E6%B3%95-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E7%AF%87-%E9%8F%88%E7%B5%90%E4%B8%B2%E5%88%97-linked-list-349a3f5ffecf


# Dictionary Comprehension
import random
numbers_dict = {number: number for number in numbers}
print(numbers_dict)

numbers_dict = {random.randint(0, 100): value for value in numbers}
print(numbers_dict)


