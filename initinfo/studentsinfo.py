#定义5门课程，每个课程班级人数为90人，一学期共20次课。
#每门课程均有5-8位同学缺席了该学期80%的课.
#此外每次课程均还有0-3位同学由于各种原因缺席。

#测试


#按照班级学号生成学生 生成10个班 每个班45人
#2130000 ---- 2130045 2130100-010145

def getstudentlist(classno):
    no = classno
    classlist = [ classno+i for i in range(1,46)]
    print(classlist)
    return classlist

def getclasslist():
    classnamedir = {"cs00","cs01","cs02","cs03"
    ,"cs04","cs05","cs06","cs07","cs08","cs09"}
    classnamedir["cs01"] = getstudentlist(2130000)
    








