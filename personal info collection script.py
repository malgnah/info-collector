first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
fav_color = input("Enter your favourite colour: ")

print(f"\n--------{first_name}'s info----------")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Favourite colour: {fav_color}")

if age < 0:
    print("**You sure this is your age? 0-0")
elif age > 116:
    print("**Congrats!! You might be the oldest person in the world!")

input("\nPress Enter To Exit...")