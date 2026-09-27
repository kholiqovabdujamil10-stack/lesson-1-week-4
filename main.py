# 1
# def welcome(func):
#     def inner(name):
#         print("Welcome!")
#         func(name)
#     return inner
# @welcome
# def show_name(name):
#     print(name)
# name = input()
# show_name(name)

# 2
# def goodbye(func):
#     def inner(city):
#         func(city)
#         print("Goodbye!")
#     return inner
# @goodbye
# def show_city(city):
#     print(city)
# city = input()
# show_city(city)


# 3
# def repeat_three_times(func):
#     def inner():
#         for i in range(3):
#             func()
#     return inner
# @repeat_three_times
# def hello():
#     print("Hello")
# hello()


# 4
# def show_function_name(func):
#     def inner(a, b):
#         print("Function:", func.__name__)
#         return func(a, b)
#     return inner
# @show_function_name
# def add(a, b):
#     return a + b
# a, b = map(int, input().split())
# print(add(a, b))


# 5
# def uppercase_result(func):
#     def inner(name):
#         result = func(name)
#         return result.upper()
#     return inner
# @uppercase_result
# def get_name(name):
#     return name
# name = input()
# print(get_name(name))


# 6
# def positive_number(func):
#     def wrapper(number):
#         if number > 0:
#             print(func(number))
#         else:
#             print("The number must be positive")
#     return wrapper
# @positive_number
# def square(number):
#     return number ** 2
# square(int(input()))


# 7
# a = int(input())
# b = int(input())
# add = lambda a, b: a + b
# print(add(a, b))


# 8
# a = int(input())
# square = lambda a: a ** 2
# print(square(a))


# 9
# numbers = [1, 2, 3, 4, 5, 6]
# result = list(filter(lambda x: x % 2 == 0, numbers))
# print(result)


# 10
# people = [('Ali', 22), ('Sara', 19), ('Bob', 25)]
# result = sorted(people, key=lambda a: a[1])
# print(result)