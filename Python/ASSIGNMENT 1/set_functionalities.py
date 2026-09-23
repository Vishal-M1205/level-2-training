numbers = {1, 2, 3, 4, 5}
print("Original:", numbers)

empty_set = set()
print("Empty set:", empty_set)

duplicates = {1, 2, 2, 3, 3, 4}
print("Duplicates removed:", duplicates)

numbers.add(6)
print("After add:", numbers)

numbers.update([7, 8])
print("After update:", numbers)

numbers.remove(1)
print("After remove:", numbers)

numbers.discard(100)
print("After discard:", numbers)

popped = numbers.pop()
print("Popped:", popped)
print("After pop:", numbers)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Set A:", a)
print("Set B:", b)

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (A - B):", a - b)
print("Symmetric Difference:", a ^ b)

sub = {1, 2}
print("Is subset:", sub.issubset(a))
print("Is superset:", a.issuperset(sub))
print("Is disjoint:", a.isdisjoint({7, 8}))

print("Membership 3 in A:", 3 in a)
print("Length of A:", len(a))
print("Max of A:", max(a))
print("Min of A:", min(a))
print("Sum of A:", sum(a))

copy_set = a.copy()
print("Copied:", copy_set)


a.clear()
print("After clear:", a)
