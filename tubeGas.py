from gas import Gas

class TubeGas:
    '''管内气体参数'''
    def __init__(self, gas1:Gas, gas2:Gas, blending_ratio:float) -> None:
        self.P = 4 * pow(10,6)
        self.T = 298.15
        self.blending_ratio = blending_ratio
        self.gas1 = gas1
        self.gas2 = gas2

        self.M = self.cal_mix_parameter(gas1.M,gas2.M)
        self.r = self.cal_mix_parameter(gas1.r,gas2.r)
        self.Cp = self.cal_mix_parameter(gas1.Cp,gas2.Cp)
        self.Cv = self.cal_mix_parameter(gas1.Cv,gas2.Cv)
        self.rho = self.cal_mix_parameter(gas1.rho,gas2.rho)
        self.critical_P = self.cal_mix_parameter(gas1.critical_P,gas2.critical_P)
        self.critical_T = self.cal_mix_parameter(gas1.critical_T,gas2.critical_T)
        self.sound_velocity = self.cal_mix_parameter(gas1.sound_velocity,gas2.sound_velocity)
        
        pass
 
    def cal_mix_parameter(self,value1,value2) -> float:
        return self.blending_ratio * value1 + (1-self.blending_ratio) * value2
    
    def print(self):
        print("=================================================")
        print("管内气体参数如下：")
        print("管内气体压力=",self.P)
        print("管内气体温度=",self.T)
        print("管内气体密度=",self.rho)
        print("管内气体绝热指数=",self.r)
        print("管内气体定压比热容=",self.Cp)
        print("管内气体定容比热容=",self.Cv)
        print("管内气体声速=",self.sound_velocity)
        print("=================================================")
