from gas import Gas

class OutTubeGas:
    '''管外气体参数'''
    def __init__(self, gas1:Gas, gas2:Gas, blending_ratio:float) -> None:
        self.blending_ratio = blending_ratio
        self.gas1 = gas1
        self.gas2 = gas2

        self.M = self.cal_mix_parameter(gas1.M,gas2.M)
        self.r = self.cal_mix_parameter(gas1.r,gas2.r)
        self.Cp = self.cal_mix_parameter(gas1.Cp,gas2.Cp)
        self.Cv = self.cal_mix_parameter(gas1.Cv,gas2.Cv)
        self.rho = self.cal_mix_parameter(gas1.rho,gas2.rho)
    
        self.cal_CPR()

    def cal_P2(self,P:float,vcr:float) -> float:
        self.P = vcr * P # 临界压力
        return self.P
    
    def cal_T2(self,T:float,vcr:float) -> float:
        self.T = T * vcr  # 临界温度
        return self.T

    def cal_mix_parameter(self,value1,value2) -> float:
        return self.blending_ratio * value1 + (1-self.blending_ratio) * value2

    def cal_CPR(self) -> None:
        self.CPR = pow(2/(self.r + 1),self.r/(self.r-1))

    def change_T(self,T) -> None:
        self.T = T * self.CPR

    def change_P(self,P) -> None:
        self.P = self.CPR * P

    def change_CPR(self,value):
        self.CPR = value

    def print(self):
        print("=================================================")
        print("管外气体参数如下：")
        print("管外气体压力=",self.P)
        print("管外气体温度=",self.T)
        print("管外气体密度=",self.rho)
        print("管外气体绝热指数=",self.r)
        print("管外气体定压比热容=",self.Cp)
        print("管外气体定容比热容=",self.Cv)
        print("=================================================")
