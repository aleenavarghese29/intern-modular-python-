class Intern:
    def __init__(self,name,domain):
        self.name=name
        self.domain=domain
    def introduce(self):
        print(f"Hi, I'm {self.name}")
        print(f"My domain is {self.domain}")    


intern=Intern("Aleena","Generative AI")        
intern.introduce()