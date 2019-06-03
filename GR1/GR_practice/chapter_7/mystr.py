# encoding=utf-8

def Isdigit(strs):
    '''
    s.isdigit()函数的作用是，如果S中所有的字符都是由数字组成，
    并且S至少有一个字符，则返回True，否则返回False
    :param strs: 字符串
    :return:False or True
    '''
    if len(strs) <=0:
        return False
    if not isinstance(strs,str):
        raise AttributeError(u'输入值得属性不是字符串！')
    num = len(strs)
    sine = 0
    for i in strs:
        if 48 <= ord(i) <= 57:
           sine +=1
    if sine == num:
        return True
    else:
        return False


def Join(lista,stra=''):
    '''
    将序列拼接为字符串，
    :param lista:
    :param stra:
    :return:
    '''
    str1 = lista[0]
    if not isinstance(lista[0],str):
            raise TypeError(u'只有字符串才能进行拼接')
    if not isinstance(stra,str):
        raise TypeError(u'连接词表示字符串')
    for i in xrange(1,len(lista)):
        if not isinstance(lista[i],str):
            raise TypeError(u'只有字符串才能进行拼接')
        str1 += stra + lista[i]
    return str1


def Split(strs,stru,num=-1):
    '''
    可以用指定的字符串将字符串进行分割，S.split([sep,[maxsplit]])
    :param strs:
    :param stru:
    :param num:
    :return:
    '''
    start = 0
    strc = ''
    lista = []
    if not isinstance(strs,str):
        raise TypeError(u'被分割值只能是字符串类型！')
    if not isinstance(stru,str):
        raise TypeError(u'指定值只能是字符串类型！')
    if not isinstance(num,int):
        raise TypeError(u'分割次数只能是正整数')
    end = len(stru)
    sine = len(stru)
    int1 = num
    if num == 0:
        return strs

    if num >= strs.count(stru) or num < 0:
        num = strs.count(stru)
    while num != 0:
        if strs[start:end] == stru:
            if start == 0 or start-1 == 0 or end==len(strs)-1:
                lista.append(strc)
            else:
                lista.append(strc)
                strc = ''
            start += sine
            end += sine
            num -= 1
        else:
            strc += strs[start]
            start += 1
            end += 1
    lista.append(strs[start:])
    if int1 >= strs.count(stru) or int1 < 0:
        if len(stru) == 1 and stru+stru == strs[-2:]:
            lista.append('')
    return lista


def Strip(str,str1='\t\n\r '):
    '''
    可以将字符串的左右空格等空白内容或指定的字符串去除，并返回处理后的结果，
    但原字符串未被改变。
    :param str:
    :param str1:
    :return:
    '''
    for i in xrange(len(str)):
        if str[i] not in str1:
            break
    str2 = str[::-1]
    for j in xrange(len(str)):
        if str2[j] not in str1:
            break
    return str[i:-j]

