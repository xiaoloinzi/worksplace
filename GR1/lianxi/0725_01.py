# encoding=utf-8
import os
def printCode(path):
    dicts = {'kongh':0,'zshi':0,'code':0}
    for i,j,s in os.walk(path):
        for n in s:
            if os.path.splitext(n)[1]==".py":
                fpath = i+os.sep+n
                with open(fpath,'r') as fp:
                    reads = fp.readlines()
                for a in reads:
                    b = a.strip()
                    if b == '':
                        dicts['kongh'] +=1
                    elif b[0] == '#':
                        dicts['zshi'] += 1
                    else:
                        dicts['code'] += 1
    return dicts

if __name__=='__main__':
    path = 'E:\\worksplace'
    print printCode(path)













