numbers = [10, 20, 30, 40, 50]
print("Original:", numbers)

print("First:", numbers[0])
print("Last:", numbers[-1])
print("Slice [1:4]:", numbers[1:4])
print("Reverse slice:", numbers[::-1])

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.extend([70, 80])
print("After extend:", numbers)

numbers[0] = 5
print("After update:", numbers)

numbers.remove(25)
print("After remove:", numbers)

removed = numbers.pop()
print("Popped:", removed)
print("After pop:", numbers)

del numbers[1]
print("After del:", numbers)

print("Index of 40:", numbers.index(40))
print("Count of 50:", numbers.count(50))

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

copy_list = numbers.copy()
print("Copied:", copy_list)

print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

squares = [x * x for x in range(1, 6)]
print("Comprehension:", squares)

numbers.clear()
print("After clear:", numbers)
