from enums import *
from can_container import CanContainer


class VendingMachine:
    def __init__(self):
        self.cans = {}
        self.payment_method = None

    def set_value(self, value):
        self.payment_method = 1
        if hasattr(self, 'coins'):
            self.coins += value
        else:
            self.coins = value

    def insert_chip(self, chipknip):
        # TODO
        # can't pay with chip in brittain
        self.payment_method = 2
        self.chipknip = chipknip

    # delivers the can if all ok
    def deliver(self, choice):
        result = None
        #
        #step 1: check if choice exists
        #
        if choice in self.cans:
            #
            # step2 : check price
            #
            if self.cans[choice].price == 0 :
                result = self.cans[choice].type
            # or price matches
            else:
                if self.payment_method == 1: # paying with coins
                    if self.coins != None and self.cans[choice].price <= self.coins:
                        result = self.cans[choice].type
                        self.coins -= self.cans[choice].price

                elif self.payment_method == 2: # paying with chipknip - 
                    # TODO: if this machine is in belgium this must be an error
                    if (self.chipknip.has_value(self.cans[choice].price)):
                        self.chipknip.reduce(self.cans[choice].price)
                        result = self.cans[choice].type

                else:
                    # TODO: Is this a valid situation?:
                    #  larry forgot the else: clause 
                    #  i added it, but i am acutally not sure as to wether this is a problem
                    #  unknown payment
                    pass # i think(i) nobody inserted anything
        else:
            result = Can.none
        #
        # step 3: check stock
        #
        if (result and result != Can.none):
            if (self.cans[choice].amount <= 0):
                result = Can.none
            else:
                self.cans[choice].amount -= 1
        #
        # if can is set then return
        # otherwise we need to return the none
        if (result is None):
            return Can.none
        return result

    def get_change(self):
        to_return = 0
        if (self.coins > 0):
            to_return = self.coins
            self.coins = 0
        return to_return

    def configure(self, choice, can_type, amount, price=0):
        self.price = price
        if (choice in self.cans):
            self.cans[choice].amount += amount
            return

        can = CanContainer()
        can.type = can_type
        can.amount = amount
        can.price = price
        self.cans[choice] = can
