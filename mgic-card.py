print("\n\n\n********* Guess a number between 1-63***********\n\n\n")

card1 = [1, 3, 5, 7, 9, 11, 13, 15,
        17, 19, 21, 23, 25, 27, 29, 31,
        33, 35, 37, 39, 41, 43, 45, 47,
        49, 51, 53, 55, 57, 59, 61, 63]

card2 = [2, 3, 6, 7, 10, 11, 14, 15,
        18, 19, 22, 23, 26, 27, 30, 31,
        34, 35, 38, 39, 42, 43, 46, 47,
        50, 51, 54, 55, 58, 59, 62, 63]

card3 = [4, 5, 6, 7, 12, 13, 14, 15,
        20, 21, 22, 23, 28, 29, 30, 31,
        36, 37, 38, 39, 44, 45, 46, 47,
        52, 53, 54, 55, 60, 61, 62, 63]

card4 = [8, 9, 10, 11, 12, 13, 14, 15,
        24, 25, 26, 27, 28, 29, 30, 31,
        40, 41, 42, 43, 44, 45, 46, 47,
        56, 57, 58, 59, 60, 61, 62, 63]

card5 = [16, 17, 18, 19, 20, 21, 22, 23,
        24, 25, 26, 27, 28, 29, 30, 31,
        48, 49, 50, 51, 52, 53, 54, 55,
        56, 57, 58, 59, 60, 61, 62, 63]

card6 = [32, 33, 34, 35, 36, 37, 38, 39,
        40, 41, 42, 43, 44, 45, 46, 47,
        48, 49, 50, 51, 52, 53, 54, 55,
        56, 57, 58, 59, 60, 61, 62, 63]
number = 0


for i in range(len(card1)):
    if (i+1) % 8 == 0:
        print(card1[i])
    else:
        print(card1[i],end = " ")
print("\nis your number present in this card  (yes/no)")
ans = input()
if ans == "yes" or ans == "YES":
    number += card1[0]


for i in range(len(card2)):
    if (i+1) % 8 == 0:
        print(card2[i])
    else:
        print(card2[i],end = " ")    
print("\nis your number present in this card (yes/no)")
ans = input()
if ans == "yes" or ans == "YES":
    number += card2[0]

    
for i in range(len(card3)):
    if (i+1) % 8 == 0:
        print(card3[i])
    else:
        print(card3[i],end = " ")
print("\nis your number present in this card (yes/no)")
ans = input()
if ans == "yes" or ans == "YES":
    number += card3[0]

    
for i in range(len(card4)):
    if (i+1) % 8 == 0:
       print(card4[i])
    else:
        print(card4[i],end = " ")
print("\nis your number present in this card (yes/no)")
ans = input()
if ans == "yes" or ans == "YES":
    number += card4[0]

    
for i in range(len(card5)):
    if (i+1) % 8 == 0:
        print(card5[i])
    else:
        print(card5[i],end = " ")
print("\nis your number present in this card (yes/no)")
ans = input()
if ans == "yes" or ans == "YES":
    number += card5[0]

for i in range(len(card6)):
    if (i+1) % 8 == 0:
        print(card6[i])
    else:
        print(card6[i],end = " ")
print("\nis your number present in this card (yes/no)")
ans = input()
if ans == "yes" or ans == "YES":
    number += card6[0]

print("Your number is: ",number)    

    
