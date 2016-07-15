from Model.Simulacija import Simulacija


class Editor():
    def __init__(self,sceneView):
        self.listaProjekata=[]
        self.sceneView=sceneView
        self.Simulacija=Simulacija(sceneView)

    def chanageActiveSimulation(self,Simulacija):
        self.Simulacija=Simulacija(self.sceneView);
        