import GA1
import PSGS11
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
        self.Algorithm = GA1.Ga()

    def RUN(self):
        FixedMes.my()
        self.Init.InitPopulation()
        self.pa = FixedMes
        self.Activities = FixedMes.act_info
        self.popNum =FixedMes.populationnumber
        self.schedulePolicy = PSGS(self.pa.total_renew_resource, self.Activities)

        print("各类型人员组成: ", self.pa.total_Huamn_resource)
        allCount = 0
        g = 0

        while allCount < self.Q:
            g += 1
            allCount += 1
            Ec = []
            if g==1:

                for pop in FixedMes.AllFit:
                    Human = []
                    Station = []
                    space = []
                    # 在标准工时下，根据串行调度生成机制，根据简单的分配规则进行人员和设备分配
                    _, _, _, workTime, act_info = self.Init.fitness(pop, Human, Station, space)
                    allCount += 1
                    pop.WorkTime = workTime
                Ec = []
                for pop in FixedMes.AllFit:
                    Ec.append(pop.WorkTime)
                Ec = sorted(Ec, key=lambda x: x)
                print("---------Emax: {}---best: {}-----".format(sum(Ec) / len(Ec), Ec[0]))

            if g > 1:
                self.Algorithm.RUN(g, FixedMes.AllFit)
                for pop in FixedMes.AllFitSon:
                    Human = []
                    Station = []
                    space = []
                    # 在标准工时下，根据串行调度生成机制，根据简单的分配规则进行人员和设备分配
                    _, _, _, workTime, act_info = self.Init.fitness(pop, Human, Station, space)
                    allCount += 1
                    pop.WorkTime = workTime

                self.Algorithm.updata()
                Ec=[]
                for pop in FixedMes.AllFit:
                    Ec.append(pop.WorkTime)
                Ec = sorted(Ec, key=lambda x: x)
                print("---------Emax: {}---best: {}-----".format(sum(Ec) / len(Ec), Ec[0]))

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
        return workTime
if __name__ == '__main__':
    JZJsim = BigSim("C:/Users/29639/Desktop/sim/dis.csv","C:/Users/29639/Desktop/sim/dis.csv")
    JZJsim.RUN()