# Check element is in the list
print("\n**************Check element is in the list*************")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if('mushrooms' in requested_toppings):
    print("This element is in the list")


print("\n**************banned_users*************")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


print("\n**************exe5-1*************")
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')