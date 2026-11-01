print("Welcome to Danuza´s Pizza, the Best from Araguaina!")

name = input("Before we start, could you please tell us your name? ")
age = int(input("And your age? "))
answer1 = input ("Do you would like to see our incredible menu? [yes/no] ").lower()


while answer1 != "yes" and answer1 !="no":
    print ("Something unexpected happened, could you try typing again? Remember only with yes or no ")
    answer1 = input ("Do you would like to see our incredible menu? [yes/no] ").lower()

delivery_fee = 4.99
total_pizza_price = 0
pizza_count = 0
total_price = 0

if answer1 == "yes":

    possiblecontinue = "yes"
    while possiblecontinue == "yes":
        
        print("--------MENU--------")
        menu = ["1. Extra Cheese Pizza", "2. Sausage Pizza", "3. Pepperoni Pizza"]
        for pizza in menu:
            print(f"{pizza}")
        
        
        user_answer1 = int(input("If you´re interested please choose the pizza that you want using the numbers as reference "))
    
        while user_answer1 != 1 and user_answer1 != 2 and user_answer1 != 3:
            user_answer1 = int(input("Choose the pizza that you want using the numbers as reference "))
    
        match user_answer1:
            
            case 1:
                price = 14.99
                pizza_count += 1
                print(f"Extra Cheese Pizza Selected! {price} | Total of Pizzas Selected = {pizza_count}")
                total_price += price
                
                
            case 2:
                price = 12.99
                pizza_count += 1
                print(f"Sausage Pizza Selected! {price} | Total of Pizzas Selected = {pizza_count}")
                total_price += price
                
                
            case 3:
                price = 13.99
                pizza_count += 1
                print(f"Pepperoni Pizza Selected! {price} | Total of Pizzas Selected = {pizza_count}")
                total_price += price
                
                
            
                   
        possiblecontinue = input("Great, Do you would like of something else? [yes/no]")
        
    total_pizza_price += total_price + delivery_fee
       
    print("--------SUMMARY--------")
        
    print(f"Thank you for your order {name}! You can pay and ask any questions on our WhatsApp´number (63) 9294-0824")
        
    print(f"Name = {name}")
    print(f"Age = {age}")
    print(f"Total of Pizzas = {pizza_count}")
    print(f"Total Price = {total_pizza_price:.2f}")
    print(f"Delievery Fee = {delivery_fee}")
        
    print(" ⚠️  The Delievery Fee will keep the same doesn´t matter the location you are in Araguaina ⚠️")

    print("--------------------------------")    
    
    print("We hope to see you again on the Digital Danuza´s Pizza Website! ♥️")

elif answer1 == "no":
    print("No problem! We hope to see you again on the Digital Danuza´s Pizza  Website ♥️")
    
        
    
        
    