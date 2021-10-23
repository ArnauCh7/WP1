import math

gravity = 9.81
class Aircraft():
    def __init__(self, lista):
        self.name = lista[0]
        self.maxWeight = float(lista[1])
        self.minWeight = float(lista[2])
        self.refWeight = float(lista[3])
        self.maxPayload = float(lista[4])
        self.S = float(lista[5])
        self.cd1 = float(lista[6])
        self.cd2 = float(lista[7])
        self.cd3 = float(lista[8])
        self.cd4 = float(lista[9])
        self.cd5 = float(lista[10])
        self.cd6 = float(lista[11])
        self.ct1 = float(lista[12])
        self.ct2 = float(lista[13])*0.3048
        self.ct3 = float(lista[14])*(1/(0.3048**2))
        self.cf1 = float(lista[15])*(1/60000)
        self.cf2 = float(lista[16])*0.514444444

    def get_Cd0(self, h):
        if h >= 610:
            return self.cd5
        elif 457<= h <610:
            return self.cd3
        elif 0<= h <457:
            return self.cd1
        else:
            return None

    def get_Cd2(self, h):
        if h >= 610:
            return self.cd6
        elif 457<= h <610:
            return self.cd4
        elif 0<= h <457:
            return self.cd2
        else:
            return None

    def getCD(self, cd0, cd2, cl):
        Cd = cd0 + cd2 * (cl**2)
        return Cd
    
    def getCL(self, mass, h, v):
        p = self.getAirDensity(h)
        Cl = 2 * mass * 9.81 / (p * self.S * v ** 2)
        return Cl

    def getThrust(self, h):
        tmax = self.ct1*(1-(h/self.ct2)+(self.ct3 *h*h))
        return tmax

    def getAirDensity(self, h):
        if h > 11000:
            P = 226.32 * 10 ** 2 * math.e ** (-9.81 / (287.04 * 216.65) * (h - 11000))
        else:
            P = 1013 * 10 ** 2 * (1 - 0.0065 * h / 288.15) ** 5.2561

        T = 288.15 - 6.5 * h / 1000
        airDensity = P / (287.04 * T)
        return airDensity
    
    def getFuelFlow(cf1, cf2, v, T):
        n = cf1 * (1 + (v / cf2))
        FF = n * T
        return FF
    

    def getAOA(self, h, mass, v):
        thrust = self.getThrust(h)
        S = self.S
        density = self.getAirDensity(h)
        cd = self.getCD(h, mass, v)
        Drag = 0.5*density*(v**2)*cd*S
        num = (thrust-Drag)/(mass*gravity)
        angle = math.asin(num)
        return angle


    def VmaxROC(self, h, mass):
        thrust = self.getThrust(h)
        Cd0 = self.get_Cd0(h)
        Cd2 = self.get_Cd2(h)
        density = self.getAirDensity(h)
        Vmax = math.sqrt((thrust+math.sqrt(thrust**2+12*(mass**2)*(gravity**2)*Cd2*Cd0))/(3*density*self.S*Cd0))
        return Vmax

    def VAnglemax(self, h, mass):
        Cd0 = self.get_Cd0(h)
        Cd2 = self.get_Cd2(h)
        density = self.getAirDensity(h)
        Vmax =(((2*mass*gravity)/(density*self.S))**(1/2))*((Cd2/Cd0)**(1/4))
        return Vmax

    def getX(self, v, t, angle):
        Vx = v*math.cos(angle)
        x = Vx*t
        return x

    def getY(self, v, t, angle):
        Vy = v*math.sin(angle)
        y = 35 + Vy*t
        return y
