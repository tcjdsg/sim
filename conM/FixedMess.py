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
    planeNum = 4


    jzjNumbers=[1,2,3,4]  #舰载机编号


    Human_resource_type = 1 #先考虑只有一类人

    #先不考虑技能匹配。。就十几个人
    # total_Huamn_resource = [4, 5, 9, 12]  # 每种人员数量
    total_Huamn_resource = [12]
    constraintOrder = defaultdict(lambda: []) #记录每类人的可作用工序，和可作用舰载机范围
    constraintOrder[0] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    # constraintOrder[0] = [ 1, 2, 5]
    # constraintOrder[1] = [3,4, 16]
    # constraintOrder[2] = [7, 8, 14]
    # constraintOrder[3] = [6, 9, 10, 11,12,13,15]



    modeflag = 0 #0是单机、1是全甲板，这里考虑全甲板，如果是全甲板
    # constraintJZJ = defaultdict(lambda: []) #保障人员可作用舰载机范围,两种模式，单机或者全甲板

    station_resource_type = 5
    total_station_resource = [7,16,6,6,8]

    #飞机数量比较少的时候，这些燃料资源的限制约束不起作用。
    total_renew_resource = [5,8,2,4,6]

    #座舱限制。相当于是每个站位都有一个座舱，每个舰载机只能用自己座舱。
    space_resource_type = 8
    total_space_resource = [1,1,1,1,1,1,1,1]


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

    #加一个空间资源,空间资源的种类在这里体现不出来。因为跟舰载机号有关。
    OrderInputMes = [[],
                     [(0, 1), (0, 0), (0,0)],  # 1
                     [(0, 1), (1, 1), (0,1)],  # 2
                     [(0, 1), (0, 0),(0,0)],  #3
                     [(0, 1), (1, 1),(0,0)],  # 4
                      [(0, 2), (2, 1),(0,0)],  # 5
                       [(0, 2), (0, 1),(0,0)],  # 6需要加油站
                    [(0, 2), (0, 0),(0,0)],  # 7,
                  [(0, 1), (1, 1),(0,1)],  # 8
                 [(0, 1), (0, 0),(0,0)],  # 9
                  [(0, 2), (3, 1),(0,0)],  # 10
                 [(0, 1), (0, 0),(0,0)],  # 11
                 [(0, 1), (0, 0),(0,0)],  # 12
                [(0, 1), (4, 1),(0,1)],  # 13
                [(0, 1), (0, 0),(0,0)] , # 14
                [(0, 1), (4, 1),(0,1)]  ,# 15
                [(0, 1), (1, 1),(0,1)]  # 16
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
    constraintSpace = []

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

        num = 0
        for i in range(len(cls.total_space_resource)):
            cls.constraintSpace.append([])
            for j in range(cls.total_space_resource[i]):
                num+=1
                cls.constraintSpace[i].append(num)
















