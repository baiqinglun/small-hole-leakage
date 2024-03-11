R = 8.314

class Gas:
    def __init__(self,name):
        self.name = "Gas"
        self.M = 0
        self.r = 0
        self.Cp = 0
        self.Cv = 0
        self.rho = 0
        self.critical_T = 0
        self.critical_P = 0
        self.specific_heat_capacity = 0
        self.sound_velocity = 0
        self.R = 0

    def print(self):
        print("=================================================")
        print("气体",self.name,"的属性如下：")
        print("分子量",self.M*1000)
        print("绝热指数",self.r)
        print("定压比热容",self.Cp)
        print("定容比热容",self.Cv)
        print("密度",self.rho)
        print("临界温度",self.critical_T)
        print("临界压力",self.critical_P)
        print("比热",self.specific_heat_capacity)
        print("个别气体常数",self.R)
        print("声速",self.sound_velocity)
        print("=================================================")

class H2_Gas(Gas):
    def __init__(self,name):
        super(H2_Gas, self).__init__(name)
        self.name = name
        self.M = 2.02 * 0.001 # kg/mol
        self.r = 1.4 # r=Cp/Cv
        self.Cp = 14000 # J/(kg K)
        self.Cv = 10000
        self.rho = 0.0838 # kg/m3
        self.critical_T = 43.6
        self.critical_P = 20.2 # Pa
        self.specific_heat_capacity = 14.4 # J/(kg K)
        self.R = R / self.M # J/(kg K)
        self.sound_velocity = pow(self.r * self.R * 298,0.5)


class CH4_Gas(Gas):
    def __init__(self,name):
        super(CH4_Gas, self).__init__(name)
        self.name = name
        self.M = 16.04 * 0.001 
        self.r = 1.31
        self.Cp = 2265
        self.Cv = 1729.01
        self.rho = 0.651
        self.critical_T = 190.65
        self.critical_P = 45.4
        self.specific_heat_capacity = 2210
        self.R = R / self.M
        self.sound_velocity = pow(self.r * self.R * 298,0.5)