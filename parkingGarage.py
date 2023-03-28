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
            print("There are no visitors.")
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
            print("Make sure to pay for your ticket with 'pay' command before you leave")
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
            print("Hey you don't need to pay! You are not in the garage!")
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
                    print("You clearly can't be reasoned with, if you would like to speak to my manager, enter 'pay later', then enter 'talk to manager")
                continue    
            
            
            print("Thank you for the payment! When ready, please leave with the 'leave' command ")
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
            print("You have not payed yet please pay with the 'pay' command")
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
        print("$"+str(int(total)))
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
        if visitor not in self.visitors:
            print("You are not currently in garage. Enter garage to talk to manager")
            return
        
        print("Ok, please explain why you have an issue with our pricing")
        issue = input()
        print("hmmmmmmmmmmmm")
        print("I hear you, but all other customers pay $5, we would appreciate it if you did to")
        print("does that work for you. If it does, please enter 'yes'")
        response = input().strip().lower()
        ticket_val = 5
        if response == "yes":
            print("Thank you for paying. Hope you have a good day. When you are ready, please leave with the 'leave' command")
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
                print("Thank you for paying. Hope you have a good day. When you are ready, please leave with the 'leave' command")
                self.visitors[visitor] = True
                self.tickets.append((visitor,ticket_val)) 
                return

        print("ok, I give up, please just leave")
        self.visitors[visitor] = True
        self.tickets.append((visitor,0)) 
        return

def create_garage():
    def print_instructions():
        print()
        print("'enter'")
        print("command to enter garage")
        print()
        print("'pay'")
        print("pay for ticket, must be done after entering")
        print()
        print("'leave'")
        print("leave garage")
        print()
        print("'commands'")
        print("repeats these commands")
        print()
        return
    
    
    print("Thanks for opening the garage!")
    while True:
        print("How many parking spots do you want in your garage?")
        spots = input()
        try:
            spots = int(spots)
        except:
            print("Please enter an integer above zero")
            continue

        if spots <= 0:
            print("Please enter an integer above zero")
            continue

        break

    garage = Garage(spots)
    print("Welcome to this garage")
    print("The following commands are ones for the general public....")
    print_instructions()

    print("enter any character to print the garage owner only commands")
    input()

    print("the following commands are just for the garage owner....")
    print()
    print("'list current visitors'")
    print("shows all current visitors in garage and their payment status")
    print()
    print("'revenue'")
    print("prints out total renvue made thus far")
    print()
    print("'shut down'")
    print("shuts down garage")
    print()
    print("Be aware, there is an option to speak to manager, but this is not advertised to guests unless needed")
    print()


    print("enter any character to print a bunch of empty lines and hide manager commands")
    input()
    for _ in range(50):
        print()
    
    while True:
        print()
        print("What would you like to do?")
        response = input().strip().lower()
        
        if response == "enter":
            print("What is your name?")
            name = input().strip().lower()
            garage.takeTicket(name)

        elif response == "pay":
            print("What is your name?")
            name = input().strip().lower()
            garage.payTicket(name)

        elif response == "leave":
            print("What is your name")
            name = input().strip().lower()
            garage.leaveGarage(name)

        elif response == "talk to manager":
            print("What is your name")
            name = input().strip().lower()
            garage.callManager(name)

        elif response == "list current visitors":
            garage.currentVisitors()
        
        elif response == "revenue":
            garage.moneyMade()

        elif response == "shut down":
            print("Garage is being shut down")
            break
        
        elif response == "commands":
            print_instructions()
        
        else:
            print("That was not a valid command. Please type 'commands' to see a list of valid commands")
        
    return


if __name__ == "__main__":
    create_garage()