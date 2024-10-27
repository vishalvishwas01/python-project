class Reservation:
    def __init__(self):
        self.LB = 0
        self.UB = 1
        self.SL = 1
        self.SU = 1
        self.MB = 1

    def preferences(self, name, gender, age, preference):
        self.name = name
        self.gender = gender
        self.age = age
        self.preference = preference

    def allotment(self):
        name = input("Enter the passenger name: ")
        gender = input("Enter the passenger gender (M/F): ")
        age = int(input("Enter the passenger age: "))
        preference = input("Enter the preferred berth (LB, UB, SL, SU, MB): ")

        # Gender validation
        if gender not in ["M", "F"]:
            print("Invalid gender")
            return

        # Age validation
        if not (15 <= age <= 100):
            print("Please enter an age between 15 and 100.")
            return

        # Berth preference handling
        if gender == "F" and preference == "LB" and self.LB > 0:
            print(f"{name}, you are allotted a Lower Berth.")
            self.LB -= 1
        elif preference == "UB" and self.UB > 0:
            print(f"{name}, you are allotted an Upper Berth.")
            self.UB -= 1
        elif preference == "SL" and self.SL > 0:
            print(f"{name}, you are allotted a Side Lower Berth.")
            self.SL -= 1
        elif preference == "SU" and self.SU > 0:
            print(f"{name}, you are allotted a Side Upper Berth.")
            self.SU -= 1
        elif preference == "MB" and self.MB > 0:
            print(f"{name}, you are allotted a Middle Berth.")
            self.MB -= 1
        else:
            print(f"Sorry {name}, your preferred berth is not available. Allotting available berth.")
            if self.LB > 0:
                print(f"You are allotted a Lower Berth.")
                self.LB -= 1
            elif self.UB > 0:
                print(f"You are allotted an Upper Berth.")
                self.UB -= 1
            elif self.SL > 0:
                print(f"You are allotted a Side Lower Berth.")
                self.SL -= 1
            elif self.SU > 0:
                print(f"You are allotted a Side Upper Berth.")
                self.SU -= 1
            elif self.MB > 0:
                print(f"You are allotted a Middle Berth.")
                self.MB -= 1
            else:
                print("Sorry, no berths available.")


#Create an instance of the Reservation class and call the methods
r = Reservation()
r.allotment()
