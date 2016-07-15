

class Projekat():
    def __init__(self):
        self.imeProjekta="Novi projekat1"
        self.br_simulacija=0
        self.ListaSimulacija=[]
    def dodavanjeNoveSimulacije(self,Simulacija):
        self.br_simulacija+=1
        self.ListaSimulacija.append(Simulacija)
    def brisanjeSimulacije(self,Simulacija):
        self.br_simulacija-=1
        index = self.ListaSimulacija.index(Simulacija)
        self.ListaSimulacija.pop(index)
    def snimiSveSimulacije(self):
        pass
    def snimanjeProjekta(self):
        pass
    