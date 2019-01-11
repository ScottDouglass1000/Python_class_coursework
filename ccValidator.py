# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:35:30 2019

@author: sdono
"""
#CC Validator Question

class CreditCard():
    def __init__(self,card_number):
       self.card_number = card_number
       self.card_length = self.card_length_meth()
       self.card_type = self.card_type_meth()
       self.card_valid = self.card_valid()

    def card_length_meth(self):
       card_length = len(self.card_number)
       if card_length == 15 or card_length == 16:
           self.card_length = True
       else:
           self.card_length = False
       return self.card_length

    def card_type_meth(self):
       if self.card_length == True:
           if self.card_number[0:2] in ["51","52","53","54","55"]:
               self.card_type = "Mastercard"
           elif self.card_number[0] == "4":
               self.card_type = "Visa"
           elif self.card_number[0:2] == "37" or self.card.type == "34":
               self.card_type = "Amex"
           elif self.card_number[0:5] == "6011":
               self.card_type = "Discover"
           else:
               self.card_type = False
           return self.card_type

    def card_valid(self):
        c = self.card_number[-2::-2]
        doubled_list = []
        result_list = []
        other_numbers_list = []
        for i in c:
            doubled_list.append(int(i)*2)        
        for i in doubled_list:
            if i > 9:
                i = i - 9
                result_list.append(i)
            else:
                result_list.append(i)
        c2 = self.card_number[-1::-2] 
        for i in c2:
            other_numbers_list.append(int(i))
        total = (sum(result_list)+sum(other_numbers_list))%10
        if total == 0:
            self.card_valid = True
        return self.card_valid

mc = CreditCard('5515460934365316')
# mc is a valid card number
print("true means card is of proper length: ", mc.card_length)
print(mc.card_type)
print("true if the number passes parity check: ", mc.card_valid)