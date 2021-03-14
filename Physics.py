import numpy
import matplotlib.pyplot as plt
#data = list of [[x1,y2],[x2,y2]]
class Varibles():
    def __init__(self,name,A=0,M=1):
        self.name = name
        self.addition= A
        self.Multiplication = M
    
class Math():  
    def __init__(self,eqn,goal):#eqn = string
        for i in range(len(eqn)):
            if eqn[i].isnumeric():
                try:
                    if eqn[i-1] == '+':
                        
        self.eqn =

    
    def find_inverse_F(self,eqn):  #y = [1 + 3x]
        left = 'y'
        eqn = eqn.split('+')
        for i in eqn:
            if 'x' in i:   
        









class Velocity:
    def __init__(self,V=None,s=None,t=None,a=None):
        self.velocity = V
        self.D_displacement = s
        self.D_time = t
        self.accleration = a
    def find_vel(self):
        if self.D_displacement != None and self.D_time != None:
            return round(self.D_displacement/self.D_time,2)
        elif self.accleration != None and self.D_time !=None:
            return round(self.accleration*self.D_time,2)
        else:
            return 'Not enough info'
    def find_s(self):
        return round(self.velocity*self.D_time,2)
    def find_acc(self):
        return round(self.velocity/self.time)

class Magnetic_flux:
    def __init__(self,Wb=None,A=None,B=None,t=0,n=1,emf =None):
        self.area = A
        self.magnetic_field = B
        self.flux = Wb
        self.tilda =t
        self.coils=n
        self.emf = emf
    def get_area(self):
        if self.area != None:
            return self.area
        else:
            return self.find_area()
    
    def get_MF(self):
        if self.magnetic_field != None:
            return self.magnetic_field
        else:
            return self.find_MF()

    def find_flux(self):
        self.flux= self.area*self.magnetic_field*numpy.cos(self.tilda)*self.coils
        return self.flux

    
def TD_graph(x,y):
    plt.plot(x,y)



def display():
    plt.show()


m = Magnetic_flux(A=100,B=10,n=1,t=0)
print(m.find_flux())