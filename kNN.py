from numpy import *
import operator
def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
    #inX=[1,1.2],dataSet=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]]),labels=['A','A','B','B'],k=3
    dataSetSize=dataSet.shape[0]
    #dataSetSize=4即dataSet的行数
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    #diffMat=[[1,1.2],[1,1.2],[1,1.2],[1,1.2]]-[[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]]=[[0,0.1],[0,0.2],[1,1.2],[1,1.1]]
    sqDiffMat=diffMat**2
    #sqDiffMat=[[0,0.01],[0,0.04],[1,1.44],[1,1.21]]
    sqDistances=sqDiffMat.sum(axis=1)
    #sqDistances=[0.01,0.04,2.44,2.21]
    distances=sqDistances**0.5
    #distances=[0.1,0.2,1.562,1.486]
    sortedDistIndicies=distances.argsort()
    #sortedDisIndicies=[0,1,3,2]
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=lambda d:d[1],reverse=True)#,key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
group,labels=createDataSet()
print(classify0([1,1.2],group,labels,3))