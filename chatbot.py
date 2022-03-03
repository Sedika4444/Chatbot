
from numpy import true_divide

"""
This program is a chatbot for room service
"""

#list of guests at hotel
guest={'1':'Sedika', '2':'tuugu', '3':'Irmuun'}
correct_info=False

room=input("please, enter room number")
if room in guests.keys():
    correct_info=True
else:
    correct_info=False

name=input("Please enter your name:")
if correct_info and guests[room].lower()==name.lower():
    correct_info = True
    print(f"Hello, {name}!")
    else:
        correct_info = False
        #Starter Order
        starters = ['Buuz','Huushur','Tsuivan']
        print("For our starters we have:")
        for x in range(len(starters)):
            print(starters[x])

Starter = input("Please type your starter:")
if starter.lower() ==
starters[0].lower():
print(f"Your have ordered{starters[0]}as your starter")
elif starter.lower() ==
starters{1}.lower():
print(f"You have ordered{starters[1]as your starter")
elif starter.lower() ==
starters[2].lower():
print(f"You have ordered{starters[2]}as your starter")

