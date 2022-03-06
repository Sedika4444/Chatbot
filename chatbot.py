
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
        starters = ['salad','Huushur','buuz']
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

# Main Course order main = ['Tsuivan','khorkhog','lavhsa',]
print("Our main dishes:") 
for x in range(len(main)):
print(main[x])
main_dish = input("please type your main dish:")
if main_dish.lower()== main[0].lower():
print(f"you have ordered {main[1]} as your main dish")
elif main_dish.lower()==main[2].lower():
print(f"you havem ordered{main[2]} as your main dish")

# Dessert Order
desserts = ['Icecream sundae', 'Chocolate Cake', 'apple pie']
print("For our dessert dishes we have:")
for x in range(len(desserts)):
    print(desserts[x])
	    
dessert = input("Please type your main dish: ")
if dessert.lower() == desserts[0].lower():
    print(f"You have ordered {desserts[0]} as your dessert")
elif dessert.lower() == desserts[1].lower():
    print(f"You have ordered {desserts[1]} as your dessert")
elif dessert.lower() == desserts[2].lower():
    print(f"You have ordered {desserts[2]} as your dessert")

#final order
print(f"Here is your final order: {starter}, {main_dish}, {dessert}")

#confirm order
order_confirm = input("Do you accept this order?")

if order_confirm.lower() == 'yes':
    print("Thank you for ordering using our chatbot service! Your food will arrive soon!")
else:
    print("Please start your order again.")

