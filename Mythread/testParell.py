import copy


class Task:
    def __init__(self, id, run_time, resources):
        self.id = id
        self.run_time = run_time
        self.resources = resources
        self.priority = 0
        self.s=0
        self.f = self.s+self.run_time


def parelle(allTasks , total_resource,code,AON):
    S =[ ] #已完工任务
    s =[]
    P =[ ] #在制任务
    D = [] #待完成任务
    t= 0
    useNowResource = [0 for i in range(len(total_resource))]

    while True:
        #更新任务集
        D = conditionCheck(allTasks,AON,code,s)
        #找到不冲突任务集W
        while True:
            W = findW(D,total_resource,P)

            if len(W) > 0:
                taskj = W[0]
                taskj.s = t
                taskj.f = t + taskj.run_time
                P.append(taskj)
                D.remove(taskj)
                s.append(taskj.id)

            else:
                break

        P.sort(key = lambda x:x.f)
        taski = P[0]
        S.append(taski)
        t = taski.f
        P.remove(taski)
        for otherp in P:
            if otherp.f == t:
                P.remove(otherp)
                S.append(otherp)
        if len(S)==len(allTasks):
            break

def findW(D,total_resource,P):

    W =[]
    useNowResource = [0 for i in range(len(total_resource))]

    for k in range(len(total_resource)):
        for p in P:
            useNowResource[k] = useNowResource[k] + p.resources[k]

    tempuseNowResource = copy.deepcopy(useNowResource)

    for task in D:
        for k in range(len(useNowResource)):
            if tempuseNowResource[k] > total_resource[k]:
                break
        flag = True
        for k in range(len(useNowResource)):
            if tempuseNowResource[k] + task.resources[k] > total_resource[k]:
                flag = False
                break
        if flag == True:
            W.append(task)

            for k in range(len(useNowResource)):
                tempuseNowResource[k] += task.resources[k]
    W.sort(key=lambda x: x.priority)
    return  W

def conditionCheck(allltasks,AON,code,s):
    D =[]
    for i in code :
        if i in s:
            continue
        flag =True
        prenumber = AON[i] #前序
        for ordernumber in prenumber:
            if ordernumber not in s:
                flag = False
                break
        if flag == True:
            D.append(allltasks[i-1])
    return D

all = []
#2,3,1,2,5,2,1,3,4
#1,1,1,1,2,1,1,1,1
all.append(Task(1,2,[1]))
all.append(Task(2,3,[1]))
all.append(Task(3,1,[1]))
all.append(Task(4,2,[1]))
all.append(Task(5,5,[2]))
all.append(Task(6,2,[1]))
all.append(Task(7,1,[1]))
all.append(Task(8,3,[1]))
all.append(Task(9,4,[1]))
total = [2]
SucOrder = [[],
            [],
            [1],
            [1],
            [1],
            [2],
            [4],
            [3],
            [3],
            [5,6,7],
            [8,9],
            []]
code =[ 1,2,3,4,5,6,7,8,9]
for ta in all:
    ta.priority = code.index(ta.id)
parelle(all,total,code,SucOrder)
print()














