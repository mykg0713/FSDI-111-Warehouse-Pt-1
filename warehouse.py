from menu import print_menu
from item import Item
import datetime
import pickle
import os

logs = []
items = []
id_count = 1
items_file = "item.data"
logs_file = "logs.data"

def clear() :
    return os.system("cls")

def get_time():
    current_date = datetime.datetime.now()
    Lime = current_date.strftime("%X")
    return get_time

def save_items():
    #open creates/open a file
    #wb = write binary info
    writer = open(items_file, "wb")
    #converts theobject into binary and writes it on the file
    pickle.dum(items,writer)
    writer.close() # closes the file stream (to release the file)
    print(" Data saved!!")

def save_log():
    # open creates/open a file
    # wb = write binary info
    writer = open(logs_file, "wb")
    #converts the object into binary and writes it on the file
    pickle.dump(logs, writer)
    writer.close() #closes the file stream (to release the file)
    print(" Log saved!!")

def read_log():
    try:
        reader = open(logs_file, "rb") #rb = open the file to read binary
        #read the binary and convert it to the original object
        temp_list = pickle.load(reader)

        for log in temp_list:
            logs.append(log)

        print(" Loaded: " + str(len(temp_list)) + " log events")

    except:
        #you get here if try block crashes
        print( " *Error: Data could not be loaded!")

def print_header(text):
    print("\n\n")
    print("*" * 40)
    print(text)
    print("*" * 40)

def print_all(header_text):
    print_header(header_text)
    print("-" * 70)
    print("ID  | Item Title        |  Category       | Price   | Stock")

    for item in items:
        print(str(item.id).ljust(3) + " | " + item.title.ljust(25) + " | " + item.category.ljust(15) +
            " | " + str(item.price).rjust(9) + " | " + str(item.stock).rjust(5))

def register_item():
    global id_count #importing the global variable, into fn scope

    print_header(" Register new Item")
    title = input ("Please input the Title")
    category = input("Please input the Category: ")
    price = float(input("Please input the Price: "))
    stock = int(input("Please input the Stock: "))

    #validations

    new_item = Item()
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock

    id_count += 1
    items.append(new_item)
    print(" Item Created!!!")

def update_stock():
    #show the user all the items
    #ask for the desired id
    #get the element from the array with that id
    #ask for the new stock
    #update the sock of the element
    #print_all("Choose an Item from the list")
    id = input("\nSelect an ID to update its stock: ")
    # find the element
    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("Please input new stock value:  ")
            item.stock = int(stock)
            found = True

            #add registry to the log
            log_line = get_time() + " | Update | " + id
            logs.append(log_line)
            save_log()

        if(not found):
            print("*** Error: ID doesn't exist, try again")

