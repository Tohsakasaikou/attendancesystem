import numpy as np
#定义5门课程，每个课程班级人数为90人，一学期共20次课。
#每门课程均有5-8位同学缺席了该学期80%的课.
#此外每次课程均还有0-3位同学由于各种原因缺席。

#target ： 生成5门课程 每门课程20节课的到勤记录 
#ps ： 学生到勤情况和gpa有关 

#按照班级学号生成学生 生成10个班 每个班45人
#2130000 ---- 2130045 2130100-010145

# dataframe ： lessonno(option) studentno gpa attend01 attend02 attend03  ....... attend20




#生成学生列表
def gen_student(lessonno):
    no = lessonno
    classlist =   np.array([ lessonno+i for i in range(1,91)])
    classlist = classlist[np.newaxis,:].T
    #print(classlist.shape)
    #print(classlist)
    return classlist




#按照正态分布生成gpa 
def gen_gpa():
    gpalist = []
    result  = np.random.normal(2.0 , 0.5 , 90)
    result = result[np.newaxis,:].T
    print(result.shape)
    return result


#nparray : studentno gpa
def merge():
    studentarray = gen_student(2130000)
    print(studentarray.shape)
    gpaarray = gen_gpa()
    data_array = np.concatenate((studentarray,gpaarray),axis=1)
    np.set_printoptions(precision=3,suppress=True)
    print(data_array)

    print(data_array.shape)

merge()