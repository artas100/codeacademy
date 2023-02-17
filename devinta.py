# squares = [number * number for number in range(10)]
# print(squares)
# name = [Jonas, Petras, Antanas, Mykolas, Auris]
# print([name for name in names if name.startswith("A") or "e" in name])

# numbers = [n for n in range(0, 1000) if '6' in str(n)]
# print(numbers)


names = {
    "gfgff": 10,
    "fgfg": 20,
    "fgfg": 30,
    "gfgf": 40,
    "fgfg": 50
}

my_dict = {name.upper(): int(str(number)[::1])
           for (name, number) in names.itiems()}
print(my_dict)
