# ======================================
# Assignment 02 - Python Lists
# Chapter 1 - What is a List?
# ======================================

Fruits = ["Apple","Mango","Banana","Kiwi"]
print(Fruits)

print(Fruits[0])
print(Fruits[1])
print(Fruits[2])

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])

print("Before:",fruits)

fruits[1] = "Mangoes"
print("After:",fruits)
print("Before:",fruits)
fruits.append("Lemon")
print("After:",fruits)

fruits.extend(["chia seed","guava","cherry"])
print(fruits)
print(len(fruits))