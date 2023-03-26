class Garage():
    """
    Class to simulate a parking garage. When instantiating, one must provide
    the total number of spaces in parking garage.
    """
    
    def __init__(self,total_spaces:int):
        self.total_spaces = total_spaces
        self.open_spots = total_spaces
        self.visitors = dict()
        self.tickets = list()

    def currentVisitors(self):
        """
        Method to print out the current visitors and their payment status
        """
        if len(self.visitors) == 0:
            print("There are no visitors turning off systems.")
            return
        length = 7
        for visitor in self.visitors.keys(): 
            length = max(length, len(visitor))
        
        print("visitors".ljust(length, " ") + "   -   " + "paid ticket")
        print()

        for visitor, payment_status in self.visitors.items():
            x = visitor.ljust(length, " ") + "   -   " + str(payment_status)
            print(x)
        return

    def takeTicket(self,visitor:str,show_text:bool=True):
        """
        Method to add a visitor to the parking garage. One must provide the visitor's name
        when doing this. There is also an option to surpress the output text when a visitor
        successfully enters the garage
        """
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
        """
        Method to pay for a visitors parking ticket. One must provide the visitor's name. 
        This must be done prior to leaving garage.
        """
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
        """
        Method for vistor to leave garage. One must provide the visitor's name. 
        """
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
        """
        Method to print the amount of money made since instantiating the garage.
        """
        total = 0
        for _,val in self.tickets:
            total += val
        print(total)
        return total
    
    def callManager(self,visitor:str):
        """
        Method to talk to manager. Can be called when visitor has issue with price of
        parking ticket. Visitors name must be provided when calling method.
        """
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
