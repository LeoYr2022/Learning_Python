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


print("\n*********************ex5-8/9*************************")
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

print("\n*********************ex5-10*************************")
current_users = [
                'zhangSan',
                'lisi',
                'wangermazi',
                'admin',
                'johen'
                ]

new_users = [
            'zhangsan',
            'Lili',
            'Wangermazi',
            'tifini',
            'aWang'
            ]

current_users_lower=[]
for current_user in current_users:
    current_users_lower.append(current_user.lower())
## print(current_users_lower)

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'The name {new_user} is used, change another one.')
    else:
        print(f'The name {new_user} is unused.')


print("\n*********************ex5-11*************************")
for n in range(1,10): ### {{{
    if n==1:
        print(f'1st')
    elif n==2:
        print(f'2nd')
    elif n==3:
        print(f'3rd')
    else:
        print(f"{n}th")
### }}}


print("\n*********************ex5-12*************************")
    


