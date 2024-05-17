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
    
print("Who are the people who play Blox Fruits")
answer_4 = input("a)Neil_Johnathan_Kevin\nb)Sam_Neil_Johnson\nc)Johnathan_Neil_Sam\nd)Johnson_Neil_Bob\n:")
if answer_4.lower() == "b" or answer_4 == "Sam_Neil_Johnson":
    print("Correct")
    x = x + 1
else:
    print("the people who play Blox Fruits are Sam_Neil_Johnson")
    
print("Who has the most brain rot")
answer_4 = input("a)Kevin\nb)Johnson\nc)Sam\nd)Neil\n:")
if answer_4.lower() == "b" or answer_4 == "Johnson":
    print("Correct")
    x = x + 1
else:
    print("The person with the most brain rot is JOHNSON")
    
print("Who wants to be racists")
answer_4 = input("a)Johnson\nb)Neil\nc)Johnathan\nd)Bob\n:")
if answer_4.lower() == "a" or answer_4 == "Johnson":
    print("Correct")
    x = x + 1
else:
    print("The person is Johnson")
    
print("Who is dieing ro4uhueUHI$EURGIU HEP PLS SAVE MEMEMEMEMEME")
answer_4 = input("a)Johnson\nb)Neil\nc)Johnathan\nd)Eric\n:")
if answer_4.lower() == "d" or answer_4 == "Eric":
    print("Correct")
    x = x + 1
else:
    print("The person is Eric AAAAAAAAAAAAEIFVIOEFHIUEFH")
    
print("LAST QUESTION what is (101*4+156)-5/5")
answer_4 = input("a)541\nb)567\nc)559\nd)666\n:")
if answer_4.lower() == "a" or answer_4 == "559":
    print("Correct")
    x = x + 1
else:
    print("it is 559")

score = float(x / 15) * 100
print(x,"out of 15, that is",score, "%")