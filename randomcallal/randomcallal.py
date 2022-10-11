from statistics import mean
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np
#读入测试集
def readdata(pathname):
    data = pd.read_csv(pathname,sep=',')
    dimdata = data[['gpa','count']]
    return data,dimdata

#kmeans
def kmeans(data, n):
    kmeans = KMeans(n_clusters=n)
    kmeans.fit(data)
    Y_predict = kmeans.predict(data)
    return Y_predict

def pca(data,data_test,k):
    pca_ = PCA(n_components=k)
    pca_ = pca_.fit(data)
    trans_data = pca_.fit_transform(data_test)
    print(trans_data.shape)
    return pd.DataFrame(trans_data)

#计算E
def get_e(data):
    y_predict = kmeans(data,2)
    print(y_predict)
    res = [(data.iloc[i,(data.shape[1]-1)])/20 for i in range(90) if y_predict[i] == 1]
    '''plt.figure(figsize=(14,7))
    plt.scatter(data.iloc[:,0],data.iloc[:,1],c= y_predict,cmap='Set3')
    #plt.axis("off")
    plt.show()'''
    return mean(res),y_predict

def get_anslist(pathname):
    e_list,dime_list = [],[]
    for i in range(1,6):
        filename = '.csv'
        data,dimdata = readdata(str(pathname + str(i)  + filename))
        e_list.append(get_e(data)[0])
        dime_list.append(get_e(dimdata)[0])
    return e_list,dime_list

if __name__ == '__main__':
    index = np.arange(5)
    e_list,dime_list = get_anslist('data\\traindata\\lessondata')
    plt.figure(figsize=(14,7))
    plt.ylabel(u'ACC') 
    plt.xlabel(u'lessonno') 
    plt.plot(index[:] , e_list[:] ,c = 'b',markersize=12,linewidth = 2,label=u"dim_data")
    plt.plot(index[:] , dime_list[:] ,c='g',linewidth = 2,markersize=12,label=u"data")
    plt.show()
    print(mean(e_list))
    print(mean(dime_list))

#暂定计划 明天要做的 添加点名策略输出
#添加层次聚类
#可选项 : 手写kmeans
