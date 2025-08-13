password = input("Enter your password: ")

first_index = password[0]
last_index = password[-1]

hide_password = password[1:-1]
print(hide_password)
stars = "*" * len(hide_password)
print(f"{first_index}{stars}{last_index}")


