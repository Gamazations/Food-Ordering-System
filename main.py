#Importing libraries that we can access later
import random
import math

#Prints the menu and assigns price values to each of the items
menu = {
  "Botero Bowl": 14.99,
  "Dubai Chocolate Cups": 4.49,
  "Bacon Egg N Cheese": 10.00,
  "PomegraNates": 7.99,
  "Tiramisu": 16.99,
  "Biggie Cheese": 6.00,
  "Acai Bowl": 7.99,
  "Tim Cheese": 99.99,
  "John Pork": 0.99
}

#Prints an introductory message, welcomg the user to our shop.
print("Hello! Welcome to the food ordering system! Look at our menu!")
#Prints the menu from the the dictionary above, alongside their price.
for item, price in menu.items():
  print(f"-> {item} - {price}")

#Resets values at the beginning of code to ensure no bugs & defines these variables/dictionary.
subtotal = 0
grandTotal = 0
quantity = {}
favoriteOrderUsed = False

#Calculator for the subtotal, updates concurrently with the user ordering food
def subtotalCalculator():
  #Defines that we are using the global variable subtotal
  global subtotal
  #Resets value to ensure no bugs with calculations
  subtotal = 0
  #Loops through every item the quantity dictionary, creates variables and assigns the price and amount of that item using quantity and menu dictionary and calculates the final subtotal after every value has been gone through in the quantity dictionary.
  for item in quantity:
    price = menu[item]
    amount = quantity[item]
    subtotal+= price*amount
  return subtotal

#Used to save your current order as a favorite
def saveFavoriteOrder():
  #Allows you to name the order
  nameOfOrder = input("Enter the name of this order: ")
  #Starts to create the line to be saved in the file with starting the order name
  orderForFile = f"{nameOfOrder}: "
  #Loops for every item in quantity, so every item that is currently being ordered and adds it to the variable for the file
  for item in quantity:
    amount = quantity[item]
    orderForFile += f"{item} - {amount}x, " 
    orderForFile = orderForFile.strip(", ")
  #Opens the file and saves it to the file
  file = open("favoriteorders.txt", "a")
  file.write(orderForFile + "\n")
  file.close()

'''
CITATIONS:
Title: Read a file line by line in Python
Author: www.geeksforgeeks.org
Date: April 16th, 2025
Code Version: Python
Availability: https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/

Title: Python String replace() Method
Author: www.geeksforgeeks.org
Date: April 16th, 2025
Code Version: Python
Availability: https://www.geeksforgeeks.org/python-string-replace/

Title: Python String split()
Author: www.geeksforgeeks.org
Date: April 16th, 2025
Code Version: Python
Availability: https://www.geeksforgeeks.org/python-string-split/
'''

#Used to show the favorite orders priorly or set new ones
def favoriteOrders():
  #First tries to read the file and saves the files contents to a variable
  try:
    file = open("favoriteorders.txt", "r")
    favOrders = file.readlines()
  #If the user has never had a favorited order before, the file will not have been created or will be emptied. These two code segments allows for the user to be notified that they have no favorite items, and guides them to create one.
  except FileNotFoundError:
    print("You have never saved an order before! Order something and in checkout, favorite it to start your favorited orders.")
    return
  if favOrders==[]:
    print("You have never saved an order before! Order something and in checkout, favorite it to start your favorited orders.")
    return

  #For every item in favOrders, it will print that item and the number with it.
  for i in range(len(favOrders)):
    print(f"{i + 1}. {favOrders[i]}")

  #Asks the user whether they want to set a new favorite or use an old one
  whichOrder = input("Would you like to (1) choose a preexisting favorited order or (2) create a new favorited order based on your current cart?: ")
  #If 2, it runs saveFavoriteOrder to start that process
  if whichOrder == "2":
    #Checks to see if the current cart is empty or not, if it is, tells user to fill cart first.
    if quantity=={}:
      print("You need to add some items to your cart first!")
      return
    else:
      saveFavoriteOrder()
    

  #If old, it clears out the current quantity dictionary
  else:
    #Sets favorite order used to True so we know that currently a favorite order is being used
    favoriteOrderUsed = True
    quantity.clear()
    #It asks the user which number
    favOrderNum = int(input("What is the number of the order you want to select?: "))
    #Due to index, we -1 and access the values from the line and save it to a new variable
    selectedFavOrder = favOrders[favOrderNum-1]
    #We split the new variable into two, the orderName and its items
    orderName, orderItems = selectedFavOrder.split(":", 1)
    #We strip it of any unnecessary spaces that are there
    cleanedSelectedFavOrder = orderItems.strip()
    #We then split it again into lists
    listSelectedFavOrder = cleanedSelectedFavOrder.split(", ")

    #For every order in the list, we split that again for the item name and item amount
    for order in listSelectedFavOrder:
      itemName, itemAmount = order.split(" - ")
      #We replace x with nothing so it can become an intenger
      itemAmount = itemAmount.replace("x", "")
      itemAmount = int(itemAmount)
      #We add these values back to the original quantity so it can be calculated.
      quantity[itemName] = itemAmount
    #Calculates the existing subtotal
    subtotalCalculator()
    #Prints a message letting us know what happened
    print(f"{orderName} has been put in your cart instead of your current order.")
      

#The main function which does all the backend of inputs, grand total calculations, etc.
def foodOrder():
  #Defines that we are editing a global variable, totalCost
  global totalCost
  #Sets wantToOrder to true so that the while loop starts to function
  #Sets favoriteOrderUsed to false so we know that currently there is not a favorite order.
  favoriteOrderUsed = False
  wantToOrder = True
  while wantToOrder == True:
    costcoChoice = input("Do you want to (1) Order, (2) GoToGo or (3) Checkout: ")
    if costcoChoice == "1":
      #Asks the user what they want to order
      order = input("What do you want to order?: ")
      #Adds the user's input to the quantity dictionary, and adds +1 to the value of the item if it has been added before-- if not, it starts it at 1. 
      if order in quantity:
        quantity[order]+=1
      else:
        quantity[order]=1
      #Calculates the current subtotal concurrently with the user's order and assigns it to variable currentSub. 
      currentSub = subtotalCalculator()
      #Prints what they just added to their cart and their current subtotal.
      print(f"You added {order} to your order!")
      print("Your current subtotal is", '{:.2f}'.format(currentSub))

    if costcoChoice == "2":
      favoriteOrders()

    if costcoChoice == "3":
      #Loops through every item that has been ordered in the dictionary quantity, and prints the quantity of the item, name of the item, and the total cost of how much of those items.
      for item in quantity:
        priceOfItem = quantity[item]*menu[item]
        print(f"{quantity[item]}x {item} = ${priceOfItem:.2f}")    

 #Checks that this is the final order-- if yes, code continues and calculates grand total and returns the value and a random order number. If not, it reruns function so user can continue ordering.
      finalOrder = input("This is your final order, correct? (Yes/No): ")
      if finalOrder == "Yes" or finalOrder == "yes":
        #This checks to see if the current order is a favorite order
        if favoriteOrderUsed == True:
          favoriteThisOrder = input("Want to favorite order? (Yes/No): ")
          if favoriteThisOrder == "Yes" or favoriteThisOrder == "yes":
            saveFavoriteOrder()
        tax = subtotal*0.06625
        grandTotal = subtotal + tax
        #EXTRA: If grandTotal is greater than 50, a discount for 10% is applied
        if grandTotal > 50:
          print("You spent over 50 dollars. You are eligible for a 10% discount!")
          grandTotal = grandTotal*0.9
        #A random order number is generated from possible values between 100000 and 999999 and displayed to the user
        orderNumber = random.randint(100000, 999999)
        print("Your order number is ", orderNumber)
        #Returns the grand total
        return print("Your grand total is", '{:.2f}'.format(grandTotal), "!")
      #If final order is not done, reruns function
      else:
        foodOrder()

#Intially runs the code for the first time
foodOrder()

