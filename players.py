print("\n******************List element*************************")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
## The same
print(players[0:3])
print(players[ :3])

## The same
print("\n")
print(players[3: ])
print(players[-2:])


print("\n******************Traverse List element*************************")
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
'''
for player in players[:3]:
    print(player.title())
'''
better_players = [player.title() for player in players[:3]]
## print(f'The better_players are: {better_players.title()}') list does not have the attribute of title()
print(f'\t{better_players}')
