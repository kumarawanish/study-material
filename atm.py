class Atm:
    def __init__(self):
        self.balance = 0
        self.user_dict = {}
    
    def menu(self):
        flag = True
        while flag:
            user_input = input('''
             hello, How would like to proceed?
             1.Enter 1 to create pin
             2.Enter 2 to deposit the amount
             3.Enter 3 to check the balance
             4.Enter 4 to withdraw the amount
             5.Enter 5 to cancel 

            ''')
            
            auth = self.authenticate()
            
            if user_input == "1":
                self.createpin()
                
            if auth:
                if user_input == "2":
                    self.deposit()
                elif user_input == "3":
                    self.check_balance()

            elif user_input == "5":
                flag = False
                
    def authenticate(self):
        user = input("Enter Username")
        pin = input("Enter Pin")
        
        if user in self.user_dict and self.user_dict[user] == pin:
            return True
        return False
        
    def withdrawMoney(self):
        pass
    
    def createpin(self):
        user = input("Enter Username")
        pin = input("Enter the pin")
        self.user_dict[user] = pin
        
        print("Pin created successfully")
    
    def deposit(self):
        
        amount = int(input("Enter the amout..."))
        self.balance += amount
        self.menu()
        
    def check_balance(self):
            print("+"*50)
            print("Total Amount: ",self.balance)
            print("+"*50)
            
            
a = Atm()
a.menu()