def calRealgas():
    Tc = 190.56
    Pc = 4.599 * pow(10,6)
    R = 8.314
    w = 0.008
    r = 1.3
    ac = 0.45724 * pow(R,2) * pow(Tc,2) / pow(Pc,2)
    b = bc = 0.07780 * R * Tc / Pc
    k = 0.37646 + 1.54226 * w - 0.26992 * pow(w,2)
    print("k=",k)
    Tr = 295
    print("Tr=",Tr)
    alT = pow((1+k*(1-pow(Tr,0.5))),2)
    aT = ac * alT
    
    v = 0.01
    T = 298
    P = 0.1 * pow(10,6)
    temp = R * T / (v-b) - aT / (v * (v+b) + b * (v - b))
    print("temp=",temp)
    while (abs(P - temp) > 100):
        # print("abs(P - temp)=",abs(P - temp))
        v += 0.000001
        temp = R * T / (v-b) - aT / (v * (v+b) + b * (v - b))
        # print("temp=",temp)

    print("v=",v)

calRealgas()