from os import listdir
from numpy import *
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
def img2vector(filename):#将矩阵转换成行向量
    returnVect=zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])
    return returnVect[0]
def handwritingClassTest():
    hwLabels=[]
    trainingFileList=listdir('trainingDigits')
    m=len(trainingFileList)
    trainingMat=zeros((m,1024))
    for i in range(m):
        fileNameStr=trainingFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:]=img2vector('trainingDigits/%s' % fileNameStr)
    testFileList=listdir('testDigits')
    errorCount=0.0
    mTest=len(testFileList)
    for i in range(mTest):
        fileNameStr=testFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
        vectorUnderTest=img2vector('testDigits/%s' % fileNameStr)
        classifierResult=classify0(vectorUnderTest,trainingMat,hwLabels,3)
        print('the classifier came back with:%d,the real answer is:%d' % (classifierResult,classNumStr))
        if classifierResult!=classNumStr:errorCount+=1.0
    print('\nthe total number of errors is:%d' % errorCount)
    print('\nthe total error rate is:'+str(errorCount/float(mTest)))
handwritingClassTest()