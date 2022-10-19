points = 0
print("Welcome to quiz 1. all letteres are in lowercase")
input()
q1 = input("I have many holes, but i can still hold water. What am i?")
if q1 == "sponge":
    print("Thats correct")
    points = points + 1

else:
    print("Thats wrong. The answer is sponge")

q2 = input("What can run but Cannot walk?")
if q2 == "river":
    print("Thats correct")
    points = points + 1

else:
    print("Thats wrong. The answer is river")

q3 = input("I’m tall when I’m young, and I’m short when I’m old. What am I?")
if q3 == "candle":
    print("Thats correct")
    points = points + 1

else:
    print("Thats wrong. The answer is candle")

q4 = input("I am part of the crew, but i betrayed them. Who am i?")

if q4 == "imposter":
    print("Thats correct.")
    points = points + 1

else:
    print("Thats wrong. The answer is imposter")

if points == 0:
    print("You have 0 points")

elif points == 1:
    print("You have 1 point")
