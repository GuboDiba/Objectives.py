class Account:
     type="KCB"
     def __init__(self,account_name,account_number,branch):
        self.account_name=account_name                    
        self.account_number = account_number
        self.branch = branch
        
     def bank_deposit(self,deposit):
         return(f"Dear {self.account_name} your deposit of {deposit} shilllings  to account number{self.account_number} {self.branch} branch is successful")
     
     def bank_withraw(self,withdraw):
         return(f"hello your withdraw {withdraw} from account {self.account_name} account number {self.account_number} {self.branch}")
     
     def display_balance(self,balance):
         return(f"Hello {self.account_name} your account balance is {balance} shillings")