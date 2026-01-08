class Intern:
    def __init__(self,name,domain):
        self.name=name
        self.domain=domain
    def introduce(self):
        print(f"Hi, I'm {self.name}")
        print(f"My domain is {self.domain}")    


intern1=Intern("Aleena","Generative AI")   
intern2=Intern("Dilna", "Generative AI")     
intern1.introduce()
intern2.introduce()