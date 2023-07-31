# Write a program that calculates the sum of all even numbers from 1 to 100

total_even = 0
for even in range(1, 101):
    if even % 2 == 0:
        total_even += even
print(total_even)


# or :

total = 0
for i in range(2, 101, 2):
    total += i
print(total)
