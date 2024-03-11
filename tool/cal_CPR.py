r_H2 = 1.4
r_CH4 = 1.3
M_H2 = 2
M_CH4 = 16

doping_ratios = [0.1,0.2,0.3]
Ms = []

def cal(H2 : float,CH4 : float,doping_ratio : float)->float:
    return H2 * doping_ratio + CH4 * (1-doping_ratio)

for doping_ratio in doping_ratios:
    r = cal(r_H2,r_CH4,doping_ratio)
    M = cal(M_H2,M_CH4,doping_ratio)
    CPR = pow((2/(r+1)),(r/(r-1)))
    print("掺混比为",format(doping_ratio, '.2f'),"r=",format(r, '.2f'),"，M=",format(M, '.2f'),"，CPR=",format(CPR, '.2f'))

