# def sum(a, b):
#     c = a + b
#     print(c)


# a = 5
# b = 3

# sum(a, b)

# def my_fn(a, b):
#     a = a + 1
#     c = a + b
#     return c


# res = my_fn(20, 3)
# print(res)


number_list = [1, 2, 3, 4, 5, 6]


def calculate_odd_even():
    odd_number = 0
    even_number = 0
    for i in number_list:
        if i % 2 == 0:
            even_number = even_number + i
        else:
            odd_number = odd_number + i

    return (odd_number - even_number)


my_tuple = calculate_odd_even()
print(my_tuple)
