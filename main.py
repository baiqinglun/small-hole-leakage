# -*- coding: utf-8 -*-
# @Time : 2024/02/20
# @Author : baiqinglun
# @introdution : 小孔泄漏程序

# 掺混比按照30%
# 压力4MPa
# 12点钟方向

# Q1 = 16.5kg/h = 0.00458kg/s

R = 8.314
PI = 3.1415926

from atmosphere import Atmosphere
from tubeGas import TubeGas
from outTubeGas import OutTubeGas
from leakage_orifice import LeakageOrifice
from gas import H2_Gas,CH4_Gas

def main():
    blending_ratio = 0.3
    H2 = H2_Gas("氢气")
    CH4 = CH4_Gas("甲烷")
    tube_gas = TubeGas(H2,CH4,blending_ratio)
    atmosphere = Atmosphere(0.1,298)
    leakage_orifice = LeakageOrifice()
    outtube_gas = OutTubeGas(H2,CH4,blending_ratio)

    # 计算初始泄漏量Q1，这个流量是理论值
    Cd = leakage_orifice.Cd
    A = leakage_orifice.A
    P1 = tube_gas.P
    M = tube_gas.M
    r = tube_gas.r
    T1 = tube_gas.T
    Q1 = Cd * A * P1 * pow(M * r/( R * T1) * pow(2/(r+1),(r+1)/(r-1)),0.5)
    
    P1 = tube_gas.P
    T1 = tube_gas.T
    sound_velocity = tube_gas.sound_velocity
    print(tube_gas.critical_P)
    print(tube_gas.critical_T)
    P1_old = tube_gas.P
    T1_old = tube_gas.T
    while True:
        vcr = pow(2/(r + 1),r/(r-1))
        while True:
            P2 = outtube_gas.cal_P2(P1,vcr)
            T2 = outtube_gas.cal_T2(T1,vcr)
            # 计算得到的出口速度
            Cp1 = tube_gas.Cp
            Cp2 = outtube_gas.Cp
            u2 = pow(2*(Cp1 * T1 - Cp2 * T2),0.5) # 出口速度
            if abs(u2 - sound_velocity) < 1:
                break;
            vcr = vcr+0.0005
            # print(" vcr = ",vcr)

        # 真实泄漏量Q0和速度
        Q0 = 0.00458
        rho = outtube_gas.rho
        A = leakage_orifice.A
        u0 = Q0 / (rho * A)
        print(rho)
        print(A)
        print(u0)
        # 动能转化为内能，温度升高Tf
        Cp2 = outtube_gas.Cp
        M = tube_gas.M
        Cv = tube_gas.Cv
        E = 0.5 * (pow(u2,2)-pow(u0,2)) / Cp2
        n = Q1 / M
        Tf = E / (n * Cv) # n是物质的摩尔数，Cv是定容摩尔热容
        # print("管外气体温度1=",outtube_gas.T)
        outtube_gas.T = outtube_gas.T + Tf
        # print("管外气体温度2=",outtube_gas.T)
        # with open('output.txt', 'a') as file:
        #     # 向文件中写入内容
        #     file.write(f"管外气体温度={outtube_gas.T}\n")
        
        # 计算流动修正系数并修正流量
        rho = outtube_gas.rho
        P2 = outtube_gas.P
        P = atmosphere.P
        leakage_orifice.modifyCv(Q0,rho,P2,P)
        Cvaver = leakage_orifice.Cv * 16 / 16
        Qnew = Cvaver * pow(rho * (P2 - P),0.5)

        if abs((Qnew - Q1)/Qnew) <= 0.001:
            break
        Q1 -= 0.00001

        # 求解P1、T1
        P1_old = P1
        P1 = Q1 / (Cd * A * pow(M * r/( R * T1) * pow(2/(r+1),(r+1)/(r-1)),0.5))
        # print(P1)
        T1_old = T1
        T1 = T1_old/P1_old * P1
        # print(T1)
        pass

    outtube_gas.print()
    # print(vcr)


if __name__=="__main__":
    main()
