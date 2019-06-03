# encoding=utf-8
# 8. 写程序将温度从华氏温度转换为摄氏温度。转换公式为C = 5 / 9*(F - 32)
#先理解华摄氏度是什么，然后把需要进行除法运算的值转换为float类型，Centigrade --摄氏度，华摄氏度--Celsius degree
celsiusDegree = float(raw_input('please input Celsius degree:'))
float1 = float(5)/float(9)

centigrade = float1 * (celsiusDegree - 32)
print u'%0.2f ℃ Celsius degree转换为Centigrade是%0.2f ℃'%(celsiusDegree,centigrade)
