import random
customer_names = input( "Enter customer names separated by commas:")
customer_list = customer_names.split(",")

index_no_of_customer = random.randint(0 ,len(customer_list)-1)

print(f"{customer_list[index_no_of_customer]} will pay the bill")