def print_employeedata(name: str, age: int, repeat: int = 5, print_line_numbers: bool = False):
    for i in range(0, repeat):
        name_age = ""
        if print_line_numbers:
            name_age = name_age + f"{i + 1} "
        name_age = name_age + f"{name} {age}"
        print(name_age)


print('begin')
print_employeedata("John Doe", 30, True)
print('mid')
print_employeedata("Jack Doe", 28)

print_employeedata(age=60, name="John Smith", print_line_numbers=True)

# Warning
# print_employeedata(100, "Jack Doe")

print('end')
