print("\n****************************************")
favorite_languages = {
    'jen'   : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil'  : 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print("\n****************************************")
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n******************keys()****************")
## for name in favorite_languages: #The result is same
for name in favorite_languages.keys():
    print(name.title())


'''
favorite_languages = {
    --snip--
}
'''

friends = ['phil', 'sarah']
for name in favorite_languages.keys(): ### {{{
    if name in friends: ### {{{
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
    ### }}}
    else:
        print(f"Hi {name.title()}.")
### }}}

print("\n******************keys() create list****************")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n******************sorted()****************")
for name in favorite_languages.keys():
    print(f"{name.title()}, thank you for taking the org poll.")

for name in sorted(favorite_languages.keys()):
    print(f"Hi, {name.title()}, thank you for taking the new poll.")


print("\n******************values()****************")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(f"\t{language.title()}")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(f"\t{language.title()}")
