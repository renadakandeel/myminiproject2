#this program is an apple inventory program that shows details of the product you want to purchase and gives you options
from appledevices import * #importing

start = True #starting 
print("Apple inventory\n------------------") 
#takes user's information
user=input("customer's name: ")
print("hello..", user,)
#making a list of devices
devices=['iPhone','iPad','MacBook']


while start: #loop
    #printing the list for the user to choose the purchase
    for i in range(len(devices)):
        print(f"{i+1} {devices[i]}") #starts at 1
    print("")
    #asking for input& storing it in a variable
    itemIndex = int(input('please select a device you want to purchase:'))
    #order item name
    orderItem = devices[itemIndex -1] #gets the order item
    print(orderItem)
    #comparing with if statements
    if orderItem=='iPhone':
        model = input("iphone X or 12?")
        if model.lower() != "x" or "12": #if not equal to any set a default choice
            model = "x"
        memory= input("64 or 128 GB of memory?")
        if memory != '64' or '128':
            memory = '64'
        sim = input("dual sim? enter True or False: ")
        if sim.lower() != "true" or "false": #boolean
            sim = "false"
        your_iPhone = iPhone(model, memory, sim, 0 ) #created new iphone
        print(your_iPhone)

    #ipad
    #comparing with if statements
    if orderItem=='iPad':
        model = input("iPad pro or max?")
        if model.lower() != "pro" or "12": #if not equal to any set a default choice
            model = "x"
        memory=input("64 or 128 GB of memory?")
        if memory != '64' or '128':
            memory = '64'
        pencil = input("would you like to purchase the pencil too? enter True or False: ")
        if pencil.lower() != "true" or "false": #boolean
            pencil = "false"
        your_iPad = iPad(model, memory, pencil,0) #created new ipad 
        print(your_iPad)

    #macbook
    #comparing with if statements
    if orderItem=='MacBook':
        model = input("MacBook AIR or PRO?")
        if model.lower() != "air" or "pro": #set default choice if not equal to
            model = "air"
        memory=input("128 or 512 GB of memory?")
        if memory != "512" or "128":
            memory = '128'
        your_MacBook = MacBook(model, memory,0) #created new macbook
        print(your_MacBook)
    
    proceed = input("would you like to purchase another item? yes or no? ") #prompts the user whether to try again or not
    if (proceed.lower() == "yes"):
        start= True #restarts the loop
    else:
        start = False #ends

    



