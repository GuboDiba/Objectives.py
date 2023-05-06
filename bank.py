class Account:
     type="KCB"
     def __init__(self,account_name,account_number,branch):
        self.account_name=account_name                    
        self.account_number = account_number
        self.branch = branch
        
     def bank_deposit(self):
         return(f"Dear {self.account_name} your deposit to account number{self.account_number} {self.branch} branch is successful")
     
k    def bank_withraw(self):
         return(f"")
     
     def display_balance(self):
         return(f"")