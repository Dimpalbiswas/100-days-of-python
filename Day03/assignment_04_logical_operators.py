age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can watch movie")
else:
    print("Entry denied.")


is_saturday = False
is_sunday = True

if is_saturday or is_sunday:
    print("This is a holiday")
else:
    print("Working day")


is_logged_in =False

if not is_logged_in:
    print("Please log in.")
else:
    print("Welcome!")


is_member = True
has_coupon = False 

if is_member and not has_coupon:
    print("member discount applied.")
else:
    print("no member discount")

username = input("Enter username: ")
password = input("Enter your password:")

if username == "dimpal" and password == "15031992":
    print("Login susscessful!")
else:
    print("Invalid username and password.")