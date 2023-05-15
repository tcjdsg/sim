from collections import defaultdict

import scipy.stats as stats

from chromosome.Chromo import Chromosome
import numpy as np

# class MyDistribution(rv_continuous):
#     def _pdf(self, x):#概率密度分布函数
#         return 1.0/x
#
# distribution = MyDistribution()
# xlist=np.linspace(-8,8,300)
# ylist=distribution.pdf(xlist)
# samples=distribution.rvs(size=200)

class FixedMes(object):
    """
    distance:
    orderInputMes:

    """

    distance = [[]]

    numJzjPos = 18
    numHumanAll = [18,60]

    planeOrderNum = 18
    planeNum = 8


    jzjNumbers=[1,2,3,4,5,6,7,8]  #舰载机编号


    Human_resource_type = 4 #先考虑只有一类人
    total_Huamn_resource = [4, 5, 6, 8]  # 每种人员数量

    # total_Huamn_resource = [30]
    constraintOrder = defaultdict(lambda: []) #记录每类人的可作用工序，和可作用舰载机范围
    # constraintOrder[0] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    constraintOrder[0] = [ 1, 2, 5]
    constraintOrder[1] = [3,4, 16,17]
    constraintOrder[2] = [7, 8, 14,16]
    constraintOrder[3] = [6, 9, 10, 11,12,13,15]



    modeflag = 0 #0是单机、1是全甲板，这里考虑全甲板，如果是全甲板
    # constraintJZJ = defaultdict(lambda: []) #保障人员可作用舰载机范围,两种模式，单机或者全甲板

    station_resource_type = 5
    total_station_resource = [4,8,3,3,4]

    #飞机数量比较少的时候，这些燃料资源的限制约束不起作用。
    total_renew_resource = [99,99,99,99,99]

    #座舱限制。相当于是每个站位都有一个座舱，每个舰载机只能用自己座舱。
    space_resource_type = 8
    total_space_resource = [1,1,1,1,1,1,1,1]
    constraintS_Order = defaultdict(lambda: [])  # 记录每类设备的可作用工序，和可作用舰载机范围

     # 设备保障范围约束
    constraintS_JZJ = defaultdict(lambda: [])

    constraintS_JZJ[0] = [[1, 2, 3],
                          [3, 4, 5],
                          [6, 7],
                          [7, 8]]
    constraintS_JZJ[1] = [[1],
                          [2],
                          [3],
                          [4],
                          [5],
                          [6],
                          [7],
                          [8]]
    constraintS_JZJ[2] = [[1,2,3,4],
                          [4,5,6,7],
                          [7,8]]
    constraintS_JZJ[3] = [[1,2,3,4],
                          [4,5,6,7],
                          [7,8]]
    constraintS_JZJ[4] = [[1,2,3],
                          [2,3,4],
                          [4,5,6],
                          [7,8]]

    Activity_num  = (planeOrderNum)*planeNum+2 #活动数量

    #工序顺序
    SUCOrder = defaultdict(lambda: [])
    SUCOrder[1] = [2,4,6,8,11,12,13]
    SUCOrder[2] = [3]
    SUCOrder[3] = [10]
    SUCOrder[4] = [5]
    SUCOrder[5] = [10]
    SUCOrder[6] = [3,5,7,9]
    SUCOrder[7] = [14]
    SUCOrder[8] = [9]
    SUCOrder[9] = [10]
    SUCOrder[10] = [14]
    SUCOrder[11] = [16]
    SUCOrder[12] = [16]
    SUCOrder[13] = [16]
    SUCOrder[14] = [15]
    SUCOrder[15] = [16]
    SUCOrder[16] = [17]
    SUCOrder[17] = [18]
    SUCOrder[18] = []

    #
    OrderInputMes = [[],
                     [(0, 0), (0, 0), (0,0)], #虚拟1
                     [(0, 1), (0, 0), (0,0)],  # 2
                     [(0, 1), (1, 1), (0,1)],  # 3
                     [(1, 1), (0, 0), (0,0)],  #4
                     [(1, 1), (1, 1), (0,0)],  # 5
                     [(0, 2), (2, 1), (0,0)],  # 6
                     [(3, 2), (0, 1), (0,0)],  # 7
                     [(2, 2), (0, 0), (0,0)],  # 8,
                     [(2, 1), (1, 1), (0,1)],  # 9
                     [(3, 1), (0, 0), (0,0)],  # 10
                     [(3, 2), (3, 1), (0,0)],  # 11
                     [(3, 1), (0, 0), (0,0)],  # 12
                     [(3, 1), (0, 0), (0,0)],  # 13
                     [(3, 1), (4, 1), (0,1)],  # 14
                     [(2, 1), (0, 0), (0,0)],  # 15
                     [(3, 1), (4, 1), (0,1)],  # 16
                     [(1, 1), (1, 1), (0,0)],  # 17
                     [(0, 0), (0, 0), (0,0)]  # 18
                       ]
    #17位 为了让虚拟从1开始

    sigma = 0.3
    shedule_num=0

    act_info={}

    lowTime = 90 #不能超过90 min

    cross = 0.5
    cross1 = 2.5
    MutationRate = 0.25
    MutationRatePmo = 0.05

    transferrate = 0.2
    transfer_iter = 50
    human_walk_speed = 800000 #人员行走速度8 m/(in)

    populationnumber = 30
    ge = 10

    threadNum = 1
    populationnumberson = populationnumber

    AgenarationIten = ge / 3
    GenarationIten = 0

    #保存每代染色体信息 父代
    AllFit = []
    AllFitSon = []
    AllFitFamily = []
    #vnsIter = -1

    resver_k1 = [ 0 for _ in range(ge)]
    resver_k2 = [ 0 for _ in range(ge)]
    #populationnumber*populationnumber
    slect_F_step_alone = [[] for _ in range(populationnumber)]
    # slect_F_step = [[] for _ in range(populationnumber)]

    Paternal = [[0,0] for _ in range(int(populationnumber/2))]
    #每一代的平均值
    Avufit = {}
    AverPopmove = 0
    AverPopTime = 0
    AverPopVar = 0
    Diversity = 0.0
    keyChainOrder = []
    #死锁辅助检查列表
    # dealLockList=[[0 for _ in range(Activity_num)] for _ in range(Activity_num)]

    bestHumanNumberTarget=[]

    Allactivity = []
    constraintHuman =[]
    constraintStation=[]
    constraintSpace = []

    humanNum = 0
    targetWeight =[1,0.3,0.1]
    boundUpper =[0,0]
    boundLowwer=[]

    OrderTime = [0,
                 0,  # 虚拟1
                 3,  # 1
                 6,  # 2
                 3,  # 3
                 5,  # 4
                 3,  # 5
                 10,  # 6
                 5,  # 7
                 3,
                 4,
                 4,
                 13,
                 8,
                 4,
                 5,
                 5,
                 0,
                 0]
    AON=[]

    @classmethod
    def getTime(cls,i):
        # 定义每种任务的时间分布
        sigma = 0.3
        if i == 0:
            return 0
        elif i == 1:
            return 0
        elif i == 2:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc = cls.OrderTime[2], scale=sigma).rvs()
        elif i == 3:
            return stats.truncnorm((-0.8) / sigma, 0.8 / sigma, loc=cls.OrderTime[3], scale=sigma).rvs()
        elif i == 4:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[4], scale=sigma).rvs()
        elif i == 5:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[5], scale=sigma).rvs()
        elif i == 5:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[5], scale=sigma).rvs()
        elif i == 6:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[6], scale=sigma).rvs()
        elif i == 7:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[7], scale=sigma).rvs()

        elif i == 8:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[8], scale=sigma).rvs()
        elif i == 9:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[9], scale=sigma).rvs()

        elif i == 10:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[10], scale=sigma).rvs()
        elif i == 11:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[11], scale=sigma).rvs()

        elif i == 12:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[12], scale=sigma).rvs()
        elif i == 13:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[13], scale=sigma).rvs()
        elif i == 14:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[14], scale=sigma).rvs()

        elif i == 15:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[15], scale=sigma).rvs()
        elif i == 16:
            return stats.truncnorm((-0.5) / sigma, 0.5 / sigma, loc=cls.OrderTime[16], scale=sigma).rvs()
        elif i == 17:
            return 0
    @classmethod
    def my(cls):

        cls.AllFit=[]
        cls.AllFitSon=[]
        for i in range(cls.populationnumber):

            cls.AllFit.append(Chromosome())
            cls.AllFitSon.append(Chromosome())
            cls.AllFitFamily.append(Chromosome())
            cls.AllFitFamily.append(Chromosome())

        for i in range(cls.planeOrderNum):
            cls.keyChainOrder.append(set())

        num=0
        for i in range(len(cls.total_Huamn_resource)):
            cls.constraintHuman.append([])
            for j in range(cls.total_Huamn_resource[i]):
                num+=1
                cls.constraintHuman[i].append(num)
        cls.humanNum = num
        num = 0
        for i in range(len(cls.total_station_resource)):
            cls.constraintStation.append([])
            for j in range(cls.total_station_resource[i]):
                num+=1
                cls.constraintStation[i].append(num)

        num = 0
        for i in range(len(cls.total_space_resource)):
            cls.constraintSpace.append([])
            for j in range(cls.total_space_resource[i]):
                num+=1
                cls.constraintSpace[i].append(num)





    # import scipy.stats as stats
    # mu, sigma = 5, 0.7
    # lower, upper = mu - 2 * sigma, mu + 2 * sigma  # 截断在[μ-2σ, μ+2σ]
    # X = stats.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
    # print(X.rvs())
    # print(X.rvs())
    #
    # x=FixedMes()
    # x.my()
    # print()







