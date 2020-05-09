from mutable_version import MyHashMap

def size(vHashMap):
	return vHashMap.size()

def extend(vHashMap,vValue):
	newHM=MyHashMap(vHashMap.length,vHashMap.to_list())
	ncount=0
	for i in newHM.flag:
		if(i==1):
			ncount+=1
	if(ncount==vHashMap.length):
		return
	newHM.insert(vValue)
	return newHM

def remove(vHashMap,vValue):
	newHM=MyHashMap(vHashMap.length,vHashMap.to_list())
	ncount=0
	for i in range(newHM.length):
		if(newHM.items[i]==vValue and newHM.flag[i]==1):
			newHM.items[i]=0
			newHM.flag[i]=0
	return newHM

def to_list(vHashMp):
	return vHashMp.to_list().copy()

def mconcat(a,b):
	if a!=None and b!=None:
		newHM=MyHashMap(a.length+b.length)
		for i in range(a.length):
			if(a.flag[i]==1):
				newHM.insert(a.items[i])
		for i in range(b.length):
			if(b.flag[i]==1):
				newHM.insert(b.items[i])
		return newHM
	elif a:
		# return MyHashMap(a.length,a.to_list())
		return a
	elif b:
		# return MyHashMap(b.length,b.to_list())
		return b
	else:
		return None

def mempty():
	return None



def iterator(vHashMap):
	newHM=vHashMap
	nIndex=0
	def foo():
		nonlocal newHM
		nonlocal nIndex
		if newHM is None: raise StopIteration
		temp=newHM.items[nIndex]
		nIndex+=1
		return temp
	return foo

