class LeakageOrifice:
    def __init__(self):
        self.hole_radius = 0.001
        self.Cd = 1 # 泄漏口形状修正系数，圆形为1
        self.A = 3.14 * pow(self.hole_radius,2)
        self.Cv = None

    def modifyCv(self,Q0:float,rho:float,P2:float,P:float) -> None:
        self.Cv = Q0 / pow(rho * (P2 - P),0.5)

    def print(self):
        print("泄漏口半径=",self.hole_radius)
        print("泄漏口形状修正系数=",self.Cd)
        print("泄漏口面积=",self.A)
        print("泄漏量修正系数=",self.Cv)
