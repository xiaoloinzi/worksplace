# encoding=utf-8
def getRabbitNum(monthNum):
    if monthNum == 1 or monthNum == 2:
        return 1
    else:
        return getRabbitNum(monthNum-1) + getRabbitNum(monthNum-2)
if __name__ == '__main__':
    try:
        while(True):
            n = int(raw_input('please input the month num:'))
            print 'the rabbit Num is:',getRabbitNum(n)
    except Exception:
        print 'Exist'