# Shopping Cart Project OPIM 243

import datetime

t = datetime.datetime.now()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

if __name__ == "__main__":

    # formatted_tax = "{0:.2f}".format(tax)
    # formatted_total = "{0:.2f}".format(total)

    products = [
        {
            "id":1, 
            "name": "Chocolate Sandwich Cookies", 
            "department": "snacks", 
            "aisle": "cookies cakes", 
            "price": 3.50
        },
        
        
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

    # for p in products:
        #  print(p)

    x = 1 # our counter variable

    #
    # INFO CAPTURE / INPUT
    #

    running_total = 0
    selected_ids = []

    print("Please type DONE when you are finished selecting products")

    while True:
            selected_id = input("Please input a product identifier: ")
            if selected_id == "DONE":
                    break
            else:
                    selected_ids.append(selected_id)
    # x = 1

    #
    # INFO DISPLAY / OUTPUT
    #

    # print(selected_ids)

    print("---------------------------")
    print("CHEN'S GROCERY")
    print("WWW.CHENS-GROCERY.COM")
    print("---------------------------")
    print("CHECKOUT AT: " + (t.strftime("%Y-%m-%d")) + " " + (t.strftime("%I:%M %p")))
    print("---------------------------")

    print("SELECTED PRODUCTS: ")

    for selected_id in selected_ids:
            matchings_products = [p for p in products if str(p["id"]) == str(selected_id)]
            product = matchings_products[0]
            running_total = running_total + product["price"]
            formatted_price = "{0:.2f}".format(product["price"])
            print("... " + product["name"] + " ($" + formatted_price + ")")

    tax = running_total * .06
    total = tax + running_total



    print("---------------------------")

    print("SUBTOTAL: $" + str(running_total))
    print("TAX: $" + to_usd(tax))
    print("TOTAL: $" + to_usd(total))

    print("---------------------------")
    print("THANKS, SEE YOU AGAIN SOON!")
