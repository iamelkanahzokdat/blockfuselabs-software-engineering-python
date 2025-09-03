class RegForm:
    amount_expected_to_be_paid = 50_000
#    # constructor
#    # self = joseph
#    # firstname = joe
#    def __init__(self, firstname):
#       self.first = firstname
#       # joseph.first = joe
#       self.first = firstname
    def __init__(self, firstname, lastname, address, amount):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.amount_to_be_paid_by_student = amount
    
    def welcome(self):
        return f"welcome to blockfuse labs! {self.firstname} {self.lastname}"

    def details(self):
        return f"firstname:{self.firstname}\nlastname:{self.lastname}\naddress:{self.address}\namount_to_be_paid_by_student:{self.amount_to_be_paid_by_student}"

    def balance(self):
        return  self.amount_expected_to_be_paid - self.amount_to_be_paid_by_student

    def balance_checker(self):
        if self.balance() == 0:
           return f"your have completed your payment, you have {self.balance()}"
        
        else:
           return f"{self.balance()} is remaining, pay up!"


joseph = RegForm("joe", "Abu", "jos", 30_000)
dorcas = RegForm("dorcas", "tanimu", "Bauchi", 50_000)

print(joseph.welcome())
print(dorcas.welcome())
print(joseph.details())
print(dorcas.details())
print(joseph.balance())
print(dorcas.balance())
print(joseph.balance_checker())
print(dorcas.balance_checker())