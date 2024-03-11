requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

print("\n*********************if-elif-else*************************")
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

print("\n*********************ex5-3*************************")
alien_color = ['green', 'yellow', 'red']

if ('green' in alien_color):
	print("You get 5 points")
elif('green' not in alien_color):
	print("You get 10 points")


print("\n")
requested_toppings = ['mushrooms', 'jiaozixian', 'green peppers', 
                      'nanguanxian','extra cheese', 'siguaxian']
empty_toppings = ['jiaozixian', 'nanguanxian', 'siguaxian']

for requested_topping in requested_toppings:
    if requested_topping in empty_toppings:
        print(f'Sorry, we are out of {requested_topping} right now.')
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

print("\n*********************empty_toppings*************************")
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


print("\n*********************multi-list*************************")
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")


print("\n*********************ex5-8*************************")
'''
users = [
        'zhangsan',
        'lisi',
        'wangermazi',
        'admin',
        'johen'
        ]
'''
users = []

if users:
    for user in users: ###{{{B-F
        if user.lower() == 'admin': ###{{{
            print(f"Hello {user.title()}, would you like to see a status report?")
        ### }}}
        else: ###{{{
            print(f"Hello {user.title()}, thank you for logging in again.")
        ### }}}
     ### E-F}}}
else:
	print("We need to find some users!")