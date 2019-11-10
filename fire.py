from time import sleep
from os import system as cmd
import random
import sys
T = 101

# perhaps = input("are you a cold boi today?: ")
# if "yes" "y" in perhaps:
#     while True:
#         Percent = int(input("what percent of the cpu do you want to use?: "))
#         while T != Percent:
#             print("sorry but you cant use " +Percent+ " because cpu don't have that much")
#             sleep(1)
#             Percent = int(input("what percent of the cpu do you want to use?: "))
#         else:
#             print("frick yeah lets chernobyl this room with heat")

Question = input("are you cold: ")
if "yes" in Question:
    while True:
        Percent = int(input("how much?"))
        if T != Percent:
            print("sorry but you cant use " + str(Percent) + " because cpu don't have that much")
            sleep(1)
            Percent = int(input("what percent of the cpu do you want to use?: "))
        else:
            print(T)

