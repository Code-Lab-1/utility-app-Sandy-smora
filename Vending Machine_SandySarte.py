# variables for each dessert item 
# this is a dictionary ^ ^
a= {"code": 87, "name": "The Grey Stuff", "price": 10, "tagline": "Be our guest to try this delectable whipped cookie & cream pudding fit for royalty!"}
b= {"code": 49, "name": "Beignets", "price": 20, "tagline": "These beignets have been a wish of your New Orleans heart. Here they are: perfect, genuine, and magical."}
c= {"code": 55, "name": "Empire biscuits", "price": 25, "tagline": "These beignets have been a wish of your New Orleans heart. Here they are: perfect, genuine, and magical."}
d= {"code": 76, "name": "Pawpsicles", "price": 10, "tagline": "Get your mitts on these cherries & lemon Pawpsicles! Get two for the price of one, it's called a hustle, sweetheart~"}
e= {"code": 19, "name": "Grumpy’s Gooseberry Pie",  "price": 20, "tagline": "The local woodland creatures lend a hand to make this delicious gooseberry pie to cheer you right up"}
f= {"code": 11, "name": "'Eat me' Cookies", "price": 25, "tagline": "Eating these cookies might just land you straight in Wonderland, ahaha! …Will it? Hmm, I don’t know…will it?"}
g= {"code": 25, "name": "Mini Aurora's Birthday Cake", "price": 25, "tagline": "Bring this mini six-layer birthday cake to reality. They say that if you dream it twice, it will come true!"}
dessert_menu = [a, b, c, d, e, f, g]
count = True
money = 0

# intro for the Vending Machine # welcome message
print('\n')
print("◉=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=◉")
print("     Welcome to the DREAMSTAR pop-up diner!")
print("◉=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=◉")
print("""
A special thank you to Disney for partnering with us to 
feature famous foods and drinks from their movies!
""")
print("""This pop-up diner will only be open for 4 months, 
and the menu choices will change every week.
""")
print("""We are always sure to deliver a new experience on 
every visit, so be sure to stop by more than once!
""")
print("""For any allergy concerns or dietary restrictions, 
please consult a server at the counter!
""")

# ready to order
print('Are you ready to order?')
input('\nPress Enter to continue\n')

# menu, borders are ASCII art
print("""
 _| |___________________________________________________________________________________________________________________________________________________________________________| |___
(______________________________________________________________________________________________________________________________________________________________________________________)
""")
print("\t\t\t\t\t◉=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○◉")
print('''\t\t\t\t\t_ _    _   ___  ___   _   _    _ _ _   _    _   _   _  _  _   _ 
\t\t\t\t\t|   \ | __|/ __|/ __|| __|| _ \|_   _| |  \/  || __|| \| || | | | 
\t\t\t\t\t| |) || _| \__ \\__ \ | _| |   /  | |   | |\/| || _| | .` || |_| | 
\t\t\t\t\t|___/ |___||___/|___/|___||_|_\  |_|   |_|  |_||___||_|\_| \___/  
''')
print("\t\t\t\t\t◉=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○◉\n")

for x in dessert_menu: #call the items
    print(f"[{x['code']}] Item: [{x['name']}] --- Price: [{x['price']}] --- Tagline: [{x['tagline']}]\n")
print("""
  _____________________________________________________________________________________________________________________________________________________________________________________
(__   ____________________________________________________________________________________________________________________________________________________________________________   __)
   | |                                                                                                                                                                            | |     
\n""")

while count == True: # while loop
    purchase = int(input("\nInput the code of the dessert item you'd like to order:\n")) # the user will order here
    for x in dessert_menu:
        if purchase == x['code']:
            dessert = x
    if dessert == '': # if the code is wrong
        print('''I’m sorry, the code inputted is incorrect.
        Please try again. \n''')
    else: # the code tells how much the AED the user will pay
        print(f"\nAn excellent choice!, thank you for purchasing {dessert['name']}. \n")
        print(f"That will be {dessert['price']} AED \n")
        
        price = dessert.get("price")
        while money < price: # while loop
            money = money + float(input("Please enter money to pay \n")) # this is where the user inputs money of any amount

        # this the receipt
        print(""" 
        \tDREAMSTAR pop-up diner \n
        ◉=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=◉
        \tThank you for your purchase!
        The receipt and the order are in the dispenser.
        Have a nice day and stop by again! :Þ
        ◉=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=◉\n
        \t""" + dessert.get("name")) # shows the item the user bought
        print('\n')
        print('\t◉=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=○=◉')
        print(f"""
        {dessert["name"]} -- {dessert['price']} AED
        """) # shows the item the user bought + the price

        money -= price
        print("\tHere is your change: " + str(money) + " AED \n") # the change returned to the user
        if money == "":
            print('''I’m sorry, the money inputted is incorrect.
                Please try again.''') # if no money is inputted

    add_dessert_item = str(input("""\nDo you wish to purchase more items? 'yes' or 'no'
    \n But if not just type another letter. \n""")) # user is offered to buy more items

    yes = ["yes", "YES" , "Yes"]
    no = ["no", "NO", "No"]

    if add_dessert_item in yes: # user can order more dessert items
        count = True
    elif add_dessert_item in no: # user either answers 'no' or nothing is inputted
        count = False 
    else:
        count = False