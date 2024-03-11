print("\n******************Copy List****************************")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] ;#this work as copy list
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n******************Copy List****************************")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n******************Not Copy List****************************")
my_foods = ['pizza', 'falafel', 'carrot cake']

# 这行不通:
friend_foods = my_foods ;# list has the attribute of inheratation

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


print("\n******************ext4-10****************************")
my_foods = ['pizza','falafel','carrot cake','jiaozi','jianbing']
list_len = len(my_foods)
print(f'The first three items in the list are: {my_foods[:3]}')
print(f'The middle three items in the list are: {my_foods[2:5]}') ;#need to judge range of index
print(f'The last three items in the list are: {my_foods[-3:]}')