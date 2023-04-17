
# num_activities,
# num_resource_type,
# total_resource,
# activities
"""
初始化，包括加载数据
初始化编码

"""
import copy
import math
import random
import sys
from collections import defaultdict

import numpy as np

from chromosome.Chromo import Chromosome
from conM.FixedMess import FixedMes
from human.Human import Human
from read.preprocess import InitM
from station.Station import Station


class MyInit(object):

    def __init__(self,filenameDis,filenameJob):
        self.geneN = 0
        self.activities = {}
        self.Init = InitM(filenameDis,filenameJob)
        FixedMes.my()



        # num_activities, num_resource_type,
        # total_resource, activities
        # 活动数int， 资源数int， 资源限量np.array，
        # 所有活动集合dic{活动代号：活动对象}
        # FixedMes.my()
        # FixedMes.distance = self.Init.readDis()
        #
        #
        # self.activities= self.Init.readData()
        # self.geneN = FixedMes.Activity_num
        #
        # FixedMes.act_info = self.activities


    def InitPopulation(self):

        FixedMes.distance = self.Init.readDis()

        self.activities = self.Init.readData()
        self.geneN = FixedMes.Activity_num

        FixedMes.act_info = self.activities

        num = 0
        print("正在生成种群。。。。")
        while num < FixedMes.populationnumber:

            iter = Chromosome()
            codes = self.encoder()
            iter.setcodes(codes)
            humanState = []
            stationState = []
            orderState = defaultdict(list)
            MyInit.fitness(iter, humanState, stationState)


            if(iter.WorkTime<FixedMes.lowTime):
                # print("第 " + str(num) + " 个粒子")
                # print(iter.WorkTime)
                FixedMes.AllFit[num] = copy.deepcopy(iter)
                num+=1

    def encoder(self):
        numbers = len(self.activities)
        cloneA = copy.deepcopy(self.activities)
        chromosome = []
        random_Ei_0 = 0

        for a in range(numbers):
            Ei_0 = []  # 紧前任务数为0的任务集编号
            for key, Ei in cloneA.items():
                prece = cloneA[key].predecessor
                if prece is None:
                    continue

                Ei_number = len(prece)

                if Ei_number == 0:
                    Ei_0.append(key)
            random.shuffle(Ei_0)
            random_Ei_0 = Ei_0[0]
            # self.taskid = taskid
            # self.belong_plane_id = jzjId
            chromosome.append([random_Ei_0,cloneA[random_Ei_0].belong_plane_id,cloneA[random_Ei_0].taskid])
            for key, Ei in cloneA.items():
                prece = cloneA[key].predecessor
                if random_Ei_0 in prece:
                    prece.remove(random_Ei_0)
            del cloneA[random_Ei_0]
        return chromosome
    @staticmethod
    def decoder (Humans, acs):
        finishTimee = acs[FixedMes.Activity_num-1].ef
        workTime = []
        movetime=0
        for typeH in Humans:
            f=[]
            for human in typeH:
                movetime+=human.getmovetime()
                f.append(human.alreadyworkTime)

            f_var = np.var(np.array(f))
            workTime.append(f_var)
        stdev = sum(workTime)

        return finishTimee,stdev,movetime,

    '''
    :param chromosome: 
    :param iter: 
    :param Humans: 
    :param Orders: 
    :return: 
    '''

    @staticmethod
    def fitness(iter,Humans,Stations):
        MyInit.initMess(Humans,Stations)
        # initMessOrder(Orders, activities)
        MyInit.serialGenerationScheme(FixedMes.act_info,iter, Humans,Stations)
        iter.WorkTime,iter.variance,iter.movetime = MyInit.decoder(Humans,FixedMes.act_info)
        iter.setf()
        return Humans,Stations


    @staticmethod
    def initMess(Humans,Stations):
        number = 0

        for i in range(FixedMes.Human_resource_type):
            Humans.append([])
            for j in range(FixedMes.total_Huamn_resource[i]):
                # ij都是从0开头 ,number也是

                Humans[i].append(Human([i,j,number]))
                number += 1

        number = 0

        for i in range(FixedMes.station_resource_type):
            Stations.append([])
            for j in range(FixedMes.total_station_resource[i]):
                # ij都是从0开头 ,number也是
                Stations[i].append(Station([i,j,number]))
                number += 1

    @staticmethod
    def initMessOrder(Orders,activities):

        # for i in range(jzjNums):
        #     Orders.append([])
        for key ,ac in activities.items():
            jzjN = ac.belong_plane_id
            Orders[jzjN].append(ac)



    '''
    串行调度生成机制，传入所有活动，资源限量，优先序列
    :param allTasks:
    :param resourceAvail:
    :param priority:
    :return:
    '''
    @staticmethod
    def serialGenerationScheme(allTasks, iter, humans,stations):

        # 记录资源转移
        priorityToUse = iter.codes.copy()
        resourceAvailH = FixedMes.total_Huamn_resource
        resourceAvailS = FixedMes.total_station_resource

        ps = [0]  # 局部调度计划初始化

        allTasks[0].es = 0  # 活动1的最早开始时间设为0
        allTasks[0].ef = allTasks[0].es + allTasks[0].duration

        for stage in range(0, len(priorityToUse)):
            selectTaskID = priorityToUse[stage][0]
            earliestStartTime = 0

            '''
            需要考虑移动时间
            '''
            now_pos = allTasks[selectTaskID].belong_plane_id
            dur = allTasks[selectTaskID].duration
            for preTaskID in allTasks[selectTaskID].predecessor:
                if allTasks[preTaskID].ef > earliestStartTime:
                    earliestStartTime = allTasks[preTaskID].ef

            startTime = earliestStartTime
            # 检查满足资源限量约束的时间点作为活动最早开始时间，即在这一时刻同时满足活动逻辑约束和资源限量约束
            t = startTime+1

            resourceSumH = np.zeros(len(resourceAvailH))
            recordH = [[] for _ in range(len(resourceAvailH))]
            resourceSumS = np.zeros(len(resourceAvailS))
            recordS = [[] for _ in range(len(resourceAvailS))]

            # 计算t时刻正在进行的活动的资源占用总量,当当前时刻大于活动开始时间小于等于活动结束时间时，说明活动在当前时刻占用资源
            while t > startTime :

                resourceSumH = np.zeros(len(resourceAvailH))
                recordH = [[] for _ in range(len(resourceAvailH))]
                resourceSumS = np.zeros(len(resourceAvailS))
                recordS = [[] for _ in range(len(resourceAvailS))]

                for type in range(len(resourceAvailH)):
                    if allTasks[selectTaskID].resourceRequestH[type]>0:
                      for human in humans[type]:

                          if (len(human.OrderOver) ==0):
                              resourceSumH[type] += 1  # 该类资源可用+1
                              recordH[type].append(human)

                          if (len(human.OrderOver) ==1):
                              Activity1 = human.OrderOver[0]
                              from_pos = Activity1.belong_plane_id
                              to_pos = Activity1.belong_plane_id
                              movetime1 = 0 if from_pos == 0 else FixedMes.distance[from_pos][
                                                                      now_pos] / FixedMes.human_walk_speed
                              movetime2 = 0 if to_pos == 0 else FixedMes.distance[to_pos][
                                                                    now_pos] / FixedMes.human_walk_speed

                              if (Activity1.ef + 1 + round(movetime1,1)) <= t \
                                      or (t + dur + 1) <= (Activity1.es - round(movetime2,1)):
                                  resourceSumH[type] += 1  # 该类资源可用+1
                                  recordH[type].append(human)

                        #遍历船员工序，找到可能可以插入的位置,如果船员没有工作，人力资源可用
                          if(len(human.OrderOver)>=2):
                              flag = False
                              for taskIndex in range(len(human.OrderOver)-1):
                                  Activity1 = human.OrderOver[taskIndex]
                                  Activity2 = human.OrderOver[taskIndex+1]

                                  from_pos = Activity1.belong_plane_id
                                  to_pos = Activity2.belong_plane_id
                                  movetime1 = 0 if from_pos==0 else FixedMes.distance[from_pos][now_pos]/FixedMes.human_walk_speed
                                  movetime2 = 0 if to_pos==0 else FixedMes.distance[to_pos][now_pos]/FixedMes.human_walk_speed

                                  if (Activity1.ef + 1 +  round(movetime1,1)) <= t \
                                     and (t + dur + 1 ) <= (Activity2.es - round(movetime2,1)):
                                       flag=True
                                       resourceSumH[type] += 1  # 该类资源可用+1
                                       recordH[type].append(human)
                                       break

                              if flag==False:
                                  Activity1 = human.OrderOver[0]
                                  Activity2 = human.OrderOver[-1]
                                  from_pos = Activity2.belong_plane_id
                                  to_pos = Activity1.belong_plane_id
                                  movetime2 = 0 if from_pos == 0 else FixedMes.distance[from_pos][
                                                                          now_pos] / FixedMes.human_walk_speed
                                  movetime1 = 0 if to_pos == 0 else FixedMes.distance[to_pos][
                                                                        now_pos] / FixedMes.human_walk_speed

                                  if (Activity2.ef + 1 + round(movetime2,1)) <= t \
                                          or (t + dur + 1) <= (Activity1.es - round(movetime1,1)):
                                      resourceSumH[type] += 1  # 该类资源可用+1
                                      recordH[type].append(human)

                for type in range(len(resourceAvailS)):
                    if allTasks[selectTaskID].resourceRequestS[type]>0:
                      for station in stations[type]:
                          # 舰载机在这个加油站的覆盖范围内：
                          if now_pos in FixedMes.constraintS_JZJ[type][station.zunumber]:

                              if (len(station.OrderOver) == 0):
                                  resourceSumS[type] += 1  # 该类资源可用+1
                                  recordS[type].append(station)

                              if (len(station.OrderOver) == 1):
                                  Activity1 = station.OrderOver[0]

                                  if (Activity1.ef + 1 ) <= t \
                                          or (t + dur + 1) <= (Activity1.es):
                                      resourceSumS[type] += 1  # 该类资源可用+1
                                      recordS[type].append(station)

                              if (len(station.OrderOver) >= 2):
                                  flag = False
                                  for taskIndex in range(len(station.OrderOver)-1):
                                      Activity1 = station.OrderOver[taskIndex]
                                      Activity2 = station.OrderOver[taskIndex+1]

                               # from_pos = Activity1.belong_plane_id
                               # to_pos = Activity2.belong_plane_id
                               # movetime1 = 0 if from_pos==0 else FixedMes.distance[from_pos][now_pos]*FixedMes.human_walk_speed
                               # movetime2 = 0 if to_pos==0 else FixedMes.distance[to_pos][now_pos]*FixedMes.human_walk_speed

                                      if (Activity1.ef + 1) <= t \
                                        and (t + dur + 1 ) <= (Activity2.es):
                                        resourceSumS[type] += 1  # 该类资源可用+1
                                        recordS[type].append(station)
                                        flag = True
                                  if flag == False:
                                      Activity1 = station.OrderOver[-1]
                                      Activity2 = station.OrderOver[0]

                                      if (Activity1.ef + 1 ) <= t or (t + 1 +dur) <= Activity2.es:
                                          resourceSumS[type] += 1
                                          recordS[type].append(station)


                # 若资源不够，则向后推一个单位时间
                if (resourceSumH < allTasks[selectTaskID].resourceRequestH).any() or (resourceSumS < allTasks[selectTaskID].resourceRequestS).any() :
                        t += 1
                else:
                    break
            # 若符合资源限量则将当前活动开始时间安排在这一时刻
            allTasks[selectTaskID].es = t
            allTasks[selectTaskID].ef = t + dur

            # 人员分配 根据 record 分配
            for type in range(len(resourceAvailH)):

                need = allTasks[selectTaskID].resourceRequestH[type]
                while need > 0:
                    alreadyWorkTime = math.inf
                    index = 0
                    for nowHuman in recordH[type]:
                        if nowHuman.alreadyworkTime < alreadyWorkTime:
                            alreadyWorkTime = nowHuman.alreadyworkTime
                            index = nowHuman.zunumber

                    # 更新人员
                    humans[type][index].update(allTasks[selectTaskID])
                    # allTasks[selectTaskID].HumanNums.append(humans[type][index].number)
                    need -= 1

            # 分配 根据 record 分配
            for type in range(len(resourceAvailS)):

                need = allTasks[selectTaskID].resourceRequestS[type]
                if need > 0:
                    alreadyWorkTime = math.inf
                    index = 0
                    for nowStaion in recordS[type]:
                        if nowStaion.alreadyworkTime < alreadyWorkTime:
                            alreadyWorkTime = nowStaion.alreadyworkTime
                            index = nowStaion.zunumber

                    # 更新
                    stations[type][index].update(allTasks[selectTaskID])
                    # allTasks[selectTaskID].SNums.append(stations[type][index].number)
                    need -= 1

            # 局部调度计划ps
            ps.append(selectTaskID)

if __name__ == '__main__':
    m = MyInit("C:/Users/29639/Desktop/dis.csv","C:/Users/29639/Desktop/order.txt")
    m.InitPopulation()
    a=[[0,1,2],[[2,3,1]]]
    b=[[1,1,2],[[2,3,1]]]


    print(a==b)












