magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
    print(magician.title())
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

print("***********************************Error show1*******************************")
magicians = ['alice', 'david', 'carolina']
for magician in magicians: # {{{Comment
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
# End }}} at sublime the foldmethod does not work

print("***********************************Error show2*******************************")
magicians = ['alice', 'david', 'carolina']
for magician in magicians: ### {{{Begin for 
    print(magician.title())
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.")
    print("Thank you, everyone. That was a great magic show!\n")
### End for}}}

print("***********************************4-2*******************************")
animals = ['dog','fish','cat']
for animal in animals: ### {{{Begin for
    print(f'A {animal} would make a greate pet.')
### End for}}}
print("Any of these animals would make a great pet!\n")
