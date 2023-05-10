import random

import matplotlib as plt

def getRandNum(start,end):
    return (random.random() *100000) % (end -start)

import numpy as np

def randomint_plus(low, high=None, cutoff=None, size=None):
    """用来生成不包含一些中间数值的随机整数或序列

    Parameters
    ----------
    low : int
        生成随机整数的下界
    high: int
        生成随机整数的上界
    cutoff: int/list
        不需要包含的一个或多个值
    size: tuple
        需要产生的随机数规模
    Notes
    -----
    1. 在调用过程中，如果high, cutoff, size都缺省，就默认返回一个[0, low)的值
    2. 如果cutoff, size缺省，返回[low, high)的一个随机整数值
    3. 如果size缺省， 则返回一个[low, cutoff)U(cutoff, high)的随机整数值
    4. 返回一个给定size的矩阵，矩阵元素为[low, cutoff)U(cutoff, high)的随机整数值

    See Also
    --------
    np.random.randint()

    """
    if high is None:
        assert low is not None, "必须给定一个值作为上界"
        high = low
        low = 0
    number = 1  # 将size拉长成为一个向量
    if size is not None:
        for i in range(len(size)):
            number = number * size[i]

    if cutoff is None:  # 如果不需要剔除值，就通过numpy提供的函数生成随机整数
        random_result = np.random.randint(low, high, size=size)
    else:
        if number == 1:  # 返回一个随机整数
            random_result = randint_digit(low, high, cutoff)
        else:  # 返回一个形状为size的随机整数数组
            random_result = np.zeros(number, )
            for i in range(number):
                random_result[i] = randint_digit(low, high, cutoff)
            random_result = random_result.reshape(size)

    return random_result.astype(int)


def randint_digit(low, high, cutoff):
    """用来生成一个在区间[low, high)排除cutoff后的随机整数

    Parameters
    ----------
    low: int
        下限，能够取到
    high: int
        上限，不能够取到
    cutoff: int/list
        一个需要剔除的数或者数组，要求在(low, high)区间之间
    """
    digit_list = list(range(low, high))
    if type(cutoff) is int:  # 只需要剔除一个值
        if cutoff in digit_list:  # 如果需要剔除的值不存在，则不执行剔除操作
            digit_list.remove(cutoff)
    else:
        for i in cutoff:  # 需要剔除多个值的情况
            if i not in digit_list:  # 如果需要剔除的值不存在，则不执行剔除操作
                continue
            digit_list.remove(i)

    np.random.shuffle(digit_list)

    return digit_list.pop()  # 生成的序列打乱并且返回当前的随机值

def gen_randint(low, high, discard):
    result_list = list(range(low, high))
    result_list.remove(discard)
    np.random.shuffle(result_list)

    return result_list.pop()

def Dominate(Pop1, Pop2):
    '''
    :param Pop1:
    :param Pop2:
    :return: If Pop1 dominate Pop2, return True
    '''
    if (Pop1.f[0] < Pop2.f[0] and Pop1.f[1] < Pop2.f[1]) or \
            (Pop1.f[0] <= Pop2.f[0] and Pop1.f[1] < Pop2.f[1]) or \
            (Pop1.f[0] < Pop2.f[0] and Pop1.f[1] <= Pop2.f[1]):
        return True
    else:
        return False

def crowding_distance(NDSet):
    Distance = [0] * len(NDSet)
    NDSet_obj = {}

    for i in range(len(NDSet)):
        NDSet_obj[i] = NDSet[i].f

    ND = sorted(NDSet_obj.items(), key=lambda x: (x[1][0],x[1][1]))

    Distance[ND[0][0]] = 1e+20
    NDSet[0].c_distance = 1e+20
    Distance[ND[-1][0]] = 1e+20
    NDSet[-1].c_distance = 1e+20
    for i in range(1, len(ND) - 1):
        if Distance[ND[i][0]] == 0:
            Distance[ND[i][0]] = abs(ND[i + 1][1][0] - ND[i - 1][1][0]) + abs(ND[i + 1][1][1] - ND[i - 1][1][1])
            NDSet[i].c_distance = Distance[ND[i][0]]
    distance = dict(enumerate(Distance))
    New_distance = sorted(distance.items(), key=lambda x: x[1], reverse=True)
    L = [A[0] for A in New_distance]
    return L

def fast_non_dominated_sort(Pop):
            S = [[] for i in range(len(Pop))]
            front = [[]]
            n = [0 for i in range(len(Pop))]
            rank = [0 for i in range(len(Pop))]

            for p in range(len(Pop)):
                S[p] = []
                n[p] = 0
                for q in range(len(Pop)):
                    if Dominate(Pop[p], Pop[q]):
                        if q not in S[p]:
                            S[p].append(q)
                            Pop[p].sp.append(q)

                    elif Dominate(Pop[q], Pop[p]):
                        n[p] = n[p] + 1
                        Pop[p].np+=1
                if n[p] == 0:
                    rank[p] = 0
                    if p not in front[0]:
                        front[0].append(p)
            i = 0
            while (front[i] != []):
                Q = []
                for p in front[i]:
                    for q in S[p]:
                        n[q] = n[q] - 1
                        if (n[q] == 0):
                            rank[q] = i + 1
                            Pop[q].rank = i+1
                            if q not in Q:
                                Q.append(q)
                i = i + 1
                front.append(Q)
            del front[len(front) - 1]
            NDSet = []
            for Fi in front:
                NDSeti = []
                for pi in Fi:

                    NDSeti.append(Pop[pi])
                NDSet.append(NDSeti)
            return NDSet

def getTwoDimensionListIndex(L, value):
    index1 = -1
    index2 = -1
    """获得二维列表某个值的一维索引值的另一种方法"""
    for i in range(len(L)):
        for j in range(len(L[i])):
            if len(L[i][j]):
                for m in range(len(L[i][j])):
                    if L[i][j][m] == value:
                        index1 = i
                        index2 = j
    return index1, index2

#判断是否存在重复
def judgeDuplicated(array):
    array.sort()
    count=0
    while count<len(array)-1:
        if array[count]==array[count+1]:
            return True
        else:
            count+=1
    return False

#多目标 帕累托前沿画图
def Plot_NonDominatedSet(EP):
    x = []
    y = []
    for i in range(len(EP)):
        x.append(EP[i].f[0])
        y.append(EP[i].f[1])
    plt.plot(x, y, '*')
    plt.xlabel('makespan')
    plt.ylabel('Average Load')
    plt.legend()
    plt.savefig(r'obj_result/'+'first'+'.png')
    plt.close()


def writeTxt(filename,content):
    with open(filename, 'w') as f:
        for i in content:
            f.write(i + '\n')

if __name__ == '__main__':
    cotent=[]
    cotent.append("2 3 4 ")
    cotent.append("2 3 4")

    writeTxt("1.txt", cotent)
