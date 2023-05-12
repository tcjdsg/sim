import PSGS11
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

        self.Algorithm = Ga(self.dis_file, self.order_file)
        self.Ns = 20

        self.Q = 100000  # 最大调度次数
        # self.popNum = self.pa.populationnumberson
        self.Cmax = 60
        print()
        self.Init = myInit.MyInit(self.dis_file, self.order_file)

    def RUN(self):
        FixedMes.my()

        self.Init.InitPopulation()
        self.pa = FixedMes
        self.Activities = FixedMes.act_info
        self.popNum =FixedMes.populationnumber
        self.schedulePolicy = PSGS(self.pa.total_renew_resource, self.Activities)

        print("各类型人员组成: ", self.pa.total_Huamn_resource)
        allCount = 0

        while allCount < self.Q:
            allCount += 1
            self.Algorithm.RUN(allCount/(self.Ns*self.popNum))
            Ecmaxs=[]
            Prs=[]
            Vs =[]
            for pop in FixedMes.AllFit:
                Human = []
                Station = []
                space = []
                _,_,_,workTime,act_info = self.Init.fitness(pop, Human, Station, space)
                pop.WorkTime = workTime
                if workTime > FixedMes.lowTime:
                    flag = False
                else:
                    edge = newAON(Human, Station, space, act_info)
                    count = self.Ns
                    SUM = 0
                    p=0
                    while count > 0:
                        workTime = CPM(edge)
                        # Draw(Human,Station)
                        # print(workTime)
                        if workTime < self.Cmax:
                            p+=1
                        SUM += workTime
                        allCount += 1
                        count -= 1
                    Ecmax = SUM/self.Ns
                    Pr = p/self.Ns
                    pop.Ecmax = Ecmax
                    pop.Pr = Pr
                    pop.setf()
                    Ecmaxs.append(Ecmax)
                    Prs.append(Pr)
                    Vs.append(0)

            if allCount > 0:
                print("---第{}代----Ecmax:{}---Prs:{}---Vs:{}---".format(allCount/(self.Ns*self.popNum), round(sum(Ecmaxs)/len(Ecmaxs), 1),
                                                                          round(sum(Prs)/len(Prs), 1),
                                                                         round(sum(Vs) / len(Vs), 1)))


        sortFit = sorted(FixedMes.AllFit,key=lambda x:x.zonghe)






if __name__ == '__main__':
    JZJsim = BigSim("C:/Users/29639/Desktop/sim/dis.csv","C:/Users/29639/Desktop/sim/dis.csv")
    JZJsim.RUN()