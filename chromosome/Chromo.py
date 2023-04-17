class Chromosome(object):
    def __init__(self):
        self.codes = []
        self.WorkTime = 9999

        self.variance = 9999.0

        self.movetime = 9999.0

        self.Maxfagiue = 0

        self.np=0
        self.sp=[]

        self.f=None       #适应度
        self.rank = -1    #用于多目标
        self.crowding_distance = -1
        # self.cal=SSGS     #解码方式。串行、并行
        #
        # self.pa=paramater()  #参数配置

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def setcodes(self,codes):
            self.codes=codes


    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        if self.rank==other.rank and self.crowding_distance < other.crowding_distance:
            return True
        return  False


    def setf(self):

        # FinishTime, all,Allpeople,_,_ = decoder(self.codes,People,self.pa)
        #
        # Junheng = getJunheng(Allpeople)
        self.f=[self.WorkTime,self.variance,self.movetime]
        return self.f