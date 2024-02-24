def launch_application():
    ask_address()
    ask_option()
    
    
def ask_address():
    global address
    address = input('''----------------------------------
Dear Customer, welcome.
                    
Please enter the address 
where you want your food delivered: ''')
    
def ask_option():
    option = input('''-----------------------------------
Do you want to view:
        
1) The Deals of the Day 
2) Menu
     
Enter your choice here [ (1) or (2) ]: ''')
    if int(option) == 1:
        deals()
    elif int(option) == 2:
        menu()
    else:
        print("Please enter a valid option.")
        ask_option()
        
def deals():
    print("-----------------------------------")
    print("Deals of the Day: ")
    print(" ___________________________________________________")
    print("| Item No |   Item Description   |  Cost  |  Deals  |")
    print("|         |                      |        |         |")
    print("| 1       | Soup                 | Rs 200 |  Rs 100 |")
    print("|         |                      |        |         |")
    print("| 2       | Gobi Manchurian      | Rs 300 |  Rs 200 |")
    print("|         |                      |        |         |")
    print("| 3       | Gobi Chilly          | Rs 400 |  Rs 300 |")
    print("|         |                      |        |         |")
    print("| 4       | Veg Fried Rice       | Rs 500 |  Rs 400 |")
    print("|         |                      |        |         |")
    print("| 5       | Veg Noodles          | Rs 600 |  Rs 500 |")
    print("|         |                      |        |         |")
    print("| 6       | Paneer Chilly        | Rs 550 |  Rs 450 |")
    print("|         |                      |        |         |")
    print("| 7       | Babycorn Manchurian  | Rs 450 |  Rs 350 |")
    print("|         |                      |        |         |")
    print("| 8       | Paneer Fried Rice    | Rs 350 |  Rs 250 |")
    print("|         |                      |        |         |")
    print("| 9       | Shangai Fried Rice   | Rs 250 |  Rs 150 |")
    print("|         |                      |        |         |")
    print("| 10      | Babycorn Chilly      | Rs 99  |  Rs 50  |")
    print(" ___________________________________________________ ")
    print("These Deals have aldready been applied to the menu.")
    print(" ")
    inp = int(input("To order items from the menu, enter (1): "))
    if inp == 1:
        menu()
    else:
        print("Please enter a valid option.")
        deals()
    
    
    
def menu():
    global menu_dict
    menu_dict = {1 : "Soup",
                 2 : "Gobi Manchurian",
                 3 : "Gobi Chilly",
                 4 : "Veg Fried Rice",
                 5 : "Veg Noodles",
                 6 : "Paneer Chilly",
                 7 : "Babycorn Manchurian",
                 8 : "Paneer Fried Rice",
                 9 : "Shangai Fried Rice",
                 10 : "Babycorn Chilly"}
    print("-----------------------------------")
    print("Menu: ")
    print(" _________________________________________ ")
    print("| Item No |   Item Description   |  Cost  |")
    print("|         |                      |        |")
    print("| 1       | Soup                 | Rs 100 |"  )
    print("|         |                      |        |")
    print("| 2       | Gobi Manchurian      | Rs 200 |"  )
    print("|         |                      |        |")
    print("| 3       | Gobi Chilly          | Rs 300 |"  )
    print("|         |                      |        |")
    print("| 4       | Veg Fried Rice       | Rs 400 |"  )
    print("|         |                      |        |")
    print("| 5       | Veg Noodles          | Rs 500 |"  )
    print("|         |                      |        |")
    print("| 6       | Paneer Chilly        | Rs 450 |"  )
    print("|         |                      |        |")
    print("| 7       | Babycorn Manchurian  | Rs 350 |"  )
    print("|         |                      |        |")
    print("| 8       | Paneer Fried Rice    | Rs 250 |"  )
    print("|         |                      |        |")
    print("| 9       | Shangai Fried Rice   | Rs 150 |"  )
    print("|         |                      |        |")
    print("| 10      | Babycorn Chilly      | Rs 50  |"  )
    print(" _________________________________________ ")
    selected_items = input('''Select the items that you wish to order 
by entering the Item Numbers here, separated by a space: ''')
    global selitelist
    selitelist = selected_items.split()
    print(" ")
    print("You have selected Items No.", selitelist)
    remove_items = input('''Do you want to remove any items you have added by mistake? 
If so, enter the Item Number below.
Else, enter 'No': ''')
    reitelist = remove_items.split()
    if remove_items.lower() != "no":
        for i in reitelist:
            selitelist.remove(str(i))
            print(" ")
            print("Item No.", i,"removed.")
        print(" ")
        print("You have selected Items No.", selitelist)
    add_items = input('''Do you want to add any items that you may have forgotten? 
If so, enter the Item Number below.
Else, enter 'No': ''')
    additelist = add_items.split()
    if add_items.lower() != "no":
        for i in additelist:
            selitelist.append(str(i))
            print(" ")
            print("Item No.", i,"added.")
        print(" ")
        print("You have selected Items No.", selitelist)
    

def reciept():
    rece = {"Soup" : 100,
            "Gobi Manchurian" : 200,
            "Gobi Chilly" : 300,
            "Veg Fried Rice" : 400,
            "Veg Noodles" : 500,
            "Paneer Chilly" : 450,
            "Babycorn Manchurian" : 350,
            "Paneer Fried Rice" : 250,
            "Shangai Fried Rice" : 150,
             "Babycorn Chilly" : 50}
    print(" ")
    print("-----------------------------------")
    print("              RECIEPT              ")
    print("-----------------------------------")
    total = 0
    for i in selitelist:
        key = (menu_dict[int(i)])
        print(i,"|", key, "|", "Rs",rece[key])
        print(" ")
        total = int(rece[key]) + total
    print("-----------------------------------")
    print("Your total is: Rs",total )
    print("-----------------------------------")
    print(" ")
    print("Thank You for ordering with us.")
    print("Your order will be delivered to", address,".")
    print(" ")
    print("We currently only accept 'Cash on Delivery'.")
    print("Sorry for the inconvience.")
    print(" ")
    import datetime
    now = datetime.datetime.now()
    print ("Current date and time of order: ")
    print (now.strftime("%d-%m-%Y %H:%M:%S"))

launch_application()
reciept()
    
    
