import time

while True:
    print(' __________________________________')
    print('|                                  |')
    print('|         Welcome to ATM           |')
    print('|                                  |')
    print('|__________________________________|')

    print('')
    print('            1. English')
    print('            2. Tamil')
    print('            3. Hindi')
    print('')


    password=12345
    balance=10000.00
    get=int(input('     Select your language....'))
    time.sleep(2)

    if get==1:
        print('')
        print('')
        print('            1. Current')
        print('            2. Savings')
        print('')
        print('')
        entry1=int(input('.....Please select the account type.....'))
        time.sleep(2)
        print('')
        print('')
        if entry1==1 or  entry1==2:
            print('')
            print('')
            print('            1. Depost')
            print('            2. Withdraw')
            print('            3. Balance')
            print('')
            print('')
        
            entry2=int(input('.....Please enter your choice.....'))
            time.sleep(0)
            print('')
            print('')
            if entry2==1:
                print('     You have selected deposit....')
                time.sleep(2)
                print('')
                print('')
                print('     Please deposit the cash inside the slot...')
                time.sleep(2)
                print('')
                print('')
                print('     Please wait validating your cash')
                time.sleep(5)
                print('')
                print('')
                deposit=int(input('.....Check and enter the deposit amount.....'))
                deposit_bal=balance+deposit
                print('')
                print('')
            
            
                print('     Your current balance is',deposit_bal)
                print('')
                print('')
                print('     Thank you for using our ATM..........')
                time.sleep(7)
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
                print('')
            
            elif entry2==2:
                print('')
                print('')
                print('     You have selected withdrawal..')
                print('')
                print('')
                time.sleep(2)
                entry3=int(input('.....Enter the amount:  '))
                with_amt=balance-entry3
                time.sleep(2)
                print('')
                print('')
                print('     Take your cash....')
                print('')
                time.sleep(2)
                print('')
                print('   Your current balance is ',with_amt)
                
                print('')
                print('')
                print('     Thank you for using our ATM....')
                print('')
                print('')
                time.sleep(7)
                
            elif entry2==3:
                time.sleep(2)
                print('')
                print('')
                print('     Your current balance is ',balanace)
                print('')
                print('')
                print('     Thank you for using our ATM...')
                print('')
                print('')
                time.sleep(5)
            else:
                print('')
                print('')
                print('     Invalid entry...')
                print('')
                print('')
                
        
        
        else:
            print('     INVALID ENTRY..')
        
    elif get==2:
        print('')
        print('')
        print('     Currently unavailable. Please choose English language...')
        print('')
        print('')
        print('')
        print('')
        print('')
        time.sleep(3)
        
    elif get==3:
        print('')
        print('')
        print('     Currently unavailable. Please choose English language...')
        print('')
        print('')
        print('')
        print('')
        print('')
        time.sleep(3)
        

    else:
        print('')
        print('')
        print('')
        print('     INCORRECT ENTRY....')
        print('')
        print('')
        print('')
                