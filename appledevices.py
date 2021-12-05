#base class 
class apple():
    def __init__(self,model_name,memory,price):
        self.model_name=model_name
        self.memory=memory
        self.price=0
#inherited classes
class iPad (apple):
    def __init__(self, model_name, memory,pencil,price): #parameters
        super().__init__(model_name, memory,price)
        self.pencil=pencil

    def get_price(self): 
        self.price = 1500 #minimum price
        if(self.model_name.lower() == "max"): #inc price depending on choices
            self.price += 200
        if(self.memory == '128'):
            self.price += 200
        if(self.pencil == True):
            self.price += 150
        return self.price
    def __str__(self) -> str: #returns the description
        return f"This Item costs ${self.get_price()}, Details - MacBook{self.model_name}','{self.memory}GB','contains a pencil {self.pencil}'\n' 'thank you for your purchase!'"


#inherits from base class
class iPhone (apple):
    def __init__(self, model_name, memory,dual_sim,price): #parameters
        super().__init__(model_name, memory,price)
        self.dual_sim=dual_sim
    
    def get_price(self):
        self.price = 800 #minimum price
        if(self.model_name.lower() == "12"):
            self.price += 99 #inc price depending on choices
        if(self.memory == '256'):
            self.price += 50
        if(self.dual_sim == True):
            self.price += 50
        return self.price
#returns the description
    def __str__(self) -> str:
        return f"This Item costs ${self.get_price()}, Details - iPhone{self.model_name}',' '{self.memory}GB'','' contains dual_sim {self.dual_sim}'\n thank you for your purchase!'"

class MacBook (apple): #inherits from base class
    def __init__(self, model_name, memory,price): #parameters
        super().__init__(model_name, memory,price)

    def get_price(self):
        self.price = 2000 #minimum price
        if(self.model_name.lower() == "pro"):
            self.price += 200 #inc price depending on choices
        if(self.memory == '512'):
            self.price += 100
        return self.price
#returns the description
    def __str__(self) -> str:
        return f"This Item costs ${self.get_price()}, Details - MacBook{self.model_name}','{self.memory}GB'\n thank you for your purchase!'"



    
        
        

        

   

