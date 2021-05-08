import pickle
import os

Clients = []
Pins = []
Balance = []
option = 0

while (option != 6) and (option != 2):
    if os.path.exists("clients.txt"):
        Clients=pickle.load(open("clients.txt","rb"))
        Pins = pickle.load(open("pins.txt","rb"))
        Balance=pickle.load(open("balance.txt","rb"))    
    
    print(Clients)
    print(Pins)
    print(Balance)
    option = int(input("<!------FARIDABAD BANK------------>\n\n1.Create Account\t2.Cash Withdrawal\n3.Cash Deposite\t\t4.Check Balance\n5.Delete Account\t6.Exit\n7.Show Accounts\nEnter : "))
    os.system('cls')
    

    if option == 1:
        name = input("Enter the name of client: ")
        pin = int(input("Enter the pin: "))
        if pin not in Pins:
            balance = float(input("Enter the amount: "))
        
            Clients.append(name)
            Pins.append(pin)
            Balance.append(balance)    

            
            pickle.dump(Clients,open('clients.txt','wb'))
            pickle.dump(Pins,open('pins.txt','wb'))
            pickle.dump(Balance,open('balance.txt','wb'))
            os.system('cls')
            print("Your Account has been Created!!")
        else:
            os.system('cls')
            print("Pin Already Exists")

        option = int(input("\n\n1.Back to Menu\t\t2.Exit\nEnter : "))
        os.system('cls')
    
    

    if option == 2:
        flag = 0
        pin = int(input("Please Enter Your Pin : "))
        os.system('cls')
        for i in range(0,len(Pins)):
            if pin == Pins[i]:
                amount = int(input("Enter the amount to Withdraw : "))
                os.system('cls')
                if amount <= Balance[i]: 
                    Balance[i] = Balance[i] - amount
                    print(f"Your money is Debited successfully !!!!\nYour current balance is : Rs {Balance[i]}")
                    pickle.dump(Balance,open("balance.txt","wb"))
                    flag=1
                    break
                else:
                    print("Insufficient Balance")
        if flag == 0:
            print("Wrong Pin")
        
        option = int(input("\n\n1.Back to Menu\t\t2.Exit\nEnter : "))
        os.system('cls')

    
    
    
    if option == 3:
        flag = 0
        pin = int(input("Please Enter Your Pin : "))
        os.system('cls')
        for i in range(0,len(Pins)):
            if pin == Pins[i]:
                amount = int(input("Enter the amount to Deposite : "))
                Balance[i] = Balance[i] + amount
                os.system('cls')
                print(f"Your money is Deposited successfully !!!!\nYour current balance is : Rs {Balance[i]}")
                pickle.dump(Balance,open("balance.txt","wb"))
                flag=1
                break
        if flag == 0:
            print("Wrong Pin")
        
        option = int(input("\n\n1.Back to Menu\t\t2.Exit\nEnter : "))
        os.system('cls')

    
    
    if option == 4:
        flag=0
        pin = int(input("Please Enter Your Pin : "))
        os.system('cls')
        for i in range(0,len(Pins)):
            if pin == Pins[i]:
                print(f"Your current balance is : Rs {Balance[i]}")
                flag=1
                break
        if flag == 0:
            print("Wrong Pin")
        
        option = int(input("\n\n1.Back to Menu\t\t2.Exit\nEnter : "))
        os.system('cls')

    
    
    if option == 5:
        flag = 0
        pin = int(input("Please Enter Your Pin : "))
        os.system('cls')
        for i in range(0,len(Pins)):
            if pin == Pins[i]:
                Clients.remove(Clients[i])
                Pins.remove(Pins[i])
                money=Balance[i]
                Balance.remove(Balance[i])
                pickle.dump(Clients,open('clients.txt','wb'))
                pickle.dump(Pins,open('pins.txt','wb'))
                pickle.dump(Balance,open('balance.txt','wb'))
                print(f"Your Account is Deleted successfully !!!!\nYour account had : Rs {money}\nYou can Take your money")
                flag = 1
                break

        if flag == 0:
            print("Wrong Pin")
        
        option = int(input("\n\n1.Back to Menu\t\t2.Exit\nEnter : "))
        os.system('cls')



    
    if option == 7:
        pasw = int(input("****(This is only for Bank Administration)*****\n---------------------------------------\nEnter the Admin Password: "))
        os.system('cls')
        if pasw == 12345:
            print("S.no\tCustomers\tBalance\t\tPin")
            print("---------------------------------------------")
            for i in range(0,len(Pins)):
                print(f"{i+1}\t{Clients[i]}\t\t{Balance[i]}\t\t{Pins[i]}")
            option = int(input("\n\n1.Back to Menu\t\t2.Exit\nEnter : "))
            os.system('cls')
        else:
            print("Incorrect Password")
            option = int(input("\n\n1.Back to Menu\t\t2.Exit\nEnter : "))
            os.system('cls')

print("------------------------\n\nThanks For Visiting FARIDABAD BANK!!!\n\n------------------------\n")




