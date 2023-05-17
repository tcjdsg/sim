
from BSO import bso
from draw import people
from draw.people import Draw, Draw1
from util.utils import *
from GA1 import Ga
from Mythread import myInit
from conM.FixedMess import FixedMes

from schedulePolicy.CreatCpc import PSGS, newAON


class BigSim():
    def __init__(self,dis_file,order_file):
        self.dis_file = dis_file
        self.order_file = order_file
        self.Ns = 20

        self.Q = 10000  # 最大调度次数
        # self.popNum = self.pa.populationnumberson
        self.Cmax = 80
        FixedMes.lowTime = self.Cmax
        # print()
        self.Init = myInit.MyInit(self.dis_file, self.order_file)
        self.Algorithm = bso(self.Init)

    def RUN(self,all):
        # 初始化
        if all == 0:
            FixedMes.my()
        self.Init.InitPopulation()
        #各参数信息
        self.pa = FixedMes
        #获取各任务信息，包括资源需求、标准时长、工时分布
        self.Activities = FixedMes.act_info
        self.popNum =FixedMes.populationnumber

        allCount = 0
        ge = FixedMes.ge
        g = 0
        while allCount < ge: #最大调度次数
            g += 1
            allCount += 1
            Ec=[]

            if g==1:

                for pop in FixedMes.AllFit:
                    Human = []
                    Station = []
                    space = []
                    # 在标准工时下，根据串行调度生成机制，根据简单的分配规则进行人员和设备分配
                    _, _, _, workTime, act_info = self.Init.fitness(pop, Human, Station, space)
                    pop.WorkTime = workTime
                for pop in FixedMes.AllFit:
                    Ec.append(pop.WorkTime)
                Ec = sorted(Ec, key=lambda x: x)
                print("---------Emax: {}---best: {}-----".format(sum(Ec) / len(Ec), Ec[0]))

            if g > 1:
                self.Algorithm.RUN(g, FixedMes.AllFit)
                self.Algorithm.updata()
                Ec=[]
                for pop in FixedMes.AllFit:
                    Ec.append(pop.WorkTime)
                Ec=sorted(Ec,key = lambda x:x)
                print("---------Emax: {}---best: {}-----".format(sum(Ec) / len(Ec),Ec[0]))


        sortFit = sorted(FixedMes.AllFit,key=lambda x:x.WorkTime)
        pop = sortFit[0]
        Human = []
        Station = []
        space = []

        _, _, _, workTime, act_info = self.Init.fitness(pop, Human, Station, space)
        pop.WorkTime = workTime

        Draw1(Human)
        Draw1(Station)
        print(pop.WorkTime)
        return WorkTime

if __name__ == '__main__':
    JZJsim = BigSim("C:/Users/29639/Desktop/sim/dis.csv","C:/Users/29639/Desktop/sim/dis.csv")
    Ecmaxs = []
    Prs =[]
    for i in range(10):
        WorkTime = JZJsim.RUN(i)
        Ecmaxs.append(WorkTime)
    print(".....Emax.{}....".format(sum(Ecmaxs)/len(Ecmaxs)))




