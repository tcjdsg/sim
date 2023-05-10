import copy
import numpy as np

# self.id = id
# self.taskid = taskid
# self.belong_plane_id = jzjId

def insert(pop,activities):
    newpop = copy.deepcopy(pop.codes)


    opt = np.random.choice([x for x in range(2, FixedMes.Activity_num-2)], 1, replace=False)[0]
    preorder=activities[opt].predecessor
    success=activities[opt].successor

    ts = 0
    es=999
    newcode=[]
    newcode.append(newpop[0][:opt]+newpop[0][opt+1:])
    newcode.append(newpop[1][:opt]+newpop[1][opt+1:])

    #得到了
    for id in preorder:
        if activities[id].es > ts:
            ts = activities[id].es

    for id in success:
        if activities[id].es <es:
            es = activities[id].es

    code=[]

    for time in newcode[0]:
        if time[1] >=ts and time[1]<=es:
            code.append(time)

    qujian = sorted(code,key=lambda x:x[1])
    optnow = np.random.choice([x for x in range(0, len(qujian)-1)], 1, replace=False)[0]
    time1 = qujian[optnow][1]
    time2 = qujian[optnow+1][1]
    import random
    a = random.uniform(time1, time2)

    newpop[0][opt] = [opt,a]
    newpop[1][opt] = [opt,a+activities[opt].duration]

    pop.codes=newpop


if __name__ == '__main__':
    from Mythread.myInit import MyInit
    m = MyInit("C:/Users/29639/Desktop/sim/dis.csv", "C:/Users/29639/Desktop/sim/dis.csv")
    m.InitPopulation()
    codes=[[[0, 0.8643338440926068], [26, 1.429243207077643], [7, 2.551201250180088], [10, 3.437986802637721], [1, 4.546821271766577], [37, 5.670126382332746], [58, 6.356943614001206], [55, 7.04023061484631], [60, 8.156199175710691], [5, 9.413315184121295], [35, 10.652948444047723], [2, 11.782369923702397], [59, 12.100725213883246], [17, 13.756590571685887], [38, 14.599392162789883], [51, 15.915764321930736], [28, 16.551253679408752], [27, 17.793097389129514], [33, 18.53199202189966], [49, 19.012878314375914], [11, 20.276133132803533], [44, 21.231617796114055], [39, 22.6724683244793], [8, 23.522819480333304], [23, 24.655878989110438], [3, 25.948468279950696], [6, 26.648391578846468], [12, 27.078643930756282], [53, 28.64726161315283], [52, 29.126215494708564], [21, 30.172313393858186], [43, 31.366880299606507], [19, 32.873658024474885], [50, 33.90864379014162], [18, 34.445075403831765], [4, 35.887587235567956], [56, 36.60961475996905], [24, 37.691004723896164], [9, 38.48301121630405], [54, 39.46695475066564], [42, 40.78125662454039], [34, 41.262869936266114], [20, 42.090265622353094], [40, 43.53435737857019], [36, 44.496044526899425], [57, 45.34436890748118], [41, 46.96380700052707], [25, 47.40346177704773], [45, 48.62827454327793], [61, 49.59520586481162], [22, 50.357689925049876], [29, 51.616575089670015], [46, 52.13993395997284], [47, 53.38272296211509], [62, 54.60367348703851], [48, 55.26555236613016], [63, 56.016717010130165], [64, 57.96882634478978], [30, 58.191568291405645], [31, 59.278439967547286], [32, 60.540611767825524], [13, 61.76133425849865], [14, 62.31772015245703], [15, 63.367377847093145], [16, 64.44226752318829], [65, 65.08455179750395]],
    [[0, 0.8643338440926068], [26, 5.4292432070776435], [7, 7.551201250180088], [10, 7.437986802637721],
     [1, 7.546821271766577], [37, 8.670126382332747], [58, 10.356943614001207], [55, 12.04023061484631],
     [60, 16.15619917571069], [5, 12.413315184121295], [35, 13.652948444047723], [2, 17.782369923702397],
     [59, 25.100725213883244], [17, 16.756590571685887], [38, 24.599392162789883], [51, 18.915764321930737],
     [28, 24.551253679408752], [27, 30.793097389129514], [33, 21.53199202189966], [49, 22.012878314375914],
     [11, 33.27613313280354], [44, 29.231617796114055], [39, 27.6724683244793], [8, 26.522819480333304],
     [23, 29.655878989110438], [3, 28.948468279950696], [6, 36.64839157884647], [12, 35.078643930756286],
     [53, 31.64726161315283], [52, 34.12621549470856], [21, 33.17231339385819], [43, 44.36688029960651],
     [19, 35.873658024474885], [50, 39.90864379014162], [18, 40.445075403831765], [4, 40.887587235567956],
     [56, 39.60961475996905], [24, 40.691004723896164], [9, 42.48301121630405], [54, 49.46695475066564],
     [42, 44.78125662454039], [34, 47.262869936266114], [20, 47.090265622353094], [40, 46.53435737857019],
     [36, 49.496044526899425], [57, 49.34436890748118], [41, 50.96380700052707], [25, 51.40346177704773],
     [45, 50.62827454327793], [61, 51.59520586481162], [22, 60.357689925049876], [29, 53.616575089670015],
     [46, 57.13993395997284], [47, 58.38272296211509], [62, 59.60367348703851], [48, 59.26555236613016],
     [63, 61.016717010130165], [64, 61.96882634478978], [30, 63.191568291405645], [31, 64.27843996754729],
     [32, 64.54061176782552], [13, 63.76133425849865], [14, 67.31772015245703], [15, 68.36737784709314],
     [16, 68.44226752318829], [65, 65.08455179750395]]]

    from conM.FixedMess import FixedMes
    insert( codes, FixedMes.act_info)
