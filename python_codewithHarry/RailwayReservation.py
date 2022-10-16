#Railway Reservation Booking in Python
pass
class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats =seats

    def getStatus(self):
        print("...............")
        print(f"The name of train is {self.name}")
        print(f"the seats available in the train are {self.seats}")
        print("...........")

    def fareinfo(self):
        print(f"The price of the ticket is : Rs{self.fare}")

    def bookTicket(self):
        if(self.seats>0):

            print(f"{y}your ticket has been booked !!!!!! your seat number is : {self.seats}")
            self.seats -=1
        else:
            print("Sorry this train is full !! No seats are available")

    def cancelTicket(self, seatNO):
        pass

intercity = Train("Intercity Express : 14520", 90,2)
intercity.getStatus()
