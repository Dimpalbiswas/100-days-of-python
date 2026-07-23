import random
number = random.randint(1, 6)
print(number)

number_1 = random.random()
print(number_1)
# random.randint(a, b)
# Returns a random integer from a to b (both included)

# random.random()
# Returns a random float from 0.0 (included)
# up to but not including 1.0

number_2 = random.random()*10
print(number_2)


number_3 = random.random()*10 
print(number_3)
print(number_3+5)
print(number_3+10)


number_4 = random.uniform(10,20)
print(number_4)
print(round(number_4 ,2))