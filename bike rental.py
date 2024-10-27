# 1 display available bikes
# 2 request a bike for rent (100 rs > 1qty)
# 3 exit

class bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("total bikes",self.stock)
    def rentforbike(self,q):

        if q<=0:
            print("enter the positive value or greater than zero")
        elif q>self.stock:
            print("enter the value (less than stock)")
        else:
            self.stock=self.stock-q
            print("total prices",q*100)
            print("total bikes",self.stock)

while True:
    obj=bikeshop(100)
    uc=int(input('''
    1 display stocks
    2 rent a bike
    3 exit
    '''))

    if uc==1:
        obj.displaybike()
    elif uc==2:
        n=int(input("enter the qty:--"))
        obj.rentforbike(n)
    else:
        break
