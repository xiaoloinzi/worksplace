# encoding=utf-8
X = 0
if X >= 0:
    print '"X" must be atleast 0!'
counter = 0
while counter < 3:
    print 'loop #%d'%(counter)
    counter += 1
for item in ['e-mail','net-surfing','homework','chat']:
    print item,
who = 'knights'
what = 'Ni!'
print '\n''We are the ',who,'who say',what,what,what,what
print 'we are the %s who say %s'%(who,((what+'')*4))
for eachNum in [0,1,2]:
    print eachNum
for ec in range(3):
    print ec
foo = 'abc'
for c in foo:
    print c
for i in range(len(foo)):
    print foo[i],'(%d)'%i
for i , ch in enumerate(foo):
    print ch ,'(%d)'%i
squared = [x**2 for x in range(4)]
for i in squared:
    print i
sqdEvens = [x**2 for x in range(8) if not x % 2]
for i in sqdEvens:
    print i
print 1 + 2 * 4