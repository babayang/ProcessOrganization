class MyHashMap(object):
    def __init__(self, length=16,vItem=None):
        self.flag=[]
        self.items = []
        self.length = length
        self.n = 0
        """Initialized to 0"""
        for i in range(length):
            self.flag.append(0)
            self.items.append(0)
        if vItem!=None:

            for i in range(len(vItem)):
                self.insert(vItem[i])
    # def __init__(self, length,vItem,vFlag):
    #     self.flag=vFlag
    #     self.items = vItem
    #     self.length = length

 
            
    def hash(self, key):
        """Calculate hashkey"""
        return hash(key) % (self.length)

    def size(self):
        nCount=0
        for i in self.flag:
            if(i!=0):
                nCount+=1
        return nCount
    
    def to_list(self):
        res = []
        for i in range(len(self.flag)):
            if self.flag[i]==1:
                res.append(self.items[i])
        return res
    
    def from_list(self,vlist):
        if len(vlist)>self.length:
            return 0
        for i in range(self.length):
            self.flag[i]=0
            self.items[i]=0
        for i in vlist:
            self.insert(i)
        return 0
    
    def insert(self, value):
        ncount=0
        for i in self.flag:
            if(i==1):
                ncount+=1
        if(ncount==self.length):
            return 
        HashKey=self.hash(value)
        if(self.flag[HashKey]==0):
            self.flag[HashKey]=1
            self.items[HashKey]=value
            return 
        for i in range(HashKey+1,self.length):
            if(self.flag[i]==0):
                self.flag[i]=1
                self.items[i]=value
                return 
        for i in range(0,HashKey):
            if(self.flag[i]==0):
                self.flag[i]=1
                self.items[i]=value
                return   
    def remove(self, value):
        for i in range(self.length):
            if self.items[i]==value and self.flag[i]==1:
                self.items[i]=0
                self.flag[i]=0
        return

    def find(self,value):
        HashKey=self.hash(value)
        if self.items[HashKey]==value and self.flag[HashKey]==1:
            return True
        for i in range(HashKey,self.length):
            if self.items[HashKey]==value and self.flag[HashKey]==1:
                return True
        for i in range(0,HashKey):
            if self.items[HashKey]==value and self.flag[HashKey]==1:
                 return True
        return False
    def filter(self,fun):
        for i in range(self.length):
            if self.flag[i]==1 and not fun(self.items[i]):
                self.flag[i]=0
                self.items[i]=0
        return 
        
    def map(self,fun):
         for i in range(self.length):
            if self.flag[i]==1:
                self.items[i]=fun(self.items[i])
        # return

    def reduce(self,fun,init_state):
        state=init_state
        for i in range(self.length):
            if self.flag[i]:
                state=fun(state, self.items[i])
        return state

    def __iter__(self):
        return self

    def __next__(self):
        if self.n==self.length:
            raise StopIteration
        while self.flag[self.n]!=1 and self.n<self.length:
            self.n+=1
            if self.n==self.length:
                raise StopIteration
        # if self.flag[self.n]:
        tmp = self.items[self.n]
        return tmp




