import math

class aircraft():
    def __init__(self, maxWeight, minWeight, refWeight, maxPayload, S, cd1, cd2, cd3, cd4, cd5, cd6, ct1, ct2, ct3, cf1, cf2):
        self.maxWeight = maxWeight
        self.minWeight = minWeight
        self.refWeight = refWeight
        self.maxPayload = maxPayload
        self.S = S
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd4 = cd4
        self.cd5 = cd5
        self.cd6 = cd6
        self.ct1 = ct1
        self.ct2 = ct2
        self.ct3 = ct3
        self.cf1 = cf1
        self.cf2 = cf2

def get_Cd0(h):
    if h >= 610:
        return aircraft.cd5
    elif 457<= h <610:
        return aircraft.cd3
    elif 0<= h <457:
        return aircraft.cd1
    else:
        return None

def get_Cd2(h):
    if h >= 610:
        return aircraft.cd6
    elif 457<= h <610:
        return aircraft.cd4
    elif 0<= h <457:
        return aircraft.cd2
    else:
        return None

def getThrust(h):
    tmax = aircraft.ct1*(1-(h/aircraft.ct2)+aircraft.ct3 * (h**2))
    return tmax

def getAirDensity(h):
    airDensity = 1.225*math.e**(-0.09543718*(h/1000)-0.001321598*(h/1000)**2)
    return airDensity    