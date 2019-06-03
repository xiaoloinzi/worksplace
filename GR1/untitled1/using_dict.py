#encoding=utf-8
ab = {'Swaroop':'sweroopch@byteofptyhon',
      'Larry':'larry@wall.org',
      'Matsumoto':'matz@ruby-lang.org',
      'Spammer':'spammer@hotmail.com'}
print("ab--\nSwaroop is %s,\nLarry is %s,"
      "\nMatsumoto is %s,\nSpammer is%s"
      % (ab['Swaroop'],ab['Larry']
     ,ab['Matsumoto'],ab['Spammer']))
print("\n there are %d contacts in the address-book\n"%len(ab))
ab['Guido'] = 'guido@python.org'
print("\n there are %d contacts in the address-book\n"%len(ab))
for name,address in ab.items():
    print("Contact %s at %s"%(name,address))
if 'Guido' in ab:
    print("\nGuido's address is %s"%ab['Guido'])
