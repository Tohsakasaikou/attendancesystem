import numpy as np
import pandas as pd
import random
#定义5门课程，每个课程班级人数为90人，一学期共20次课。
#每门课程均有5-8位同学缺席了该学期80%的课.
#此外每次课程均还有0-3位同学由于各种原因缺席。

#target ： 生成5门课程 每门课程20节课的到勤记录 
#ps ： 学生到勤情况和gpa有关 

#step1
#按照班级学号生成学生 生成5个班 每个班90人
#2130000 ---- 2130090 2130100-010190 ......
#生成 dataframe : lessonno(option) studentno gpa 

#step2
#根据gpa生成每个学生的到勤情况 attend01 attend02 attend03 ...
#转换为dataframe 准备拼接

#target : 
#dataframe ： lessonno(option) studentno gpa attend01 attend02 attend03  ....... attend20

#生成学生列表
def gen_student(lessonno):
    classlist =   np.array([ lessonno+i for i in range(1,91)])
    classlist = classlist[np.newaxis,:].T
    return classlist

#按照正态分布生成gpa 
def gen_gpa():
    gpalist = []
    result  = np.random.normal(2.2 , 0.5 , 90)
    result = result[np.newaxis,:].T
    return result



#计算得到一个分段线性函数 
def getcount(x):
    x1,y1,y2,x3,y3 = 0.8 , 18 , 14 , 4 , 0
    x2 = (np.random.randint(14,17))/10
    #print(x2)
    k1 = (y1-y2)/(x1-x2)
    b1 = y1-k1*x1
    k2 = (2.5-y3)/(x2-x3)
    b2 = -(k2*x3)
    return np.piecewise(x, [x < x2 , x >= x2 ], [lambda x: k1*x+b1, lambda x: k2*x+b2])

#根据分段函数生成润的课的次数
def getattendcount(gpalist):
    attendlist = []
    for gpa in gpalist:
        count = getcount(gpa)
        if count>=0 :
            attendlist.append(int(count))
        else :
            attendlist.append(0)
    attendlist = np.array(attendlist)
    print(attendlist)
    return attendlist

#然后按照次数生成润的情况的列表 这里生成了单个学生的到勤情况 
def gen_stuattendlist(count):
    list = []
    for i in range(20):
        if count>= 1:
            list.append(1)
            count-=1
        else :
            list.append(0)
    '''list = np.array(random.sample(list,20))
    print(list[np.newaxis,:])'''
    #return list[np.newaxis,:]
    return list 

#生成所有学生的到勤情况 然后拼接？
def gen_allstuattendlist(attendlist):
    res = []
    for attendsumconut in attendlist:
        temp = gen_stuattendlist(attendsumconut)
        temp.append(attendsumconut)
        res.append(temp)
    return res

#输入班级号生成数据
def gen_data(lessonno):
    np.set_printoptions(precision=3,suppress=True)
    #生成学号
    studentarray = gen_student(lessonno)
    #生成gpa 列向量
    gpaarray = gen_gpa()
    #根据gpa生成每个学生到勤总次数
    attendlist = getattendcount(gpaarray)
    #根据每个学生学期到勤总次数生成这个学期的到勤情况
    #nparray : 1-20 sumcount
    attendchart = np.array(gen_allstuattendlist(attendlist))
    #拼接
    res_array = np.concatenate((studentarray,gpaarray),axis=1)
    res_array = np.concatenate((res_array,attendchart),axis=1)
    print(res_array.dtype)
    #设置显示的样式
    #np.set_printoptions(precision=3,suppress=True)
    col_names = ['studentno','gpa','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','count']
    res_df = pd.DataFrame(res_array, columns=col_names)
    res_df = res_df.infer_objects()
    res_df['studentno'] = res_df['studentno'].astype('int')
    res_df['count'] = res_df['count'].astype('int')
    list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    for lesson in list:
        res_df[lesson] = res_df[lesson].astype('int')
    res_df = res_df.round({'gpa': 2})
    return res_df

if __name__ == '__main__':
    #np.set_printoptions(precision=3,suppress=True)
    for i in range(1,6):
        lessonno = 2130000
        substr = 'data\\lessondata'
        filename = '.csv'
        df = gen_data(lessonno + i*100)
        df.to_csv(str(substr + str(i)  + filename), sep = ',',index = False)
        #print(df.sort_values(by="gpa" , ascending=True)['studentno'][:8] )
