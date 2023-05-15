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

        self.Q = 100000  # 最大调度次数
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
        g = 0
        while allCount < self.Q: #最大调度次数
            g += 1
            allCount += 1
            Ecmaxs = []  #记录每代的项目期望完工时间
            Prs = []     #记录每代的按时完工率
            Ec=[]

            if g==1:
                self.pops = FixedMes.AllFit
            if g > 1:
                #采用
                self.Algorithm.RUN(g, FixedMes.AllFit)
                self.pops = FixedMes.AllFitSon

            for pop in self.pops:
                Human = []
                Station = []
                space = []
                #在标准工时下，根据串行调度生成机制，根据简单的分配规则进行人员和设备分配
                _,_,_,workTime,act_info = self.Init.fitness(pop, Human, Station, space)
                pop.WorkTime = workTime
                Ec.append(workTime)
                #基于人员分配、设备分配，在任务网络中添加新的约束
                edge = newAON(Human, Station, space, act_info)

                # 当标准工时下项目完成时间大于规定值时，不采用蒙特卡洛评估， 减少调度评价次数的浪费
                if workTime > FixedMes.lowTime:
                    flag = False
                else:
                    SUM = 0
                    p=0
                    #在 Ns 个采样场景下 ，计算期望完工时间、按时完工概率
                    count = self.Ns
                    while count > 0:
                        # 采样
                        newworkTime = CPM(edge)
                        if newworkTime < self.Cmax:
                            p+=1
                        SUM += newworkTime
                        allCount += 1
                        count -= 1
                    Ecmax = SUM/self.Ns
                    Pr = p/self.Ns
                    pop.Ecmax = Ecmax
                    pop.Pr = Pr
                    pop.setf()
                    Ecmaxs.append(Ecmax)
                    Prs.append(Pr)

            if g > 1:
                self.Algorithm.updata()

            if len(Ecmaxs)>0:
                print("---第{}代---cmax:{}---Ecmaxs:{}---Prs:{}-----".format(g, round(sum(Ec) / len(Ec), 3),round(sum(Ecmaxs) / len(Ecmaxs), 3),
                                                                         round(sum(Prs) / len(Prs), 3)
                                                                         ))
        sortFit = sorted(FixedMes.AllFit,key=lambda x:x.Pr)
        pop = sortFit[0]
        Human = []
        Station = []
        space = []
        SUM = 0
        p = 0
        _, _, _, workTime, act_info = self.Init.fitness(pop, Human, Station, space)
        pop.WorkTime = workTime
        edge = newAON(Human, Station, space, act_info)
        count = 1000

        while count > 0:
            newworkTime = CPM(edge)
            if newworkTime < self.Cmax:
                p += 1
            SUM += newworkTime
            count -= 1

        Ecmax = SUM / 3000
        Pr = p / 3000
        pop.Ecmax = Ecmax
        pop.Pr = Pr

        # Draw1(Human)
        # Draw1(Station)

        print(pop.Ecmax)
        print(pop.Pr)
        print(pop.WorkTime)
        return Ecmax , Pr

if __name__ == '__main__':
    JZJsim = BigSim("C:/Users/29639/Desktop/sim/dis.csv","C:/Users/29639/Desktop/sim/dis.csv")
    Ecmaxs = []
    Prs =[]
    for i in range(10):
        Ecmax , Pr = JZJsim.RUN(i)
        Ecmaxs.append(Ecmaxs)
        Prs.append(Pr)

    print(".....Emax.{}....".format(sum(Ecmaxs)/len(Ecmaxs)))
    print(".....Pr.{}....".format(sum(Prs)/len(Prs)))



