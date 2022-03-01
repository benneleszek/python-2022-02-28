from time import process_time_ns


numbers = [1,5,1,13,7,9,11,21,33,44,55,11,22,30,11]
evens = [2,4,6,8]

print(numbers)
print(evens)

names = ['Jack Doe', "John Doe", "Jane Doe"]

employee = ["Jack Doe", 30]

print(names)
print(employee)

for number in numbers:
    print(number)

print(names[2])

names[2] = 'Jane Smith'
print(names[2])

names.append("John Smith")
print(names)

dogs = []
print(dogs)
dogs.append("Morzsi")
print(dogs)

print(names[1:3])
print(numbers[3:8:2])
print(numbers[6:])
print(numbers[8:3:-1])
print(numbers[8:3:-2])
print(numbers[::-1])

count = 0
for number in numbers:
    if number % 2 == 0:
        count +=1

print(count)

