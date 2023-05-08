from collections import defaultdict

from chromosome.Chromo import Chromosome


class FixedMes(object):
    """
    distance:
    orderInputMes:

    """
    distance = [[]]

    numJzjPos = 18
    numHumanAll = [18,60]

    planeOrderNum = 16
    planeNum = 8


    jzjNumbers=[1,2,3,4,5,6,7,8]  #舰载机编号


    Human_resource_type = 10 #四种人，和加油站
    total_Huamn_resource = [4, 5, 9, 12]  # 每种人员数量

    constraintOrder = defaultdict(lambda: []) #记录每类人的可作用工序，和可作用舰载机范围
    constraintOrder[0] = [ 1, 2, 5]
    constraintOrder[1] = [3,4, 16]
    constraintOrder[2] = [7, 8, 14]
    constraintOrder[3] = [6, 9, 10, 11,12,13,15]


    modeflag = 0 #0是单机、1是全甲板，这里考虑全甲板，如果是全甲板
    # constraintJZJ = defaultdict(lambda: []) #保障人员可作用舰载机范围,两种模式，单机或者全甲板

    station_resource_type = 5
    total_station_resource = [7,16,6,6,8]
    constraintS_Order = defaultdict(lambda: [])  # 记录每类设备的可作用工序，和可作用舰载机范围

     # 设备保障范围约束
    constraintS_JZJ = defaultdict(lambda: [])

    constraintS_JZJ[0] = [[1, 2, 3],
                          [3, 4, 5],
                          [6, 7],
                          [7, 8, 9],
                          [9, 10, 11],
                          [12, 13, 14],
                          [14, 15, 16]]
    constraintS_JZJ[1] = [[1],
                          [2],
                          [3],
                          [4],
                          [5],
                          [6],
                          [7],
                          [8],
                          [9],
                          [10],
                          [11],
                          [12],
                          [13],
                          [14],
                          [15],
                          [16]]
    constraintS_JZJ[2] = [[1,2,3,4],
                          [4,5,6,7],
                          [7,8,9],
                          [9,10,11],
                          [12,13,14],
                          [14,15,16]]
    constraintS_JZJ[3] = [[1,2,3,4],
                          [4,5,6,7],
                          [7,8,9],
                          [9,10,11],
                          [12,13,14],
                          [14,15,16]]
    constraintS_JZJ[4] = [[1,2,3],
                          [2,3,4],
                          [4,5,6],
                          [7,8,9],
                          [9,10,11],
                          [12,13],
                          [14,15],
                          [15,16]]

    Activity_num  = (planeOrderNum)*planeNum+2 #活动数量

    #工序顺序
    SUCOrder = defaultdict(lambda: [])
    SUCOrder[1] = [2, 9, 13 ,14, 15,16]
    SUCOrder[2] = [9, 13 ,14, 15,16]
    SUCOrder[3] = [4,9, 13 ,14, 15,16]
    SUCOrder[4] = [9, 13 ,14, 15,16]
    SUCOrder[5] = [2,4,6,8,9, 13 ,14, 15,16]
    SUCOrder[6] = [ 13,14,15,16]
    SUCOrder[7] = [8,9,13 ,14, 15,16]
    SUCOrder[8] = [9,13 ,14, 15,16]
    SUCOrder[9] = [13 , 14,15,16]
    SUCOrder[10] = [16]
    SUCOrder[11] = [16]
    SUCOrder[12] = [16]
    SUCOrder[13] = [14,15,16]
    SUCOrder[14] = [15,16]
    SUCOrder[15] = [16]
    SUCOrder[16] = []

    #    constraintOrder[0] = [ 1, 2, 5]
    #     constraintOrder[1] = [3,4, 16]
    #     constraintOrder[2] = [7, 8, 14]
    #     constraintOrder[3] = [6, 9, 10, 11,12,13,15]
    OrderInputMes = [[],
                     [(0, 1), (0, 0)],  # 1
                     [(0, 1), (1, 1)],  # 2
                     [(1, 1), (0, 0)],  #3
                     [(1, 1), (1, 1)],  # 4
                      [(0, 2), (2, 1)],  # 5
                       [(3, 2), (0, 1)],  # 6需要加油站
                    [(2, 2), (0, 0)],  # 7,
                  [(2, 1), (1, 1)],  # 8
                 [(3, 1), (0, 0)],  # 9
                  [(3, 2), (3, 1)],  # 10
                 [(3, 1), (0, 0)],  # 11
                 [(3, 1), (0, 0)],  # 12
                [(3, 1), (4, 1)],  # 13
                [(2, 1), (0, 0)] , # 14
                [(3, 1), (4, 1)]  ,# 15
                [(1, 1), (1, 1)]  # 16
                       ]
    #16位 为了让虚拟从1开始
    OrderTime = [0,
                 3,#1
                 6,#2
                 3,#3
                 5,#4
                 3,#5
                 10,#6
                 5,#7
                 3,
                 3,
                 3,
                 13,
                 8,
                 1,
                 5,
                5,
                 4]
    act_info={}

    lowTime = 120 #不能超过90 min

    cross = 0.5
    cross1 = 2.5
    MutationRate = 0.25
    MutationRatePmo = 0.05

    transferrate = 0.2
    transfer_iter = 50
    human_walk_speed = 80 #人员行走速度8 m/(in)

    populationnumber = 10
    ge = 4

    threadNum = 1
    populationnumberson = populationnumber/threadNum

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

    Paternal = [[0,0] for _ in range(populationnumber)]

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

    humanNum = 0
    targetWeight =[1,0.3,0.1]

    @classmethod
    def my(cls):
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
















