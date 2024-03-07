for value in range(5): ### {{{Begin_for
    print(value)
### End_for}}}

print("\n**************range(5) vs. rang(1,5)***************************")
for value in range(1,5): ### {{{Begin_for
    print(value)
### End_for}}}

print("\n**************list(range(m,n))***************************")
numbers = list(range(1, 6))
print(numbers)