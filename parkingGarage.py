
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
        
        # times refused to pay
        times_refused = -1
        while True:
            times_refused += 1
            print('Please type $5 to pay your ticket!')
            pay = input().strip()
            if pay == "pay later":
                print("You have opted to pay later, please come again when ready to make payment")
                return
            
            if pay != "$5":
                print("You have entered the incorrect amount.")

                if times_refused >= 1:
                    print("You clearly can't be reasoned with, if you would like to speak to my manager, enter 'pay later', then call the manager'.callManager()' method")
                continue    
            
            
            print("Thank you for the payment! Leave garage with '.leaveGarage()' ")
            break
        
        self.visitors[visitor] = True

        # Add name to ticket list to store record of their paid ticket
        ticket_val = 5.0
        self.tickets.append((visitor,ticket_val)) 

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
    
    def moneyMade(self):
        total = 0
        for _,val in self.tickets:
            total += val
        print(total)
        return total
    
    def callManager(self,visitor:str):
        # Please explain why ypu have an issue with our pricing scheme.
        # print(hmmmm)
        # All other customers pay $5, we would appreciate it if you did to
        # does that work for you. Please enter "yes" if it does
        # if it does, do standard pay for ticket
        print("Ok, please explain why you have an issue with our pricing")
        issue = input()
        print("hmmmmmmmmmmmm")
        print("I hear you, but all other customers pay $5, we would appreciate it if you did to")
        print("does that work for you. If it does, please enter 'yes'")
        response = input().strip().lower()
        ticket_val = 5
        if response == "yes":
            print("Thank you for paying. Hope you have a good day. When you are ready, please leave with the '.leaveGarage()' method")
            self.visitors[visitor] = True
            self.tickets.append((visitor,ticket_val)) 
            return
        while ticket_val > 1:
            ticket_val -= 1
            print("Ok, I understand that the price can be considered a lot")
            print("Please explain why you think the price should be lower")
            issue = input()
            print("hmmmmmmmmmmmm")
            print(f"Ok. What if I made the price ${ticket_val}?")
            print("Enter 'yes' if you are ok with that price")
            response = input().strip().lower()
            if response == "yes":
                print("Thank you for paying. Hope you have a good day. When you are ready, please leave with the '.leaveGarage()' method")
                self.visitors[visitor] = True
                self.tickets.append((visitor,ticket_val)) 
                return

        print("ok, I give up, please just leave")
        self.visitors[visitor] = True
        self.tickets.append((visitor,0)) 
        return
            













        


my_garage = Garage(2)
my_garage.takeTicket("tommy")
my_garage.currentVisitors()
my_garage.takeTicket("mark")
# my_garage.payTicket('mark')
my_garage.callManager("mark")
my_garage.currentVisitors()
my_garage.moneyMade()