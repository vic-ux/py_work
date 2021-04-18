import datetime

import random
from random import randint
import time 


allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove']
print ("Register with a username and a password")
nameReg = input("Enter a username: \n")
passReg = input ("Enter a unique password: \n")
passReg2 = input("Re-enter your password: \n")

if nameReg in allowedUsers :
    print("Username already exist, try another username.")
else:
    allowedUsers.append(nameReg)
    if passReg == passReg2:
        allowedPassword.append(passReg)
        wait_time = random.randint(1,10)
        time.sleep(wait_time)
        print("Your registration was successful...")  
        print ("You can proceed to login.")  
        
    
        for i in range(4):
        
            name = input ("Enter your username? \n")
            
            if (name in allowedUsers):
                password = input("Enter your password? \n")
                userId = allowedUsers.index(name)
                if (password == allowedPassword[userId]):
                    print("Welcome %s"% name)
                    moment = datetime.datetime.now()
                    print(moment.strftime("%d-%b-%Y %I:%M:%S %p\n"))
                    
                    print ("These are the available options:\n")
                    print('1. Withdrawal')
                    print('2. Cash Deposit')
                    print('3. Complaint\n')
                        
                    selectedOption = int(input ('Please select an option: \n'))
                    if (selectedOption == 1):
                        withdraw = int(input ('How much would you like to withdraw? \n'))
                        print('Take your cash.')
                        break
                    
                    elif (selectedOption == 2):
                        deposit = int(input ('How much would you like to deposit? \n'))
                        print('Current Balance ...')
                        break
                        
                    elif (selectedOption == 3):
                        complaint = input('What issue will you like to report? \n')
                        print('Thank you for contacting us.')
                        break
                    
                    else:
                        print ('Invalid Option selected, please try again.')
                        
                
                else:
                    print("Password Incorrect,please try again.")

            else:
                print ("Name not found,please try again.")
        
    
        print("Wait for a few minutes, then retry login")    
            
    else:
        print ("password does not match.")