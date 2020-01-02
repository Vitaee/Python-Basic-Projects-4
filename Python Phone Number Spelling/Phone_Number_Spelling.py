# -*- coding: utf-8 -*-
"""

"""

# PHONE NUMBER SPELLİNG PROGRAM

Number_Dict={'0':'0','1':'1', '2':('A','B','C'), '3':('D','E','F'), \
             '4':('G','H','I'),'5':('J','K','L'),'6':('M','N','O'), \
             '7':('P','Q','R','S'),'8':('T','U','V'),'9':('W','X','Y','Z')}

PhoneNum_Last4Digits=input("Please enter the last four digits of your phone number: ")

while len(PhoneNum_Last4Digits) != 4:
    PhoneNum_Last4Digits=input("Please enter the last four digits of your phone number: ")

for i in Number_Dict[PhoneNum_Last4Digits[0]]:
    for j in Number_Dict[PhoneNum_Last4Digits[1]]:
        for k in Number_Dict[PhoneNum_Last4Digits[2]]:
            for l in Number_Dict[PhoneNum_Last4Digits[3]]:
                print(i+j+k+l)

