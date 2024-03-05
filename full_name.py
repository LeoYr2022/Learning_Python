first_name = "ada"
last_name = "loveLace"
full_name = f"{first_name} {last_name}"
message_1 = f"Hello, {full_name.title()}"
message_2 = "Hello, {} {}".format(first_name, last_name)

print(message_1)
print(message_2.title())