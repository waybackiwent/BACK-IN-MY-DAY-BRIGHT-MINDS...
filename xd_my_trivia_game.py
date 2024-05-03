x = 0
score = x

print("What is 4 * 12")
answer_1 = input("a)36\nb)48\nc)39\nd)44\n:")
if answer_1.lower() == "b" or answer_1.lower() == "48":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, 4 * 12 is ")

print("Who is the crazyest person in class?")
answer_2 = input("a)Sam\nb)Kevin\nc)Johnson\nd)Neil\n:")
if answer_2.lower() == "c" or answer_2.lower() == "Johnson":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The crazyest person in class is Johnson")

print("True or False... is Kevin the quiets and nicest person in class?")
answer_3 = input(":")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")  

print("Who always rages while playing a game in class")
answer_4 = input("a)Neil\nb)Sam\nc)Kevin\nd)Johnson\n:")
if answer_4.lower() == "a" or answer_4 == "Neil":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The person that rages is Neil")

print("True or False... Is Sam SUS")
answer_5 = input(":")
if answer_5.lower() == "true" or answer_5.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Sam is SUS")

print("True or False... Is not Sam Gay")
answer_5 = input(":")
if answer_5.lower() == "false" or answer_5.lower() == "f":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Sam is Racist")
    
print("Who is making a gimkit to get a 10 dollar gift card")
answer_4 = input("a)Neil\nb)Sam\nc)Kevin\nd)Johnson\n:")
if answer_4.lower() == "d" or answer_4 == "Johnson":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, It is Johnson")
    
print("Who doesn't have a girl friend")
answer_4 = input("a)Neil\nb)Sam\nc)Johnathan\nd)Johnson\n:")
if answer_4.lower() == "c" or answer_4 == "Johnathan":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, It is Johnathan")
    
print("Who got lucky with coke")
answer_4 = input("a)Neil\nb)Sam\nc)Johnathan\nd)Johnson\n:")
if answer_4.lower() == "a" or answer_4 == "Neil":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The person that got lucky is Neil")

score = float(x / 10) * 100
print(x,"out of 10, that is",score, "%")