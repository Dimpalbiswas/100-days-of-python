import random
friends = ["Ravi","Gita","Kanika","Diti","Dimpal"]
number = random.randint(0,4)
print(number)
print(f"{friends[number]} will pay the bill")

print(f"{random.choice(friends)} will pay the bill")


customer_names = input( "Enter user name = ")
customer_list = customer_names.split(",")
print(f"{random.choice(customer_list)} will pay the bill")