import vpython as vp
import time as tm
vp.rate(60)
dt = 0.15
class sim:
    def __init__(self):
        self.omega = 0
        self.alpha = 0
        self.obj = vp.box(texture = vp.textures.wood)

    def destab(self, currang = 0, desiredang = 0, oscillationConstant = 1, dampeningOrder = 1, dampeningConstant = 1):
        self.omega = 0
        self.currang = currang
        self.theta = desiredang-self.currang
        while round(self.theta, 4) != 0:
            tm.sleep(0.15)
            self.theta = desiredang-self.currang
            self.alpha = self.theta*oscillationConstant - (self.omega**dampeningOrder)*dampeningConstant
            self.omega = self.omega + self.alpha*dt
            self.currang = self.currang + self.omega*dt
            self.obj.rotate(angle = self.omega*dt, axis=vp.vector(0, 0, 1), origin=vp.vector(0, 0, 0))