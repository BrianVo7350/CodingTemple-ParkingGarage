
# # # Brainstorming area

# Assignment
# https://classroom.google.com/c/NTA4ODEzMzI2MDg2/a/NTA4ODEzMzI2MjQ3/details

# Parking Garage Class
    # Thing to track
        # Total Spaces
        # Occupied Spaces
        # Cost

    # Things we care about
    
    # Functions
        # Enter Garage
        
        # Pay ticket
        # Only can if ticket has been paid
        # Print current occupancy
        # CheckIfOpen
            # Visitor calls this
            # If opening get ticket

# When you 


# Sudo code

tickets = [0,1,2,3,4,5,6,7,8,9]

class Garage():
    def __init__(self,total_spaces:int):
        self.total_spaces = total_spaces
        self.open_spots = total_spaces
        self.visitors = dict()
        self.tickets = list()

    def currentVisitors(self):
        for visitor, payment_status in self.visitors.items():
            print(visitor, payment_status)
        return
    
    def takeTicket(self,visitor:str,show_text:bool=True):
        if self.open_spots == 0:
            print(f"Sorry {visitor}, no parking space-available")
            return
        
        if not isinstance(visitor,str) or not visitor:
            print("Visitor's name must be a non-empty string")
            return
        
        visitor = visitor.strip().lower()

        if visitor in self.visitors:
            print("Sorry, someone is already in here with that name, so we can't let you in. If you must come in, please use a nickname or add numbers to your name")
            return
        
        self.visitors[visitor] = False
        self.open_spots -= 1
        if show_text:
            print(f"Welcome to the garage {visitor}, enjoy your time!")
            print("Make sure to pay for your ticket with '.payTicket()' before you leave")
        return

    def payTicket(self, visitor:str):
        if not isinstance(visitor,str) or not visitor:
            print("Visitor's name must be a non-empty string")
            return

        visitor = visitor.strip().lower()
        if visitor not in self.visitors:
            print("Hey don't you need to pay! You are not in the garage!")
            return

        if self.visitors[visitor] == True:
            print("You have already paid. Feel free to leave whenever!")
            return

        while True:
            print('Please type $5 to pay your ticket!')
            pay = input().strip()
            if pay != "$5":
                print("You have entered the incorrect amount.")
                continue
            print("Thank you for the payment! Leave garage with '.leaveGarage()' ")
            break
        
        self.visitors[visitor] = True
        return

    def leaveGarage(self, visitor:str):
        if not isinstance(visitor,str) or not visitor:
            print("Visitor's name must be a non-empty string")
            return
        
        visitor = visitor.strip().lower()
        if visitor not in self.visitors:
            print("You never got a ticket how are you trying to leave?")
            return

        
        if self.visitors[visitor] == False:
            print("You have not payed yet please pay with '.payTicket()' ")
            return


        print(f"Thank you for visiting our garage {visitor} come again soon!")
        
        del self.visitors[visitor]
        self.open_spots += 1
        return





            


        


my_garage = Garage(2)
my_garage.takeTicket("tommy")
my_garage.currentVisitors()
my_garage.takeTicket("mark")
my_garage.currentVisitors()
my_garage.payTicket("mark")
my_garage.currentVisitors()
my_garage.leaveGarage("mark")
my_garage.currentVisitors()