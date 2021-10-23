import math
import matplotlib.pyplot as pyplot
import aircraft
print("start")

archivo = open("Data.txt")
aircraftList = []
Xmax = 350000
h = 35
line = archivo.readline()

while line != "":
    info = line.split(" ")
    if "\n" in info:
        info.remove("\n")
    avion = aircraft.Aircraft(info)
    aircraftList.append(avion)
    line = archivo.readline()
archivo.close()

def graphTime(aircraft, t):
    VRCaircraft = aircraft
    VAaircraft = aircraft

    XvectorRC = []
    YvectorRC = []

    XvectorMaxAngle = []
    YVectorMaxAngle = []

    YvectorRC.append(10)
    YVectorMaxAngle.append(10)
    XvectorRC.append(0)
    XvectorMaxAngle.append(0)

    VRC = [0]
    VMaxA = [0]
    i=0
    while i < len(t)-1:
        Tvrc = VRCaircraft.getThrust(YvectorROC[-1])
        Tva = VAaircraft.getThrust(YVectorMaxAngle[-1])

        if VRCaircraft.refWeight > VRCaircraft.minWeight:
            VRCaircraft.refWeight = VRCaircraft.refWeight - getFF(VRCaircraft.Cf1, VRCaircraft.Cf2, VRC[-1], Tvrc)
        if VAaircraft.refWeighteight > VAaircraft.minWeight:
            VAaircraft.refWeight = VAaircraft.refWeight - getFF(VAaircraft.Cf1, VAaircraft.Cf2, VMaxA[-1], Tva)
        
        vrc = VRCaircraft.VmaxROC(YvectorROC[-1], VRCaircraft.refWeight)
        vangle = VAaircraft.VAnglemax(YVectorMaxAngle[-1], VAaircraft.refWeight)

        ClVRC = VRCaircraft.getCL(VRCaircraft.refWeight, YvectorROC[-1], vrc)
        ClVA = VAaircraft.getCL(VAaircraft.refWeight, YVectorMaxAngle[-1], vangle)

        CdVRC = VRCaircraft.get_Cd0(YvectorROC[-1]) + VRCaircraft.get_Cd2(YvectorROC[-1]) * (ClVRC**2)
        CdVA = VAaircraft.get_Cd0(YVectorMaxAngle[-1]) + VAaircraft.get_Cd2(YVectorMaxAngle[-1]) * (ClVA**2)

        dragVRC = 0.5 * VRCaircraft.getAirDensity(YvectorROC[-1])*(vrc**2) * VRCaircraft.S * CdVRC
        dragVA = 0.5 * VAaircraft.getAirDensity(YVectorMaxAngle[-1])*(vangle**2) * VAaircraft.S * CdVA

        alphaVRC = ((Tvrc - dragVRC)/(VRCaircraft.refWeight*9.81))
        alphaVA = ((Tva - dragVA)/(VAaircraft.refWeight*9.81))

        xRC = XvectorRC[-1] + vrc * math.cos(alphaVRC)
        yRC = YvectorRC[-1] + vrc * math.cos(alphaVRC)

        xVA = XvectorMaxAngle[-1] + vangle * math.cos(alphaVA)
        yVA = YvectorMaxAngle[-1] + vangle * math.cos(alphaVA)

        XvectorRC.append(xRC)
        YvectorRC.append(yRC)
        XvectorMaxAngle.append(xVA)
        YVectorMaxAngle.append(yVA)

        VRC.append(vrc)
        VMaxA.append(vangle)

        i+= 1
    return XvectorRC, YvectorRC, XvectorMaxAngle, YVectorMaxAngle
















'''listXROC = []
listXAngle = []
listYROC = []
listYAngle = []

Xroc = 0
t = 0
for i in aircraftList:
    while Xroc < Xmax:
        vmaxAngle = i.VAnglemax(h, i.getMass(i.maxWeight, i.cf1, t))
        AoAAngle = i.getAOA(h, i.getMass(i.maxWeight, i.cf1, t), vmaxAngle)
        vmaxROC = i.VmaxROC(h, i.getMass(i.maxWeight, i.cf1, t))
        AoAROC = i.getAOA(h, i.getMass(i.maxWeight, i.cf1, t), vmaxROC)
        Xroc = i.getX(vmaxROC, t, AoAROC)
        XAngle = i.getX(vmaxAngle, t, AoAAngle)
        Yroc = i.getY(vmaxROC, t, AoAROC)
        YAngle = i.getY(vmaxAngle, t, AoAAngle)
        listXAngle.append(XAngle)
        listXROC.append(Xroc)
        listYAngle.append(YAngle)
        listYROC.append(Yroc)
        

        print(Xroc)
        
        t+=1

pyplot.plot(listXAngle, listYAngle)
pyplot.plot(listXROC, listYROC)
pyplot.show()
print("hola")'''


    