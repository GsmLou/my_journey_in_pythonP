import time
#Prepare for a Challenge

time.sleep(3) # to delay the run time of the file

total = 0 # to the points of the correct answers

item_1 = input("1.) Who is the father of Computer science? ")  # this is a function that prints question and allow the user to input ther answer.
if item_1.lower() == "charles babbage": #  if the user input identical to the charle babbage  or equal to the user input i will print correct.
    print("correct!") # correct will be the output if the answer of the user is correct.
    total += 1  # if the answer of the user is correct the total will add 1 
else:
    print("incorrect answer!") # if the answer is wrong it will print incorrect answer

item_2 = input("2.) In a computer, most processing takes place in _______? ")
if item_2.lower() == "cpu" or "control processing unit":
    print("correct!")
    total += 1
else:
    print("incorrect answer!")
    
item_3 = input("3.)First page of Website is termed as _______? ")
if item_3.lower() == "homepage":
    print("correct!")
    total += 1
else:
    print("incorrect answer!")

item_4 = input("4.) In which year, the Microsoft company was founded? ")
if item_4.lower() == "1975":
    print("correct!")
    total += 1
else:
    print("incorrect answer!")
    
item_5 = input("5.) A computer cannot ‘boot’ if it does not have the _______? ")
if item_5.lower() == "os" or "operating system":
    print("correct!")
    total += 1
else:
    print("incorrect answer!")

item_6 = input("6.) Full form of LAN? ")
if item_6.lower() == "local area network":
    print("correct!")
    total += 1
else:
    print("incorrect answer!")

item_7 = input("7.) Where are the CPU and memory located? ")
if item_7.lower() == "motherboard":
    print("correct!")
    total += 1
else:
    print("incorrect answer!")

item_8 = input("8.) What is correcting errors in a program called? ")
if item_8.lower() == "debugging":
    print("correct!")
    total += 1
else:
    print("incorrect answer!")
    
item_9 = input("9.) A fault in a computer program which prevents it from working correctly is known as _______? ")
if item_9.lower() == "bug":
    print("correct!")
    total += 1
else:
    print("incorrect answer!")

item_10 = input("10.) What does RAM stand for? ")
if item_10.lower() == "random access memory":
    print("correct!")
    total += 1
else:
    print("incorrect answer!")
    
print(f"your total correct answers is {total} out of 10 ")

if total <= 5 : # if the total score is less than 5 the output is in the line 81
    print("you need more study!")
elif total >= 6: # and if the total is greater than 6 or more the output is in the line 83
    print("goodjob!")

    
