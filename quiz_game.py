print("!!!_____WELCOME TO KBC_____!!!")

print("THEE ANSWERS OF LIST ON YOUR SCREEN")

numbers = [4,8,16,32,64,128,256,36,97,0,83,69,74,67,39,86,365,87,76,56,43]
print("list is : " , numbers)
money = 0
max = 0
min = 0

# QUESTION NUMBER 1
print("question number one is :: WHAT IS 2+2 ")
print("A. numbers[2]")
print("B. numbers[4]")
print("C. numbers[0]")
print("D. numbers[9]")

q1 = input("enter the option(A/B/C/D): ").upper()
if q1 == "C":
   money += 1000
   print("you won 1000 rupees on this question")
else:
    print("wrong answer , Butter luck next time")

# QUESTION NUMBER 2
print("question number one is :: WHAT IS 4+4 ")
print("A. numbers[4]")
print("B. numbers[5]")
print("C. numbers[9]")
print("D. numbers[1]")

q1 = input("enter the option(A/B/C/D): ").upper()
if q1 == "D":
   money += 2000
   print("you won 2000 rupees on this question")
else:
    print("wrong answer , Butter luck next time")

# QUESTION NUMBER 3
print("question number one is :: WHAT IS 8+8 ")
print("A. numbers[7]")
print("B. numbers[9]")
print("C. numbers[9]")
print("D. numbers[2]")

q1 = input("enter the option(A/B/C/D): ").upper()
if q1 == "D":
   money += 3000
   print("you won 3000 rupees on this question")
else:
    print("wrong answer , Butter luck next time")

# QUESTION NUMBER 4
print("question number one is :: WHAT IS 16+16 ")
print("A. numbers[6]")
print("B. numbers[3]")
print("C. numbers[7]")
print("D. numbers[9]")

q1 = input("enter the option(A/B/C/D): ").upper()
if q1 == "B":
   money += 4000
   print("you won 4000 rupees on this question")
else:
    print("wrong answer , Butter luck next time")


# QUESTION NUMBER 5
print("question number one is :: WHAT IS 32+32 ")
print("A. numbers[7]")
print("B. numbers[1]")
print("C. numbers[4]")
print("D. numbers[0]")

q1 = input("enter the option(A/B/C/D): ").upper()
if q1 == "C":
   money += 5000
   print("you won 5000 rupees on this question")
else:
    print("wrong answer , Butter luck next time")

# QUESTION NUMBER 6
print("question number one is :: WHAT IS 64+64 ")
print("A. numbers[8]")
print("B. numbers[0]")
print("C. numbers[5]")
print("D. numbers[3]")

q1 = input("enter the option(A/B/C/D): ").upper()
if q1 == "C":
   money += 6000
   print("you won 6000 rupees on this question")
else:
    print("wrong answer , Butter luck next time")


# QUESTION NUMBER 7
print("question number one is :: WHAT IS 128+128 ")
print("A. numbers[6]")
print("B. numbers[2]")
print("C. numbers[6]")
print("D. numbers[5]")

q1 = input("enter the option(A/B/C/D): ").upper()
if q1 == "A":
   money += 7000
   print("you won 7000 rupees on this question")
else:
    print("wrong answer , Butter luck next time")

print("TOTAL MONEY YOU WON :",money)

if money == max:
    print("congratualtions!!! YOU WON THE FULL AMOUNT")
else:
    print("YOU DID NOT WON FULL AMOUNT!!!, BUTTER LUCK NEXT TIME ANY WAY CONGRATUALTIONS, YOU TRIES YOUR BEST")





