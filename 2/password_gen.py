

length = 4
password = ""

use_digit= True

available_characters = string.ascii_letters
if use_digit:
    available_characters = available_characters + string.digits
items_count = len(available_characters)

for _ in range(length):
    index = random.randint(0, items_count - 1)
    password = password + available_characters[index]


print(f"generated password: {password}")