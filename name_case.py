name = "eric"
message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)

string = "zAch"
print(string)
print(string.title())
print(string.lower())
print(string.upper())

name = " Albert Einstein "
words = "A person who never made a mistake never tried anything new."
## message = f"{name} once said, \n\t\"{words}\""
## print(message)
message = f"{name.strip().title()} once said, \n\t\"{words}\""
print(message)

message = f"{name.lstrip().title()} once said, \n\t\"{words}\""
print(message)

message = f"{name.rstrip().title()} once said, \n\t\"{words}\""
print(message)
