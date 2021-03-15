import Dictionary
import numpy as np
class  DNA:
    def __init__(self,data,Value):
        self.data = data
        self.data['Value'] =Value
    def step_up(self):
        return self.data['Step up']
    def step_down(self):
        return self.data['Step down']
    def get_up(self):
        return self.data['Up']
    def get_down(self):
        return self.data['Down']
    def get_value(self):
        return float(self.data['Value'])
    def get_units(self):
        return self.data['Word']

    def display(self):
        print(self.data['Value'])
        print(self.data['Units'])
        print(self.data['Measures'])
        print(self.data['Step up'])
class Physic_Dic(Dictionary.Dictionary):

    def __int__(self):
        super().__init__()
    
                
    def delete_collection(self):
        self.collection.drop()
    def restart(self):
        self.delete_collection()
        file = open('C:/Users/Chua Wei Yang/Desktop/Project/Ouroborus/unitss.txt','r')
        for line in file:
            if line !='\n':
                line = line.strip()
                line = line.split(',')
                add ={}
                for i in line:
                    field, data = i.split(':')
                    try: 
                        add[field] = float(data)
                    except:
                        add[field] = data
                
                self.collection.insert_one(add)
class Classic_mechanics:
    def __init__(self):
        self.gravity = -9.80665
        self.Variables = {}
        self.Dictionary = Physic_Dic('Dictionary','Physics')
    def read(self,text):
        sentence = text.split(' ')
        flag = False
        for index,word in enumerate(sentence):
            
            
            temp = self.Dictionary.collection.find_one({'Word':word},{'Catagory':1,'Query':1})
            if temp ==None:
                pass
            elif temp['Catagory'] == 'term' and flag ==True:
                
                print(self.query(temp['Query']))
            elif temp['Catagory'] == 'unit':
                self.add_data(sentence[index - 1] + ' ' + word)
            elif temp['Catagory'] == 'query':
                flag =True 
    def display(self):
        for i in self.Variables:
            print(i,':',self.Variables[i].get_value(),self.Variables[i].get_units()) 
    def create_obj(self,data):
        
        value , unit = data.split(' ')

        if self.Dictionary.Exist(unit):
            doc = self.Dictionary.collection.find_one({'Word':unit},{'_id':0})

            d = DNA(doc,value)
        else:
            print('obj error')
        return d       
    def add_data(self,data,special=None): # data =  e.g 10 m,100 cm,0.1 km, 
        obj = self.create_obj(data)
        key = obj.data['Measures']
        
        while key in self.Variables:
            key +='I'
        if special != None:
            self.Variables[special] =obj
        else:
            self.Variables[key] = obj
        

    def query(self,key):
        func = getattr(self,'get_'+key)
        return func()
    def check(self,func):
        test = getattr(self,'get_'+func)()
        print(test)
        test = float(test.split(' ')[0])
        if self.Variables['time'].get_value() == test:
            return True
        else:
            return False
    def get_area(self):
        
        try:
            result = str(self.Variables['length'].get_value()*self.Variables['lengthI'].get_value())+' '+self.Variables['length'].get_units()+'^2'
            return result
        except:
            print('Area Erreor')
    def STEP_UP(self,obj):
        new =  obj.get_value()/ obj.step_up()
        new_obj = self.create_obj(str(new) +' '+obj.get_up())
        return new_obj

    def STEP_DOWN(self,obj):
        new = obj.get_value() * obj.step_down()
        new_obj = self.create_obj(str(new)+' '+obj.get_down())
        return new_obj
    def get_pressure(self):
        if 'area'  not in self.Variables:
            self.add_data(self.get_area())
        
        if 'force' not in self.Variables:
            self.add_data(self.get_force())
            
        area = self.Variables['area']
        force = self.Variables['force']
        while area.get_units() != 'm^2':
            area = self.STEP_UP(area)
        
        try:
            result = str(force.get_value() / area.get_value()) +' '+'Pa'
            return result
        except:
            print(' pressure Error')
    def get_mass(self):  
        if 'volume' not in self.Variables:
            self.add_data(self.get_volume)     
        volume = self.Variables['volume'] 
        density = self.Variables['density']

        try:
            return str(volume.get_value() * density.get_value()) + ' g'
        except:
            print('Get_mass error')
    
    def get_velocity(self):
        time  = self.Variables['time']
        distance = self.Variables['length']
        while time.get_units() !='s':
            time  = self.STEP_DOWN(time)
        try:
            return str(distance.get_value()/ time.get_value())+' m/s'
        except:
            print('velocity area')
    def get_power(self):
        energy = self.Variables['energy']
        time = self.Variables['time']
        while time.get_units() != 's':
            time = self.STEP_DOWN(time)
        try:
            return str(energy.get_value()/time.get_value()) + ' W'
        except:
            print('power erroe')
    def get_accleration(self):
        if 'velocity' not in self.Variables:
            self.add_data(self.get_velocity)
        
        time = self.Variables['time']
        velocity_1 = self.Variables['Velocity']
        velocity_2 = self.Variables['VelocityI']
        try :
            
            average_v = velocity_2.get_value() - velocity_1.get_value()
            return str(average_v/time.get_value()) + ' m/s^2'
        except:
            print('Accelration error')
    def get_force(self):
        if 'mass'  not in self.Variables:
            self.add_data(self.get_mass())
        
        if 'accleration' not in self.Variables:
            self.add_data(self.get_accleration())
                    
        mass = self.Variables['mass']
        accel = self.Variables['accleration']
        try:
            return str(mass.get_value() * accel.get_value()) + ' N'
        except:
            print('Force error')
    def get_heat_capacity(self):
        if 'power' not in self.Variables:
            self.add_data(self.get_power())
        power = self.Variables['power']
        time = self.Variables['time']
        mass = self.Variables['mass']
        temp_1 = self.Variables['temperature']
        temp_2 = self.Variables['temperatureI']
        while time.get_units() !='s':
            time  = self.STEP_DOWN(time) 
        while mass.get_units() != 'g':
            mass = self.STEP_DOWN(mass)
        temp_change = temp_2.get_value() - temp_1.get_value()
        return str((power.get_value()*time.get_value())/(mass.get_value()*temp_change)) +' J/C'
    def get_trajectory_distance(self):
        if 'time' not in self.Variables:
            self.add_data(self.get_time_trajectory())
        if 'x_velocity' not in self.Variables:
            self.get_xy_velocity()
        time = self.Variables['time']
        x_velocity = self.Variables['x_velocity']
        
        try:
            return str(time.get_value()*x_velocity.get_value()) +' m'
        except:
            print('trajectory  error')
    def get_xy_velocity(self):
        if 'velocity' not in self.Variables:
            self.add_data(self.get_velocity())
        velocity =self.Variables['velocity']
        angle = self.Variables['angle']
        try :
            self.add_data(str(velocity.get_value()*np.cos(angle.get_value()*np.pi/180))+' m/s','x_velocity')
            self.add_data(str(velocity.get_value()*np.sin(angle.get_value()*np.pi/180))+' m/s','y_velocity')
        except:
            print('xy error')
    def get_trajectory_time(self):
        if 'y_velocity' not in self.Variables:
            self.get_xy_velocity()
        velocity = self.Variables['y_velocity']
        
        try:
            return  str(2*(velocity.get_value())/(-self.gravity)) +' s' 
        except:
            print('time trajectory')
    def get_trajectory_angle(self):
        distance= self.Variables['length']
        velocity = self.Variables['velocity']
        temp = (-self.gravity)*distance.get_value()/velocity.get_value()**2
        
        try:
            return str(0.5*(np.arcsin(temp)*180/np.pi)) + ' degree'
        except:
            print('angle error')
    def get_trajectory_velocity(self):
        if 'time' not in self.Variables:
            self.add_data(self.get_trajectory_time())
        if 'anlge' not in self.Variables:
            self.add_data(self.get_trajectory_angle())
        angle = self.Variables['angle']
        time = self.Variables['time']

        try:
            
            return str(0.5*(-self.gravity)*time.get_value()**2/time.get_value()/np.sin(angle.get_value()*np.pi/180)) +' m/s'


        except:
            print('tra velocity ')
    def get_trajectory_height(self):
        if 'time' not in self.Variables:
            self.add_data(self.get_trajectory_time())
        if 'y_velocity' not in self.Variables:
            self.get_xy_velocity()
        time = self.Variables['time']
        y_velocity = self.Variables['y_velocity']

        while time.get_units() != 's':
            time = self.STEP_DOWN(time)
        try:
            return str(y_velocity.get_value()*(time.get_value()/2) + 0.5*self.gravity*(time.get_value()/2)**2) +' m'
        except:
            print('trajectory height error')

if __name__ == '__main__':  
    Sim = Classic_mechanics()
    Sim.Dictionary.restart()
    #Sim.read('An object is launched at a velocity of 20 m/s in a direction making an angle of 25 degree upward with the horizontal. What is the maximum height reached by the object?')
    Sim.read('A ball kicked from ground level at an initial velocity of 60 m/s and an angle θ with ground reaches a horizontal distance of 200 m . What is the size of angle θ?')