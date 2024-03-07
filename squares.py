print("\n*********************Create list*************************")
squares = []
for value in range(1, 11): ### {{{
    square = value ** 2
    squares.append(square)
### }}}

print(squares)

print("\n*********************list comprehension*************************")
## print("***********************view is clean, difficutl to know***********")
squares = [value**2 for value in range(1, 11)] ;#pay attention for wo ":"
print(squares)
# print(f'\[value**2 for value in range(1, 11)\]')  This does not work

print("\n*********************min/max/sum*************************")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f'The min of digits is {min(digits)}')
print(f'The max of digits is {max(digits)}')
print(f'The sum of digits are {sum(digits)}')

print("\n***********************exe4-3/4/5***********")
counters = [value for value in range(1, 1_000_001)] 
## print(counters) ;#
print(f'The min of counters is {min(counters)}')
print(f'The max of counters is {max(counters)}')
print(f'The sum of counters are {sum(counters)}')

print("\n***********************exe4-6***********")
odds=[value for value in range(1,20,2)]
print(odds)

print("\n***********************exe4-7***********")
times3=[value*3 for value in range(3,30)]
print(times3)

print("\n***********************exe4-8/9***********")
cubes=[value**3 for value in range(1,11)]
print(cubes)
