class Human :
    def __init__(self,name,occupation) :
        self.name=name
        self.occupation=occupation

    def do_work(self):
        if self.occupation== "actor":
            print(self.name,"shoots a film")
        elif self.occupation== "tennis player":
            print(self.name,"plays tennis")

    def speak(self):
        print(self.name,"says hello")


# tom=Human("tom","actor")
# tom.do_work()
# tom.speak()

alina=Human("Alina","tennis player")
alina.do_work()
alina.speak()
