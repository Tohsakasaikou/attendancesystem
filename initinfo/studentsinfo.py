import numpy as np
import pandas as pd
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
    no = lessonno
    classlist =   np.array([ lessonno+i for i in range(1,91)])
    classlist = classlist[np.newaxis,:].T
    return classlist




#按照正态分布生成gpa 
def gen_gpa():
    gpalist = []
    result  = np.random.normal(2.0 , 0.4 , 90)
    result = result[np.newaxis,:].T
    return result


#nparray : studentno gpa
def merge():
    studentarray = gen_student(2130000)
    gpaarray = gen_gpa()
    #拼接
    res_array = np.concatenate((studentarray,gpaarray),axis=1)
    #设置显示的样式
    #np.set_printoptions(precision=3,suppress=True)
    res_df = pd.DataFrame(res_array, columns=['studentno', 'gpa'])
    res_df['studentno'] = res_df['studentno'].astype('int')
    print(res_df.dtypes)
    return res_df


#计算得到一个分段线性函数 根据分段函数生成润的课的次数
#然后按照次数生成润的情况的列表
#然后列表和gpa拼接转换为dataframe 并和第一个表拼接的到单个班的到勤情况
#可以生成10个班的到勤情况 前五个班作为训练集 后五个班作为测试集计算出最后的e
df = merge()
print(df.sort_values(by="gpa" , ascending=True)['studentno'][:8] )

data = df.sort_values(by="gpa" , ascending=True)['studentno'].values
data = data[np.newaxis,:].T
print(data)