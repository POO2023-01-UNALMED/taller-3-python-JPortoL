class TV:
    numTV=0
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.precio = 500
        self.volumen = 1
        self.control = None
        TV.numTV += 1
#gets y sets
    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca
    
    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control
    
    def setPrecio(self, precio):
        self.precio = precio

    def getPrecio(self):
        return self.precio
    
    def setVolumen(self, volumen):
        if self.estado == True and 0 <= volumen <=7:
            self.volumen = volumen

    def getVolumen(self):
        return self.volumen
    
    def setCanal(self, canal):
        if self.estado == True and 0 <= canal <=7:
            self.canal = canal

    def getCanal(self):
        return self.canal

    def getNumTV(self):
        return self.numTV
    
    def setNumTV(self, numtv):
        self.numTV = numtv

    def setEstado(self, estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado
#metodos
    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False
    
    def canalUp(self):
        if self.canal < 120 and self.estado == True:
            self.canal += 1

    def canalDown(self):
        if self.canal > 0 and self.estado == True:
            self.canal -= 1

    def volumenUp(self):
        if self.volumen < 7 and self.estado == True:
            self.canal += 1

    def volumenDown(self):
        if self.volumen > 0 and self.estado == True:
            self.canal -= 1