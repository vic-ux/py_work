import datetime

name = input ("What is your name? \n")
allowedUsers = ['Seyi','Mike','Love']

allowedPassword = ['passwordSeyi','passwordMike','passwordLove']

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
        balance = 0
        
        if (selectedOption == 1):
            withdraw = int(input ('How much would you like to withdraw? \n'))
            if balance < withdraw :
                print ("Insufficient Balance.")
            else:
                print('Take your cash.')
        
        elif (selectedOption == 2):
            deposit = int(input ('How much would you like to deposit? \n'))
            balance = balance + deposit
            print('Current Balance : % balance'. format(balance))
            
        elif (selectedOption == 3):
            complaint = input('What issue will you like to report? \n')
            print('Thank you for contacting us.')
        
        else:
            print ('Invalid Option selected, please try again.')
            
    
    else:
        print("Password Incorrect,please try again.")

else:
    print ("Name not found,please try again.")