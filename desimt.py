# import random


# def get_random_number():
#     print(random.randint(0, 10))


# print(get_random_number())

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))


# ch = input("Enter operation +,-,*,/: ")

# result = 0
# if ch == '+':
#     result = num1 + num2
# elif ch == '-':
#     result = num1 - num2
# elif ch == '*':
#     result = num1 * num2
# elif ch == '/':
#     result = num1 / num2
# else:
#     print("Input character is not recognized!")

# print(num1, ch, num2, "=", result)


def unique_characters(string_in):
    if (len(set(string_in)) == len(string_in)):
        return True
    else:
        return False


print(unique_characters("tadas"))
