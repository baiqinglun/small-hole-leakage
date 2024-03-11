class Atmosphere:
    '''大气条件'''
    def __init__(self, P:float, T:float) -> None:
        self.P = P * pow(10,6)
        self.T = T
        self.ua = 310 # 当地声速
 