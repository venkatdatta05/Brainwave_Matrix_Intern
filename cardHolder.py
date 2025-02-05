class cardHolder():
    def __init__(self, cardNumb, pin, firstname, lastname, balance):
        self.cardNumb = cardNumb
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance


    # get
    def get_cardNumb(self):
        return self.cardNumb
    def get_pin(self):
        return self.pin
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_balance(self):
        return self.balance
    
    #set
    def set_cardNumb(self, Newvalue):
        self.cardNumb = Newvalue
    def set_pin(self, Newvalue):
        self.pin = Newvalue
    def set_firstname(self, Newvalue):
        self.firstname = Newvalue
    def set_lastname(self, Newvalue):
        self.lastname = Newvalue
    def set_balance(self, Newvalue):
        self.balance = Newvalue
    