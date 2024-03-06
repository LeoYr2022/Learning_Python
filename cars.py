# sort() Changes to the order of list elements are permanent
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

print("\n *********************reverse=True*****************************")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# sorted() Changes to the order of list elements are temporary
print("\n **************************************************")
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the sorted list:")
print(sorted(cars,reverse=True))

print("\nHere is the original list again:")
print(cars)


print("\n *******************reverse()*******************************")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'{cars}')

cars.reverse()
print(f'{cars}')

print("\n *******************len()*******************************")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'{len(cars)}')

print("\n *******************exe3-8/9/10*******************************")
places = ['shangdong','qingdao','wuyi','taiwan','beijing']
print(places)

print("\nHere is the temporary sorted list:")
print(sorted(places))
print(sorted(places,reverse=True))
print(f'The origial place: {places}')

print("\nHere is the permanent reversed list:")
print(f'The origial place: {places}')
places.reverse()
print(places) ;#print(places.reserse()) does not work

places.reverse()
print(places) 

print("\nHere is the permanent sorted list:")
print(f'The origial place: {places}')
places.sort()
print(places) 

places.sort(reverse=True)
print(places)
print(f'There are {len(places)} here.')
